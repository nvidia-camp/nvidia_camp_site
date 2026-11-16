# Day14 강의 구조·핵심 설명

2026-11-05 · Vision·멀티모달 AI 응용 2/4 · 전이학습 기반 Vision 모델 구성과 데이터셋 설계

교시 설명과 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준이며 이 PDF는 인쇄 쪽수와 PDF 쪽수가 같습니다(전체 99쪽). 도입·마무리·참고자료는 별도 묶음으로 유지했습니다.

## 강의 목차

```text
도입 · 업무 흐름과 수업 범위
├─ 이미지 분류 실험의 전체 지도
│  ├─ Vision·멀티모달 AI 응용 (PDF p.1)
│  ├─ 현업의 이미지 분류와 전이학습 (PDF p.2)
│  ├─ 오늘 만드는 분류 실험의 전체 구조 (PDF p.3)
│  ├─ 데이터셋에서 한 장의 이미지까지 (PDF p.4)
│  ├─ 분류 모델 안의 Backbone과 Head (PDF p.5)
│  ├─ Head 안에서 학습하는 Weight와 Bias (PDF p.6)
│  ├─ 학습할 범위를 선택하는 Freeze와 Fine-tuning (PDF p.7)
│  ├─ 전체 점수와 클래스별 실패를 함께 보는 이유 (PDF p.8)
│  ├─ 오류 이미지와 Grad-CAM으로 원인 후보 찾기 (PDF p.9)
│  ├─ 모델 비교에서 고정하고 기록할 조건 (PDF p.10)
│  └─ 전이학습 분류 프로젝트로 다시 합치기 (PDF p.11)
└─ 복습·운영·환경
   ├─ 어제 우리가 배운 것 (PDF p.12)
   ├─ 3분 확인 퀴즈 · 전처리에서 전이학습으로 (PDF p.13)
   ├─ 오늘의 목표와 8교시 운영 (PDF p.14)
   ├─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)
   └─ 실습 전 환경과 데이터 조건을 확인한다 (PDF p.16)

1교시 · 데이터셋 설계·분할·누수
├─ 샘플 정보와 ImageFolder 라벨 계약
│  ├─ 좋은 Vision 모델은 데이터셋 설계에서 시작한다 (PDF p.17)
│  ├─ 한 장의 이미지가 가져야 할 정보 (PDF p.18)
│  ├─ ImageFolder 구조와 class_to_idx (PDF p.19)
│  ├─ 클래스별 파일 수와 라벨 매핑 확인 (PDF p.20)
│  └─ torchvision.datasets.ImageFolder (PDF p.21)
├─ 데이터 품질과 누수 없는 분할
│  ├─ 분할 전에 확인할 데이터 품질 (PDF p.22)
│  ├─ 같은 장면이 train과 test에 동시에 들어가면 안 된다 (PDF p.23)
│  └─ Vision 데이터 분할 설계 (PDF p.24)
└─ 실습과 개념 확인
   ├─ 실습 01 · 데이터셋 구조와 누수 점검 (PDF p.25)
   └─ 3분 퀴즈 · 데이터셋 설계 (PDF p.26)

2교시 · 사전학습 Backbone·Head 교체
├─ Backbone과 Head의 역할 분리
│  ├─ 사전학습 Backbone의 표현을 새 문제에 재사용한다 (PDF p.27)
│  ├─ Backbone과 Head를 분리해서 생각한다 (PDF p.28)
│  └─ Head-only와 Fine-tuning 비교 (PDF p.29)
├─ ResNet18 Head 교체와 입력 전처리
│  ├─ ResNet18 Head 교체와 Backbone 고정 (PDF p.30)
│  ├─ torchvision.models.resnet18 (PDF p.31)
│  └─ ResNet18_Weights와 전처리 (PDF p.32)
├─ 학습 범위 점검과 BatchNorm 모드
│  ├─ 학습 가능한 파라미터 수 확인 (PDF p.33)
│  └─ 고정된 Backbone의 train/eval 모드를 구분한다 (PDF p.34)
└─ 실습과 개념 확인
   ├─ 실습 02 · 사전학습 Backbone과 새 Head (PDF p.35)
   └─ 3분 퀴즈 · 전이학습 기초 (PDF p.36)

3교시 · Freeze·Partial/Full Fine-tuning
├─ 단계적 해제와 층별 학습률
│  ├─ Head 기준선 이후 일부 층을 연다 (PDF p.37)
│  ├─ 마지막 Stage와 Head에 서로 다른 학습률 적용 (PDF p.38)
│  └─ named_parameters·requires_grad·Parameter Group (PDF p.39)
├─ 실험 계획과 결과 해석
│  ├─ Fine-tuning 실험 계획 (PDF p.40)
│  ├─ 합성 예시의 validation accuracy 곡선 (PDF p.41)
│  ├─ Scratch·Head-only·Partial fine-tuning 결과 (PDF p.42)
│  └─ 전이학습이 항상 더 좋은 것은 아니다 (PDF p.43)
├─ Fine-tuning 오류 점검
│  └─ Fine-tuning에서 자주 발생하는 오류 (PDF p.44)
└─ 실습과 개념 확인
   ├─ 실습 03 · Head-only·Partial Fine-tuning 비교 (PDF p.45)
   └─ 3분 퀴즈 · Fine-tuning (PDF p.46)

4교시 · 클래스 불균형·Loss·Sampler
├─ 불균형이 가리는 소수 클래스 실패
│  ├─ 클래스 불균형은 학습과 평가를 함께 바꾼다 (PDF p.47)
│  ├─ 다수 클래스 Accuracy가 소수 클래스 실패를 가릴 수 있다 (PDF p.48)
│  └─ 학습 데이터의 클래스별 개수 (PDF p.49)
├─ Class weight와 Weighted sampler
│  ├─ 불균형 대응 방법 비교 (PDF p.50)
│  ├─ nn.CrossEntropyLoss의 class weight (PDF p.51)
│  ├─ WeightedRandomSampler (PDF p.52)
│  ├─ 클래스 개수로 Loss weight 만들기 (PDF p.53)
│  └─ 샘플별 weight로 추출 빈도 조정 (PDF p.54)
├─ 대응 전략 결과 비교
│  ├─ 불균형 대응 전략의 validation Macro F1 (PDF p.55)
│  └─ 합성 예시의 클래스별 Recall 비교 (PDF p.56)
└─ 실습과 개념 확인
   ├─ 실습 04 · 클래스 불균형 대응 (PDF p.57)
   └─ 3분 퀴즈 · 클래스 불균형 (PDF p.58)

5교시 · 평가·Confusion Matrix·오류 분석
├─ Confusion Matrix와 클래스별 지표
│  ├─ 평가표에는 전체 점수와 클래스별 실패를 함께 남긴다 (PDF p.59)
│  ├─ 합성 예시: Sampler의 Confusion Matrix (PDF p.60)
│  ├─ 클래스별 지표가 답하는 질문 (PDF p.61)
│  └─ Macro와 Weighted 평균을 구분한다 (PDF p.62)
├─ 분류 보고서 생성
│  ├─ Confusion Matrix와 분류 보고서 (PDF p.63)
│  └─ classification_report (PDF p.64)
├─ 오류 원인 후보와 오류 이미지
│  ├─ 오류를 원인 후보로 분류한다 (PDF p.65)
│  └─ 오류 이미지는 예측값과 함께 검토한다 (PDF p.66)
└─ 실습과 개념 확인
   ├─ 실습 05 · 평가표와 오류 이미지 분석 (PDF p.67)
   └─ 3분 퀴즈 · 평가와 오류 분석 (PDF p.68)

6교시 · Grad-CAM·편향·설명 한계
├─ Grad-CAM 원리와 대상 층
│  ├─ Grad-CAM은 예측에 기여한 공간 영역을 시각화한다 (PDF p.69)
│  ├─ Grad-CAM 계산 흐름 (PDF p.70)
│  └─ 어떤 층을 선택할 것인가? (PDF p.71)
├─ Hook 기록과 Heatmap 계산
│  ├─ Activation과 Gradient를 Hook으로 기록 (PDF p.72)
│  ├─ Module과 Tensor Hook (PDF p.73)
│  ├─ 채널 weight와 Heatmap 계산 (PDF p.74)
│  └─ 합성 이미지의 Grad-CAM 예시 (PDF p.75)
├─ 해석 한계와 데이터 편향 점검
│  ├─ Grad-CAM을 정답 근거처럼 해석하지 않는다 (PDF p.76)
│  └─ 시각 설명으로 데이터 편향 후보를 찾는다 (PDF p.77)
└─ 실습과 개념 확인
   ├─ 실습 06 · Grad-CAM과 편향 점검 (PDF p.78)
   └─ 3분 퀴즈 · Grad-CAM (PDF p.79)

7교시 · 모델 비교·프로젝트 통합
├─ 비교 조건과 합성 예시 결과
│  ├─ 모델 비교 전에 고정할 조건 (PDF p.80)
│  ├─ 수업용 합성 예시 비교표 (PDF p.81)
│  ├─ 전략별 Macro F1 비교 (PDF p.82)
│  ├─ 합성 예시의 학습곡선 읽기 (PDF p.83)
│  └─ 학습 범위와 비용을 함께 기록 (PDF p.84)
├─ 프로젝트 구조와 산출물
│  ├─ 전이학습 분류 프로젝트 구조 예시 (PDF p.85)
│  ├─ 프로젝트 공통 작업 순서 (PDF p.86)
│  └─ 단계별 프로젝트 산출물 (PDF p.87)
└─ 통합 실습과 경계 상황
   ├─ 실습 07 · 전이학습 분류 프로젝트 통합 (PDF p.88)
   └─ 정상·경계·실패 상황 (PDF p.89)

8교시 · 실습평가·시연·회고
├─ 최종 프로젝트 요구와 평가 기준
│  ├─ 최종 미니 프로젝트 · 전이학습 분류 모델 (PDF p.90)
│  ├─ 단계별 최종 제출물 (PDF p.91)
│  └─ 형성평가 기준 · 100점 (PDF p.92)
└─ 최종 검증 실습
   └─ 실습 08 · 최종 검증·보고서·시연 (PDF p.93)

마무리 · 정리와 다음 수업
└─ 확인 퀴즈·핵심 정리·객체탐지 예고
   ├─ 마무리 3분 확인 퀴즈 (PDF p.94)
   ├─ 오늘의 핵심 정리 (PDF p.95)
   └─ 다음 수업 · 11월 6일 객체탐지 (PDF p.96)

참고자료 · 공식 문서와 Weight 점검
└─ 참고자료와 부록
   ├─ 공식 참고자료 · PyTorch·Torchvision (PDF p.97)
   ├─ 공식 참고자료 · 평가와 설명 (PDF p.98)
   └─ 사전학습 Weight 사용 전 점검 (PDF p.99)
```

