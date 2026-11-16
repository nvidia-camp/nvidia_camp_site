# Day15 강의 구조·핵심 설명

2026-11-06 · Vision·멀티모달 AI 응용 3/4 · 객체탐지·IoU·mAP → YOLO 학습·추론 → 추적·결과 분석

교시 설명과 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준이며 이 PDF는 인쇄 쪽수와 PDF 쪽수가 같습니다(전체 106쪽). 도입·마무리·참고자료는 별도 묶음으로 유지했습니다.

## 강의 목차

```text
도입 · 업무 흐름과 수업 범위
├─ 탐지·추적 데모의 전체 지도
│  ├─ Vision·멀티모달 AI 응용 (PDF p.1)
│  ├─ 현업의 영상 분석과 객체 탐지·추적 (PDF p.2)
│  ├─ 오늘 만드는 탐지·추적 데모의 전체 구조 (PDF p.3)
│  ├─ 한 프레임이 YOLO 탐지 결과가 되기까지 (PDF p.4)
│  ├─ 탐지 결과 한 건 안의 Box·Class·Confidence (PDF p.5)
│  ├─ 픽셀 박스와 YOLO 라벨의 연결 (PDF p.6)
│  ├─ Confidence·NMS IoU·평가 IoU의 역할 (PDF p.7)
│  ├─ 탐지 결과를 TP·FP·FN과 mAP로 평가 (PDF p.8)
│  ├─ 프레임 사이의 객체 연결과 Track ID (PDF p.9)
│  ├─ 비교 조건과 속도 측정 범위 (PDF p.10)
│  └─ 탐지·추적 프로젝트로 다시 합치기 (PDF p.11)
└─ 복습·운영·환경
   ├─ 어제 우리가 배운 것 (PDF p.12)
   ├─ 3분 확인 퀴즈 · 분류에서 탐지로 (PDF p.13)
   ├─ 오늘의 목표와 8교시 운영 (PDF p.14)
   ├─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)
   ├─ 오늘 남길 결과물 (PDF p.16)
   └─ 실습 환경 점검 (PDF p.17)

1교시 · 객체탐지·BBox·좌표
├─ 분류에서 객체탐지로
│  ├─ 분류·객체탐지·분할은 출력 단위가 다르다 (PDF p.18)
│  ├─ 객체탐지가 필요한 이유 (PDF p.19)
│  └─ 탐지 결과 한 건에 포함되는 정보 (PDF p.20)
├─ Bounding Box 좌표 형식과 정규화
│  ├─ Bounding Box 좌표 표현 (PDF p.21)
│  └─ Pixel Box를 YOLO 정규화 좌표로 변환 (PDF p.22)
├─ OpenCV 박스 시각화
│  ├─ OpenCV로 탐지 결과를 그린다 (PDF p.23)
│  └─ cv2.rectangle() · cv2.putText() (PDF p.24)
└─ 실습과 개념 확인
   ├─ 실습 01 · 이미지와 Bounding Box 좌표 (PDF p.25)
   └─ 3분 퀴즈 · Bounding Box (PDF p.26)

2교시 · IoU·NMS·Precision·Recall·mAP
├─ IoU 정의와 계산
│  ├─ IoU는 두 박스의 겹침 비율이다 (PDF p.27)
│  ├─ Intersection over Union (PDF p.28)
│  └─ IoU 계산 순서 (PDF p.29)
├─ 정답 매칭과 TP·FP·FN
│  └─ IoU와 클래스가 TP·FP·FN을 결정한다 (PDF p.30)
├─ NMS 중복 후보 정리
│  ├─ NMS는 겹치는 중복 후보를 정리한다 (PDF p.31)
│  └─ Non-Maximum Suppression 절차 (PDF p.32)
├─ Precision·Recall·AP·mAP
│  ├─ Detection 평가는 박스·클래스·점수 순위를 함께 본다 (PDF p.33)
│  ├─ 탐지 오류를 두 방향에서 본다 (PDF p.34)
│  ├─ mAP50과 mAP50-95를 구분한다 (PDF p.35)
│  └─ 예시 지표를 읽는 방법 (PDF p.36)
└─ 실습과 개념 확인
   ├─ 실습 02 · IoU·NMS·mAP 해석 (PDF p.37)
   └─ 3분 퀴즈 · IoU와 mAP (PDF p.38)

3교시 · 라벨링 규칙·YOLO 포맷·데이터 감사
├─ 라벨 품질과 라벨링 정책
│  ├─ 탐지 학습의 기반이 되는 라벨 품질 (PDF p.39)
│  ├─ Bounding Box 라벨링 기본 규칙 (PDF p.40)
│  └─ 가림·잘림·군집 객체의 처리 정책 (PDF p.41)
├─ YOLO 라벨 TXT 형식과 저장
│  ├─ YOLO Label TXT 형식 (PDF p.42)
│  └─ Pixel Box를 YOLO Label로 저장 (PDF p.43)
├─ 데이터 폴더와 dataset.yaml
│  ├─ YOLO Detect 데이터 폴더 구조 (PDF p.44)
│  ├─ dataset.yaml 작성 (PDF p.45)
│  └─ 데이터·설정·학습 결과가 한 흐름으로 연결된다 (PDF p.46)
├─ 누수 방지와 Negative image
│  ├─ 탐지 데이터에서도 누수를 막아야 한다 (PDF p.47)
│  └─ 탐지 대상 객체가 없는 이미지도 학습 데이터다 (PDF p.48)
└─ 실습과 개념 확인
   ├─ 실습 03 · 라벨 포맷과 품질 감사 (PDF p.49)
   └─ 3분 퀴즈 · 라벨과 데이터 (PDF p.50)

4교시 · YOLO 구조·환경·학습 시작
├─ One-stage YOLO 구조
│  ├─ YOLO는 한 번의 순전파로 여러 위치·크기의 객체를 예측한다 (PDF p.51)
│  ├─ One-stage Detector의 큰 그림 (PDF p.52)
│  ├─ Backbone·Neck·Head의 역할 (PDF p.53)
│  └─ 왜 여러 해상도에서 탐지하는가? (PDF p.54)
├─ 추론 순서와 환경 설치
│  ├─ YOLO26의 NMS 경로에서 추론하는 순서 (PDF p.55)
│  └─ Ultralytics 환경 설치와 확인 (PDF p.56)
├─ YOLO 모델 객체 생성
│  ├─ YOLO 모델 객체 생성 (PDF p.57)
│  └─ YOLO(model, task=None, verbose=False) (PDF p.58)
├─ 학습 흐름과 실행 방법
│  ├─ YOLO 학습은 데이터 계약과 실행 기록을 함께 남긴다 (PDF p.59)
│  ├─ Python API로 YOLO 학습 시작 (PDF p.60)
│  ├─ model.train() (PDF p.61)
│  └─ PowerShell에서 같은 학습 실행 (PDF p.62)
└─ 실습과 개념 확인
   ├─ 실습 04 · YOLO 환경·구조·학습 시작 (PDF p.63)
   └─ 3분 퀴즈 · YOLO 학습 (PDF p.64)

5교시 · 검증·Metric·Checkpoint·과적합
├─ 학습 전 데이터 계약과 학습 설정
│  ├─ 학습 전 데이터 계약을 먼저 확인한다 (PDF p.65)
│  ├─ 주요 학습 인자와 영향 (PDF p.66)
│  └─ 탐지 증강은 Box도 같이 변환해야 한다 (PDF p.67)
├─ 학습 산출물과 검증 실행
│  ├─ 학습 폴더에서 확인할 결과 (PDF p.68)
│  ├─ 검증 데이터로 성능 측정 (PDF p.69)
│  └─ model.val() (PDF p.70)
├─ 검증 지표 해석과 오류 진단
│  ├─ 검증 출력의 주요 항목 (PDF p.71)
│  └─ 학습곡선과 지표로 오류 패턴 진단 (PDF p.72)
├─ Checkpoint 구분
│  └─ best·last·resume를 구분한다 (PDF p.73)
└─ 실습과 개념 확인
   ├─ 실습 05 · 검증·Metric·Checkpoint 분석 (PDF p.74)
   └─ 3분 퀴즈 · 검증과 Checkpoint (PDF p.75)

6교시 · 추론·Results·오류 분석
├─ predict 실행
│  ├─ 이미지·영상·폴더를 추론한다 (PDF p.76)
│  └─ model.predict() (PDF p.77)
├─ Results 읽기와 저장
│  ├─ Results 객체에서 확인할 정보 (PDF p.78)
│  ├─ Box 좌표·신뢰도·클래스 읽기 (PDF p.79)
│  └─ 시각화 결과 저장 (PDF p.80)
├─ 입력 방식과 stream
│  └─ Predict 입력 방식과 stream 선택 (PDF p.81)
├─ 오류 유형과 Threshold 효과
│  ├─ 탐지 오류를 유형별로 나눈다 (PDF p.82)
│  ├─ Confidence Threshold의 효과 (PDF p.83)
│  └─ NMS IoU Threshold의 효과 (PDF p.84)
└─ 실습과 개념 확인
   ├─ 실습 06 · YOLO 추론·결과 분석 (PDF p.85)
   └─ 3분 퀴즈 · Predict와 Results (PDF p.86)

7교시 · 다중 객체 추적·속도 측정
├─ Tracking 개념과 Detect 비교
│  ├─ Tracking은 Frame 사이에서 같은 객체의 ID를 유지한다 (PDF p.87)
│  └─ 탐지와 추적의 차이 (PDF p.88)
├─ track() 실행과 Tracker 상태
│  ├─ 영상 객체 추적 (PDF p.89)
│  ├─ model.track() (PDF p.90)
│  ├─ persist와 Tracker 상태 관리 (PDF p.91)
│  └─ Track ID별 중심점 궤적 수집 (PDF p.92)
├─ 추적 오류와 속도 측정
│  ├─ 추적 결과에서 확인할 오류 (PDF p.93)
│  └─ 속도·지연시간·처리량을 구분한다 (PDF p.94)
├─ 데모 프로젝트 구조
│  └─ YOLO 탐지·추적 데모 프로젝트 구조 (PDF p.95)
└─ 통합 실습과 개념 확인
   ├─ 실습 07 · YOLO 탐지·추적 데모 통합 (PDF p.96)
   └─ 3분 퀴즈 · 객체 추적 (PDF p.97)

8교시 · YOLO 탐지·추적 데모 통합
├─ 최종 제출물과 점검 상황
│  ├─ 최종 제출물 (PDF p.98)
│  └─ 정상·경계·실패 상황 (PDF p.99)
├─ 평가 기준
│  └─ 형성평가 기준 · 100점 (PDF p.100)
└─ 최종 검증 실습
   └─ 실습 08 · 최종 검증·보고서·시연 (PDF p.101)

마무리 · 정리와 다음 수업
└─ 확인 퀴즈·핵심 정리·OCR·VLM 예고
   ├─ 마무리 3분 확인 퀴즈 (PDF p.102)
   ├─ 오늘의 핵심 정리 (PDF p.103)
   └─ 다음 수업 · OCR·VLM·추론 시스템 (PDF p.104)

참고자료 · 공식 문서
└─ Ultralytics·OpenCV 공식 참고자료
   ├─ 공식 참고자료 · 객체탐지와 데이터 (PDF p.105)
   └─ 공식 참고자료 · 추론과 추적 (PDF p.106)
```

