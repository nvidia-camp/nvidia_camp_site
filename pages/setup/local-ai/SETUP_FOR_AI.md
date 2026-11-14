# OpenCode + 로컬 AI 모델 설치 가이드 (AI 에이전트 실행용)

> 2026-11-14 강사 PC에서 검증한 순서입니다. 화면 캡처는 https://nvidiasesac.vercel.app/setup/local-ai/ 에 있습니다.

---

## 학생에게

이 파일을 AI 코딩 에이전트(Claude Code 등)에게 주고 이렇게 말하세요.

> "이 문서대로 내 PC에 OpenCode와 로컬 AI 모델을 설치해줘."

- AI가 명령을 실행하기 전에 승인을 요청합니다. **명령이 무엇을 하는지 읽고 승인하세요.**
- 🙋 표시가 있는 단계는 **여러분이 직접** 해야 합니다. 설치 가이드 페이지의 화면 캡처(빨간 네모)를 따라 하면 됩니다.
- 전체 소요 시간: 약 30분 (모델 다운로드 13GB 포함)

### 완료되면 이렇게 됩니다

| 항목 | 설정 |
|---|---|
| 로컬 AI 모델 | `gpt-oss:20b` — 내 PC의 GPU에서 실행, 코드가 외부로 나가지 않음 |
| 기억할 수 있는 대화 길이 | 64K (이 PC의 최적값) |
| 모델 유지 시간 | 1시간 (다시 물을 때 로딩 대기 없음) |
| OpenCode 기본 모델 | 로컬 모델로 고정 (클라우드로 시작하지 않음) |
| 안전 설정 | `git push` 등은 실행 전에 확인, `git push --force` 등은 차단 |

---

## AI 에이전트에게 (지시사항)

너는 학생의 Windows PC에 OpenCode와 로컬 LLM 환경을 설치한다. 다음 규칙을 지켜라.

1. 각 단계는 **실행 → 확인 명령 → 성공 기준 판정** 순서로 진행한다. 성공 기준을 만족하지 못하면 다음 단계로 넘어가지 말고 원인을 설명한다.
2. 🙋 단계에서는 멈추고, 학생이 무엇을 해야 하는지 한국어로 짧게 안내한 뒤 완료를 확인받는다.
3. 이 문서에 없는 프로그램을 설치하거나, 시스템 설정을 임의로 바꾸지 않는다. **이미 있는 설정 파일은 덮어쓰지 않는다** (5단계 참고).
4. 모든 명령은 PowerShell 기준이다.
   - `ollama`를 인자 없이 실행하지 않는다 (대화형 메뉴가 떠서 멈춤). 항상 `ollama --version`, `ollama pull ...`처럼 하위 명령을 붙인다.
   - `opencode`를 인자 없이 실행하지 않는다 (대화형 화면). 확인용으로는 `opencode --version`, `opencode debug config`, `opencode run "..."`만 사용한다.
5. 설치 직후 `ollama`/`node`/`npm`/`opencode`를 찾지 못하면, 너의 셸이 설치 전에 시작되어 PATH가 갱신되지 않은 것이다. 아래로 PATH를 다시 읽은 뒤 재시도한다:
   `$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')`
6. 마지막에 "최종 확인" 표를 채우고, "사용 전 꼭 기억할 것"을 학생에게 그대로 보여준다.

### 대상 사양 (이 문서가 가정하는 PC)

- Windows 11, NVIDIA RTX 5080 Laptop (VRAM 16GB), RAM 32GB
- 사양이 다르면 0단계에서 멈추고 학생에게 강사에게 문의하라고 안내한다.

### 설치되는 것 (강사 PC 검증 버전, 2026-11-14)