## 핵심 설명

### 도입 · 업무 흐름과 수업 범위

#### 이미지 분류 실험의 전체 지도

##### Vision·멀티모달 AI 응용 (PDF p.1)

- 정규교과 2/4 표지
- 데이터셋 설계 → 전이학습·Fine-tuning → 불균형 평가 → 오류 분석·Grad-CAM 순서의 하루 흐름 제시

##### 현업의 이미지 분류와 전이학습 (PDF p.2)

- 제품·문서 사진 → 전처리와 분류 모델 → 클래스별 점수·예측 결과 → 검토·분류 업무로 이어지는 흐름
- 제품 사진의 정상·결함 유형 분류, 문서 사진의 영수증·명세서·기타 분류를 가상 사례로 사용
- 이미 학습한 표현을 출발점으로 삼되 우리 데이터에서 성능을 다시 확인
- 어제의 입력 준비에서 오늘의 분류 모델 학습과 실패 사례 분석으로 확장

##### 오늘 만드는 분류 실험의 전체 구조 (PDF p.3)

- 데이터셋·분할 → 사전학습 Backbone·새 Head 연결 → 학습 범위 선택·불균형 대응 → 지표·오류 이미지·Grad-CAM 분석 → 비교표와 다음 실험 가설의 순환 구조
- 다음 실험은 valid로 결정하고 test는 최종 확인에만 사용
- 결과물은 예측값과 함께 설정·지표·오류 근거를 남기는 분류 프로젝트

##### 데이터셋에서 한 장의 이미지까지 (PDF p.4)

- 한 샘플은 이미지·정답·그룹 ID를 함께 가져야 학습과 평가가 가능
- 폴더 이름과 숫자 라벨의 연결 `class_to_idx`는 circle 0·square 1·triangle 2 예시
- 모든 분할에서 같은 클래스 매핑 유지
- 관련 원본·개체는 같은 분할에 배치
- RGB·크기·Normalize는 선택한 Weight의 입력 조건에 맞춤

##### 분류 모델 안의 Backbone과 Head (PDF p.5)

- Backbone은 RGB 이미지 Batch에서 특징을 추출·풀링해 512개 특징 벡터 생성
- 새 Head `Linear(512, 3)`가 특징을 3개 클래스 Logit으로 변환
- Backbone은 기존 파라미터를 가져오고 새 Head는 우리 데이터의 정답으로 학습
- 전이학습의 출발점은 기존 표현이며 우리 데이터에서의 성능은 별도 평가

##### Head 안에서 학습하는 Weight와 Bias (PDF p.6)

- `nn.Linear(512, 3)`의 weight 크기 `[3, 512]`, 개수 1,536
- bias 크기 `[3]`, 개수 3
- 512개 특징을 Weight로 조합하고 Bias를 더해 클래스 점수 3개 계산
- Head 학습 파라미터는 512 × 3 + 3 = 1,539개

##### 학습할 범위를 선택하는 Freeze와 Fine-tuning (PDF p.7)

- Head-only는 앞쪽 Backbone·layer4 고정, 새 Head만 학습
- Partial은 앞쪽 Backbone 고정, layer4와 새 Head 학습
- Full은 전체 학습
- `requires_grad`는 Gradient 계산 대상, Optimizer는 파라미터 갱신 대상, train/eval은 BatchNorm·Dropout 동작을 결정하는 서로 다른 설정
- 고정한 부분도 순전파 계산은 수행, BatchNorm 통계 상태는 별도 관리

##### 전체 점수와 클래스별 실패를 함께 보는 이유 (PDF p.8)

- 10장 예시에서 모두 circle로 예측하면 Accuracy 80%(8/10)
- 같은 예시에서 triangle Recall 0%(0/1), Macro F1 ≈ 0.296
- 자주 나온 클래스만 맞혀도 전체 Accuracy는 높게 보일 수 있음
- 전체 Accuracy와 클래스별 Recall·support, 실제 오류 이미지를 함께 확인

##### 오류 이미지와 Grad-CAM으로 원인 후보 찾기 (PDF p.9)