## 핵심 설명

### 도입 · 업무 흐름과 수업 범위

#### 탐지·추적 데모의 전체 지도

##### Vision·멀티모달 AI 응용 (PDF p.1)

- 정규교과 3/4 표지
- 객체탐지·IoU·mAP → YOLO 학습·추론 → 추적·결과 분석 순서의 하루 흐름 제시

##### 현업의 영상 분석과 객체 탐지·추적 (PDF p.2)

- 현장 이미지·영상 → 프레임마다 탐지(종류와 위치) → 프레임 사이 추적(같은 객체 연결) → 위치·이동 기록(CSV·영상 확인)의 가상 업무 흐름
- 주차장의 차량 위치·이동 흐름 확인, 작업 현장의 관심 객체 위치와 놓친 장면 검토를 예시로 사용
- 같은 객체를 여러 프레임에서 연결해야 이동 기록 해석 가능

##### 오늘 만드는 탐지·추적 데모의 전체 구조 (PDF p.3)

- 준비 단계는 이미지·라벨 교차검수와 분할 → 짧은 학습 점검·검증 또는 제공 가중치 확인 → 사용할 가중치의 클래스·설정 확인
- 실행 단계는 이미지·영상 프레임 읽기 → 탐지(Box·Class·점수) → Tracker·ID로 영상의 객체 연결 → CSV·이미지·영상 저장과 오류 분석
- 정답 라벨은 학습·평가에 사용하고 새 입력의 추론은 이미지만으로 실행
- 기본 데모는 제공 가중치로 시작, 긴 재학습은 완료 조건에 포함하지 않음

##### 한 프레임이 YOLO 탐지 결과가 되기까지 (PDF p.4)

- 프레임 전처리 → Backbone 특징 추출 → Neck 다중 크기 결합 → Head 위치·클래스 후보 → 점수 필터·NMS → Results
- 전날의 Backbone·Head 구조에 여러 크기의 특징을 결합하는 Neck이 추가된 형태
- 그림은 오늘 사용하는 NMS 경로이며 정리한 결과를 추적과 저장으로 연결

##### 탐지 결과 한 건 안의 Box·Class·Confidence (PDF p.5)

- 프레임별 Results 안에서 탐지한 객체마다 한 행의 데이터로 읽기
- 가상 맞춤 모델의 클래스는 0 helmet, 1 no_helmet, 2 person
- Frame 125 예시는 `2 · person` 0.87 `[64,48,320,288]`, `0 · helmet` 0.93 `[112,52,192,112]`의 탐지 2건
- Box는 위치, Class는 `model.names`로 읽는 종류, 점수는 후보의 정렬·선별 기준
- Track ID는 탐지 단계가 아니라 추적 단계에서 부여
- 객체가 여러 개면 여러 행, 탐지가 없으면 N=0인 결과로 처리

##### 픽셀 박스와 YOLO 라벨의 연결 (PDF p.6)

- 640×480 프레임에서 같은 박스를 xyxy Pixel `[64, 48, 320, 288]`, 중심·크기 Pixel `[192, 168, 256, 240]`, 정규화 중심·크기 `[0.30, 0.35, 0.40, 0.50]`으로 표현
- 학습 라벨 한 줄은 `class_id cx cy w h` 형식, 예 `2 0.300000 0.350000 0.400000 0.500000`
- 학습 라벨은 클래스와 좌표만 저장
- 저장한 숫자를 다시 그려 그림의 박스와 같은 위치인지 교차검수

##### Confidence·NMS IoU·평가 IoU의 역할 (PDF p.7)

- Confidence는 각 후보의 예측 점수, 낮은 점수 후보 선별에 사용
- NMS IoU는 같은 클래스의 예측과 예측을 비교, 겹치는 중복 후보 정리에 사용
- 평가 IoU는 예측 박스와 정답 박스를 비교, TP 매칭의 위치 기준으로 사용
- 그림 예시는 예측끼리 IoU = 0.875, 예측과 정답 IoU ≈ 0.714
- 실습은 `nms=True` 경로이며 평가 IoU와 NMS `iou`를 별개 값으로 구분

##### 탐지 결과를 TP·FP·FN과 mAP로 평가 (PDF p.8)

- 클래스와 평가 IoU 조건으로 정답 3개와 예측 4개를 비교하는 가상 예
- person A·B는 TP, 배경을 person으로 예측한 것과 helmet을 person으로 예측한 것은 FP, 매칭되지 않은 helmet C는 FN
- TP/FP/FN = 2/2/1, Precision = 2/4 = 0.50, Recall = 2/3 ≈ 0.67
- AP는 점수 순위별 PR을 요약한 값, mAP는 클래스별 AP의 평균
- mAP50은 평가 IoU 0.50 기준, mAP50-95는 0.50~0.95의 10개 기준 평균

##### 프레임 사이의 객체 연결과 Track ID (PDF p.9)

- 종류를 나타내는 Class ID와 시간에 따라 같은 객체를 연결하는 Track ID 구분
- 기록 단위는 `stream_id`·`frame_idx`·`track_id`·중심점·박스 좌표, 예 `video_A`의 125 → 126 → 127 프레임에서 ID 7 유지
- 가림·누락으로 ID가 바뀔 수 있음
- 새 영상은 별도의 추적 상태로 시작

##### 비교 조건과 속도 측정 범위 (PDF p.10)

- 입력·가중치·크기·장치는 고정
- 한 번에 바꾸는 조건은 Confidence 또는 Tracker 하나
- 버전·NMS·프레임 수·결과를 함께 기록
- 처리 구간은 영상 읽기 → 전처리 → 모델 추론 → 후처리·추적 → 결과 저장
- 추론 시간은 모델 추론 구간만, 전체 처리 시간은 영상 입출력까지 포함
- 모델 추론 시간의 역수를 전체 영상 처리 FPS로 해석하지 않음

##### 탐지·추적 프로젝트로 다시 합치기 (PDF p.11)

