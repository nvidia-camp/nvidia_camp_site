# nvidia_camp_site

AI 코어 엔지니어 과정의 학습 사이트(https://nvidiasesac.vercel.app/)를 만드는 저장소입니다.
매일 요약, 과목 종합, 치트시트, 설치 가이드, 강사님 강의 HTML을 한곳에 모읍니다.
강의 원본 자료(강의 PDF, 실습 코드)는 private 저장소 `nvidia_camp`에 있고, 이 저장소는 그 안의 `site/` 폴더입니다.

AI 에이전트와 함께 작업한다면 **[AGENTS.md](AGENTS.md)** 의 규칙을 먼저 봅니다.

## 구조

```text
pages/                 ← 페이지 원본. 폴더 이름만 맞추면 자동으로 사이트에 들어간다
├─ <과목>/<YYYYMMDD>/    매일 요약 → /<과목>/<YYYYMMDD>/ (같은 날 두 번째 회차는 -2)
│   ├─ index.html        요약 (그림은 data URI로 안에 넣는다)
│   ├─ tree.md           강의 목차 (요약이 없으면 이것만으로 그날 페이지가 생김)
│   └─ lecture/          강사님 강의 HTML (sync_lecture_html.py가 넣음, 고치지 않음)
├─ <과목>/all/           과목 종합 → /<과목>/ (없으면 날짜 카드 목록)
├─ cheatsheet/<이름>/    치트시트 → /cheatsheet/<이름>/
└─ setup/<이름>/         설치 가이드 → /setup/<이름>/ (여러 쪽이면 하위 폴더)

site.toml              ← 설정: 과목, 치트시트·가이드 등록, 공개 여부, Colab 링크
web/                   ← 모든 페이지에 끼우는 CSS·JS·아이콘
│   nav.css list.css tree.css theme.css   위쪽 메뉴 · 홈 목록 · 강의 목차 · 다크 모드
│   theme.js analytics.js                 다크 모드 전환 · Google Analytics
│   totop.css totop-dark.css totop.js     강의 요약 맨 위로 버튼 (읽은 만큼 차는 원)
│   copy.css copy.js                      <pre data-copy> 코드 셀 오른쪽 위 복사 아이콘
│   icons/*.svg
sitebuild/             ← 빌드 코드 (역할별, 아래 표)
build_site.py          ← 빌드 시작점: pages/ + site.toml + web/ → public/
public/                ← 빌드 결과 (직접 고치지 않음. 빌드할 때마다 지우고 새로 만듦)

lectures.json          ← 실제 일정(Day·날짜·과목·Slack 자료 링크). sync_lectures.py가 시트에서 만듦
sync_lectures.py       ← 학습 자료 시트 → lectures.json (gws-work로 읽기만)
sync_lecture_html.py   ← nvidia_camp의 강의 HTML → pages/<과목>/<날짜>/lecture/
auto_release.sh        ← 매일 18:20 자동 배포 (launchd)
Makefile               ← 자주 쓰는 명령 (make build, make check …)
AGENTS.md              ← AI·사람 공통 작업 규칙 (CLAUDE.md는 이 파일을 가리킴)
DESIGN.md · LOG.md     ← 디자인 원칙 · 작업 기록
```

빌드 코드 (`sitebuild/`, import는 위에서 아래 한 방향)

| 파일 | 하는 일 |
|---|---|
| `config.py` | 경로, `site.toml`·`web/` 읽기, `--release`·`--as-of` |
| `tree.py` | `tree.md` 읽기, '강의 목차 한눈에 보기' 블록 |
| `data.py` | `lectures.json`·`pages/`에서 Day 목록과 제목 |
| `fonts.py` | 글꼴 통일 (본문 Pretendard) |
| `nav.py` | 위쪽 메뉴, 라이트/다크 전환, 방문 통계 |
| `content.py` | 요약·가이드·강의 HTML을 `public/`으로 복사 |
| `listing.py` | 홈, 과목 페이지, 요약 전 강의 목차 페이지 |
| `check.py` | 빌드 결과 검사 (`make check`) |

## 자주 하는 일

| 하고 싶은 일 | 방법 |
|---|---|
| 새 요약 페이지 | `pages/<과목>/<날짜>/index.html`을 만든다. 과목 key: `python` `ml` `dl` `vision` `llm` |
| Colab 실습 폴더 링크 | `site.toml`의 `[colab]`에 `"llm/20261120" = "https://drive.google.com/..."` 한 줄 |
| 치트시트·설치 가이드 등록 | `site.toml`의 `[cheatsheets.<키>]`·`[setup.<키>]`. 가이드가 여러 쪽이면 `[setup_pages]`에 순서 |
| 공개 전으로 두기 | `[setup.<키>]`의 `public = false` (main 빌드에는 있고 `--release`에서 빠짐) |
| 페이지와 함께 받을 파일 | `site.toml`의 `[files]`에 등록하고, 페이지에서는 `<a data-site href="…">`로 링크 |
| 시트 일정이 바뀜 | `uv run sync_lectures.py` |
| 강사님 강의 HTML | 아래 "강의 자료 바로 보기" |

- 페이지 안의 상대 링크는 빌드할 때 글자로 바뀝니다. 사이트의 다른 페이지로 가는 링크만 `data-site`를 붙이면 살아 있습니다.
- "HTML 받기"로 사이트 메뉴·통계를 뺀 원본 HTML 한 파일을 받습니다(그림까지 들어 있어 인터넷 없이 열림). PDF는 만들지 않습니다(2026-11-14 폐지).
- 제작 스크립트는 `nvidia_camp`의 실습 코드·데이터를 읽기만 합니다. `nvidia_camp`는 이 폴더를 참조하지 않습니다.

## 명령

```bash
cd ~/workspace/nvidia_camp/site
make build            # main 빌드 (공개 전 페이지까지)
make serve            # http://localhost:8000 에서 보기
make check            # 커밋 전 검사: ruff·JS 문법 → main·release 빌드 검사
make release          # 배포용 빌드 (공개 전 페이지 제외)
make snapshot AS_OF=2026-11-19   # 정리 작업 전 빌드 저장
make compare  AS_OF=2026-11-19   # 정리 작업 뒤 빌드가 같은지
```

`AS_OF`를 비우면 지금 시각 기준입니다. 사이트의 '오늘'은 18:20부터 다음 수업일입니다.

## 브랜치와 배포

- `main`은 작업용입니다(push하면 Vercel 미리보기: https://nvidiasesac-git-main-test11-ebb8.vercel.app/ , Vercel 로그인 필요).
- `deploy`는 실제 사이트입니다. main을 그대로 올리지 않고, **main 커밋으로 `--release` 빌드한 결과를 `release: …` 커밋으로** 올립니다. 순서는 [AGENTS.md](AGENTS.md) 3장에 있습니다.
- **자동 배포:** `auto_release.sh`를 launchd(`~/Library/LaunchAgents/app.nvidiasesac.auto-release.plist`)가 매일 18:20에 실행합니다. origin/main에 다음 수업일 페이지가 있으면 `--release`로 빌드해 deploy에 release 커밋을 올리고, 실제 사이트를 확인한 뒤 맥 알림을 띄웁니다. main의 다른 변경도 함께 나가고, 공개 전 페이지가 빌드에 남아 있으면 중단합니다. Mac이 잠자기 중이면 돌지 않습니다(그날 23:59 전에 깨어나면 그때 실행).
  - 로그: `~/Library/Logs/nvidiasesac_auto_release.log`
  - 미리 보기: `FORCE_TIME=1 DRY_RUN=1 ./auto_release.sh`
- 그래서 **main에는 언제 배포돼도 괜찮은 상태만** 올립니다.

## 방문 통계

- Vercel Web Analytics와 Google Analytics 4(`web/analytics.js`)를 함께 씁니다. 원본(`download.html`)과 강의 화면(`view.html`)에는 넣지 않습니다.
- GA는 실제 사이트 주소에서만 보냅니다. 주소 끝에 `?ga_debug=1`을 붙이면 GA 관리 > DebugView에서 바로 보입니다.
- 이벤트: `section_view`(단락 도달) · `toc_open`(강의 목차 펼침) · `site_click`(링크, `link_type`으로 구분) · `theme_toggle` · `slide_view`·`lecture_progress`(강의 슬라이드)

## 강의 자료 바로 보기 (강사님 강의 HTML)

강사님이 강의 HTML을 주시면(웹사이트 게시 허락, 2026-11-14):

1. `nvidia_camp/<과목>/<YYYYMMDD>/` 바로 아래에 둡니다. 같은 날 두 번째 회차는 `Day*_02/` 아래. nvidia_camp에서는 `.gitignore`로 제외됩니다.
2. `uv run sync_lecture_html.py` → `pages/<과목>/<날짜>/lecture/index.html`로 복사(원본 그대로, 바뀐 것만).
3. `make build` → `/<과목>/<날짜>/lecture/`가 생기고, 홈 Day 줄과 Day 페이지 메뉴에 **강의 자료 보기**가 붙습니다.

- Slack 로고는 학습 자료 시트의 Slack 링크(원본 게시물)입니다.
- 강의 HTML은 고치지 않습니다. 사이트 메뉴 아래 화면 전체에 띄우고, 메뉴의 "HTML 받기"로 원본을 그대로 받습니다.