- 선택 클래스의 Logit을 합성곱 Feature Map에 대해 미분하고 Gradient의 공간 평균으로 채널 Weight 계산
- 채널 Weight × Feature Map 가중합에 ReLU를 적용하고 Heatmap을 확대해 원본과 비교
- 대상·배경 중 어떤 영역과 관련되는지 보고 가림 실험 등으로 원인 후보 확인
- Grad-CAM은 분석용 Gradient 사용 단계이며 Optimizer로 모델을 갱신하지 않음

##### 모델 비교에서 고정하고 기록할 조건 (PDF p.10)

- 분할·클래스 매핑, 평가 입력·주 지표, 비교 기준은 고정
- Weight·시작 checkpoint, 학습 범위·학습률·학습량, BN 정책·Loss·Sampler·seed는 변경 사항으로 기록
- 후보 A(Head-only)와 B(Partial 등)는 valid에서 비교·선택하고 선택 후 test로 최종 확인
- 순차 학습은 앞 단계의 학습량도 기록
- epoch가 같아도 학습시간까지 같지는 않음

##### 전이학습 분류 프로젝트로 다시 합치기 (PDF p.11)

- 3클래스 데이터 매핑·분할 확인 → Head-only 기준 모델 → 지표·예측·오류·Grad-CAM → 재실행·결과 설명의 흐름
- 기본필수는 기준 모델 결과 생성과 오류·핵심 결과 설명
- 응용은 Partial·불균형 대응 후보를 비교표에 추가
- 심화·특심화는 오류 가설 검증·설정 기반 실험·재현성 도구
- 01 데이터부터 08 검증까지 실습 번호와 주제 대응

#### 복습·운영·환경

##### 어제 우리가 배운 것 (PDF p.12)

- 이미지를 BGR/RGB·Gray·HSV 배열로 표현하고 Resize·Filter·형태학 처리 적용
- 영상을 Frame 단위로 처리하고 FPS·크기·Frame 수를 확인하며 저장
- 원본과 결과를 재읽어 Shape·픽셀·재생시간을 비교하고 정보 손실 검증
- 오늘은 이미지 처리 코드에서 분류 모델 학습과 실패 분석 실험으로 이동

##### 3분 확인 퀴즈 · 전처리에서 전이학습으로 (PDF p.13)

- train과 valid에 같은 무작위 증강을 적용하지 않고 valid를 고정된 평가 입력으로 유지하는지 확인
- OpenCV BGR 이미지를 ResNet18에 넣기 전 RGB 변환과 Weight에 맞는 Normalize 확인
- Shape가 같아도 픽셀·라벨 의미·오류 사례를 함께 확인해야 의미 보존을 판단할 수 있다는 점 확인

##### 오늘의 목표와 8교시 운영 (PDF p.14)

- 1교시 데이터셋 설계·분할·누수, 설명·시연 30분과 실습·리뷰 20분
- 2~7교시는 Backbone·Head 교체, Fine-tuning, 불균형, 평가·오류 분석, Grad-CAM, 모델 비교·프로젝트 통합 순서로 각 25분·25분
- 8교시 실습평가·시연·회고, 설명·시연 20분과 실습·리뷰 30분

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)

- 오늘은 데이터셋 구조·분할·클래스 불균형 진단
- 사전학습 Vision Backbone과 새 Head 연결
- Fine-tuning 범위를 단계적으로 열고 공정하게 비교
- Confusion Matrix·오류 이미지·Grad-CAM으로 실패 설명
- 11월 6일에는 객체탐지의 Bounding Box·IoU·mAP와 YOLO 학습·추론·추적, 라벨 품질 점검으로 확장
- 오늘의 분할·오류 분석·시각 설명 원칙을 탐지 결과에도 적용

##### 실습 전 환경과 데이터 조건을 확인한다 (PDF p.16)

- PyTorch·torchvision·OpenCV import, CUDA 사용 가능 여부, 선택한 device 기록
- 사전학습 Weight는 수업 전에 다운로드하거나 캐시에 준비
- 네트워크 실패 시 임의 Weight로 대체하지 않음
- train·valid·test 폴더의 클래스 이름·개수·중복 파일을 먼저 검사
- 오늘의 수치·시각화는 합성 데이터 설명용 예시이며 실제 자연 이미지 성능이 아님

### 1교시 · 데이터셋 설계·분할·누수

#### 샘플 정보와 ImageFolder 라벨 계약

##### 좋은 Vision 모델은 데이터셋 설계에서 시작한다 (PDF p.17)

- 수업용 합성 데이터는 circle·square·triangle 3클래스
- 위치·색·잡음이 달라도 라벨 의미는 유지

##### 한 장의 이미지가 가져야 할 정보 (PDF p.18)

- 샘플 단위로 이미지 경로와 고유 ID 보관
- 정답 클래스와 라벨 기준 명시
- 촬영·생성 출처와 그룹 ID 기록
- train/valid/test 분할 정보 기록
- 모델 입력 계약은 색공간·채널 순서, 입력 크기와 보간법, 값 범위·Normalize
- 증강은 허용 범위와 라벨 보존 조건을 함께 정의

##### ImageFolder 구조와 class_to_idx (PDF p.19)

- `root/train/class_a/*.jpg`처럼 분할 아래 클래스별 하위 폴더 배치
- 클래스 폴더 이름을 정렬해 `class_to_idx`를 만들므로 폴더명이 곧 라벨 계약
- train·valid·test에서 같은 클래스 이름과 같은 인덱스 순서 유지
- 빈 폴더·숨김 파일·지원하지 않는 확장자를 먼저 검사

##### 클래스별 파일 수와 라벨 매핑 확인 (PDF p.20)

- 세 분할을 각각 `ImageFolder`로 읽고 `class_to_idx`가 서로 같은지 `assert`로 확인
- `Counter(ds.targets)`로 분할별 클래스 개수 출력
- 클래스별 수의 치우침, 빈 클래스, 잘못된 확장자 여부 점검
- 예시 출력은 `{'circle': 0, 'square': 1, 'triangle': 2}`와 train 120·40·20

##### torchvision.datasets.ImageFolder (PDF p.21)

- `root`만 필수 인자이며 클래스 폴더가 있는 최상위 경로
- `transform`은 입력 이미지 변환, `target_transform`은 라벨 변환
- `is_valid_file`은 파일 검사 함수, `allow_empty=False`는 빈 클래스 허용 여부
- `samples`는 (파일 경로, 라벨) 목록, `classes`·`class_to_idx`·`targets` 제공
- 폴더명 변경은 라벨 계약 변경

#### 데이터 품질과 누수 없는 분할

##### 분할 전에 확인할 데이터 품질 (PDF p.22)

- 같은 파일이나 거의 같은 장면이 train과 test에 동시에 들어가면 평가가 부풀려짐
- 같은 환자·제품·영상에서 나온 Frame은 하나의 분할에 묶음
- 클래스 기준이 모호하거나 annotator 간 규칙이 다르면 모델 오류와 데이터 오류가 섞임
- train에만 특정 배경·카메라·조명이 있으면 모델이 대상보다 환경을 학습할 수 있음

##### 같은 장면이 train과 test에 동시에 들어가면 안 된다 (PDF p.23)

- 같은 이미지가 여러 분할에 포함된 누수의 잘못된 예시
- 원본·그룹 ID를 기준으로 한 분할에 묶어 방지

##### Vision 데이터 분할 설계 (PDF p.24)

- 독립 상품 사진은 각 촬영이 독립이면 이미지 단위 분할 가능
- 환자·사람 사진은 같은 사람의 특징이 test로 새지 않도록 사람/환자 ID 단위 분할
- 영상 Frame은 인접 Frame이 거의 동일하므로 영상 또는 장면 ID 단위로 분할하고 Frame 단위 분할 금지
- 증강 이미지는 원본과 증강본을 같은 분할에 유지하도록 원본 ID 단위 분할