- 입력·라벨 확인 → 제공 가중치로 탐지·추적 실행 → CSV·영상 저장과 오류 사례 확인 → 재실행과 결과 설명의 통합 흐름
- 검수·지표 해석 산출물은 `label_audit.csv`·`metrics_summary.csv`
- 탐지·추적 결과 산출물은 `detections.csv`·`tracking.csv`·`demo.mp4`
- 설명·재실행 산출물은 `demo_report.md`·`README.md`
- 기본필수는 제공 가중치·입력으로 데모 완성, 응용 이상은 조건 비교·오류 분석·실행 자동화
- 교시 연결은 좌표·라벨·지표(1~3교시), 학습·검증(4~5), 추론·추적(6~7), 통합(8)

#### 복습·운영·환경

##### 어제 우리가 배운 것 (PDF p.12)

- train·valid·test 분리와 `class_to_idx` 확인
- Head-only·Partial fine-tuning의 학습 범위 비교
- Macro F1·클래스별 Recall·오류 이미지·Grad-CAM 연결
- 오늘은 이미지 전체 분류에서 객체의 종류와 위치를 동시에 예측하는 문제로 확장

##### 3분 확인 퀴즈 · 분류에서 탐지로 (PDF p.13)

- 분류 모델의 출력이 이미지 전체에 대한 클래스 점수 또는 확률이라는 점 확인
- 객체탐지에는 클래스 외에 객체별 Bounding Box와 신뢰도가 필요하다는 점 확인
- 탐지에서도 모델·설정은 valid에서 선택하고 test는 최종 확인에만 사용하는 원칙 확인

##### 오늘의 목표와 8교시 운영 (PDF p.14)

- 1교시 객체탐지·BBox·좌표(설명 30분·실습 20분)
- 2교시 IoU·NMS·Precision·Recall·mAP
- 3교시 라벨링 규칙·YOLO 포맷·데이터 감사
- 4교시 YOLO 구조·환경·학습 시작
- 5교시 검증·Metric·Checkpoint·과적합
- 6교시 추론·Results·오류 분석
- 7교시 다중 객체 추적·속도 측정
- 8교시 YOLO 탐지·추적 데모 통합(설명 20분·실습 30분)
- 2~7교시는 설명 25분·실습 25분, 전체 400분 중 설명·시연 약 200분과 실습·리뷰 약 200분

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)

- 오늘 범위는 객체탐지 출력과 Bounding Box, IoU·NMS·Precision·Recall·mAP, 라벨링 규칙과 YOLO 데이터 포맷, YOLO 학습·검증·추론·추적, 탐지·추적 데모와 결과 분석
- 11월 9일 범위는 OCR 파이프라인과 문서 구조, 텍스트 영역 탐지·인식·후처리, VLM 시각 질의응답, TensorRT·Jetson·DeepStream 추론 흐름, OCR·VLM 미니 애플리케이션

##### 오늘 남길 결과물 (PDF p.16)

- 라벨 감사표는 클래스·박스·중복·누락·분할 규칙
- 탐지 실험표는 Precision·Recall·mAP50·mAP50-95·속도
- 추론 결과는 이미지·영상의 박스·클래스·신뢰도·오류 사례
- 추적 데모는 객체 ID·프레임 처리량·한계, 궤적은 선택 확장
- 완료 기준은 박스가 보이는 것이 아니라 데이터·지표·실패 사례·실행 조건을 함께 설명하는 것

##### 실습 환경 점검 (PDF p.17)

- `python -m pip install "ultralytics==8.4.142" opencv-python` 후 Python·PyTorch·OpenCV·Ultralytics 버전 출력
- `torch.cuda.is_available()`로 CUDA 사용 가능 여부 확인
- GPU 이름·VRAM과 강의 폴더 쓰기 권한 확인
- GPU가 없어도 라벨·IoU·포맷·CPU 추론은 진행
- 예제 기준은 Ultralytics 8.4.142·YOLO26n

### 1교시 · 객체탐지·BBox·좌표

#### 분류에서 객체탐지로

##### 분류·객체탐지·분할은 출력 단위가 다르다 (PDF p.18)

- 단일 라벨 분류는 이미지 전체에 클래스 하나
- 탐지는 객체마다 클래스·박스·신뢰도
- 분할은 객체 또는 영역의 픽셀 Mask
- 오늘의 중심 작업은 Detect와 Track

##### 객체탐지가 필요한 이유 (PDF p.19)

- 한 이미지 안에 여러 객체가 동시에 존재
- 같은 클래스 객체도 위치와 크기가 서로 다름
- "무엇인가?"와 함께 "어디에 있는가?"를 예측
- 영상에서는 프레임마다 탐지를 반복하고 객체의 이동까지 연결
- 안전모 미착용 탐지, 불량 부품 위치, 차량·보행자 탐지, 문서 영역 탐지를 실무 예로 제시

##### 탐지 결과 한 건에 포함되는 정보 (PDF p.20)

- `class`는 예측한 객체 종류
- `confidence`는 후보를 정렬·필터링하는 예측 점수
- `box`는 `x1,y1,x2,y2` 등으로 표현한 객체 위치
- `image_id`·`frame`은 어느 입력의 결과인지 표시
- `track_id`는 추적 시 프레임 간 연결에 쓰는 ID

#### Bounding Box 좌표 형식과 정규화

##### Bounding Box 좌표 표현 (PDF p.21)

- xyxy는 왼쪽 위 `(x1,y1)`과 오른쪽 아래 `(x2,y2)`, 그리기·IoU 계산에 사용
- OpenCV Rect는 왼쪽 위 x,y와 width,height
- 중심 xywh는 중심 x,y와 width,height, Ultralytics `boxes.xywh` 형식
- normalized는 이미지 크기로 나눈 0~1 좌표, 해상도와 무관한 라벨 저장에 사용

##### Pixel Box를 YOLO 정규화 좌표로 변환 (PDF p.22)

- `cx=(x1+x2)/(2×W)`, `cy=(y1+y2)/(2×H)`, `w=(x2−x1)/W`, `h=(y2−y1)/H`
- W·H는 원본 이미지의 너비와 높이
- 정규화 후 값은 일반적으로 0~1 범위
- 640×480 이미지의 `(64,48)~(320,288)` 박스는 cx=0.30, cy=0.35, w=0.40, h=0.50

#### OpenCV 박스 시각화

##### OpenCV로 탐지 결과를 그린다 (PDF p.23)

- `cv2.imread` 결과가 `None`이면 `FileNotFoundError`로 중단
- `cv2.rectangle`로 박스, `cv2.putText`로 `"dog 0.87"` 라벨을 박스 위쪽에 표시
- `cv2.imwrite` 반환값이 거짓이면 `OSError`로 중단
- OpenCV 좌표는 정수 Pixel, 색은 BGR 순서
- 박스와 라벨 위치가 이미지 경계 안에 있는지 확인
- 원본은 유지하고 결과는 새 파일 `detected.jpg`로 저장

##### cv2.rectangle() · cv2.putText() (PDF p.24)

- 이미지 배열 위에 Bounding Box와 설명 문자열을 그리는 함수
- `rectangle`의 필수 인자는 img·시작/끝 좌표·color
- `putText`의 필수 인자는 img·text·org·fontFace·fontScale·color
- 공통 선택 인자는 thickness·lineType, `rectangle`에는 shift 추가
- 반환값은 원본 배열을 수정한 이미지 배열
- BGR 색 순서, 음수 좌표, 이미지 밖 라벨, 원본 덮어쓰기 점검

#### 실습과 개념 확인

##### 실습 01 · 이미지와 Bounding Box 좌표 (PDF p.25)

- 20분 실습, 4단계 난이도
- 기본필수는 제공 이미지와 정답 box 3개를 읽어 xyxy 박스를 그려 저장하고 좌표와 클래스 출력
- 응용은 xyxy ↔ YOLO cxcywh 변환을 추가하고 왕복 후 Pixel 오차 확인
- 심화는 박스를 이미지 경계 안으로 clip하고 작은 박스·잘린 객체 사례 비교
- 특심화는 좌표 형식·dtype·정규화 범위를 검사하는 Box 데이터 클래스와 단위 테스트 작성
- 기본필수부터 완료하고 동일 데이터·분할·평가 조건을 유지한 채 선택 단계로 확장

##### 3분 퀴즈 · Bounding Box (PDF p.26)

- YOLO 라벨 좌표가 Pixel 값이 아니라 0~1로 정규화한 중심 x,y와 width,height라는 점 확인
- width와 height 순서가 바뀌면 x·y의 정규화 기준이 뒤바뀌어 박스 위치와 크기가 틀어진다는 점 확인
- OpenCV 색 순서가 BGR이며 Matplotlib의 RGB와 혼동하면 색이 바뀐다는 점 확인

**핵심:** 같은 박스라도 xyxy·중심 xywh·정규화 좌표 중 어떤 형식인지와 기준 이미지 크기를 함께 알아야 위치를 올바르게 저장·표시할 수 있음.

