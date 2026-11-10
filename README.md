# nvidia_camp_site

AI 코어 엔지니어 과정의 요약 HTML(매일 요약, 과목별 4일 종합, 전체 연결 요약, 라이브러리 치트시트, 설치 가이드)을 모아 배포하는 저장소입니다.
강의 원본 자료(강의 PDF, 실습 코드)는 private 저장소 `nvidia_camp`에 있고, 이 저장소는 그 안의 `site/` 폴더입니다.

## 구조

```text
pages/                     ← 원본 (구성안·템플릿·제작 스크립트·index.html·요약 PDF)
├─ <과목>/<YYYYMMDD>/       매일 요약          → /<과목>/<YYYYMMDD>/ (같은 날 두 번째 회차는 -2)
├─ <과목>/all/              과목 4일 종합      → /<과목>/
├─ overview/                전체 과목 연결 요약 → /overview/
├─ cheatsheet/<이름>/        라이브러리 치트시트 → /cheatsheet/<이름>/
└─ setup/<이름>/             설치 가이드         → /setup/<이름>/
public/                    ← build_site.py가 만드는 배포본 (Vercel이 이 폴더만 배포)
sync_lectures.py           ← 학습 자료 시트 → lectures.json (Day·날짜·과목·강의 자료 링크)
lectures.json              ← 실제 일정. 사이트의 Day 번호와 날짜 기준
build_site.py              ← pages/ → public/ (위쪽 메뉴, 홈·과목 목록)
DESIGN.md                  ← 모든 페이지 공통 디자인 원칙
```

- 과목 key: `ml`, `dl`, `vision`, `llm`. 새 요약은 위 규칙의 폴더에 `index.html`을 만들면 자동으로 들어갑니다. 치트시트는 `build_site.py`의 `CHEATSHEETS`에, 설치 가이드는 `SETUP`에 이름과 과목을 한 줄 추가합니다. 홈과 과목 목록에서 그 과목 아래 '참고' 줄에 링크로 나옵니다.
- 요약 PDF는 페이지 폴더에 함께 둡니다. 사이트에서는 위쪽 메뉴의 PDF 링크로 열립니다. 강의 교재 PDF는 넣지 않습니다.
- 제작 스크립트는 실습 코드·데이터를 `nvidia_camp`에서 읽기만 합니다. `nvidia_camp`는 이 폴더를 참조하지 않습니다.
- 진행 기록은 `LOG.md`, 페이지별 제작 기록은 각 폴더의 `DESIGN.md`에 남깁니다.

## 업데이트와 배포

브랜치: `main`은 작업용(push하면 미리보기), `deploy`는 실제 사이트(https://nvidiasesac.vercel.app/).

```bash
cd ~/workspace/nvidia_camp/site
uv run sync_lectures.py                # (시트가 바뀌었을 때) gws-work로 읽기만 함
uv run build_site.py                   # pages/ → public/
python3 -m http.server -d public 8000  # (선택) 내 컴퓨터에서 http://localhost:8000 으로 확인
git add -A && git commit -m "..." && git push        # main → 미리보기
```

- main 미리보기: https://nvidiasesac-git-main-test11-ebb8.vercel.app/ (Vercel 로그인 필요, 항상 main 최신)
- 사이트는 2026-11-10에 출시됐습니다. 작업은 main에만 올리고, 배포는 따로 요청할 때만 합니다.
- 공개 전 페이지: `SETUP`의 공개 여부가 False인 페이지는 main 빌드에는 그대로 들어가(따로 표시 없음) 미리보기에서 볼 수 있습니다. `uv run build_site.py --release`로 만들면 빠집니다.
- 실제 배포: 공개 전 페이지가 없으면 `git push origin main:deploy`. 있으면 main을 그대로 올리지 않고, `--release`로 다시 만든 public/을 deploy에 올립니다.
