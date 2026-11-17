# Docker 가이드

공통 기준: [사이트 DESIGN.md](../../../DESIGN.md). 스타일 토큰·그림 엔진·탭은 `setup/git`과 같다.

## 구성 (2026-11-17 초안, 미공개)

- 사용자 요청: Git 가이드처럼 만든다. 핵심은 애니메이션, 예외 대응보다 핵심 줄기.
- 이전 판(설치 → 명령 표 → Compose → '막히면' 6줄)은 구조가 안 보여 이해가 어렵다는 의견 → 탭 4쪽으로 다시 씀.
- ① 기본(`/setup/docker/`) · ② Dockerfile · build(`build/`) · ③ port · volume(`port-volume/`) · ④ compose(`compose/`).
- 설치(WSL 2 · Docker Desktop · hello-world)는 ① 안의 접힌 토글. '막히면' 표는 없애고 "Docker Desktop 켜고 기다리기" 한 줄만 남김.
- 용어는 영어 원어(image · container · port · volume · compose).

## 움직이는 그림

- ① Docker Hub → `pull` → 이미지 → `run` → 컨테이너 → `-p` → 브라우저. stop은 점선(멈춤), rm은 컨테이너만 사라지고 이미지는 남음, run 다시는 pull 없이.
- ② 프로젝트 폴더 → `build` → 이미지(FROM · COPY · CMD 층이 하나씩 쌓임) → `run` → 컨테이너(실행 중 → 종료). app.py 수정 후 build 다시: FROM 층은 CACHED.
- ③ 두 그림. port: `-p` 없이 접속 실패(통로가 흔들림) → `-p 8080:80`으로 다시 → 성공. volume: `-v` 없이 rm하면 데이터도 사라짐 → `-v pgdata:...` → rm해도 볼륨에 남음 → 다시 연결.
- ④ compose.yaml → `up` → web · db 컨테이너 + 볼륨 → `down`은 컨테이너만 지움 → `up` 다시.
- 컨테이너 칸은 굵은 테두리(`.zone.wall`) = 벽으로 막힌 상자.
- 엔진은 Git 가이드의 tokenOps에 `label`(화살표 글자 바꾸기) · `cls`(화살표 상태) · 칸별 카드 최소 폭(`data-minw`)을 더함.

## 코드 표기

- docker 명령은 한 줄로 쓰면 PowerShell · Git Bash가 같으므로 모두 "공통" 블록. 줄 이어 쓰기(`` ` `` / `\`)와 `-it`(Git Bash에서 winpty 필요), 현재 폴더 바인드 마운트(`${PWD}` / `$(pwd)`)는 쓰지 않는다.
- Dockerfile은 줄 끝 주석을 붙이지 않는다(인자로 읽힘). 설명은 옆 표로.
- 명령·출력은 Docker 29.0.1(Docker Desktop)에서 실제로 실행해 확인(2026-11-17). postgres 18 이미지의 데이터 경로는 `/var/lib/postgresql`.