### 2교시 · IoU·NMS·Precision·Recall·mAP

#### IoU 정의와 계산

##### IoU는 두 박스의 겹침 비율이다 (PDF p.27)

- Intersection은 두 박스가 겹친 영역
- Union은 두 박스가 차지하는 전체 영역
- 0이면 겹침 없음, 1이면 완전히 동일
- 매칭·NMS·mAP의 공통 핵심 기준

##### Intersection over Union (PDF p.28)

- IoU = Area(Prediction ∩ Ground Truth) ÷ Area(Prediction ∪ Ground Truth)
- 박스 크기와 위치가 모두 맞아야 높아짐
- 클래스 일치 여부는 IoU와 별도로 확인
- 교집합 6,400px²·합집합 22,400px²이면 IoU = 0.286

##### IoU 계산 순서 (PDF p.29)

- 교집합 좌표는 시작점 max, 끝점 min, 가로·세로 중 하나라도 겹치지 않으면 0
- 교집합 width·height 계산 시 음수는 0으로 처리
- 각 박스 면적 계산 전 좌표 순서 확인
- union = A + B − intersection, 중복 영역은 한 번만 포함
- IoU = intersection / union, union = 0인 경우 분모 0 방지

#### 정답 매칭과 TP·FP·FN

##### IoU와 클래스가 TP·FP·FN을 결정한다 (PDF p.30)

- TP는 같은 클래스의 정답과 충분한 IoU로 1:1 매칭된 예측
- FP는 정답과 매칭되지 않은 탐지, 잘못된 클래스, 중복 탐지
- FN은 존재하지만 어떤 예측과도 매칭되지 않은 정답 객체
- 한 정답 객체에 여러 예측이 겹쳐도 일반적으로 하나만 TP
- IoU 임계값이 높을수록 더 정확한 위치여야 TP로 인정

#### NMS 중복 후보 정리

##### NMS는 겹치는 중복 후보를 정리한다 (PDF p.31)

- 신뢰도가 가장 높은 후보를 먼저 선택
- 같은 클래스에서 IoU가 높은 후보 제거
- conf 기준과 IoU 기준은 서로 다른 역할
- 작은 객체·밀집 객체에서는 실제 객체까지 지나치게 제거될 수 있음

##### Non-Maximum Suppression 절차 (PDF p.32)

- confidence 기준 이하 후보 제거
- 남은 후보를 confidence 내림차순 정렬
- 가장 높은 후보를 결과에 추가
- 같은 클래스에서 선택 후보와 IoU가 큰 후보 제거
- 후보가 없을 때까지 반복

#### Precision·Recall·AP·mAP

##### Detection 평가는 박스·클래스·점수 순위를 함께 본다 (PDF p.33)

- confidence 기준을 바꾸며 Precision·Recall 곡선 생성
- AP는 한 클래스의 PR 곡선 아래 면적
- mAP는 클래스별 AP의 평균
- mAP50-95는 여러 IoU 임계값의 결과 평균

##### 탐지 오류를 두 방향에서 본다 (PDF p.34)

- Precision = TP / (TP + FP), 탐지한 것 중 맞은 비율
- Recall = TP / (TP + FN), 존재하는 객체 중 찾은 비율
- TP=8, FP=2, FN=4이면 Precision 0.80, Recall 0.67

##### mAP50과 mAP50-95를 구분한다 (PDF p.35)

- AP는 한 클래스의 Precision–Recall 곡선 요약
- mAP50은 IoU 0.50에서의 클래스별 AP 평균
- mAP50-95는 IoU 0.50~0.95를 0.05 간격으로 평균
- mAP50이 높고 mAP50-95가 낮으면 위치 정밀도 부족 가능성

##### 예시 지표를 읽는 방법 (PDF p.36)

- Precision 0.82는 탐지 결과의 18%가 거짓 탐지일 수 있다는 의미
- Recall 0.61은 실제 객체의 39%를 놓쳤다는 의미
- mAP50 0.78은 IoU 0.50 기준의 전반적 탐지 성능
- mAP50-95 0.46은 더 엄격한 위치 기준에서 성능이 하락했다는 의미
- Speed 7.8ms/image는 전처리·추론·후처리 범위를 구분해 기록
- 모든 수치는 설명용이며 P·R은 단일 클래스·고정 조건 예시, 실제 모델 결과 아님

#### 실습과 개념 확인

##### 실습 02 · IoU·NMS·mAP 해석 (PDF p.37)

- 25분 실습, 4단계 난이도
- 기본필수는 예측 box 4개와 정답 box 3개의 IoU를 계산하고 TP·FP·FN을 표로 정리
- 응용은 confidence·NMS IoU 임계값을 각각 바꾸어 남는 박스 수와 Precision·Recall 변화 비교
- 심화는 클래스별 AP와 mAP50·mAP50-95 예시를 계산하고 위치 오차와 분류 오차 구분
- 특심화는 여러 이미지·클래스의 매칭을 구현하고 IoU 임계값별 AP 계산 테스트
- 기본필수부터 완료하고 동일 데이터·분할·평가 조건을 유지한 채 선택 단계로 확장

##### 3분 퀴즈 · IoU와 mAP (PDF p.38)

- Confidence 0.5는 후보 점수 기준, IoU 0.5는 박스 겹침 기준으로 서로 다르다는 점 확인
- 높은 IoU 임계값까지 평균하는 mAP50-95가 위치 정확도에 더 엄격하다는 점 확인
- 한 정답 객체에 중복 박스 3개가 남으면 일반적으로 1개만 TP, 나머지는 FP라는 점 확인

**핵심:** Confidence는 후보 점수, NMS IoU는 예측 간 중복, 평가 IoU는 예측과 정답의 위치 일치를 판단하며 이 기준을 섞지 않아야 TP·FP·FN과 mAP를 올바르게 해석할 수 있음.

### 3교시 · 라벨링 규칙·YOLO 포맷·데이터 감사

#### 라벨 품질과 라벨링 정책

##### 탐지 학습의 기반이 되는 라벨 품질 (PDF p.39)

- 박스는 객체에 가능한 한 밀착
- 같은 규칙을 모든 이미지에 일관되게 적용
- 누락·중복·잘린 객체 정책을 문서화
- 애매한 사례는 개인 판단보다 정해진 규칙 우선

##### Bounding Box 라벨링 기본 규칙 (PDF p.40)

- 박스 안에 대상 객체를 포함하고 불필요한 배경은 최소화
- 일부 가려진 객체는 보이는 부분과 전체 추정 중 하나의 정책으로 고정
- 이미지 경계에 잘린 객체의 포함·제외 기준 결정
- 아주 작은 객체·불명확한 객체의 최소 크기와 제외 기준 결정

##### 가림·잘림·군집 객체의 처리 정책 (PDF p.41)

- Occlusion은 보이는 부분만 박스인지 전체 추정인지 결정하고 가림 비율 기준 기록
- Truncation은 경계에 잘린 객체의 학습 여부를 결정하고 포함·제외 기준 기록
- Crowd는 개별 박스를 그릴 수 있는지 판단하고 최소 분리 기준 기록
- Small object는 제외할 Pixel 크기를 정하고 최소 width·height 기록
- Ambiguous class는 정해진 클래스로 구분 가능한지 판단하고 검토·제외 기준 기록

#### YOLO 라벨 TXT 형식과 저장

##### YOLO Label TXT 형식 (PDF p.42)

- 한 행은 `class_id cx cy w h`
- `class_id`는 0부터 시작하는 정수
- `cx,cy,w,h`는 원본 W·H로 정규화한 값
- 이미지와 같은 이름의 TXT 파일 사용, 예 `scene.jpg`와 `scene.txt`
- 객체마다 숫자 5개를 한 행에 기록
- 헤더·주석은 저장하지 않음

##### Pixel Box를 YOLO Label로 저장 (PDF p.43)

- 이미지 크기 W·H를 사용해 중심과 크기를 정규화
- 저장 전 좌표 순서와 범위 확인
- 소수점은 `:.6f`처럼 충분히 유지
- 왕복 변환으로 원래 위치와 일치하는지 확인
- 640×480의 `(64,48)~(320,288)` 박스는 `0 0.300000 0.350000 0.400000 0.500000`

#### 데이터 폴더와 dataset.yaml

##### YOLO Detect 데이터 폴더 구조 (PDF p.44)

- `dataset/images/train`은 학습 이미지, `dataset/images/val`은 검증 이미지
- `dataset/images/test`는 선택 항목인 최종 확인 이미지
- `dataset/labels/train`·`dataset/labels/val`에는 이미지와 같은 이름의 txt
- `dataset.yaml`은 root·split 경로·names 정의

##### dataset.yaml 작성 (PDF p.45)

