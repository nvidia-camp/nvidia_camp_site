# Python 가상환경 가이드

공통 기준: [사이트 DESIGN.md](../../../DESIGN.md), 개인 스킬 `sesac-html-design`의 디자인 기준과 구현 토큰.

## 터미널 활성화와 VS Code 선택 (2026-11-15)

- 기존 PDF 팔레트를 재사용한다. 남색 `--color-primary`, 연한 청색 `--color-soft`, 본문·보조 글자·테두리도 기존 토큰을 사용하며 새 색상은 추가하지 않는다.
- 기존 카드 반경과 간격을 유지한다. 두 실행 경로는 데스크톱에서 같은 너비로 나란히, 720px 이하에서는 터미널 → VS Code 순서로 쌓는다.
- 도식은 실제 HTML 텍스트·순서 목록으로 만든다. 키보드·화면 읽기·오프라인 다운로드에서도 내용을 읽을 수 있다.
- 같은 환경 폴더를 두 곳에서 선택하는 예시를 보여 준다. 터미널의 PATH 변경, VS Code의 인터프리터 선택, 새 통합 터미널의 자동 활성화 가능성을 구분한다.
- 비교 결과는 `sys.executable`로 확인한다. 기대 경로는 예시이며 Windows 실측 결과로 소개하지 않는다. `.ipynb`의 커널 선택은 별도로 안내한다.
- 근거: [Python venv 동작](https://docs.python.org/3.13/library/venv.html#how-venvs-work), [VS Code Python 환경](https://code.visualstudio.com/docs/python/environments), [커널 선택](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management). 2026-11-15 확인.