| 프로그램 | 버전 | 설치 위치 |
|---|---|---|
| Node.js LTS (npm 포함) | v26.13.1 / npm 11.20.0 | `C:\Program Files\nodejs` |
| Ollama | 0.40.16 | `%LOCALAPPDATA%\Programs\Ollama` |
| 모델 `gpt-oss:20b` | 13GB | `%USERPROFILE%\.ollama\models` |
| OpenCode (v2) | 2.3.0 | `%APPDATA%\npm` |
| OpenCode 설정 | — | `%USERPROFILE%\.config\opencode\` (`opencode.jsonc`, `AGENTS.md`) |

---

## 0단계. 사전 점검

```powershell
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv
[math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory/1GB,1)
[math]::Round((Get-PSDrive C).Free/1GB,1)
node -v
Get-ExecutionPolicy -List
Test-Path "$HOME\.config\opencode\opencode.jsonc", "$HOME\.config\opencode\AGENTS.md"
```

성공 기준:
- GPU 메모리 16000 MiB 이상, 드라이버 551.61 이상
- RAM 30GB 이상
- C: 여유 공간 **40GB 이상** (모델 파일 때문)
- `node -v`가 v20 이상 → 명령을 못 찾으면 1-1단계 수행
- 실행 정책과 설정 파일 존재 여부(`True`/`False`)를 기록해 둔다 (4·5단계에서 사용)

## 1단계. 필수 프로그램 설치

### 1-1. Node.js LTS (없을 때만)

Node.js를 설치하면 npm이 함께 설치된다. npm을 따로 설치하지 않는다.

```powershell
winget install --id OpenJS.NodeJS.LTS -e --accept-package-agreements --accept-source-agreements
```

- 🙋 관리자 권한(UAC) 창이 뜨면 학생이 "예"를 누른다.
- winget이 안 되면 🙋 학생이 https://nodejs.org/ko/download 에서 **"Windows 설치 프로그램 (.msi)"** 버튼으로 설치한다.
  같은 페이지 위쪽의 fnm 방식은 PowerShell 프로필 설정이 추가로 필요하므로 **사용하지 않는다**.

확인 (PATH 재로딩 후): `node -v` → `v26.x.x`, `npm -v` → `11.x.x`

### 1-2. Ollama

Ollama 공식 설치 스크립트를 사용한다 (설치 파일의 디지털 서명을 검사한 뒤 설치함). **관리자 권한이 필요 없다.**

```powershell
irm https://ollama.com/install.ps1 | iex
ollama --version
```

성공 기준: `ollama version is 0.x.x` 출력. 설치 후 Ollama가 백그라운드(트레이)에서 자동 실행된다.

## 2단계. Ollama 설정

### 2-1. 모델 유지 시간 1시간 (에이전트가 실행)

Ollama는 5분 동안 쓰지 않으면 모델을 내려서, 다시 쓸 때 약 10초씩 로딩한다.

```powershell
setx OLLAMA_KEEP_ALIVE 1h
```

성공 기준: `성공: 지정한 값을 저장했습니다.` (적용은 2-3단계 재시작 후)

### 2-2. 🙋 컨텍스트 길이 64K (학생이 앱에서)

OpenCode는 64K 이상 컨텍스트가 필요하다. VRAM 24GB 미만 PC의 Ollama 기본값은 **4K**라서 반드시 바꿔야 한다.

학생에게 안내:

1. 시작 메뉴에서 **Ollama** 앱을 연다. (첫 화면의 Apps 목록 — OpenCode 등 — 은 **누르지 않는다**. OpenCode는 4단계에서 따로 설치한다.)
2. 왼쪽 사이드바에서 **Settings**
3. **Context length** 슬라이더를 **64k**로 옮긴다.

- **64k보다 크게 올리지 않는다.** 128k는 VRAM 16GB를 넘어 21%가 CPU로 밀려나 느려진다 (강사 PC 실측).
- 같은 화면의 "Expose Ollama to the network"는 **꺼진 상태 그대로** 둔다.

### 2-3. Ollama 재시작 (에이전트가 실행)

2-1의 환경변수를 적용하려면 Ollama를 재시작해야 한다. 학생이 2-2를 마쳤다고 확인한 뒤 실행한다.

```powershell
Get-Process "ollama app","ollama" -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep 2
$env:OLLAMA_KEEP_ALIVE = "1h"   # 이 셸에서 실행하는 Ollama에도 확실히 적용
Start-Process "$env:LOCALAPPDATA\Programs\Ollama\ollama app.exe"
Start-Sleep 5
Get-Process "ollama app","ollama" | Select-Object Name,Id,StartTime
```

성공 기준: `ollama app`, `ollama` 두 프로세스가 방금 시각으로 실행 중.

- 이 방법이 안 되면 🙋 학생에게: 트레이의 **Ollama 아이콘 우클릭 → Quit** → 시작 메뉴에서 **Ollama 다시 실행**

## 3단계. 모델 다운로드 및 GPU 확인

```powershell
ollama pull gpt-oss:20b
```

- 약 13GB, 24MB/s 기준 약 9분. 마지막에 `success`가 나오면 완료.
- 중간에 끊기면 같은 명령을 다시 실행하면 이어 받는다.

확인 (두 명령을 연달아 실행):

```powershell
ollama run gpt-oss:20b "안녕" --verbose
ollama ps
nvidia-smi --query-gpu=memory.used --format=csv,noheader
```

성공 기준 (강사 PC 실측값):

| 확인 | 기준 | 다르면 |
|---|---|---|
| 응답 | 한국어 답이 나옴 (`Thinking...`은 모델의 생각 과정으로 정상) | |
| `eval rate` | 약 80 tokens/s | 40 미만이면 PROCESSOR 확인 |
| PROCESSOR | **`100% GPU`** | 게임·브라우저 등 GPU 쓰는 프로그램 종료 |
| CONTEXT | **`65536`** | 4096이면 2-2단계 다시 |
| UNTIL | **`59 minutes from now`** 근처 | `4 minutes`면 2-3단계 다시 |
| VRAM 사용 | 약 **14,100 MiB** | `ollama ps`의 SIZE(12GB)는 실제보다 작게 표시됨 |

> 컨텍스트 설정을 바꿀 때는 먼저 `ollama stop gpt-oss:20b`로 모델을 내린다. 모델이 올라간 상태에서 다른 컨텍스트로 요청하면 Ollama 실행기가 CUDA 오류로 종료될 수 있다 (강사 PC에서 발생).

## 4단계. OpenCode 설치

OpenCode **v2** 패키지(`@opencode/cli`)를 설치한다.
**`opencode-ai` 패키지는 구버전(v1)이므로 설치하지 않는다** (Ollama 연동 문서에 남아 있는 옛 명령).

```powershell
npm install -g --allow-scripts=@opencode/cli @opencode/cli
opencode --version
```

성공 기준: `opencode v2.x.x` 출력.

- `--allow-scripts` 없이 설치하면 `npm warn install-scripts` 경고가 나오지만 동작에는 문제없다.
- "이 시스템에서 스크립트를 실행할 수 없으므로" 오류 → PowerShell 실행 정책 문제. 학생에게 설명하고 승인받은 뒤:
  `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (현재 사용자에게만 적용, 관리자 권한 불필요)