- `path`는 실제 데이터셋 절대경로, 본인 경로로 수정
- `train`·`val`·`test`는 `path` 기준 상대 경로
- `names`는 class id와 이름, 예 0 helmet·1 no_helmet·2 person
- test가 없으면 해당 줄 생략
- 이미지·라벨 파일명 대응 검사
- `class_id`가 0~2 범위인지 검사
- train/val 사이 중복 없음 검사

##### 데이터·설정·학습 결과가 한 흐름으로 연결된다 (PDF p.46)

- split별 이미지와 라벨을 함께 관리
- YAML이 경로와 클래스 정의를 연결
- 학습 결과는 weight·곡선·metric으로 저장
- 원본·라벨·설정·결과의 버전을 함께 기록

#### 누수 방지와 Negative image

##### 탐지 데이터에서도 누수를 막아야 한다 (PDF p.47)

- 같은 원본 이미지의 resize·crop·증강본은 서로 다른 split에 넣지 않음
- 영상 Frame은 같은 영상·같은 구간을 그룹으로 묶어 분할
- 연속 촬영·같은 개체·같은 현장·같은 카메라는 그룹 ID로 관리
- test 라벨을 보며 라벨링 규칙·augmentation·threshold를 반복 조정하지 않음

##### 탐지 대상 객체가 없는 이미지도 학습 데이터다 (PDF p.48)

- 배경만 있는 장면에서 거짓 탐지 감소
- 비슷한 패턴을 객체로 오인하는 문제 확인
- 실제 운영 환경의 빈 장면 반영
- 진짜 객체 누락을 Negative로 만들지 않음
- 빈 라벨 파일 처리 규칙 확인
- Negative 비율이 과도하면 Recall 하락 가능
- train/valid 모두 실제 분포 반영

#### 실습과 개념 확인

##### 실습 03 · 라벨 포맷과 품질 감사 (PDF p.49)

- 25분 실습, 4단계 난이도
- 기본필수는 이미지 6장과 label txt를 읽어 클래스·박스 수·정규화 범위를 표로 출력
- 응용은 박스 면적·가로세로 비율·클래스 비율과 split 중복 검사
- 심화는 영상 그룹 ID로 Group split을 만들고 이미지 단위 split과 누수 차이 비교
- 특심화는 누락·중복·경계 밖 박스·근접 중복 이미지를 보고서로 저장하는 라벨 감사 도구 작성
- 분할 방식 비교는 누수 시연으로 구분하고 실제 평가 분할은 고정

##### 3분 퀴즈 · 라벨과 데이터 (PDF p.50)

- 객체가 4개인 이미지의 label txt는 객체마다 한 줄인 4줄이라는 점 확인
- 같은 영상의 연속 Frame을 무작위로 train·val에 나누면 거의 같은 장면이 섞여 평가가 낙관적으로 된다는 점 확인
- 정확히 라벨된 Negative image는 나쁜 데이터가 아니라 거짓 탐지 감소에 도움이 된다는 점 확인

**핵심:** 일관된 라벨링 정책·정확한 YOLO 포맷·그룹 단위 분할이 갖춰져야 이후 학습과 지표가 의미를 가짐.

### 4교시 · YOLO 구조·환경·학습 시작

#### One-stage YOLO 구조

##### YOLO는 한 번의 순전파로 여러 위치·크기의 객체를 예측한다 (PDF p.51)

- Backbone은 이미지 특징 추출
- Neck은 여러 해상도의 특징 결합
- Head는 클래스·박스·신뢰도 예측
- 오늘의 경로는 점수 필터와 NMS

##### One-stage Detector의 큰 그림 (PDF p.52)

- 입력 이미지를 한 번의 모델 순전파로 처리
- 여러 위치와 크기의 후보를 동시에 예측
- 오늘의 NMS 경로에서 낮은 점수와 중복 후보 정리
- 정확도와 함께 지연시간·FPS·메모리도 평가 기준

##### Backbone·Neck·Head의 역할 (PDF p.53)

- Backbone은 Edge·Texture·Shape 등 특징 추출, 해상도 감소와 채널 증가 관찰
- Neck은 얕은·깊은 특징을 여러 Scale로 결합, 작은 객체·큰 객체 대응
- Head는 클래스와 Box 예측, Scale별 Detection output 생성
- Postprocess는 점수 필터·NMS, `nms=True`·`conf`·`iou` 설정으로 제어

##### 왜 여러 해상도에서 탐지하는가? (PDF p.54)

- 고해상도 Feature는 위치 정보가 비교적 자세하고 작은 객체 탐지에 유리
- 고해상도 Feature는 계산량과 메모리 증가
- 저해상도 Feature는 넓은 영역의 문맥을 반영하고 큰 객체·전체 형태에 유리
- 저해상도 Feature는 위치 정밀도가 상대적으로 낮을 수 있음

#### 추론 순서와 환경 설치

##### YOLO26의 NMS 경로에서 추론하는 순서 (PDF p.55)

- 입력 읽기·크기 조정·정규화
- 모델 순전파로 다수 후보 생성
- confidence 기준 이하 후보 제거
- NMS로 중복 박스 정리
- 원본 좌표로 복원하고 결과 저장·표시

##### Ultralytics 환경 설치와 확인 (PDF p.56)

- `ultralytics==8.4.142`와 `opencv-python` 설치 후 `pip show`·버전 출력으로 확인
- 예제 기준은 Ultralytics 8.4.142, YOLO26n과 NMS 경로 사용
- PyTorch·CUDA·Driver는 실제 설치 버전을 기록
- 완료 기준은 import 성공, CUDA 사용 여부 출력, GPU 모델·VRAM 기록

#### YOLO 모델 객체 생성

##### YOLO 모델 객체 생성 (PDF p.57)

- `YOLO("yolo26n.pt")`로 공식 Detect 사전학습 checkpoint 로드
- `YOLO()` 객체 하나가 train·val·predict·track 모드 제공
- `model.task`는 `detect`, `model.names`는 COCO 클래스 매핑 출력

##### YOLO(model, task=None, verbose=False) (PDF p.58)

- 모델 구조와 가중치를 불러와 여러 실행 모드를 제공하는 객체 생성
- 필수 인자 `model`은 checkpoint 경로·모델 이름·YAML 설정 경로
- `task`는 detect 등 작업을 명시할 때, `verbose`는 로딩 정보 출력 여부
- 반환값은 Ultralytics YOLO 모델 객체
- 신뢰할 수 있는 weight만 로드
- 모델 task와 데이터 라벨 형식의 일치 확인

#### 학습 흐름과 실행 방법

##### YOLO 학습은 데이터 계약과 실행 기록을 함께 남긴다 (PDF p.59)

- images·labels·dataset.yaml 검증
- 사전학습 checkpoint 또는 YAML 구조 선택
- 학습·검증 곡선과 metric 저장
- best.pt·last.pt·설정·환경 기록

##### Python API로 YOLO 학습 시작 (PDF p.60)

- `if __name__ == "__main__":` 안에서 실행
- `torch.cuda.is_available()`이면 `device=0`, 아니면 `"cpu"`
- `model.train(data="dataset.yaml", epochs=30, imgsz=640, batch=16, device=device, workers=0, nms=True, project="runs/day15", name="helmet_yolo")` 형태로 실행
- 흐름은 모델 로드 → dataset.yaml 지정 → 실험 조건 기록 → train 실행 → best.pt와 결과 확인
- 실제 저장 경로는 `model.trainer.save_dir`로 확인
- 결과 폴더에는 `weights/best.pt`·`weights/last.pt`·`results.csv`·plots

##### model.train() (PDF p.61)

- 데이터를 읽어 Detection 모델을 학습하고 검증 결과와 checkpoint 저장
- 필수 인자는 `data`, dataset.yaml 경로
- 주요 선택 인자는 epochs·imgsz·batch·device·workers·nms·seed·patience·resume
- 학습 지표를 반환하고 실행 폴더에 checkpoint·CSV 저장
- 한 번에 여러 조건을 바꾸지 않음
- test는 모델 선택에 사용하지 않음

##### PowerShell에서 같은 학습 실행 (PDF p.62)

- CLI 문법은 `yolo TASK MODE ARGS`, 예 `yolo detect train`
- 인자는 `arg=value` 형식, `--epochs` 형식이 아님
- PowerShell 줄 연결은 백틱
- Python API는 코드 흐름·후처리, CLI는 빠른 실험·자동화에 적합
- GPU가 없으면 `device=cpu`
- 기본 실행 점검은 `epochs=1~3`

#### 실습과 개념 확인

##### 실습 04 · YOLO 환경·구조·학습 시작 (PDF p.63)

