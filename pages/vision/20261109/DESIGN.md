# Day16 oneday 요약 · 디자인 기록

## 목적

Day16(2026-11-09, Vision·멀티모달 AI 응용 4/4) 수업을 처음 배우는 사람이 한 장으로 파악하게 한다. 문서 이미지에서 값을 꺼낼 때 근거(원문·위치·점수)를 함께 남기고, 근거가 없는 값은 사람이 보도록 남기는 흐름이 중심이다.

## 사용자 지정 (이번 판에서 정한 것)

- 핵심 코드는 **초보자가 위에서 아래로 읽으면 이해되는 코드**: 축약 문법(한 줄 if…else, map, 중첩 호출) 없이, 중간 결과에 이름을 붙이고, import를 모두 적는다.
- 함수를 부를 때 **파라미터 이름을 모두 적는다**(`cv2.adaptiveThreshold(src=page, maxValue=255, ..., blockSize=31, C=11)`). 이름은 공식 문서의 파라미터 이름이다. 인자가 셋 이상이면 한 줄에 하나씩 쓰고 뜻을 주석으로 단다. `getPerspectiveTransform(src=dst, ...)`처럼 헷갈리지 않게 정면 모서리 변수는 `front`로 부른다. 핵심 코드는 98줄 → 132줄이 됐다.
- 코드는 **그대로 실행된다**: pip OpenCV에는 예제 이미지가 없어 `skimage.data.page()`(내장 스캔)와 `cv2.putText`로 그린 청구서를 쓴다. VLM도 실제로 호출한다(SmolVLM-256M).
- 같은 코드를 노트북으로 공유한다. 이 폴더의 `Day16_핵심코드.ipynb`(로컬 Jupyter)와 Colab https://colab.research.google.com/drive/1Y4kNNXgtcSb3C9V-so_3avv-qtU2RNBS (work 계정)는 `build_nb.py`가 같은 셀로 만든다.
- 교시별 핵심은 **핵심 질문과 개념(한 줄 뜻)만**. 난이도 계단, "응용·심화는 무엇을 더 요구하나", 전체 파라미터 지도는 뺐다.
- 함수는 표가 아니라 **사용 가이드**: 용도 / 사용법 / 확인할 점.
- 긴 이론 설명은 넣지 않고, 실측 그림이 대신 보여 준다.

## 색 근거

강의 PDF p.3 「오늘 만드는 문서 AI의 전체 구조」를 100dpi로 렌더링해 픽셀 빈도로 확인했다. Day13~15(`#E9F5EC`·`#FBF2DF`·`#F0ECF8`)와 값이 달라 Day16 값을 썼다.

| 토큰 | 값 | PDF p.3에서 |
|---|---|---|
| `--zone-ocr` | `#E9F3FC` | OCR용 전처리 · OCR 상자 |
| `--zone-vlm` | `#FFF3D8` | VLM 상자 |
| `--zone-check` | `#E9F5EE` | 구조화·검증 상자 |
| `--zone-deploy` | `#EEF1F6` | p.3에 없는 단계라 중립 회청색(파생값) |

교시 배지·구역 글자 색은 면 색을 어둡게 만든 **파생값**이다: `#245C9C`(OCR), `#7A4F0E`(VLM), `#2E6B45`(검증), `#4A5870`(배포). `build.py`가 흰 글자 대비 4.5:1 이상인지 검사한다. 결과 숫자 색: 나빠짐 `#8A4B2A`, 좋아짐 `#2E6B45`.

## 레이아웃 (1440px 세로 한 장)

1. **한 장으로 보는 문서 AI**: 문서 이미지 → [OCR 경로: 보정본 → 단어 Box → 값+근거] / [VLM 경로: 질문 → VLM → 답 후보] → 대조 → 근거와 함께 기록. 아래에 꼭 알 개념 3, 하루 약속 3.
2. **하루 전체 지도**: OCR 경로(1~3) → VLM 경로(4~5) → 배포 설계(6) → 통합·검증(7~8).
3. **교시별 핵심**: 교시 배지 + 핵심 질문, 개념 칩(이름 + 한 줄 뜻).
4. **코드로 보는 하루 흐름**: 흐름 띠 9칸 → 교시별 코드 블록 + 설명 → 함수 사용 가이드 카드 8장 → 파라미터 diff 14행(묶음 4개, 꼭 기억 7) + 묶음마다 실측 그림.

75rem 이하에서는 구조 그림·지도·코드 설명·diff 행이 세로로 쌓이고, 40rem 이하에서는 표 칸을 줄인다.

## 그림 데이터

