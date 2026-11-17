# Git · GitHub 가이드

공통 기준: [사이트 DESIGN.md](../../../DESIGN.md). 스타일 토큰과 코드 블록·셸 탭·복사 버튼은 `setup/python-venv`와 같다.

## 구성 (2026-11-17 초안)

- Part 1 기본 가이드: 0 큰 그림 → 1 처음 한 번 → 2 매일 루프 → 3 upstream → 4 브랜치·머지 → 5 되돌리기 → 6 .gitignore → 7 치트시트.
- Part 2 실전 세팅(맨 아래): 강사님 실습 저장소를 upstream(push 막음)으로, 내 빈 저장소를 origin으로 두고 날짜 폴더만 `git restore -s upstream/main -- 폴더`로 가져온다. 기준 저장소: nvidia-camp/practice의 GIT_ROUTINE.md. 사용자 결정: 이 방식은 기본 가이드의 3번에 해당하는 실제 상황 세팅이라 중심이 아니고 맨 아래에 둔다.

## 움직이는 그림

- 사용자가 가장 중요하게 본 부분: 작업 폴더 → Staging → 로컬 저장소 → GitHub의 위계와 이동.
- 외부 라이브러리 없이 HTML 칸 + 절대 위치 카드(transform 전환)로 만든다. 칸 위치를 매번 측정해 배치하므로 화면 폭이 바뀌어도 맞는다(ResizeObserver).
- 단계 버튼을 누르면 처음 상태에서 앞 단계를 즉시 재생한 뒤 그 단계만 움직인다. 화면에 들어오면 자동 재생하고, 버튼을 누르면 수동으로 바뀐다. `prefers-reduced-motion`이면 자동 재생과 이동 효과를 끈다.
- 그림 아래에 실제 입력 명령(어두운 터미널 줄), 한 줄 설명, `git status`·출력 한 줄을 둔다. 출력 문구는 임시 저장소에서 실제로 나온 문장이다.
- 브랜치 그림은 SVG: 커밋 원·선이 차례로 그려지고, 이름표(main·feature)와 HEAD가 이동한다.

## 코드 표기

- 한 줄에 명령 하나, 오른쪽에 짧은 주석. git 명령은 PowerShell·Git Bash가 같으므로 "PowerShell · Git Bash 공통" 블록으로 쓰고, 셸마다 다른 줄(`curl.exe`/`curl`)만 탭으로 나눈다.
- PowerShell에서 깨지는 문법(`@{1}` 등)은 쓰지 않는다.