#### 실습과 개념 확인

##### 실습 01 · 데이터셋 구조와 누수 점검 (PDF p.25)

- 20분 실습, 4단계 난이도
- 기본필수는 클래스 폴더 3개의 파일 수·`class_to_idx`를 출력하고 세 분할의 매핑 일치 확인
- 응용은 클래스별 비율과 중복 파일 목록을 표로 만들고 누수 가능 항목을 한 문장으로 기록
- 심화는 그룹 ID 기반 Group 단위 분할을 설계해 이미지 단위 분할과 비교
- 특심화는 파일 해시·지각 해시·메타데이터를 조합한 데이터 감사 도구 작성과 근접 중복 기준 문서화

##### 3분 퀴즈 · 데이터셋 설계 (PDF p.26)

- ImageFolder 라벨 번호가 클래스 폴더 이름의 정렬 순서로 정해진다는 점 확인
- 한 영상의 Frame을 무작위로 train과 test에 나누면 장면 정보가 평가 자료로 누출되는 이유 확인
- 증강본과 원본을 같은 원본 ID로 묶어 한 분할에 두는 원칙 확인

**핵심:** 라벨 매핑과 원본·그룹 단위 분할이 고정되어야 이후 모든 평가 수치를 신뢰할 수 있음.

### 2교시 · 사전학습 Backbone·Head 교체

#### Backbone과 Head의 역할 분리

##### 사전학습 Backbone의 표현을 새 문제에 재사용한다 (PDF p.27)

- Head-only, Partial fine-tuning, Full fine-tuning 세 전략의 학습 범위를 위에서 아래로 비교한 그림
- 사전학습 표현을 새 문제의 출발점으로 재사용하는 전이학습 개념

##### Backbone과 Head를 분리해서 생각한다 (PDF p.28)

- Backbone은 가장자리·질감·형태처럼 여러 이미지 문제에서 재사용 가능한 표현 생성
- Head는 현재 데이터셋의 클래스 수에 맞는 Logit 출력
- Head-only는 빠르고 안정적이지만 새 도메인과 차이가 크면 표현이 부족할 수 있음
- Fine-tuning은 일부 또는 전체 Backbone을 열어 새 문제에 맞게 표현 조정

##### Head-only와 Fine-tuning 비교 (PDF p.29)

- Head-only는 Backbone `requires_grad=False`, 새 Head만 학습
- Head-only는 학습 파라미터와 VRAM이 적어 작은 데이터·유사 도메인의 첫 기준선
- Fine-tuning은 마지막 Stage부터 단계적으로 해제하고 Backbone에는 작은 학습률 사용
- Fine-tuning은 연산량과 과적합 위험이 커서 도메인 차이가 클 때 검토

#### ResNet18 Head 교체와 입력 전처리

##### ResNet18 Head 교체와 Backbone 고정 (PDF p.30)

- `ResNet18_Weights.DEFAULT`로 Weight를 먼저 불러온 뒤 모든 기존 파라미터의 `requires_grad`를 `False`로 고정
- `model.fc.in_features`로 입력 수를 읽어 `nn.Linear(in_features, num_classes)`로 교체
- 새 fc는 고정 이후 생성되므로 기본적으로 학습 가능
- 평가는 `weights.transforms()`, 학습은 같은 입력 규격의 증강 사용
- 결과적으로 학습 대상은 `model.fc.weight`·`bias`

##### torchvision.models.resnet18 (PDF p.31)

- 필수 위치 인자가 없고 주요 인자는 키워드 전용
- `weights`는 `None` 또는 `ResNet18_Weights` 값
- `weights=None`은 무작위 초기화
- DEFAULT Weight는 다운로드·캐시 필요
- 사전학습 모델의 fc는 로드 후 교체

##### ResNet18_Weights와 전처리 (PDF p.32)

- `weights.transforms()`가 평가용 기본 변환 제공
- 기본 변환은 Resize·CenterCrop·값 범위 변환·ImageNet mean/std Normalize
- 사전학습 Weight와 입력 전처리는 한 묶음
- 임의 Normalize는 특징 분포를 바꿈

#### 학습 범위 점검과 BatchNorm 모드

##### 학습 가능한 파라미터 수 확인 (PDF p.33)

- `requires_grad`가 켜진 파라미터의 `numel()` 합과 전체 파라미터 수를 함께 출력
- 고정했다고 생각한 층이 실제로 열려 있지 않은지 확인
- 실험표에 학습 범위와 계산 비용을 함께 기록
- 학습 가능한 파라미터는 Optimizer에 전달한 파라미터와 일치
- Head-only라면 전체 중 분류 Head만 학습 대상으로 출력

##### 고정된 Backbone의 train/eval 모드를 구분한다 (PDF p.34)

- `requires_grad=False`는 해당 파라미터의 gradient 계산만 끄며 train/eval 모드와 별개
- BatchNorm은 train 모드에서 Batch 통계를 사용하고 Running 통계를 갱신
- 완전히 고정한 Backbone의 BatchNorm까지 유지하려면 해당 Module의 eval 모드 정책 결정
- Dropout·BatchNorm 정책은 학습 가능한 파라미터와 별도로 실험표에 기록

#### 실습과 개념 확인

##### 실습 02 · 사전학습 Backbone과 새 Head (PDF p.35)

- 25분 실습, 4단계 난이도
- 기본필수는 ResNet18의 fc를 3클래스로 교체하고 Backbone을 고정한 뒤 학습 가능한 파라미터 수 출력
- 응용은 Weight 기본 변환과 직접 만든 변환의 Resize·Normalize 차이를 표로 비교
- 심화는 Head-only 모델의 BatchNorm 모드를 확인하고 Backbone eval 정책 유무에 따른 valid 결과 비교
- 특심화는 고정·학습 대상을 자동 표시하는 모델 구조 리포트를 만들고 Optimizer 파라미터와 대조

##### 3분 퀴즈 · 전이학습 기초 (PDF p.36)

- Head-only에서 학습하는 파라미터가 새 분류 Head의 weight와 bias임을 확인
- `requires_grad=False`가 BatchNorm Running 통계를 자동으로 멈추지 않는다는 점 확인
- 사전학습 Weight와 함께 Resize·Crop·Normalize 변환을 확인하는 이유 확인

**핵심:** 사전학습 Weight는 입력 전처리·고정 범위·BatchNorm 모드와 한 묶음으로 다뤄야 Head 교체 결과를 올바르게 해석할 수 있음.

### 3교시 · Freeze·Partial/Full Fine-tuning

#### 단계적 해제와 층별 학습률

##### Head 기준선 이후 일부 층을 연다 (PDF p.37)

- 1단계는 Head-only로 데이터·라벨·학습 루프의 정상 여부 확인
- 2단계는 layer4 등 마지막 Stage만 열고 적은 학습률로 조정
- 3단계는 개선이 없거나 데이터가 충분할 때 더 앞쪽 층을 여는 별도 실험
- 각 단계는 같은 분할·평가지표·epoch 예산으로 비교하고 test는 최종 확인까지 보관

##### 마지막 Stage와 Head에 서로 다른 학습률 적용 (PDF p.38)

- `model.layer4` 파라미터의 `requires_grad`를 `True`로 해제
- AdamW Parameter Group으로 layer4는 `1e-4`, fc는 `1e-3` 학습률 지정
- Backbone 표현은 작은 폭으로 조정하고 새 Head에는 더 큰 학습률을 주는 예
- 같은 파라미터가 두 그룹에 중복되지 않도록 확인