- 25분 실습, 4단계 난이도
- 기본필수는 YOLO 객체를 만들어 task·class names·device를 출력하고 소형 데이터로 1~3 epoch smoke test 수행
- 응용은 Python API와 CLI의 동일 설정을 비교하고 runs 폴더·best/last 경로 기록
- 심화는 모델 규모 또는 imgsz 한 가지를 바꾸어 파라미터 수·시간·metric 변화 비교
- 특심화는 데이터 hash·환경·인자·artifact manifest를 저장하는 Config-driven 학습 Harness 작성
- 기본필수부터 완료하고 동일 데이터·분할·평가 조건을 유지한 채 선택 단계로 확장

##### 3분 퀴즈 · YOLO 학습 (PDF p.64)

- `model.train()`의 필수 데이터 인자가 `data`이며 보통 dataset.yaml 경로라는 점 확인
- Ultralytics CLI 인자는 `--epochs 30`이 아니라 `epochs=30` 형식이라는 점 확인
- best.pt는 검증 기준 최적 checkpoint, last.pt는 마지막 epoch 상태라는 점 확인

**핵심:** YOLO 학습은 Backbone·Neck·Head 구조와 dataset.yaml 계약을 확인한 뒤 짧은 smoke test로 연결을 점검하고, 실행 조건과 결과 경로를 함께 기록하는 과정.

### 5교시 · 검증·Metric·Checkpoint·과적합

#### 학습 전 데이터 계약과 학습 설정

##### 학습 전 데이터 계약을 먼저 확인한다 (PDF p.65)

- 대상 객체가 있는 이미지는 label 파일 필수, 객체가 있는데 txt가 없으면 실패
- 좌표는 0~1 범위와 박스 경계 확인, width=1.4 같은 값은 실패
- 박스 크기는 w>0, h>0, 0 크기 box는 실패
- `class_id`는 0~N−1의 정수, names 3개인데 class 4가 있으면 실패
- split 사이 group·hash 중복 없음, 같은 Frame이 train/val에 있으면 실패
- 클래스·박스 크기 분포 확인, 희소 클래스가 거의 없는 경우 점검

##### 주요 학습 인자와 영향 (PDF p.66)

- `epochs`는 전체 train 반복 횟수, 과소·과적합 관찰
- `imgsz`는 모델 입력 크기, 작은 객체·메모리·속도 관찰
- `batch`는 한 번에 로드하는 이미지 묶음 크기, VRAM·gradient 변동 관찰
- `device`는 CPU·GPU 선택, 환경·속도 관찰
- `workers`는 데이터 로딩 프로세스 수, CPU·I/O 병목 관찰
- `seed`는 초기화·증강 순서 재현, 실행 변동 관찰

##### 탐지 증강은 Box도 같이 변환해야 한다 (PDF p.67)

- 좌우 반전, 밝기·색상 변화, Scale·Crop, Mosaic·MixUp 등은 도움이 될 수 있는 변환
- 상하 반전으로 의미가 바뀌는 경우 주의
- 작은 객체가 사라지는 과도한 Crop 주의
- 현실에 없는 색·형태 주의
- valid/test에 무작위 증강을 반복 적용하지 않음
- 증강은 실제 운영 변동을 반영
- 이미지 변환과 동일한 변환을 라벨 박스에도 적용

#### 학습 산출물과 검증 실행

##### 학습 폴더에서 확인할 결과 (PDF p.68)

- `weights/best.pt`·`weights/last.pt`
- `results.csv`의 epoch별 loss·metric·learning rate
- PR·F1·confusion matrix·label distribution plots
- `train_batch`·`val_batch` 예시 이미지
- `args.yaml`은 실행 인자만 기록, 패키지·장치 환경은 별도 기록

##### 검증 데이터로 성능 측정 (PDF p.69)

- `YOLO("runs/day15/helmet_yolo/weights/best.pt")`로 학습 결과 로드
- `model.val(data="dataset.yaml", split="val", imgsz=640, device=device, workers=0, nms=True, conf=0.001, iou=0.70)` 형태로 검증
- `metrics.box.map50`·`metrics.box.map`으로 mAP50·mAP50-95 출력
- 검증은 후보 모델·설정 비교, 클래스별 Precision·Recall·AP 확인, 오류 이미지 분석에 사용
- test는 최종 확인까지 보관
- mAP50 0.78·mAP50-95 0.46은 예시 수치

##### model.val() (PDF p.70)

- 학습된 모델을 지정 split에서 평가하고 Detection metric과 속도 계산
- 학습 metadata가 없으면 `data` 경로 필요
- 주요 선택 인자는 split·imgsz·conf·iou·nms·device·batch·plots·save_json
- 반환 metrics 객체에서 `box.map50`·`box.map`·`speed` 확인
- `iou`는 NMS 기준이며 mAP의 평가 IoU와 구분
- valid와 test의 역할 유지

#### 검증 지표 해석과 오류 진단

##### 검증 출력의 주요 항목 (PDF p.71)

- Images는 검증 이미지 수, 클래스별 표본 수 확인
- Instances는 객체 수이며 이미지 수와 다름
- P가 낮으면 FP 점검
- R이 낮으면 FN 점검
- mAP50은 관대한 위치 기준 성능, 탐지 가능성 판단
- mAP50-95는 엄격한 위치 기준까지 평균, 박스 정밀도 판단
- Speed는 전처리·추론·후처리 시간, 실시간 가능성 판단

##### 학습곡선과 지표로 오류 패턴 진단 (PDF p.72)

- train은 개선되고 val이 정체하면 과적합·분포 차이 의심, split·augmentation·epoch 우선 확인
- P가 높고 R이 낮으면 놓침이 많거나 conf가 높은 상황, 작은 객체·라벨 누락 우선 확인
- R이 높고 P가 낮으면 거짓 탐지가 많은 상황, Negative image·conf 우선 확인
- mAP50이 mAP50-95보다 크게 높으면 박스 위치 부정확, 라벨 밀착·해상도 우선 확인
- 클래스별 편차가 크면 불균형·라벨 규칙 차이 의심, 표본 수·혼동 클래스 우선 확인

#### Checkpoint 구분

##### best·last·resume를 구분한다 (PDF p.73)

- best.pt는 검증 기준 최적 checkpoint
- best.pt는 추론·최종 평가의 기본 후보
- best.pt 사용 시 기준 metric과 epoch 기록
- last.pt는 마지막으로 저장한 checkpoint
- resume에는 재개 가능한 학습 상태 필요
- 완료된 run의 추가 학습은 resume과 별도로 구분

#### 실습과 개념 확인

##### 실습 05 · 검증·Metric·Checkpoint 분석 (PDF p.74)

- 25분 실습, 4단계 난이도
- 기본필수는 제공된 results.csv와 선정 기준에서 best epoch·mAP50·mAP50-95를 찾아 한 문장으로 해석
- 응용은 클래스별 Precision·Recall·AP를 비교하고 가장 먼저 확인할 오류 이미지 범주 결정
- 심화는 best.pt·last.pt 추론 결과를 같은 입력에서 비교하고 차이를 보고서에 기록
- 특심화는 중단·재개 실험으로 model·optimizer·epoch·seed·args·artifact hash의 연속성 검증
- 기본필수부터 완료하고 동일 데이터·분할·평가 조건을 유지한 채 선택 단계로 확장

##### 3분 퀴즈 · 검증과 Checkpoint (PDF p.75)

- mAP50이 높고 mAP50-95가 낮으면 객체는 찾지만 박스 위치가 정밀하지 않을 가능성 확인
- best.pt가 마지막 epoch가 아니라 검증 기준이 가장 좋았던 epoch일 수 있다는 점 확인
- resume 시 데이터와 설정이 달라지면 비교의 의미가 깨지므로 버전과 설정을 고정·기록하는 원칙 확인

**핵심:** 검증 지표는 valid에서만 모델과 설정을 고르는 근거이며, P·R·mAP50·mAP50-95의 차이와 학습곡선을 함께 읽어 오류 원인 후보와 사용할 checkpoint를 정함.

### 6교시 · 추론·Results·오류 분석

#### predict 실행

##### 이미지·영상·폴더를 추론한다 (PDF p.76)

- `YOLO("best.pt")`로 학습 모델 로드
- `model.predict(source="samples/", conf=0.25, iou=0.70, nms=True, imgsz=640, save=True, stream=False)` 형태로 추론
- source는 이미지 경로·폴더·URL·Video·PIL Image·OpenCV ndarray·Webcam index 0·입력 List
- 결과는 Results 객체 List, 각 결과에 박스·클래스·신뢰도·원본 Shape 포함
- `save=True`면 시각화 결과 저장
- `result.path`와 `len(result.boxes)`로 입력별 탐지 수 확인

##### model.predict() (PDF p.77)

