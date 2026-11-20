#!/bin/zsh
# 전날 18:20 자동 배포: 다음 수업일 자료가 origin/main에 있으면 --release로 빌드해 deploy에 올린다.
#   launchd(~/Library/LaunchAgents/app.nvidiasesac.auto-release.plist)가 매일 18:20에 실행한다.
#   - 18:20~23:59에만 동작한다 (잠자기 후 늦게 깨어나 다음 날 아침에 돌면 그냥 끝낸다).
#   - 공개 전(SETUP 공개=False) 페이지(Docker 등)는 --release가 빼고, 빌드 결과에 남아 있으면 배포하지 않는다.
#   - main의 다른 변경도 함께 나간다. 바뀐 페이지 목록을 커밋 메시지·알림·로그에 남긴다.
#   - deploy는 fast-forward push만 한다 (force 없음).
# 수동 실행: ./auto_release.sh   (시각 검사를 건너뛰려면 FORCE_TIME=1, 실제 push 없이 보려면 DRY_RUN=1)
set -euo pipefail
export PATH="/opt/homebrew/bin:$HOME/.local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
SITE="${0:A:h}"
LIVE="https://nvidiasesac.vercel.app"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/nvsite-auto-release.XXXXXX")"

log() { print -r -- "[$(date '+%F %T')] $*"; }
notify() {  # 맥 알림 (제목, 내용)
  osascript -e "display notification \"${2//\"/\\\"}\" with title \"${1//\"/\\\"}\"" 2>/dev/null || true
}
cleanup() {
  git -C "$SITE" worktree remove --force "$WORK/main" 2>/dev/null || true
  git -C "$SITE" worktree remove --force "$WORK/deploy" 2>/dev/null || true
  rm -rf "$WORK"
}
fail() { log "실패: $*"; notify "사이트 자동 배포 실패" "$*"; exit 1; }
trap cleanup EXIT
trap 'fail "${funcstack[1]:-스크립트} ${LINENO}행에서 멈춤 (로그 확인)"' ERR

HM=$(date +%H%M)
if [[ -z "${FORCE_TIME:-}" && ( $HM -lt 1820 ) ]]; then
  log "건너뜀: ${HM:0:2}:${HM:2}는 18:20 전"; exit 0
fi

cd "$SITE"
git fetch -q origin main deploy
git worktree add -q --detach "$WORK/main" origin/main
git worktree add -q --detach "$WORK/deploy" origin/deploy

# 다음 수업일과 그날 페이지 경로, 공개 전 SETUP 항목 (build_site.py의 규칙을 그대로 쓴다)
INFO=$(cd "$WORK/main" && uv run --quiet --no-project python - <<'EOF'
import datetime, json
import build_site as b
today = datetime.date.today().isoformat()
rows = json.loads(b.LECTURES.read_text(encoding="utf-8"))
nxt = min((r["date"] for r in rows if r["date"] > today), default="")
print(nxt)
for d in b.read_days():
    if d["date"] == nxt and d["key"]:
        print("day", f'Day{d["n"]}', f'{d["key"]}/{d["ymd"]}')
for k, v in b.SETUP.items():
    if not v[4]:
        print("hidden", k)
EOF
)
NEXT=${${(f)INFO}[1]}
[[ -n "$NEXT" ]] || { log "건너뜀: 남은 수업일 없음"; exit 0; }
DAYS=(${(f)"$(print -r -- "$INFO" | awk '$1=="day"{print $2" "$3}')"})
HIDDEN=(${(f)"$(print -r -- "$INFO" | awk '$1=="hidden"{print $2}')"})
log "다음 수업일 $NEXT · ${DAYS[*]:-수업 없음} · 공개 전: ${HIDDEN[*]:-없음}"

# 다음 수업일 기준 배포 빌드
(cd "$WORK/main" && uv run --quiet build_site.py --release --as-of "$NEXT" >/dev/null)

READY=()
for d in "${DAYS[@]}"; do
  [[ -f "$WORK/main/public/${d#* }/index.html" ]] && READY+=("$d")
done
if (( ${#READY} == 0 )); then
  log "건너뜀: main에 $NEXT 강의 자료가 아직 없음"
  notify "사이트 자동 배포 건너뜀" "$NEXT 강의 자료가 main에 아직 없습니다."
  exit 0
fi

# 공개 전 페이지가 빌드 결과에 남아 있으면 배포하지 않는다
for k in "${HIDDEN[@]}"; do
  if [[ -e "$WORK/main/public/setup/$k" ]] || grep -rqs "href=\"[^\"]*setup/$k/" "$WORK/main/public"; then
    fail "공개 전 페이지 setup/$k 가 배포 빌드에 들어 있어 중단"
  fi
done

# deploy에 반영: 실제로 쓰이는 public/과 vercel.json만 바꾼다
# --checksum: 크기·수정 시각이 같아도 내용으로 비교한다 (600→760처럼 길이가 같은 수정이 건너뛰어지던 문제, 2026-11-20)
rsync -a --delete --checksum "$WORK/main/public/" "$WORK/deploy/public/"
cp "$WORK/main/vercel.json" "$WORK/deploy/vercel.json"
cd "$WORK/deploy"
git add -A public vercel.json
if git diff --cached --quiet; then
  log "건너뜀: deploy가 이미 최신 (${READY[*]})"; exit 0
fi
CHANGED=$(git diff --cached --name-only | sed -E 's#^public/##; s#/[^/]*$##' | awk -F/ '{ if (NF == 1 && $1 ~ /\.html$/) print "홈"; else if (NF >= 2) print $1 "/" $2; else print $1 }' | sort -u | tr '\n' ' ')
NAMES=${(j:·:)${READY%% *}}
MSG="release: 자동 · $NEXT ${NAMES} 전날 공개 (공개 전 ${(j:·:)HIDDEN} 제외)"
git -c user.name="$(git -C "$SITE" config user.name)" -c user.email="$(git -C "$SITE" config user.email)" \
  commit -q -m "$MSG" -m "main $(git -C "$WORK/main" rev-parse --short HEAD) 기준 auto_release.sh" -m "바뀐 곳: $CHANGED"
log "$MSG"
log "바뀐 곳: $CHANGED"
if [[ -n "${DRY_RUN:-}" ]]; then log "DRY_RUN: push 안 함"; exit 0; fi
git push -q origin HEAD:deploy || fail "deploy push 거부 (다른 배포가 먼저 올라감?) — 다시 실행하면 됩니다"
log "push 완료 $(git rev-parse --short HEAD)"

# 실제 사이트 확인 (Vercel 반영까지 최대 10분)
for d in "${READY[@]}"; do
  url="$LIVE/${d#* }/"
  for i in {1..40}; do
    [[ "$(curl -s -o /dev/null -w '%{http_code}' "$url")" == 200 ]] && break
    (( i == 40 )) && fail "${d%% *} 페이지가 10분 안에 열리지 않음: $url"
    sleep 15
  done
  log "확인 200 $url"
done
for k in "${HIDDEN[@]}"; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "$LIVE/setup/$k/")
  [[ "$code" == 404 ]] || fail "공개 전 페이지가 보임: /setup/$k/ ($code)"
  log "확인 404 /setup/$k/"
done
notify "사이트 자동 배포 완료" "$NEXT ${NAMES} 공개 · 바뀐 곳: $CHANGED"