##### named_parameters·requires_grad·Parameter Group (PDF p.39)

- `model.named_parameters()`는 인자 없이 (이름, Parameter)를 순회
- `param.requires_grad_(True)`로 해제, `False`로 고정
- Parameter Group마다 `lr`·`weight_decay`·`betas`·`eps` 등 다른 설정 가능
- Optimizer에는 실제 학습할 Parameter만 전달
- 중복 등록은 오류를 만들고 누락은 해당 층이 학습되지 않게 함

#### 실험 계획과 결과 해석

##### Fine-tuning 실험 계획 (PDF p.40)

- A는 새 Head만 `1e-3`으로 학습하고 기준 성능·오류 클래스 관찰
- B는 layer4 + Head를 `1e-4 / 1e-3`으로 학습하고 valid 개선·과적합 관찰
- C는 전체 Backbone + Head를 `1e-5 / 5e-4`로 학습하고 성능·시간·VRAM·안정성 관찰

##### 합성 예시의 validation accuracy 곡선 (PDF p.41)

- Scratch·Head-only·Partial FT의 epoch별 validation accuracy 곡선을 읽는 예시
- 실제 비교에는 실행 ID·선택 지표·평가 epoch를 함께 기록

##### Scratch·Head-only·Partial fine-tuning 결과 (PDF p.42)

- Scratch는 학습 파라미터 6,131, Valid Accuracy 0.911, Macro F1 0.911
- Head-only는 99, 0.389, 0.269
- Partial FT는 4,739, 0.678, 0.674
- 설명용 소형 모델 예시이며 ResNet18 결과가 아님

##### 전이학습이 항상 더 좋은 것은 아니다 (PDF p.43)

- Source에서 학습한 특징이 Target의 배경·잡음·색 변화와 맞지 않으면 Head-only 성능이 낮을 수 있음
- Partial fine-tuning도 학습률·epoch·불균형 때문에 다시 한 클래스에 치우칠 수 있음
- Scratch가 더 좋으면 전이학습 결과를 숨기지 않고 도메인 차이와 학습 조건으로 설명
- 사전학습 모델·데이터 규모·분할·증강·학습 예산을 함께 기록해야 비교가 의미 있음

#### Fine-tuning 오류 점검

##### Fine-tuning에서 자주 발생하는 오류 (PDF p.44)

- Head-only인데 Backbone을 고정하지 않고 전체 파라미터를 Optimizer에 등록하는 오류
- 새로 연 파라미터가 Optimizer에 없어 해당 층이 갱신되지 않는 오류
- 사전학습 Weight의 Normalize를 빠뜨려 입력 분포가 달라지는 오류
- valid 점수를 보고 epoch·층·학습률을 계속 바꾼 뒤 그 값을 최종 성능처럼 보고하는 오류

#### 실습과 개념 확인

##### 실습 03 · Head-only·Partial Fine-tuning 비교 (PDF p.45)

- 25분 실습, 4단계 난이도
- 기본필수는 Head-only와 layer4+Head 두 전략을 같은 분할·epoch에서 학습하고 valid accuracy 비교
- 응용은 학습 파라미터 수·학습시간·best epoch를 추가해 비용과 성능을 함께 정리
- 심화는 Head-only→Partial 순차 학습과 처음부터 Partial 학습을 비교하고 Optimizer 재구성 시점 설명
- 특심화는 층별 학습률·BatchNorm 정책·gradient norm을 기록하는 Fine-tuning Scheduler 구현과 설정 변경 이력 기록

##### 3분 퀴즈 · Fine-tuning (PDF p.46)

- 층을 새로 unfreeze한 뒤 Optimizer를 다시 구성하거나 그룹을 추가하는 이유 확인
- Backbone에 Head보다 작은 학습률을 쓰는 경우가 많다는 점 확인
- 전이학습이 Scratch보다 낮을 때 도메인 차이·불균형·학습 조건을 분석하는 태도 확인

**핵심:** 학습 범위를 넓힐 때마다 Optimizer 등록과 학습률을 맞추고 같은 조건의 valid로 비교해야 Fine-tuning 효과를 판단할 수 있음.

### 4교시 · 클래스 불균형·Loss·Sampler

#### 불균형이 가리는 소수 클래스 실패

##### 클래스 불균형은 학습과 평가를 함께 바꾼다 (PDF p.47)

- 수업용 Target train은 circle 120 · square 40 · triangle 20의 불균형 구성
- 불균형이 학습 과정과 평가 해석에 동시에 영향을 주는 개념도

##### 다수 클래스 Accuracy가 소수 클래스 실패를 가릴 수 있다 (PDF p.48)

- 불균형 train에서 circle만 예측해도 Accuracy는 120/180 ≈ 66.7%
- triangle Recall이 낮아 실제 triangle 대부분을 놓쳐도 전체 Accuracy 영향은 작음
- train 분포와 실제 운영 분포가 다르면 필요한 균형 전략을 별도로 결정
- valid/test는 평가 목적에 맞는 분포를 유지하고 Sampling·Loss 조정은 train에서만 수행

##### 학습 데이터의 클래스별 개수 (PDF p.49)

- train은 불균형, valid/test는 클래스별 30개로 비교 가능하게 구성한 수업용 예시

#### Class weight와 Weighted sampler

##### 불균형 대응 방법 비교 (PDF p.50)

- Class weight는 Loss 기여도를 바꾸며 구현이 단순하지만 가중치가 너무 크면 불안정
- Weighted sampler는 Batch 표본 빈도를 바꿔 소수 클래스를 더 자주 학습하며 중복 Sampling·확률 기록 필요
- 데이터 수집·증강은 학습 자료 범위를 보완하며 라벨 의미·편향 검증 필요
- Threshold/후처리는 운영 판단 규칙에 업무 비용을 반영하며 다중 클래스·확률 보정 고려

##### nn.CrossEntropyLoss의 class weight (PDF p.51)

- 필수 위치 인자 없음, Forward 시 input logits와 target 필요
- `weight`는 길이 C의 Tensor
- `ignore_index`는 제외할 target 값
- `reduction`은 `none`·`mean`·`sum`, 기본 `mean`은 scalar 반환
- weight는 클래스별 학습 기여도만 조정하며 평가 지표의 계산식은 바꾸지 않음

##### WeightedRandomSampler (PDF p.52)

- `weights`는 각 샘플의 Sampling weight, `num_samples`는 한 epoch에서 뽑을 수
- `replacement=True`는 복원 추출, `generator`는 난수 재현성
- 인덱스를 반복하는 Sampler 반환
- `shuffle`과 동시에 사용하지 않음
- 클래스 weight가 아니라 샘플별 weight

##### 클래스 개수로 Loss weight 만들기 (PDF p.53)

- counts `[120, 40, 20]`에서 전체 합 / counts로 역빈도 weight 계산 후 평균으로 정규화
- 적은 클래스일수록 더 큰 loss 기여도 부여
- 정규화는 절대값보다 상대 비율을 유지하기 위한 선택
- 결과 예시 `tensor([0.30, 0.90, 1.80])`
- 학습 안정성과 클래스별 Recall을 함께 확인

##### 샘플별 weight로 추출 빈도 조정 (PDF p.54)