## 5단계. OpenCode 추천 설정

두 파일을 `$HOME\.config\opencode\`에 만든다.
**0단계에서 이미 있다고 나온 파일은 덮어쓰지 말고**, 학생에게 기존 내용과 아래 내용을 보여준 뒤 합칠지 물어본다.

```powershell
New-Item -ItemType Directory -Force "$HOME\.config\opencode" | Out-Null
```

### 5-1. `opencode.jsonc` — 기본 모델과 안전 규칙

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  // 기본 모델: 로컬 Ollama (첫 화면이 클라우드 모델로 시작하지 않게)
  "model": "ollama/gpt-oss:20b",
  // 되돌리기 어려운 명령은 실행 전에 묻거나 막는다 (아래 규칙이 우선)
  "permissions": [
    { "action": "shell", "resource": "git push *", "effect": "ask" },
    { "action": "shell", "resource": "git reset --hard*", "effect": "ask" },
    { "action": "shell", "resource": "git clean *", "effect": "ask" },
    { "action": "shell", "resource": "git push --force*", "effect": "deny" },
    { "action": "shell", "resource": "gh repo delete *", "effect": "deny" }
  ]
}
```

### 5-2. `AGENTS.md` — 모든 프로젝트에 적용되는 기본 안내

로컬 모델은 매 요청마다 이 내용을 읽으므로 **짧게** 유지한다.

