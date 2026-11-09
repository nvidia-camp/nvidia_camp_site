# Day15 oneday 요약 · 설계 메모

## 목적

수강생이 하루치 내용을 한 장으로 파악하게 한다. 오늘 무엇을 배우는지, 어떤 파라미터를 이해해야 하는지가 중심이다. 오늘의 목표는 YOLO 내부 구조가 아니다. **탐지 결과를 채점하는 기준을 알고, YOLO 설정을 바꿨을 때 결과가 왜 달라지는지 설명하는 것**이다.

- 내용과 흐름: `구성안.md`
- 배포본: `index.html`(오프라인 단일 파일)과 `Day15_oneday요약.pdf`(1440px 폭 세로 한 장)

## 사용자 지정

**흐름과 코드**
- 흐름은 강의를 따른다. 코드는 **공식 문서의 기본 사용법**을 따르고, 단순하고 핵심만 남긴다.
- 관례적인 이름만 쓴다(`results`, `result`, `metrics`). 직접 구현보다 공식 API를 쓴다(`box_iou`, `box_convert`).
- 줄마다 출처 문서를 적고, 설치된 버전에서 실제로 실행해 확인한다.
- 강의 코드와 문서의 사소한 차이는 따로 적지 않는다.

**YOLO 개념**
- 개념은 세 가지만 넣는다: 격자 칸마다 후보, 세 가지 크기의 격자, conf와 NMS의 두 단계 거름.
- 1구역의 실측 깔때기 그림 하나로 설명한다. 앵커, 손실 함수, 층 이름은 넣지 않는다.

**문서 형식**
- 제목: "객체 탐지와 YOLO 학습·추론·추적"
- 실측: 8개, "꼭 기억" 7개
- 하단 참고는 짧게 둔다(모델을 만든 방법, 환경, 합성 데이터).

## 색

강의 PDF p.3·p.4를 100dpi로 렌더링해 확인했다. Day13·Day14와 같은 면 색이다.
- 면: `#F0F6FD` · 준비 `#E9F5EC` · 학습 `#FBF2DF` · 설명 `#F0ECF8`
- 구역 글자·배지(면 색을 어둡게 만든 파생값): `#2E6B45` · `#7A4F0E` · `#54458A`

하루 지도는 강의 p.11의 네 묶음을 따른다.

| 묶음 | 교시 | 색 |
|---|---|---|
| 좌표·라벨·지표 | 1~3 | 초록 |
| 학습·검증 | 4~5 | 노랑 |
| 추론·추적 | 6~7 | 보라 |
| 통합 | 8 | 흰 면 + 남색 |

결과 숫자의 색: 나빠짐 `#8A4B2A`, 좋아짐 초록, 중립 남색. 그림의 TP는 초록, FP는 주황 `#C0703E`이다.

## 레이아웃

1. **한 장으로 보는 YOLO:** 깔때기 [격자 3종 · 후보 420] → [conf 후 11] → [NMS 후 4] → [채점 TP 3 · FP 1]. 아래에 개념 3과 약속 3.
2. **하루 전체 지도:** 네 묶음의 교시 카드.
3. **교시별 핵심:** 교시 · 질문 | 기본 → 응용 → 심화 계단. `구성안.md`의 표를 읽는다.
4. **코드로 보는 하루 흐름:**
   - ①~⑧ 흐름 띠
   - 교시 블록별 코드 + 설명 + 출처 문서. 3교시에는 dataset.yaml을 붙인다.
   - 코드 속 파라미터 8행
   - 응용·심화가 더 요구하는 것
5. **전체 파라미터 지도:** A~F 카드마다 실측 그림 + 파라미터 행.

## 그림 데이터

모든 숫자와 그림은 `make_figures.py`가 실제로 실행해 `facts.json`에 저장한다.