- 새 이미지·영상·스트림에서 객체의 클래스와 위치 추론
- 필수 인자는 `source`
- 주요 선택 인자는 conf·iou·nms·imgsz·classes·device·save·save_txt·stream
- `stream=False`는 Results List, `stream=True`는 순차 Generator 반환
- 긴 영상은 `stream=True` 사용
- nms·conf·NMS iou와 처리한 Frame 수 기록

#### Results 읽기와 저장

##### Results 객체에서 확인할 정보 (PDF p.78)

- `result.path`는 입력 파일 경로
- `result.orig_shape`는 원본 이미지 H,W
- `result.names`는 class id → 이름 Mapping
- `result.boxes`는 탐지 박스 집합
- `result.plot()`은 박스·Label이 그려진 ndarray 반환
- `result.save()`는 시각화 이미지 저장
- `result.to_df()`·`save_txt` 등으로 표·파일 형태 활용

##### Box 좌표·신뢰도·클래스 읽기 (PDF p.79)

- `boxes.xyxy`는 원본 Pixel 좌표 `[N,4]`
- `boxes.xywh`는 중심 x,y,w,h
- `xyxyn`·`xywhn`은 정규화 좌표
- `conf`·`cls`는 `[N]` 크기의 점수와 클래스 ID
- GPU Tensor는 `.cpu()` 후 NumPy로 변환
- 클래스 ID는 int로 변환한 뒤 `result.names[class_id]`로 이름 조회
- 탐지가 없으면 N=0

##### 시각화 결과 저장 (PDF p.80)

- `outputs` 폴더를 `mkdir(parents=True, exist_ok=True)`로 생성
- `result.plot()`은 BGR 시각화 배열, `cv2.imwrite` 실패 시 `OSError`로 중단
- 결과마다 TXT를 빈 문자열로 먼저 써서 재실행 시 중복 행 방지
- `result.save_txt(..., save_conf=True)`는 정규화 중심 Box와 점수 저장
- 예측 TXT는 학습용 5열 라벨과 구분
- 후속 분석용 CSV는 별도로 생성
- 입력별 JPG·TXT 한 쌍 확인, 빈 탐지는 빈 TXT

#### 입력 방식과 stream

##### Predict 입력 방식과 stream 선택 (PDF p.81)

- 이미지 1장 `"bus.jpg"`는 List 결과
- 폴더 `"images/"`는 Batch 또는 stream
- 영상 `"video.mp4"`는 `stream=True` 권장
- Webcam `0`은 실시간 Loop
- OpenCV ndarray `cv2.imread(...)`는 메모리 입력
- List `[img1,img2]`는 소규모 Batch

#### 오류 유형과 Threshold 효과

##### 탐지 오류를 유형별로 나눈다 (PDF p.82)

- Missed object는 작은 사람을 놓친 경우, 해상도·라벨·Recall 가설
- False positive는 나뭇가지를 사람으로 탐지한 경우, Negative image·conf 가설
- Wrong class는 고양이를 개로 분류한 경우, 클래스 경계·불균형 가설
- Loose box는 박스가 배경을 많이 포함한 경우, 라벨 품질·imgsz 가설
- Duplicate box는 한 객체에 여러 박스가 남은 경우, NMS IoU·conf 가설
- Domain shift는 야간·비·새 카메라에서 악화된 경우, 데이터 분포 가설

##### Confidence Threshold의 효과 (PDF p.83)

- Threshold를 낮추면 후보가 많아지고 Recall 증가 가능
- Threshold를 낮추면 FP 증가와 후처리·검토 비용 증가 가능
- Threshold를 높이면 강한 후보만 남고 Precision 증가 가능
- Threshold를 높이면 FN 증가와 작은·어려운 객체 누락 가능

##### NMS IoU Threshold의 효과 (PDF p.84)

- 낮게 설정하면 낮은 겹침부터 후보를 제거해 중복 박스 감소
- 낮게 설정하면 밀집 객체를 놓칠 위험
- 높게 설정하면 많이 겹쳐도 후보를 유지해 가까운 객체 분리 가능
- 높게 설정하면 중복 박스가 남을 위험

#### 실습과 개념 확인

##### 실습 06 · YOLO 추론·결과 분석 (PDF p.85)

- 25분 실습, 4단계 난이도
- 기본필수는 제공 이미지 폴더를 predict하고 파일별 탐지 수·class·confidence를 CSV로 저장
- 응용은 conf 0.15·0.25·0.50을 비교해 탐지 수·FP·FN 변화 기록
- 심화는 오류 이미지를 Miss·FP·Wrong class·Loose box·Duplicate로 분류하고 우선 개선안 작성
- 특심화는 대규모 입력을 stream으로 처리하고 result·artifact·오류 Slice를 재현 가능하게 저장
- 기본필수부터 완료하고 동일 데이터·분할·평가 조건을 유지한 채 선택 단계로 확장

##### 3분 퀴즈 · Predict와 Results (PDF p.86)

- 긴 영상을 List로 받으면 모든 Results를 메모리에 보관해 사용량이 커질 수 있다는 점 확인
- `boxes.xyxy`는 원본 Pixel 좌표이고 정규화 좌표는 `xyxyn`이라는 점 확인
- Confidence를 높이면 낮은 점수의 실제 객체까지 제거되어 Recall이 떨어질 수 있다는 점 확인

**핵심:** 추론 결과는 Results에서 좌표 형식과 클래스 이름을 정확히 읽어 저장하고, 오류를 유형별로 나눠 conf·NMS IoU·데이터 중 무엇을 먼저 바꿀지 판단함.

### 7교시 · 다중 객체 추적·속도 측정

#### Tracking 개념과 Detect 비교

##### Tracking은 Frame 사이에서 같은 객체의 ID를 유지한다 (PDF p.87)

- Detection은 각 Frame의 박스·클래스
- Association은 이전 Frame과 현재 탐지의 연결
- Track ID는 객체의 연속된 식별자
- 궤적·카운팅·체류시간 분석으로 확장

##### 탐지와 추적의 차이 (PDF p.88)

- Detect 입력은 이미지 또는 각 Frame, Track 입력은 연속 Frame Sequence
- Detect 출력은 box·class·confidence, Track 출력은 여기에 track_id 추가
- Detect는 Frame 간 상태가 없고 Track은 이전 Frame 상태 사용
- Detect의 주요 실패는 Miss·FP·Wrong class, Track의 주요 실패는 ID switch·track loss
- Detect는 객체 위치, Track은 카운팅·궤적·체류시간에 활용

#### track() 실행과 Tracker 상태

##### 영상 객체 추적 (PDF p.89)

- 새 영상은 새 `YOLO("best.pt")` 객체로 시작해 새 Tracker 상태 사용
- `model.track(source="traffic.mp4", persist=True, tracker="botsort.yaml", conf=0.25, iou=0.70, nms=True, stream=True, save=True)` 형태로 실행
- `persist=True`는 호출 사이에 Tracker 상태 유지
- `tracker`로 BoT-SORT·ByteTrack 선택
- 출력은 box·class·confidence·track_id와 시각화 영상
- `result.boxes.id`로 Track ID 확인

##### model.track() (PDF p.90)

- 객체탐지와 Tracker를 연결해 연속 Frame에서 객체 ID 유지
- 필수 인자는 `source`, 영상·카메라·연속 Frame
- 주요 선택 인자는 persist·tracker·conf·iou·nms·imgsz·device·save·stream
- 반환값은 Results Sequence, `boxes.id`에 Track ID가 포함될 수 있음
- `persist=True`는 같은 영상의 연속 Frame에만 사용
- 서로 다른 Stream의 Tracker 상태를 섞지 않음

##### persist와 Tracker 상태 관리 (PDF p.91)

- 같은 영상의 연속 Frame 호출은 `persist=True`로 이전 상태 재사용
- 새로운 영상·카메라는 새 YOLO 객체로 Tracker 상태 초기화
- Frame을 건너뛰면 빠른 객체·가림에서 ID 유지가 어려워질 수 있음
- Tracker 설정은 YAML로, Track ID·궤적은 추론 중 상태로 관리

##### Track ID별 중심점 궤적 수집 (PDF p.92)

- `enumerate(model.track(..., stream=True), start=1)`로 Frame 번호와 결과를 함께 순회
- `boxes`가 `None`이거나 `boxes.id`가 `None`인 Frame은 건너뜀
- `boxes.id.int().cpu().tolist()`로 ID, `boxes.xywh`로 중심 좌표 추출
- `tracks.setdefault(tid, []).append((frame_idx, cx, cy))`로 ID별 궤적 누적
- 객체별 궤적 그리기·라인 통과 카운팅·ROI 체류시간·속도 추정으로 확장
- ID switch·가림·재등장 주의
- 속도 추정에는 Frame rate와 Pixel → 실거리 보정 필요