- `torch.bincount`로 클래스 개수를 세고 모든 클래스가 0보다 큰지 `assert`
- 클래스 역빈도 `1.0 / counts`를 각 샘플의 target에 매핑해 sample weight 생성
- `WeightedRandomSampler`를 `replacement=True`로 만들어 DataLoader의 `sampler`에 전달
- 역빈도는 클래스별 추출 확률을 맞추지만 개별 Batch의 균등 개수는 보장하지 않음
- 한 epoch에서 같은 샘플이 여러 번 뽑힐 수 있음
- Sampler 사용 시 DataLoader `shuffle`은 끔

#### 대응 전략 결과 비교

##### 불균형 대응 전략의 validation Macro F1 (PDF p.55)

- 합성 예시의 Macro F1은 Scratch 0.91, Head-only 0.27, Partial FT 0.67, Class weight 0.76, Sampler 0.81
- 이 순위가 다른 데이터에서도 유지되지는 않음

##### 합성 예시의 클래스별 Recall 비교 (PDF p.56)

- Head-only는 circle 1.000, square 0.167, triangle 0.000, Macro F1 0.269
- Class weight는 1.000, 0.667, 0.633, Macro F1 0.763
- Sampler는 1.000, 0.733, 0.700, Macro F1 0.810
- 불균형 대응의 효과는 소수 클래스 Recall 변화로 확인

#### 실습과 개념 확인

##### 실습 04 · 클래스 불균형 대응 (PDF p.57)

- 25분 실습, 4단계 난이도
- 기본필수는 클래스별 개수와 비율을 출력하고 Accuracy 외에 Macro F1·클래스별 Recall 계산
- 응용은 Class weight와 Weighted sampler 중 한 방법을 적용해 기준 모델과 비교
- 심화는 두 방법을 같은 seed·epoch에서 비교하고 minority Recall과 과적합 징후 해석
- 특심화는 Sampling 분포·Loss weight·gradient norm을 기록하고 비용 행렬 기반 학습·평가 정책 설계

##### 3분 퀴즈 · 클래스 불균형 (PDF p.58)

- Class weight는 valid 클래스 수가 아니라 train loss의 클래스별 기여도를 조정한다는 점 확인
- WeightedRandomSampler의 weights는 샘플별 값이며 보통 클래스 역빈도를 매핑한다는 점 확인
- 불균형 데이터에서 Accuracy만 보면 다수 클래스 예측만으로 높은 점수가 나와 소수 클래스를 놓치는 이유 확인

**핵심:** 불균형 대응은 train의 Loss·Sampling만 바꾸고 valid/test 분포는 유지한 채 소수 클래스 Recall과 Macro F1로 효과를 판단함.

### 5교시 · 평가·Confusion Matrix·오류 분석

#### Confusion Matrix와 클래스별 지표

##### 평가표에는 전체 점수와 클래스별 실패를 함께 남긴다 (PDF p.59)

- Confusion Matrix로 실제 클래스와 예측 클래스의 교차 빈도 확인
- Precision·Recall·F1을 클래스별로 계산해 놓치거나 과도하게 예측하는 클래스 확인
- Macro 평균은 각 클래스를 같은 비중, Weighted 평균은 support 비중으로 평균
- 오류 이미지를 원본·예측확률·데이터 출처와 함께 검토해 다음 실험 가설 생성

##### 합성 예시: Sampler의 Confusion Matrix (PDF p.60)

- 행은 실제 클래스, 열은 예측 클래스
- circle 30/30 정답
- square는 22장 정답, 8장을 circle로 예측
- triangle은 21장 정답, 5장 circle·4장 square로 예측

##### 클래스별 지표가 답하는 질문 (PDF p.61)

- Precision은 해당 클래스로 예측한 것 중 정답 비율, 예측을 얼마나 믿을 수 있는지에 답함
- Recall은 실제 해당 클래스 중 찾아낸 비율, 실제 대상을 얼마나 놓치지 않았는지에 답함
- F1은 Precision·Recall의 조화평균
- Support는 실제 클래스 표본 수, 지표가 몇 장을 근거로 하는지에 답함

##### Macro와 Weighted 평균을 구분한다 (PDF p.62)

- Macro average는 클래스별 지표의 단순 평균이며 소수 클래스도 동일 비중
- Macro는 불균형 문제의 전반적 균형 확인에 사용
- Weighted average는 support를 가중치로 평균하며 다수 클래스 영향이 큼
- Weighted는 전체 데이터 분포 기준의 성능 요약에 사용

#### 분류 보고서 생성

##### Confusion Matrix와 분류 보고서 (PDF p.63)

- `confusion_matrix(y_true, y_pred, labels=labels)`로 행렬 생성
- `labels`와 `target_names`는 `class_to_idx`와 같은 순서로 지정
- `output_dict=True`로 표·JSON 저장용 사전 반환
- `zero_division=0`은 분모가 0일 때의 경고·값 정책
- 예시 행렬의 Macro F1 ≈ 0.810

##### classification_report (PDF p.64)

- `y_true`·`y_pred`가 필수 인자
- `labels`·`target_names`·`sample_weight`·`digits`·`output_dict`·`zero_division`은 선택 인자
- 문자열 또는 중첩 Dict 반환
- 라벨과 클래스 이름의 순서 불일치 주의

#### 오류 원인 후보와 오류 이미지

##### 오류를 원인 후보로 분류한다 (PDF p.65)

- 데이터 부족은 minority 클래스의 형태·배경·조명 다양성 부족
- 도메인 차이는 사전학습 표현과 현재 촬영 환경의 차이
- 라벨 문제는 모호한 클래스 기준·오라벨·중복
- 모델 문제는 입력 크기·증강·동결 범위·학습률이 데이터에 맞지 않는 경우

##### 오류 이미지는 예측값과 함께 검토한다 (PDF p.66)

- 이미지마다 T=실제 클래스, P=예측 클래스를 표시한 오류 갤러리
- 빨간 제목으로 오분류 사례 구분

#### 실습과 개념 확인

##### 실습 05 · 평가표와 오류 이미지 분석 (PDF p.67)

- 25분 실습, 4단계 난이도
- 기본필수는 Confusion Matrix와 클래스별 Precision·Recall·F1을 출력하고 가장 어려운 클래스 찾기
- 응용은 오분류 이미지 최대 8장을 실제·예측·확률과 함께 저장하고 공통 패턴 기록
- 심화는 오류를 데이터·라벨·도메인·모델 가설로 분류하고 다음 실험 우선순위 결정
- 특심화는 오류 Slice별 지표와 Bootstrap 신뢰구간을 계산하고 데이터 수정 전후 회귀 검사 설계

##### 3분 퀴즈 · 평가와 오류 분석 (PDF p.68)

- Macro F1이 표본 수가 적은 클래스도 같은 비중으로 평균한다는 점 확인
- Confusion Matrix만으로 오류 원인을 확정하지 않고 실제 이미지·라벨·출처를 함께 확인하는 이유 확인
- Weighted F1이 높아도 다수 클래스 support가 평균을 지배해 minority Recall을 보장하지 않는다는 점 확인

**핵심:** 지표는 어디서 틀렸는지 알려 주고 원인은 오류 이미지·라벨·출처를 함께 본 가설로만 세움.

### 6교시 · Grad-CAM·편향·설명 한계

#### Grad-CAM 원리와 대상 층

##### Grad-CAM은 예측에 기여한 공간 영역을 시각화한다 (PDF p.69)

- 클래스 점수의 gradient와 Feature Map으로 coarse heatmap을 만드는 개념도
- 출처는 Selvaraju et al., Grad-CAM, ICCV 2017

##### Grad-CAM 계산 흐름 (PDF p.70)