| 그림 | 데이터 | 내용 |
|---|---|---|
| 1 깔때기 | 응용 val `standard_val_000` | 공식 추론 경로(`predictor.preprocess/inference`, `non_max_suppression`)의 후보 420 → conf>0.25에서 11 → NMS 후 4. `predict` 결과 개수와 같은지 assert |
| A W·H 순서 | `scene.png`, `boxes_gt.csv` | `box_convert` 뒤 `[H, W, H, W]`로 나눴다가 되돌린 박스의 IoU 0.49·0.15·0.06 |
| B 매칭 | `boxes_fixture.csv` | 예측 4 · 정답 3, TP 2 · FP 2 · FN 1 |
| B mAP 곡선 | 응용 val | `metrics.box.all_ap`의 IoU 기준별 평균. mAP50 0.977, mAP50-95 0.710 |
| C 분할 | `manifest.csv` train+val 48장 | 24그룹. 번갈아 나누면 걸치는 그룹 24, 그룹 단위면 0 |
| D 학습 곡선 | `results.csv` | 1~17 epoch mAP 0. best 50 epoch(mAP50-95 최대), last 60. `epochs=1` 별도 학습도 0 |
| E conf | 응용 val | conf 0.05~0.95별 P·R(평가 IoU 0.5 1:1 매칭) |
| E NMS IoU | 응용 val | conf 0.25에서 iou 0.3~0.95별 남는 박스. 0.7은 FP 13, 0.5는 0 |
| F 추적 | `demo.avi`, `track_ground_truth.csv` | ByteTrack. 객체 3개에 ID 11개. ID를 정답 객체와 IoU 0.5로 연결해 색칠 |
| F persist | `demo.avi` 두 번 | 같은 객체 + `persist=True`면 ID가 45까지 이어짐. 새 객체면 첫 실행과 같은 ID |

**실측 모델**
- 응용 데이터 train 36장으로 `yolo26n.yaml`을 처음부터 60 epoch 학습했다.
- 설정: imgsz 160, batch 4, seed 42, deterministic, CPU, 약 2분.
- 실습의 `data/demo.pt`는 배포본에 없어서 이렇게 만들었다.

**확인한 함정**
- 공식 추론은 160×128을 그대로 넣는다. 그래서 후보는 525가 아니라 420개다(20×16 + 10×8 + 5×4).
- 저장된 best.pt의 `epoch` 값은 -1로 지워져 있다. best epoch은 results.csv에서 fitness로 다시 계산한다. 이 버전의 fitness는 mAP50-95 단독이다(가중치 `[0, 0, 0, 1]`).
- `track()`은 conf를 주지 않으면 0.1을 쓴다. 핵심 코드와 같게 conf를 따로 주지 않았다.
- Negative image를 빼고 학습해도 객체 없는 val 2장의 거짓 탐지는 두 모델 모두 0개였다. 쉬운 합성 데이터라 효과가 드러나지 않아 실측 행에서 뺐다.
- Ultralytics는 데이터 폴더에 `labels/*.cache`를 쓴다. 그래서 원본 실습 폴더 대신 사본으로 실행한다.

## 재검증

- `make_figures.py`를 처음부터 다시 돌렸을 때, 앞선 시험 실행과 모든 숫자가 같았다.
  - 확인한 숫자: mAP50 0.9773 · mAP50-95 0.7095, conf·NMS 표, 추적 ID.
  - 같은 결과가 나오는 이유: seed 42와 deterministic 설정.
- `build.py`는 실측 행의 핵심 숫자를 assert로 확인한다. "꼭 기억"이 7개인지도 확인한다.
- 렌더링 결과: 375·768·1280·1440px 모두 가로 넘침 0, 스크립트 오류 0.
- PDF는 1쪽(1080 × 6200pt)이고 `pdftotext`로 글자가 추출된다.
- OpenCV `rectangle` 시그니처는 설치된 OpenCV 5.0.0의 공식 docstring으로 대조했다. docs.opencv.org는 자동 접속을 막는다(HTTP 403).

## 다시 만드는 명령 (site/pages/vision/20261106 폴더에서)

```bash
# 1. 실측 (원본 대신 02_intermediate 사본을 넘긴다. 학습 결과는 작업 폴더에 저장)
cp -R ../../../../04_vision/20261106/02_intermediate /tmp/day15_app
uv run --project ~/envs/dl --with ultralytics --with opencv-python-headless --with lap \
    python -I make_figures.py /tmp/day15_app /tmp/day15_work .

# 2. HTML
python3 build.py

# 3. 화면 폭 검증 + PDF
uv run render.py index.html Day15_oneday요약.pdf [스크린샷 폴더]
```

## 파일

| 파일 | 역할 |
|---|---|
| `구성안.md` | 내용과 흐름(기획안). `build.py`가 코드 블록과 표를 직접 읽는다 |
| `make_figures.py` | 학습과 실측 → `facts.json` |
| `facts.json` | 실측 숫자와 그림 데이터(base64 PNG 포함) |
| `template.html` | 고정 문구와 CSS |
| `build.py` | 구성안 + facts → `index.html` |
| `render.py` | 화면 폭 검증과 세로 한 장 PDF |
| `index.html`, `Day15_oneday요약.pdf` | 배포본 |
