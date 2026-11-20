# AGENTS.md — 이 저장소에서 일하는 AI·사람 공통 규칙

학습 사이트(https://nvidiasesac.vercel.app/) 저장소입니다. 학생들이 매일 보는 사이트라서,
**실제 사이트를 깨뜨리지 않는 것**이 다른 무엇보다 먼저입니다. 처음 보면 README.md를 먼저 읽으세요.

## 1. 무엇을 어디서 고치나

| 하고 싶은 일 | 고칠 곳 | 고치면 안 되는 곳 |
|---|---|---|
| 요약·가이드 페이지 내용 | `pages/<…>/index.html` | `public/` (빌드할 때마다 지워짐) |
| Colab 링크·가이드 등록·공개 여부 | `site.toml` | `sitebuild/*.py` |
| 위쪽 메뉴·홈 디자인(CSS) | `web/*.css` | 페이지마다 복사하지 말 것 |
| GA·다크 모드 동작(JS) | `web/analytics.js`, `web/theme.js` | 파이썬 문자열 안에 JS를 다시 넣지 말 것 |
| 빌드 규칙 | `sitebuild/<역할>.py` (README의 코드 위치 참고) | `build_site.py`에는 main()만 |

- `site.toml`은 TOML 규칙을 지킵니다. `[표 이름]` 아래 줄은 다음 `[표 이름]`까지 그 표에 속하고, 표 밖의 값은 파일 맨 위에만 둡니다.
- 사이트에 나가는 파일은 `index.html`, `tree.md`, `lecture/index.html`, `site.toml [files]`에 등록한 파일뿐입니다. 그림은 index.html 안에 data URI로 넣습니다. `pages/` 안의 나머지 파일(제작 스크립트·캡처·DESIGN.md·구성안)은 빌드가 무시합니다.
- 강사님 강의 HTML(`lecture/index.html`)은 고치지 않습니다. 강의 교재 PDF는 넣지 않습니다.
- `auto_release.sh`는 `build_site.py`를 import해서 `LECTURES`, `SETUP`, `read_days`를 씁니다. 이 이름을 바꾸거나 옮기지 마세요. `auto_release.sh`·`sync_*.py`의 위치도 바꾸지 마세요(launchd와 스크립트가 이 경로를 씁니다).

## 2. 고친 뒤 확인

```bash
make check                 # 파이썬·JS 검사 → release 빌드 검사 → main 빌드 검사 (끝나면 public/은 main 빌드)
make serve                 # http://localhost:8000 에서 직접 보기
```

- **결과가 바뀌면 안 되는 정리 작업**(코드 옮기기·이름 정리)은 `make snapshot AS_OF=YYYY-MM-DD` → 수정 → `make compare AS_OF=YYYY-MM-DD`로 빌드가 바이트 단위로 같은지 확인합니다. 날짜를 고정하지 않으면 18:20 기준일 때문에 결과가 달라질 수 있습니다.
- 화면을 바꿨으면 바뀐 페이지를 실제로 열어 봅니다. 다크 모드가 있는 페이지는 두 모드 모두 봅니다.
- GA 이벤트를 바꿨으면 `?ga_debug=1`을 붙여 실제 사이트에서 GA DebugView로 확인합니다. 미리보기·로컬에서는 GA가 아무것도 보내지 않습니다.

## 3. 브랜치와 배포

| 브랜치 | 역할 |
|---|---|
| `main` | 작업용. push하면 Vercel 미리보기만 생김 |
| `deploy` | 실제 사이트. **`release: …` 커밋으로만** 올림 (main의 fast-forward가 아님) |

배포 순서 (항상 이 순서):
1. main에 커밋하고 push합니다.
2. **그 main 커밋**으로 임시 worktree에서 `uv run build_site.py --release`를 실행합니다.
3. `origin/deploy`의 worktree에 `public/`과 `vercel.json`을 `rsync -a --delete --checksum`으로 덮어씁니다. `--checksum`을 빼면 크기·수정 시각이 같은 파일(예: `600px`→`760px`처럼 길이가 같은 수정)이 건너뛰어집니다.
4. `LOG.md`에 한 줄 쓰고, `release: <무엇> (공개 전 … 제외)`로 커밋해 deploy에 push합니다.
5. 실제 사이트에서 바뀐 페이지를 확인합니다. 확인 전에는 "배포했다"고 말하지 않습니다.

- 배포 전에 `git log origin/deploy`를 봅니다. 다른 세션이 이미 배포했을 수 있습니다.
- **deploy에 force push 금지.** 공개 전 페이지(`site.toml`에서 `public = false`)가 있으면 main 빌드를 그대로 올리지 않습니다.
- 다음 수업일 자료는 **전날 18:20**에 `auto_release.sh`(launchd)가 origin/main으로 자동 배포합니다. 그래서 main에는 **언제 배포돼도 괜찮은 상태만** 올립니다. 큰 개편은 별도 브랜치에서 하고, 검증이 끝난 뒤 합칩니다.
- 사용자가 "배포해 줘"라고 해도 합의한 내용만 내보냅니다. 공개 전 자료의 공개 일정을 지킵니다.

## 4. 여러 세션이 동시에 일할 때

- 이 폴더는 여러 AI 세션이 함께 씁니다. **`git add -A`나 `git add .` 금지.** 내가 고친 파일만 이름으로 add합니다.
- 큰 작업은 `git worktree add`로 따로 폴더를 만들어 합니다.
- 커밋 전에 `git status`·`git diff --cached`로 남의 작업이 섞이지 않았는지 봅니다.

## 5. 기록과 커밋

- 작업 단위마다 `LOG.md`에 한 줄(날짜 | 페이지 | 한 일 | 상태)을 씁니다. 페이지별 제작 기록은 그 폴더의 `DESIGN.md`에 씁니다.
- 커밋 메시지: `type(scope): 한국어 설명` + 짧은 본문. 예: `feat(llm): Day25 Colab 실습 폴더 링크 등록`
- 디자인 원칙은 `DESIGN.md`. 용어는 실제 기술 용어(SQL 키워드, 라이브러리 이름)를 그대로 씁니다.