- 입력을 Forward하고 관심 클래스의 Logit 선택
- 선택 Logit을 마지막 Convolution Feature Map에 대해 미분
- Gradient를 공간축 평균해 채널별 중요도 weight 계산
- Feature Map 가중합에 ReLU를 적용하고 입력 크기로 확대해 Overlay

##### 어떤 층을 선택할 것인가? (PDF p.71)

- 깊은 합성곱 층은 클래스 의미가 강하지만 공간 해상도가 낮음
- 보통 마지막 Conv block 사용
- 얕은 합성곱 층은 가장자리·질감 해상도가 높지만 클래스 구분력이 상대적으로 약함
- 다중 층 비교는 별도 실험으로 기록

#### Hook 기록과 Heatmap 계산

##### Activation과 Gradient를 Hook으로 기록 (PDF p.72)

- `target_layer = model.layer4[-1]`에 forward hook을 등록해 activation 저장
- forward hook 안에서 출력 Tensor에 `register_hook`을 걸어 gradient 저장
- 저장 값은 `detach()`로 분리
- `model.eval()`에서도 `torch.enable_grad()`로 gradient 계산을 켜고 `inference_mode` 밖에서 실행
- `logits[0, target_class].backward()`로 선택 클래스 점수만 미분
- `finally`에서 모든 handle을 `remove()`
- 모델 파라미터를 갱신하는 `optimizer.step`은 호출하지 않음

##### Module과 Tensor Hook (PDF p.73)

- `module.register_forward_hook(hook)`의 hook은 (module, args, output)을 받음
- `tensor.register_hook(hook)`의 hook은 (grad)를 받음
- full backward hook은 (module, grad_input, grad_output)을 받음
- 모든 등록은 RemovableHandle을 반환하며 사용 후 `handle.remove()`
- Module backward hook은 inplace 연산에 주의
- 저장할 값은 detach해 그래프 보관을 줄임

##### 채널 weight와 Heatmap 계산 (PDF p.74)

- gradient와 activation은 `[C,H,W]` 형태
- `alpha = grads.mean(dim=(1, 2))`는 클래스 점수에 대한 채널별 중요도
- `alpha`로 가중합한 뒤 ReLU를 적용해 해당 클래스에 긍정적으로 기여한 영역만 강조
- 최대값으로 정규화하고 `interpolate(mode="bilinear")`로 이미지 크기에 맞춰 확대
- Heatmap은 인과 설명이 아니라 모델 의존성의 시각 단서

##### 합성 이미지의 Grad-CAM 예시 (PDF p.75)

- 실제 square를 circle로 예측한 합성 예시의 Heatmap
- 입력 Crop에 맞춰 표시하고 Target class·층을 함께 기록

#### 해석 한계와 데이터 편향 점검

##### Grad-CAM을 정답 근거처럼 해석하지 않는다 (PDF p.76)

- Heatmap은 해상도가 낮고 선택한 층·클래스·정규화 방식에 따라 결과가 달라짐
- 강한 색이 반드시 사람에게 의미 있는 객체 부분을 뜻하지 않음
- 예측이 맞아도 배경·워터마크·촬영 장비에 의존하는 편향이 드러날 수 있음
- Occlusion·Counterfactual·데이터 Slice 분석과 함께 사용해 가설 검증

##### 시각 설명으로 데이터 편향 후보를 찾는다 (PDF p.77)

- 모델이 객체보다 배경 색·테두리·문자·촬영 위치에 집중하는지 확인
- 클래스마다 다른 카메라·해상도·압축률이 있는지 메타데이터와 연결
- Heatmap만으로 편향을 확정하지 않고 해당 영역을 가리거나 바꾼 입력으로 예측 변화 확인
- 수정한 데이터셋에서 같은 오류 Slice와 Grad-CAM을 다시 비교

#### 실습과 개념 확인

##### 실습 06 · Grad-CAM과 편향 점검 (PDF p.78)

- 25분 실습, 4단계 난이도
- 기본필수는 존재하는 정답·오답 각 1장의 Grad-CAM을 저장하고 강조 영역 설명, 해당 사례가 없으면 그 사실을 기록
- 응용은 두 클래스의 Target Logit을 바꿔 같은 이미지의 Heatmap 변화 비교
- 심화는 배경을 가린 입력과 원본의 예측·Heatmap을 비교해 편향 가설 검증
- 특심화는 다중 층 Grad-CAM·Occlusion Sensitivity를 구현하고 설명 안정성·fidelity 지표 비교

##### 3분 퀴즈 · Grad-CAM (PDF p.79)

- Grad-CAM이 관심 클래스의 Logit 또는 target score를 마지막 Conv Feature Map에 대해 미분한다는 점 확인
- 빨간 영역을 실제 원인으로 확정하지 않고 추가 실험이 필요한 이유 확인
- Hook을 계속 등록해 두면 중복 호출과 메모리 증가가 생겨 `handle.remove()`가 필요한 이유 확인

**핵심:** Grad-CAM은 선택한 클래스·층에 대한 모델 의존성의 단서이며 가림·대조 실험으로 검증해야 편향 가설이 됨.

### 7교시 · 모델 비교·프로젝트 통합

#### 비교 조건과 합성 예시 결과

##### 모델 비교 전에 고정할 조건 (PDF p.80)

- 동일한 train·valid·test 분할과 클래스 매핑 사용
- 입력 크기·Normalize·train/valid 변환 기록
- 모델별 학습 범위·학습률·epoch·seed·Loss/Sampler 정책 명시
- 주 지표는 Macro F1, 보조 지표는 Accuracy·클래스별 Recall·시간·학습 파라미터 수

##### 수업용 합성 예시 비교표 (PDF p.81)

- Scratch는 전체 6,131 params, Valid Acc 0.911, Macro F1 0.911
- Head-only는 Head 99 params, 0.389, 0.269
- Partial FT는 마지막 block + Head, 0.678, 0.674
- Class weight는 불균형 Loss 보정, 0.767, 0.763
- Sampler는 균형 Sampling, 0.811, 0.810
- 설명용 소형 모델 예시이며 ResNet18 결과가 아님

##### 전략별 Macro F1 비교 (PDF p.82)

- 전략별 Macro F1을 막대그래프로 비교
- 도메인 차이와 클래스 불균형을 분리해 해석

##### 합성 예시의 학습곡선 읽기 (PDF p.83)

- 마지막 epoch와 선택한 epoch는 다를 수 있음
- 표와 곡선은 같은 실행과 같은 선택 기준으로 대조

##### 학습 범위와 비용을 함께 기록 (PDF p.84)

- Head-only는 학습 파라미터 99 / 총 6,131, 1.6%
- Partial FT는 4,739 / 6,131, 77.3%
- Scratch / Full은 6,131 / 6,131, 100%
- 설명용 소형 모델 예시이며 ResNet18 결과가 아님

#### 프로젝트 구조와 산출물

##### 전이학습 분류 프로젝트 구조 예시 (PDF p.85)

- `day14_transfer/` 아래 `main.py`·`data.py`·`models.py`·`train.py`·`evaluate.py`·`explain.py`와 `data/`·`outputs/`·`reports/` 구성
- `data.py`는 클래스·분할·변환·Sampler 담당
- `models.py`는 Head-only·Partial 모델 구성 담당
- `evaluate.py`는 지표·오류 표 담당
- `explain.py`는 Grad-CAM 생성 담당

##### 프로젝트 공통 작업 순서 (PDF p.86)

- 클래스·파일 수·중복·분할 검사
- 사전학습 Weight와 입력 변환 고정
- 기본필수는 Head-only, 응용은 Fine-tuning·불균형 대응 후보를 valid로 비교
- 지표·오류 이미지·Grad-CAM·환경 정보를 결과 파일과 보고서에 기록