```markdown
# 환경
- Windows 11, PowerShell. bash 명령(head, grep, ls -la 등) 대신 PowerShell 명령을 사용한다.
- 답변과 설명은 한국어로 한다.

# 작업 규칙
- 파일을 고친 뒤에는 반드시 실행해서 결과를 확인하고, 확인한 결과를 보여준다.
- 테스트 파일은 요청이 없으면 수정하지 않는다.
- 새 패키지 설치나 git push 전에는 먼저 물어본다.

# 사용할 수 있는 CLI
- 최신 라이브러리 문서: `npx ctx7 library <이름> "<질문>"` → `npx ctx7 docs <ID> "<질문>"`
- 파이썬 패키지: pip 대신 `uv` (`uv run`, `uv add`)
```

> 마지막 `uv` 줄은 학생 PC에 `uv`가 없으면 빼거나, `winget install astral-sh.uv` 설치 여부를 학생에게 물어본다.

### 5-3. 설정 확인

```powershell
opencode reload
opencode debug config
mkdir $HOME\opencode-test -Force | Out-Null
cd $HOME\opencode-test
opencode run "ok 라고만 답해"
```

성공 기준:
- `opencode reload` → `Configuration reloaded`
- `debug config` 출력에 `"providerID": "ollama"`, `"model": "gpt-oss:20b"`와 `permissions` 5개가 보임
- `opencode run` → `ok` 응답 (로컬 모델이 OpenCode를 통해 응답함)

## 6단계. 🙋 OpenCode 실행 및 모델 확인

에이전트는 아래를 안내만 하고, 학생이 **새 PowerShell 창**에서 직접 한다.

1. 테스트 폴더에서 OpenCode를 실행한다.

   ```powershell
   cd $HOME\opencode-test
   opencode
   ```

   - OpenCode는 실행한 폴더의 파일을 직접 읽고 고친다. 처음에는 **빈 폴더**에서 시험한다.
   - `$HOME`은 내 사용자 폴더(`C:\Users\<내 이름>`)를 뜻한다.

2. 입력창 아래가 **`gpt-oss:20b Ollama`** 인지 확인한다 (5단계 설정 덕분에 바로 로컬 모델이어야 정상).

3. ⚠️ 만약 **`Iceman Free OpenCode`**(클라우드 무료 모델)로 보이면, 이 상태로 질문하면 외부 서버로 전송된다. 아래 순서로 바꾼다.

   - 입력창에 `/models` 입력 → **Switch model** 선택

   - `gpt`로 검색 → **`gpt-oss:20b`** 선택

## 7단계. 🙋 첫 작업 테스트

학생이 OpenCode 입력창에 다음을 입력한다:

```
hello.py 파일을 만들고, "Hello, OpenCode!"를 출력하는 프로그램을 작성한 뒤 python으로 실행해서 결과를 보여줘
```

- 명령 실행 승인 요청이 나오면 내용을 읽고 허용한다.
- 성공 기준: `opencode-test` 폴더에 `hello.py`가 생기고, 화면에 실행 결과 `Hello, OpenCode!`가 보인다.
- 에이전트는 학생이 끝냈다고 하면 확인한다: `Get-Content $HOME\opencode-test\hello.py`

## 8단계. (선택) 추천 CLI 도구

학생에게 설치할지 먼저 물어본다. AI가 터미널에서 직접 쓰는 도구들이며, MCP보다 컨텍스트를 적게 쓴다.

| 도구 | 용도 |
|---|---|
| `gh` | GitHub 이슈·PR·CI 실패 로그 |
| `uv` | 파이썬 실행·패키지 관리 (pip 대신) |
| `ruff` | 파이썬 오류 검사·자동 수정 |
| `gitleaks` | 커밋 전 비밀번호·API 키 유출 검사 |
| `jq` | 긴 JSON 출력에서 필요한 값만 추출 |

```powershell
winget install GitHub.cli astral-sh.uv astral-sh.ruff Gitleaks.Gitleaks jqlang.jq --accept-package-agreements --accept-source-agreements
```

- 이미 설치된 도구는 건너뛴다. 여러 개를 한 번에 설치하지 못하면 하나씩 설치한다.
- 설치 후 PATH 재로딩(지시사항 5번), 확인: `gh --version`, `uv --version`, `ruff --version`, `gitleaks version`, `jq --version`
- 🙋 `gh auth login` — GitHub 계정 로그인은 학생이 직접 한다 (브라우저 인증). 에이전트는 대신 로그인하거나 토큰을 다루지 않는다.
- 설치한 도구는 5-2단계 `AGENTS.md`의 "사용할 수 있는 CLI"에 한 줄씩 추가한다:

```markdown
- 파이썬: 파일을 고친 뒤 `ruff check`
- GitHub: `gh` (출력은 `--json 필드 --limit N`으로 줄이기). CI 실패는 `gh run view --log-failed`
- 커밋 전: `gitleaks dir . -v`
```

자세한 활용법: https://nvidiasesac.vercel.app/setup/cli/

## 최종 확인

| 항목 | 결과 | 강사 PC 기준값 |
|---|---|---|
| Node.js / npm 버전 | | v26.13.1 / 11.20.0 |
| Ollama 버전 | | 0.40.16 |
| 모델 | | gpt-oss:20b |
| PROCESSOR (`ollama ps`) | | 100% GPU |
| CONTEXT (`ollama ps`) | | 65536 |
| UNTIL (`ollama ps`) | | 59 minutes from now |
| eval rate (tokens/s) | | 82.8 |
| VRAM 사용 (`nvidia-smi`) | | 약 14,100 MiB |
| OpenCode 버전 | | 2.3.0 |
| OpenCode 기본 모델 (`debug config`) | | ollama / gpt-oss:20b |
| OpenCode 화면 모델 표시 | | gpt-oss:20b Ollama |
| 7단계 테스트 | 성공 / 실패 | hello.py 생성 |

## 학생에게: 사용 전 꼭 기억할 것

설치가 끝나면 에이전트는 학생에게 아래 5가지를 그대로 보여준다.

1. AI가 "완료했다"고 해도 **직접 확인**하세요 (파일이 바뀌었는지, 실행 결과가 맞는지).
2. 작업 전에 **git 커밋**으로 저장점을 만드세요. 잘못되면 `/undo`.
3. 주제가 바뀌면 **`/new`**. 화면의 컨텍스트 %는 128K 기준이라 **50% 근처면 이미 한계(64K)** 입니다.
4. **작게** 시키세요. 큰 작업은 `Shift+Tab`으로 Plan에서 계획부터.
5. 입력창 아래가 **`gpt-oss:20b Ollama`** 인지 확인하세요. 아니면 외부 서버로 전송됩니다.

## 문제 해결

| 증상 | 원인 / 조치 |
|---|---|
| `ollama` / `node` / `opencode` 명령을 찾을 수 없음 | 설치 직후 PATH 미반영 → 🙋 터미널 재시작 (에이전트는 지시사항 5번으로 PATH 재로딩) |
| `ollama`만 입력했더니 메뉴가 뜸 | 정상. `Esc`로 닫고 하위 명령(`ollama pull` 등)을 사용 |
| CONTEXT가 4096 | 2-2단계 설정이 안 됨 → Ollama 앱 Settings에서 64k 확인 |
| UNTIL이 `4 minutes from now` | 2-3단계 재시작이 안 됨 → Ollama 재시작 |
| PROCESSOR에 CPU 비율이 높음 | 다른 프로그램이 VRAM 사용 중이거나 컨텍스트를 64k보다 크게 설정함 |
| `llama-server process has terminated ... CUDA error` | 모델이 올라간 상태에서 설정이 바뀜 → `ollama stop gpt-oss:20b` 후 다시 실행 |
| OpenCode 입력창 아래가 `Iceman Free OpenCode` | 클라우드 모델 상태 → 6단계 3번으로 로컬 모델 선택, 5-3단계 설정 확인 |
| OpenCode가 파일을 수정하지 않고 말로만 답함 | 도구 호출 실패 → 모델이 `gpt-oss:20b Ollama`인지, CONTEXT 65536인지 확인 |
| "스크립트를 실행할 수 없으므로" | 실행 정책 → 4단계의 `Set-ExecutionPolicy` 안내 |
| 다운로드가 매우 느림 | 네트워크 문제 → 강사에게 문의 (USB로 모델 파일 배포 가능) |
| `nvidia-smi`가 없음 | NVIDIA 드라이버 미설치 → 🙋 강사에게 문의 |