#### 추적 오류와 속도 측정

##### 추적 결과에서 확인할 오류 (PDF p.93)

- ID switch는 같은 객체의 ID가 바뀌는 현상, 가림·유사 객체·낮은 FPS가 원인 후보
- Track fragmentation은 하나의 궤적이 여러 조각으로 나뉘는 현상, Detection miss·짧은 buffer가 원인 후보
- False track은 배경에 ID가 생기는 현상, FP·낮은 conf가 원인 후보
- Lost track은 가림 후 복귀 실패, association 설정이 원인 후보
- Duplicate track은 한 객체에 여러 ID, 중복 Detection·NMS가 원인 후보

##### 속도·지연시간·처리량을 구분한다 (PDF p.94)

- Latency는 한 Frame 완료까지 걸린 시간, 전처리·추론·후처리 범위 기록
- FPS는 1초에 처리 가능한 Frame 수, Batch·입력 크기·device 기록
- Throughput은 단위 시간당 이미지 수, Batch inference 조건 기록
- Peak VRAM은 최대 GPU 메모리, 모델·imgsz·batch 기록
- End-to-end는 Decode → Track → Encode 전체, I/O 포함
- CUDA는 비동기이므로 정확한 구간 측정 시 synchronize 필요

#### 데모 프로젝트 구조

##### YOLO 탐지·추적 데모 프로젝트 구조 (PDF p.95)

- `data/images·videos`는 입력 이미지·영상
- `data/dataset.yaml`은 경로·class names
- `src/infer.py`는 이미지·영상 추론
- `src/track.py`는 Tracker·ID·궤적
- `src/evaluate.py`는 IoU·오류·속도 요약
- `outputs/`는 시각화·CSV·영상
- `reports/demo_report.md`는 Metric·오류·한계·재현 조건

#### 통합 실습과 개념 확인

##### 실습 07 · YOLO 탐지·추적 데모 통합 (PDF p.96)

- 25분 실습, 4단계 난이도
- 기본필수는 제공 weight와 입력으로 이미지 탐지·영상 추적을 실행하고 결과 CSV·영상 저장
- 응용은 conf 후보 비교 또는 Tracker 2종 비교 중 하나를 택해 탐지 수·관찰한 ID 전환·FPS 기록
- 심화는 오류 Slice·클래스별 지표·추적 실패 Frame을 연결해 우선 개선안 작성
- 특심화는 Config-driven 실행 Harness·artifact manifest·checkpoint·성능 회귀 검사 구현
- 기본필수부터 완료하고 동일 데이터·분할·평가 조건을 유지한 채 선택 단계로 확장

##### 3분 퀴즈 · 객체 추적 (PDF p.97)

- Tracking ID는 모델 weight에 저장되지 않고 Tracker가 추론 중 유지하는 상태라는 점 확인
- 서로 다른 영상에 `persist=True` 상태를 이어 쓰면 관련 없는 Stream의 상태가 섞인다는 점 확인
- Detector의 miss와 FP가 추적 품질의 상한을 제한하므로 Tracker 교체만으로 해결되지 않는다는 점 확인

**핵심:** 추적은 같은 Stream 안에서만 Tracker 상태를 이어 Track ID를 유지하는 작업이며, 추적 품질은 탐지 품질에 묶이고 속도는 측정 구간을 명시해야 비교 가능함.

### 8교시 · YOLO 탐지·추적 데모 통합

#### 최종 제출물과 점검 상황

##### 최종 제출물 (PDF p.98)

- `label_audit.csv`는 클래스·박스·누락·중복·split 검사
- `metrics_summary.csv`는 P·R·mAP50·mAP50-95·속도
- `detections.csv`는 파일·box·class·confidence
- `tracking.csv`는 frame·track_id·box·class
- `demo.mp4`는 박스·ID 시각화, 궤적은 선택 확장
- `demo_report.md`는 설정·오류 사례·한계·개선안
- `README.md`는 환경·실행 명령·결과 재생성 방법

##### 정상·경계·실패 상황 (PDF p.99)

- 정상 이미지는 박스·클래스·신뢰도 저장, 원본 크기·파일 수 확인
- 객체 없음은 빈 결과를 정상 처리, 오류가 아님
- 작은 객체는 Miss 가능성 기록, imgsz·라벨 확인
- 겹친 객체는 중복·NMS 영향 확인, conf·IoU 확인
- 손상 label은 학습 전 감사에서 실패 처리, 문제 파일 경로 확인
- 새 영상 Stream은 Tracker 상태 초기화, ID 재시작 확인
- CPU-only는 기본 추론 가능, device·속도 기록

#### 평가 기준

##### 형성평가 기준 · 100점 (PDF p.100)

- 라벨·데이터 20점은 YOLO 포맷·분할·누수·품질 점검
- IoU·지표 20점은 TP/FP/FN·P/R·mAP 해석
- 학습·검증 20점은 설정·best/last·Metric·재현 조건
- 추론·추적 20점은 Results·ID·속도·오류 분석
- 프로젝트 설명 20점은 실행·결과·한계·개선안을 본인 말로 설명
- 절대 성능 점수보다 데이터 계약·실험 구조·오류 해석·재현성을 평가

#### 최종 검증 실습

##### 실습 08 · 최종 검증·보고서·시연 (PDF p.101)

- 30분 실습, 4단계 난이도
- 기본필수는 같은 입력·설정으로 다시 실행해 파일·Frame 수와 지표를 허용오차 내에서 비교하고 핵심 결과 설명
- 응용은 짝이 README만 보고 실행하게 하고 결과가 다르면 model·data·conf·iou·tracker·device 확인
- 심화는 정상·객체 없음·작은 객체·겹친 객체·새 Stream을 시연하고 배포 전 점검표 작성
- 특심화는 다중 Stream·AMP·비동기 I/O·checkpoint resume·성능 회귀를 포함한 검증 Suite 구현
- 기본필수부터 완료하고 동일 데이터·분할·평가 조건을 유지한 채 선택 단계로 확장

**핵심:** 최종 데모는 박스가 보이는 결과물이 아니라 같은 조건으로 재실행해 같은 결과를 얻고, 데이터·지표·오류·한계를 본인 말로 설명할 수 있는 상태.

### 마무리 · 정리와 다음 수업

#### 확인 퀴즈·핵심 정리·OCR·VLM 예고

##### 마무리 3분 확인 퀴즈 (PDF p.102)

- 더 엄격한 IoU 기준을 포함하는 mAP50-95가 mAP50보다 일반적으로 낮다는 점 확인
- Confidence와 NMS IoU는 valid에서 선택하고 test는 최종 확인에만 사용한다는 점 확인
- Track ID가 바뀌는 문제는 ID switch이며 Detector miss·가림·association 설정을 함께 확인한다는 점 확인

##### 오늘의 핵심 정리 (PDF p.103)

- 객체탐지는 객체마다 클래스·Bounding Box·신뢰도를 예측
- IoU·NMS·Precision·Recall·mAP는 서로 다른 질문에 답하는 기준
- 좋은 라벨·그룹 분할·Negative image가 모델 성능의 기반
- YOLO의 train·val·predict·track 결과를 데이터·설정·오류 사례와 함께 기록
- 설명할 수 있어야 할 흐름은 좌표 형식 → IoU·NMS → YOLO 데이터 → 학습·검증 → 추론·추적

##### 다음 수업 · OCR·VLM·추론 시스템 (PDF p.104)

- 11월 9일은 OCR 문서 영역 탐지·텍스트 인식, 문서 정보 구조화와 후처리, VLM 시각 질의응답, OCR·VLM 미니 애플리케이션
- Detection은 OCR Text Box 탐지로 확장
- Box·Confidence·오류 분석 원칙은 그대로 유지
- 영상 Stream 처리는 DeepStream 흐름과 연결
- TensorRT·Jetson 배포에서도 속도·메모리 측정 원칙 유지

### 참고자료 · 공식 문서

#### Ultralytics·OpenCV 공식 참고자료

##### 공식 참고자료 · 객체탐지와 데이터 (PDF p.105)

- Ultralytics의 Object Detection Datasets Overview
- Ultralytics의 YOLO Performance Metrics
- Ultralytics의 Python Usage · Train / Val / Predict
- OpenCV의 Drawing Functions · rectangle / putText
- 문서 확인일 2026.10.30, 예제 기준 Ultralytics 8.4.142, 실행 환경 버전은 별도 기록

##### 공식 참고자료 · 추론과 추적 (PDF p.106)

- Ultralytics의 Command Line Interface
- Ultralytics의 Configuration
- Ultralytics의 Multi-Object Tracking in Video
- Ultralytics의 Results API
- 예제 버전과 checkpoint를 고정하고 변경 시 NMS·Results·Tracker 동작 재확인