| 그림 | 데이터 | 숫자 |
|---|---|---|
| 구조 그림 | 코드로 그린 청구서 사진 → 보정본 → 단어 Box | CER 0.008, 합계 33000 conf 95.5, VLM 질문 6개 중 채택 3 |
| 이진화 방법 3장 | 내장 스캔 페이지 | Gray 0.324 · Otsu(기준 157) 0.361 · Adaptive(31, 11) 0.057 |
| blockSize·C 막대 | 내장 스캔 페이지 | blockSize 3/15/31/101 → 0.137/0.050/0.057/0.084, C 0/11/30/60 → 0.388/0.057/0.020/0.221 |
| confidence 막대 | 보정본 단어 21개 | 오답 DOCO3 65.6, 나머지 92.8 이상 |
| VLM 질문 표 | 보정본 + SmolVLM-256M | 합계·공급자·발행일 채택, 세금 `0.`·할인액 `33000`·전화번호 `ALPHA STUDIO` 보류 |
| 모서리 순서 3장 | 비스듬한 청구서 사진 | 보정 0.008 · 시작점이 오른쪽 위 1.254(필드 0/3) · 두 점 맞바꿈 1.0(화면 99% 검정) |
| CER과 필드 표 | 보정본을 0.5·0.4배로 줄임 | 0.041 3/3 · 0.066 2/3(공급자 놓침) · 2배 확대 0.008 3/3 |

CER은 `jiwer.cer`, 공백·줄바꿈을 한 칸으로 정리한 뒤 계산했다. 스캔 페이지의 정답은 손으로 옮긴 7줄이다.

## 재검증 결과

- 가로 넘침: 375·768·1280·1440px 모두 0px. 스크립트 오류 없음.
- PDF: 1쪽(1440×9518px, 파라미터 이름을 단 뒤), `pdftotext`로 글자 추출됨.
- 1440px 스크린샷을 1,250px 구간으로 잘라 직접 확인하고 고친 것: 구조 그림 JSON 잘림, 6교시 제목 단어 중간 줄바꿈, 모서리 순서 그림이 전부 검은 화면(→ 시작점을 잘못 잡은 예로 교체), CER 1.0이 "1"로 표시, 375px에서 구조 그림이 세로 막대로 짓눌림.
- `build.py`는 파라미터 행의 결과 문장(구성안)에 실측 숫자가 들어 있는지 대조한다.
- 실측 환경: Tesseract 5.5.2, OpenCV 5.0.0, scikit-image 0.26.0, transformers 4.57.6, torch 2.14.0, SmolVLM-256M-Instruct(do_sample=False, Apple MPS).

## 노트북

- `build_nb.py`가 `구성안.md`의 핵심 코드 블록을 직접 읽어 셀을 만든다. 구성안 코드를 고치면 다시 실행해 두 노트북을 함께 갱신한다.
- 셀 39개: 설치(Colab에서만 동작) → import → 이미지 보기 준비 → 준비·1~7교시 → 바꿔 보기 ①~⑤ → VLM 질문.
- Colab에만 있는 `cv2_imshow`는 로컬에서 같은 이름의 함수(`cv2.imencode` → `IPython.display.Image`)로 대신한다.
- 로컬 실행: 커널 `Python (dl)`. `~/envs/dl`에 `opencv-python-headless`·`pytesseract`·`scikit-image`·`jiwer`를 추가했다(2026-11-09). Tesseract 엔진은 Homebrew.
- 함정: IPython은 셀 안에서 `>>> `로 시작하는 줄의 프롬프트를 지운다(문자열 안이어도). 스캔 페이지 정답의 끝줄 `>>> markers = ...`가 잘려 CER이 0.057 → 0.061로 달라졌다. 정답을 줄 목록(`page_lines`)으로 적어 고쳤다.
- 검증: `jupyter nbconvert --execute`(커널 dl)로 오류 0, 이미지 6장, 숫자가 위 그림 데이터 표와 일치. Drive 업로드 후 내려받은 파일이 로컬 Colab용 파일과 같음을 확인했다.
- 실행하면 이 폴더에 `invoice.png`, `doc03.json`이 생긴다(노트북 출력물, 배포 대상 아님).

## 다시 만드는 명령

```bash
cd site/pages/vision/20261109
uv run --project ~/envs/dl --with opencv-python-headless --with pytesseract \
    --with scikit-image --with jiwer python make_figures.py     # facts.json (Tesseract 엔진 필요)
python3 build.py                                                 # index.html
uv run render.py index.html Day16_oneday요약.pdf [스크린샷 폴더]  # PDF + 폭별 검증
python3 build_nb.py [colab용.ipynb]                                # Day16_핵심코드.ipynb (+ Colab 업로드용)
```

`make_figures.py`는 실행 중 `_work/invoice.png`를 만든다(VLM 입력용). 배포 대상이 아니라 실행 뒤 지웠다.

## 파일

| 파일 | 역할 |
|---|---|
| `구성안.md` | 내용·흐름 원고. `build.py`가 문장·표·코드를 직접 읽는다 |
| `make_figures.py` | 핵심 코드와 같은 데이터로 OCR·VLM을 실제 실행 → `facts.json` |
| `facts.json` | 실측 숫자 + base64 PNG |
| `template.html` | 고정 문구와 CSS |
| `build.py` | 구성안 + facts → `index.html` |
| `render.py` | 폭별 검증 + 세로 한 장 PDF |
| `index.html` | 오프라인 단일 HTML |
| `Day16_oneday요약.pdf` | 배포용 세로 한 장 PDF |
| `build_nb.py` | 구성안 핵심 코드 → 노트북 (로컬·Colab) |
| `Day16_핵심코드.ipynb` | 로컬 Jupyter용 노트북 (커널 Python (dl)) |