##### 단계별 프로젝트 산출물 (PDF p.87)

- `metrics.csv`는 설정·Accuracy·Macro F1·클래스별 Recall, 시간은 확장 항목
- `predictions.csv`는 파일 경로·실제·예측·확률
- `confusion_matrix.png`는 라벨 순서·support가 보이는 행렬
- `errors/`는 대표 오분류 원본과 예측 정보
- `gradcam/`은 정답·오답 Heatmap과 target class
- `model_card.md`는 기본필수에서 핵심 결과 설명, 확장 단계에서 근거·한계·재현 문서

#### 통합 실습과 경계 상황

##### 실습 07 · 전이학습 분류 프로젝트 통합 (PDF p.88)

- 25분 실습, 4단계 난이도
- 기본필수는 데이터 개수·클래스 매핑을 확인하고 Head-only 모델의 지표·예측 파일 생성
- 응용은 Partial fine-tuning과 class weight 또는 sampler를 추가해 비교표 완성
- 심화는 오류 이미지·클래스별 지표·Grad-CAM을 연결해 데이터 또는 모델 개선안 작성
- 특심화는 Config-driven 실험 Harness와 재현 가능한 checkpoint·artifact manifest를 구현해 환경별 결과 차이 분석

##### 정상·경계·실패 상황 (PDF p.89)

- 정상 3클래스 폴더는 Batch·라벨·학습이 정상이며 `class_to_idx`·Shape로 확인
- minority 1장은 지표 계산이 가능하되 경고를 기록하며 support·`zero_division`으로 확인
- train/test 중복은 실행 전 감사에서 실패 처리하며 파일/지각 해시로 확인
- Weight 미준비는 명확한 안내 후 중단하며 임의 random weight 대체 금지
- 저장 모델 복원은 동일 입력 Logit이 허용오차 안에서 일치해야 하며 classes·transform·state_dict로 확인

**핵심:** 같은 분할·변환·주 지표로 고정한 비교표와 재생성 가능한 산출물이 있어야 전략 간 차이를 설명할 수 있음.

### 8교시 · 실습평가·시연·회고

#### 최종 프로젝트 요구와 평가 기준

##### 최종 미니 프로젝트 · 전이학습 분류 모델 (PDF p.90)

- 3개 이상의 이미지 클래스를 분류하고 minority 클래스 오류 설명
- 기본필수는 Head-only, 응용은 Fine-tuning 또는 불균형 대응 후보 비교
- Macro F1·Confusion Matrix·클래스별 Recall·대표 오류 이미지 보고
- Grad-CAM은 데이터 편향 가설을 제시하는 보조 증거로 사용

##### 단계별 최종 제출물 (PDF p.91)

- 실행 코드는 환경·설정·실행 방법을 따라 재실행 가능해야 완료
- `metrics.csv`는 설정·주/보조 지표 포함, 시간·파라미터 수 비교는 확장
- `predictions.csv`는 파일 ID·실제·예측·확률 포함
- 오류/Grad-CAM은 존재하는 정답·오답 각 1장, 없으면 명시
- `model_card.md`는 핵심 결과 설명, 확장은 선택 근거·한계·다음 개선
- Git 이력은 기능 단위 커밋과 실행 가능한 최종 상태

##### 형성평가 기준 · 100점 (PDF p.92)

- 데이터셋 설계 20점, 클래스·분할·누수·불균형 점검
- 전이학습 구현 25점, Head 교체와 자기 단계의 학습 범위 정확성
- 평가·오류 분석 25점, Macro F1·클래스별 Recall·오류 이미지
- Grad-CAM·해석 15점, target class·층·한계 구분
- 재현·설명 15점, 환경·설정·결과 파일·개인 설명

#### 최종 검증 실습

##### 실습 08 · 최종 검증·보고서·시연 (PDF p.93)

- 30분 실습, 4단계 난이도
- 기본필수는 프로젝트를 다시 실행해 metrics·예측·오류 이미지·Grad-CAM을 재생성하고 핵심 결과 설명
- 응용은 짝이 README만 읽고 실행하게 하고 결과가 다르면 Weight·transform·seed·`class_to_idx` 확인
- 심화는 정상·불균형·중복·도메인 변화 상황을 시연하고 실무 배포 전 점검표 작성
- 특심화는 분산 학습·AMP·checkpoint resume·데이터 버전 고정을 포함한 재현성 검증 Suite 구현과 비결정성 보고

**핵심:** 최종 결과는 다른 사람이 같은 설정으로 재생성하고 같은 근거로 설명할 수 있을 때 완료로 판단함.

### 마무리 · 정리와 다음 수업

#### 확인 퀴즈·핵심 정리·객체탐지 예고

##### 마무리 3분 확인 퀴즈 (PDF p.94)

- 전이학습이 Source·Target 도메인과 학습 조건에 따라 Scratch보다 낮을 수도 있다는 점 확인
- 클래스 불균형에서 Macro F1·클래스별 Recall·support를 함께 보는 이유 확인
- Grad-CAM이 인과 원인이 아니라 특정 모델·클래스 점수에 대한 공간 의존성의 단서라는 점 확인

##### 오늘의 핵심 정리 (PDF p.95)

- 데이터셋의 클래스·그룹·중복·분할을 먼저 설계해야 평가를 신뢰할 수 있음
- 사전학습 Backbone과 Head를 분리하고 Head-only → Partial fine-tuning 순서로 확장
- 불균형 데이터는 Loss·Sampler·데이터 개선과 클래스별 지표를 함께 사용
- 오류 이미지와 Grad-CAM은 다음 실험의 가설을 만들지만 단독으로 원인을 확정하지 않음

##### 다음 수업 · 11월 6일 객체탐지 (PDF p.96)

- 분류는 이미지 전체에 클래스 하나, 탐지는 객체마다 Bounding Box와 클래스
- 분류의 Confusion Matrix·클래스별 Recall이 탐지에서는 IoU·Precision/Recall·mAP로 확장
- 분류의 Grad-CAM 공간 단서 확인이 탐지에서는 라벨 위치·크기·품질 교차검수로 확장

### 참고자료 · 공식 문서와 Weight 점검

#### 참고자료와 부록

##### 공식 참고자료 · PyTorch·Torchvision (PDF p.97)

- Torchvision의 ImageFolder / DatasetFolder / Transforms
- Torchvision의 resnet18 / ResNet18_Weights / Weight transforms
- PyTorch의 CrossEntropyLoss / WeightedRandomSampler / DataLoader
- PyTorch의 Module Hook / AdamW / named_parameters
- 2026년 10월 공식 문서 기준

##### 공식 참고자료 · 평가와 설명 (PDF p.98)

- scikit-learn의 confusion_matrix / classification_report
- Grad-CAM 원 논문, ICCV 2017
- Heatmap·지표·오류 원본·데이터 메타데이터를 함께 검토하는 실무 해석 원칙
- 수업용 합성 예시는 설명용이며 실제 실습 결과는 실행 조건과 함께 별도로 기록

##### 사전학습 Weight 사용 전 점검 (PDF p.99)

- 인터넷이 필요한 최초 다운로드를 수업 전에 완료하고 캐시 경로 확인
- Weight 파일의 출처·버전·해시와 torchvision 버전 기록
- 다운로드 실패 시 `weights=None`으로 조용히 대체하지 않고 실습을 Head 구조 확인 모드로 구분
- 신뢰할 수 없는 checkpoint는 `torch.load`하지 않으며 직접 생성한 파일만 복원
