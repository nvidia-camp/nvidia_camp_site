# Day11 강의 구조와 핵심 설명

교시명은 PDF p.14 운영표의 핵심 내용 기준. 중간 학습 주제는 편집한 표현이며 마지막 단계는 원문 슬라이드 제목. 페이지는 현재 103쪽 PDF의 뷰어 기준. 도입·마무리·참고자료는 교시 밖에 별도 배치.

기본필수만으로 공통 평가 충족. 응용·심화·특심화는 선택 확장. 교재의 구조·입력 크기 예시와 배포 실습 조건 구분. 자료에 기재된 예시·검수 결과는 이번 정리 작업에서의 코드 재실행이나 실제 수업 완료를 의미하지 않음.

## 강의 목차

```text
도입 · 이미지 분류의 전체 지도와 수업 준비
├─ 업무에서 Kernel까지의 전체 구조
│  ├─ 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)
│  ├─ 현업에서 이미지 분류가 필요한 순간 (PDF p.2)
│  ├─ 전체 지도에서 오늘의 위치 (PDF p.3)
│  ├─ CNN의 특징 추출부와 분류 Head (PDF p.4)
│  ├─ 특징 추출부 안의 Conv 블록 (PDF p.5)
│  └─ Kernel 하나가 Feature Map을 만드는 과정 (PDF p.6)
├─ 입력 준비와 학습·비교의 연결
│  ├─ 모델에 들어갈 이미지 Tensor와 전처리 (PDF p.7)
│  ├─ CNN에서도 이어지는 학습·검증 원칙 (PDF p.8)
│  ├─ 전이학습으로 이미 배운 특징을 재사용 (PDF p.9)
│  ├─ 모델 선택과 CPU·GPU 비교의 기준 (PDF p.10)
│  └─ 오늘 완성할 이미지 분류 모델과 성능표 (PDF p.11)
└─ 선행 학습 복습과 수업 운영
   ├─ 지난 수업에서 만든 학습 안정화 흐름 (PDF p.12)
   ├─ 3분 확인 퀴즈 · ANN에서 CNN으로 (PDF p.13)
   ├─ 오늘의 목표와 8교시 운영 (PDF p.14)
   ├─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)
   └─ 실습 전 환경과 입력 데이터를 확인한다 (PDF p.16)

1교시 · 이미지 Tensor·CNN 필요성
├─ 이미지 분류와 CNN의 필요성
│  ├─ 이미지 분류의 전체 흐름 (PDF p.17)
│  └─ 이미지에 MLP 대신 CNN을 사용하는 이유 (PDF p.18)
├─ Tensor의 축과 입력 조건
│  ├─ 이미지 Tensor의 네 축을 읽는다 (PDF p.19)
│  ├─ 이미지 Tensor의 Shape·dtype·device 확인 (PDF p.20)
│  └─ unsqueeze()·permute()로 축을 맞춘다 (PDF p.21)
└─ 실습 01의 단계별 입력 검증
   └─ 실습 01 · 이미지 Tensor와 CNN 입력 형태 (PDF p.22)

2교시 · 합성곱·Kernel·Stride·Padding
├─ 국소 연산과 합성곱 출력 Shape
│  ├─ 합성곱은 작은 창으로 국소 패턴을 찾는다 (PDF p.23)
│  ├─ Kernel이 입력을 이동하며 Feature Map을 만든다 (PDF p.24)
│  ├─ Kernel·Stride·Padding을 한 문장으로 구분 (PDF p.25)
│  ├─ 합성곱 출력 크기 계산 (PDF p.26)
│  └─ 다중 채널 입력과 출력 채널 (PDF p.27)
├─ Conv2d의 인자와 중간 표현
│  ├─ nn.Conv2d · 2차원 합성곱 층 (PDF p.28)
│  ├─ Conv2d의 선택 인자를 언제 바꾸는가 (PDF p.29)
│  ├─ Conv2d 적용 전후 Shape 확인 (PDF p.30)
│  └─ Feature Map은 무엇을 보여 주는가? (PDF p.31)
└─ 실습 02와 합성곱 개념 확인
   ├─ 실습 02 · 합성곱 Shape와 파라미터 계산 (PDF p.32)
   └─ 3분 퀴즈 · 합성곱 (PDF p.33)

3교시 · Pooling·CNN 구조·Shape 추적
├─ Pooling과 Conv 블록
│  ├─ Pooling과 CNN 구조를 연결한다 (PDF p.34)
│  ├─ Pooling은 작은 영역을 대표값으로 줄인다 (PDF p.35)
│  ├─ nn.MaxPool2d · 최대값 기반 Downsampling (PDF p.36)
│  └─ Conv Block의 기본 패턴 (PDF p.37)
├─ Global Pool·Flatten·Head의 연결
│  ├─ CNN은 공간을 줄이며 특징을 누적한다 (PDF p.38)
│  ├─ CNN의 Shape를 단계별로 추적한다 (PDF p.39)
│  ├─ nn.AdaptiveAvgPool2d · 출력 크기를 직접 지정 (PDF p.40)
│  ├─ 작은 CNN 클래스 구현 (PDF p.41)
│  └─ nn.Sequential·torch.flatten·nn.Linear (PDF p.42)
└─ Shape 오류 진단과 실습 03
   ├─ CNN에서 자주 발생하는 Shape 오류 (PDF p.43)
   ├─ 실습 03 · Pooling과 작은 CNN 구조 (PDF p.44)
   └─ 3분 퀴즈 · Pooling과 CNN (PDF p.45)

4교시 · ImageFolder·Transforms·증강
├─ 클래스 폴더와 기본 변환
│  ├─ 이미지 폴더와 변환 파이프라인 (PDF p.46)
│  ├─ ImageFolder가 이해하는 폴더 구조 (PDF p.47)
│  ├─ torchvision.datasets.ImageFolder (PDF p.48)
│  ├─ 이미지 변환을 순서대로 연결한다 (PDF p.49)
│  ├─ Compose·Resize·ToTensor (PDF p.50)
│  └─ Normalize · 채널별 평균과 표준편차로 변환 (PDF p.51)
├─ 라벨을 보존하는 증강과 분할 정책
│  ├─ Data Augmentation은 같은 의미의 다양한 입력을 만든다 (PDF p.52)
│  ├─ RandomHorizontalFlip·RandomRotation·ColorJitter (PDF p.53)
│  └─ train과 valid/test 변환을 분리한다 (PDF p.54)
└─ Batch 구성과 실습 04
   ├─ DataLoader · 이미지 Batch 구성 (PDF p.55)
   ├─ ImageFolder와 DataLoader로 Batch 확인 (PDF p.56)
   ├─ 실습 04 · ImageFolder·Transforms·DataLoader (PDF p.57)
   └─ 3분 퀴즈 · 이미지 데이터 (PDF p.58)

5교시 · CNN 학습·평가·Best model
├─ Batch 학습과 표본 가중 지표
│  ├─ CNN 학습·평가·Best model (PDF p.59)
│  ├─ 이미지 분류 학습의 한 Batch (PDF p.60)
│  ├─ Logit·Loss·예측을 구분한다 (PDF p.61)
│  ├─ CNN 한 Epoch 학습 함수 (PDF p.62)
│  └─ train()·zero_grad()·backward()·step() (PDF p.63)
├─ 평가 모드와 오류 분석
│  ├─ 평가 함수 · gradient 없이 loss와 accuracy 계산 (PDF p.64)
│  └─ Accuracy만 보고 끝내지 않는다 (PDF p.65)
└─ Best 저장·복원과 실습 05
   ├─ 학습곡선과 Best model 기록 (PDF p.66)
   ├─ Best model 저장과 복원 (PDF p.67)
   ├─ 실습 05 · CNN 학습·평가와 Best model (PDF p.68)
   └─ 3분 퀴즈 · CNN 학습 (PDF p.69)

6교시 · 전이학습·Freeze·Fine-tuning
├─ 사전학습 표현과 가중치 전처리
│  ├─ 사전학습 CNN의 표현을 재사용한다 (PDF p.70)
│  ├─ Feature Extractor와 Fine-tuning (PDF p.71)
│  ├─ 처음부터 학습과 전이학습 비교 (PDF p.72)
│  ├─ torchvision.models.resnet18 (PDF p.73)
│  └─ Weights 객체와 전처리 (PDF p.74)
├─ Head 교체와 부분 미세조정 정책
│  ├─ ResNet18의 분류 Head 교체 (PDF p.75)
│  ├─ 부분 미세조정 순서 (PDF p.76)
│  └─ 학습률을 Parameter Group으로 분리 (PDF p.77)
└─ 모델 비교·오류 점검·실습 06
   ├─ 모델 비교표에 반드시 남길 항목 (PDF p.78)
   ├─ 전이학습에서 자주 발생하는 오류 (PDF p.79)
   ├─ 실습 06 · 전이학습·Freeze·Fine-tuning 비교 (PDF p.80)
   └─ 3분 퀴즈 · 전이학습 (PDF p.81)

7교시 · CPU·GPU 시간·VRAM 비교
├─ 장치 특성과 공정한 시간·메모리 측정
│  ├─ CPU·GPU 학습시간과 VRAM을 공정하게 측정한다 (PDF p.82)
│  ├─ 병렬 계산과 VRAM의 역할 (PDF p.83)
│  ├─ 공정한 시간 비교 조건 (PDF p.84)
│  ├─ torch.cuda.synchronize · 비동기 CUDA 완료 대기 (PDF p.85)
│  └─ GPU Peak Memory 측정 함수 (PDF p.86)
├─ 계측 구현과 Batch별 결과 해석
│  ├─ 한 Epoch 시간과 Peak VRAM 측정 (PDF p.87)
│  ├─ Batch size와 속도·VRAM의 관계 (PDF p.88)
│  ├─ CPU·GPU 모델 성능표 템플릿 (PDF p.89)
│  └─ 측정값을 과장하지 않고 해석한다 (PDF p.90)
└─ 실습 07과 성능 측정 확인
   ├─ 실습 07 · CPU·GPU 학습시간과 VRAM 비교 (PDF p.91)
   └─ 3분 퀴즈 · 성능 측정 (PDF p.92)

8교시 · 이미지 분류 프로젝트·시연
├─ 프로젝트 작업 흐름과 단계별 산출물
│  ├─ 최종 프로젝트 · 이미지 분류 모델과 성능표 (PDF p.93)
│  ├─ 심화 참고 · VS Code 프로젝트 구조 (PDF p.94)
│  ├─ 프로젝트 공통 작업 순서 (PDF p.95)
│  └─ 단계별 제출물 · 기본필수부터 완성 (PDF p.96)
└─ 실습 08·형성평가·경계 검증
   ├─ 실습 08 · 이미지 분류 프로젝트 통합·시연 (PDF p.97)
   ├─ 형성평가 기준 · 기본필수로 100점 (PDF p.98)
   └─ 정상·경계·실패 상황을 구분한다 (PDF p.99)

마무리 · 핵심 회수와 다음 수업
└─ 오늘의 정리와 다음 구조 연결
   ├─ 오늘의 핵심 정리 (PDF p.100)
   └─ 다음 수업 · 11월 3일 아키텍처 비교 (PDF p.101)

참고자료 · 공식 문서의 범위
└─ PyTorch와 Torchvision 참고 범위
   ├─ 공식 참고자료 · PyTorch Core (PDF p.102)
   └─ 공식 참고자료 · Torchvision (PDF p.103)
```

## 핵심 설명

### 도입 · 이미지 분류의 전체 지도와 수업 준비

#### 업무에서 Kernel까지의 전체 구조

##### 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)

- Day11의 이미지 Tensor·CNN·이미지 분류·전이학습·GPU 비교를 소개하는 표지

##### 현업에서 이미지 분류가 필요한 순간 (PDF p.2)

- 제품 사진 분류를 담당자 판단에 연결하는 업무 적용 예시
- 오늘의 실습은 가로·세로 줄무늬 두 클래스로 데이터 준비부터 모델 선택까지 연습하는 구성

##### 전체 지도에서 오늘의 위치 (PDF p.3)

- 서비스 → CNN → 특징 추출부 → Conv 블록 → Kernel로 내려가는 전체 구조
- 모델 밖의 데이터 준비·학습·검증·장치 비교까지 포함하는 개발 범위

##### CNN의 특징 추출부와 분류 Head (PDF p.4)

- 특징 추출부는 이미지에서 분류에 유용한 표현을 학습하는 부분
- Global Pool·Flatten 뒤 분류 Head가 클래스 수 K에 맞는 `[N,K]` 점수 출력
- 오늘 실습의 K는 2

##### 특징 추출부 안의 Conv 블록 (PDF p.5)

- Conv2d의 패턴 반응 → ReLU의 비선형 변환 → MaxPool2d의 공간 축소
- 2×2 MaxPool은 영역의 최댓값 하나를 남기며 채널 수 유지
- Downsampling에 따른 연산 절감과 세부 정보 손실을 함께 확인

##### Kernel 하나가 Feature Map을 만드는 과정 (PDF p.6)

- 1채널·stride=1·padding=0·bias=0에서 5×5 입력과 3×3 Kernel로 3×3 Feature Map 생성
- 같은 Kernel을 이동시키며 대응값의 곱을 합산하는 연산
- 실제 Kernel 값은 학습 대상이며 여러 필터가 서로 다른 특징 채널 생성

#### 입력 준비와 학습·비교의 연결

##### 모델에 들어갈 이미지 Tensor와 전처리 (PDF p.7)

- ImageFolder의 클래스 폴더 → 이미지 변환 → `[C,H,W]` → `[N,C,H,W]` 순서
- train은 의미를 보존하는 증강을 적용하고 valid/test는 결정적 변환 사용
- 클래스 순서·입력 크기·Normalize를 모델과 함께 관리

##### CNN에서도 이어지는 학습·검증 원칙 (PDF p.8)

- Batch별 forward → loss → backward → Optimizer 갱신의 학습 흐름
- valid에서는 eval·inference_mode로 가중치 갱신 없이 선택 지표 기록
- test는 모델·설정 선택 중 보관

##### 전이학습으로 이미 배운 특징을 재사용 (PDF p.9)

- Head-only는 Backbone을 고정하고 새 Head만 학습하는 전이학습
- 부분 미세조정은 마지막 Stage와 Head를 학습하는 확장
- 학습 범위·학습률·BatchNorm 통계 정책을 함께 결정

##### 모델 선택과 CPU·GPU 비교의 기준 (PDF p.10)

- 모델 선택은 같은 분할의 valid 지표와 오류 유형을 근거로 판단
- 장치 비교는 같은 모델·입력·Batch·측정 범위의 시간·처리량·Peak VRAM 기준
- 학습 시간은 서비스 추론 지연과 구분하며 GPU가 없으면 N/A 기록

##### 오늘 완성할 이미지 분류 모델과 성능표 (PDF p.11)

- SmallCNN·ResNet18 Head·ResNet18 Partial의 학습 범위와 valid·시간·장치·메모리 기록
- 기본필수는 SmallCNN·best_model.pt·학습/모델/환경 기록·README 완성
- 가중치나 GPU 미준비 항목은 미실행 사유와 N/A 기록

#### 선행 학습 복습과 수업 운영

##### 지난 수업에서 만든 학습 안정화 흐름 (PDF p.12)

- Optimizer·학습률·Batch·Epoch로 구성한 지난 수업의 학습 제어 복습
- 과적합 제어와 train/eval·best 복원 원칙을 공간 구조가 있는 이미지로 확장

##### 3분 확인 퀴즈 · ANN에서 CNN으로 (PDF p.13)

- Flatten과 공간 관계의 연결을 확인하는 복습 퀴즈
- 평가 모드 전환과 train·valid·test·best model 원칙을 점검하는 문항

##### 오늘의 목표와 8교시 운영 (PDF p.14)

- 이미지 Tensor부터 합성곱·Pooling·데이터 변환·학습·전이학습·계측·프로젝트로 이어지는 8교시 운영
- 교시마다 설명·시연과 실습·리뷰를 배치한 50분 구성

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)

- 오늘 범위는 CNN·이미지 데이터·전이학습·CPU/GPU 계측
- 다음 수업 예고는 RNN·LSTM·Autoencoder·Transformer의 구조 비교

##### 실습 전 환경과 입력 데이터를 확인한다 (PDF p.16)

- torch·torchvision import와 CUDA 사용 가능 여부 확인
- NCHW 축 순서와 분할별 동일 클래스 폴더 구조 점검
- GPU 미보유 환경의 기본 실습은 CPU 진행

### 1교시 · 이미지 Tensor·CNN 필요성

#### 이미지 분류와 CNN의 필요성

##### 이미지 분류의 전체 흐름 (PDF p.17)

- 이미지 Tensor → 합성곱 Feature Map → Pooling/Stride → 분류 Head의 연결
- 최종 Head의 출력은 클래스별 Logit

##### 이미지에 MLP 대신 CNN을 사용하는 이유 (PDF p.18)

- MLP의 Flatten은 이미지의 2차원 이웃 관계를 직접 드러내지 않는 입력 표현
- CNN은 국소 연결과 위치별 가중치 공유로 공간 패턴을 다루는 구조
- 고해상도 MLP 첫 Linear와 작은 Conv의 파라미터 규모 비교

#### Tensor의 축과 입력 조건

##### 이미지 Tensor의 네 축을 읽는다 (PDF p.19)

- N은 Batch의 이미지 수
- C는 이미지나 Feature Map의 채널 수
- H·W는 높이·너비이며 입력 축 순서는 NCHW

##### 이미지 Tensor의 Shape·dtype·device 확인 (PDF p.20)

- 이미지 `[8,3,64,64]`는 RGB 이미지 8장의 Batch
- 실수 입력의 dtype과 모델 가중치 dtype 확인
- 모델과 입력의 device 일치 확인
- 라벨 `[8]`은 이미지당 정답 하나에 대응

##### unsqueeze()·permute()로 축을 맞춘다 (PDF p.21)

- `unsqueeze(dim)`은 지정 위치에 크기 1의 축을 추가하는 연산
- `permute(*dims)`는 모든 축의 순서를 재배치하는 연산
- CHW 한 장의 Batch 추가와 화면 표시용 HWC 변환을 구분
- view 반환 가능성과 contiguous 상태 확인

#### 실습 01의 단계별 입력 검증

##### 실습 01 · 이미지 Tensor와 CNN 입력 형태 (PDF p.22)

- 기본필수는 RGB Tensor 4장의 NCHW·dtype·device 확인
- 응용은 CHW·HWC·NCHW 왕복 변환과 이미지 표시
- 심화는 MLP와 Conv2d 파라미터 수 비교
- 특심화 01은 NCHW 축을 유지한 channels_last의 출력·gradient 동등성 검증
- 완료 기준은 각 축의 의미와 축 순서 변경·메모리 형식 변경의 차이 설명

**핵심:** 이미지의 공간 관계와 NCHW·dtype·device를 확인한 입력이 CNN 학습의 출발점.

### 2교시 · 합성곱·Kernel·Stride·Padding

#### 국소 연산과 합성곱 출력 Shape

##### 합성곱은 작은 창으로 국소 패턴을 찾는다 (PDF p.23)

- 작은 창의 국소 연산과 같은 Kernel의 위치별 공유를 소개하는 2교시 도입

##### Kernel이 입력을 이동하며 Feature Map을 만든다 (PDF p.24)

- Kernel과 입력 영역의 원소별 곱을 합산해 위치별 반응 생성
- 한 Kernel의 이동으로 Feature Map 하나 생성
- 여러 Kernel로 서로 다른 패턴 반응 채널 구성

##### Kernel·Stride·Padding을 한 문장으로 구분 (PDF p.25)

- kernel_size는 한 번에 관찰하는 창의 크기
- stride는 창의 이동 간격
- padding은 입력 가장자리의 추가 테두리
- out_channels는 출력 Feature Map을 만드는 Kernel 개수

##### 합성곱 출력 크기 계산 (PDF p.26)

- 출력 높이는 `floor((Hin + 2P − D(K−1) − 1) / S + 1)`로 계산
- 너비도 같은 방식으로 계산
- 32×32 입력에 K=3·P=1일 때 S=1은 32×32 유지, S=2는 16×16
- 후속 Linear 입력 오류를 찾기 위한 단계별 Shape 확인

##### 다중 채널 입력과 출력 채널 (PDF p.27)

- groups=1에서 각 Kernel은 모든 입력 채널과 연결
- 가중치 Shape는 `[Cout,Cin,kH,kW]`이며 출력은 `[N,Cout,Hout,Wout]`
- 채널 수 확대에 따른 표현력·연산량·메모리 변화 확인

#### Conv2d의 인자와 중간 표현

##### nn.Conv2d · 2차원 합성곱 층 (PDF p.28)

- Conv2d 생성의 필수 인자는 in_channels·out_channels·kernel_size
- 기본 선택값은 stride=1·padding=0·dilation=1·groups=1·bias=True·padding_mode="zeros"
- 층 생성과 입력 Tensor에 층을 적용하는 계산을 구분

##### Conv2d의 선택 인자를 언제 바꾸는가 (PDF p.29)

- stride>1은 합성곱과 공간 축소를 함께 수행하는 설정
- padding="same"은 stride=1에서 공간 크기를 유지하는 설정
- dilation>1은 파라미터 수 증가 없이 수용영역을 넓히는 설정
- groups=Cin은 Depthwise 구성에 사용하는 설정
- BatchNorm 앞의 bias=False와 padding_mode 선택에 따른 연산 조건 확인

##### Conv2d 적용 전후 Shape 확인 (PDF p.30)

- 입력 `[8,3,32,32]`에 3→16·3×3·stride=1·padding=1 Conv를 적용하면 `[8,16,32,32]`
- 공간 크기 유지 여부와 bias를 포함한 파라미터 계산 대조

##### Feature Map은 무엇을 보여 주는가? (PDF p.31)

- 초기 층의 가장자리·밝기·질감 반응과 깊은 층의 조합된 표현 구분
- Feature Map은 중간 표현의 진단 자료
- 밝은 반응을 예측의 인과적 원인으로 단정하지 않는 해석 범위

#### 실습 02와 합성곱 개념 확인

##### 실습 02 · 합성곱 Shape와 파라미터 계산 (PDF p.32)

- 기본필수는 3→8·3×3·padding=1 Conv의 출력 Shape 확인
- 응용은 stride=1과 2의 공간 크기·계산량 비교
- 심화는 Kernel·채널 후보의 파라미터와 Feature Map 개수 비교
- 특심화 02는 일반·Depthwise·Dilated Conv 계산량과 그룹별 구현의 수치 대조
- 완료 기준은 Shape 계산과 실제 출력의 일치 및 파라미터 수·연산량의 구분

##### 3분 퀴즈 · 합성곱 (PDF p.33)

- 출력 채널 결정 요인과 합성곱 출력 크기를 점검하는 퀴즈
- padding 증가의 효과와 한계를 구분하는 문항

**핵심:** Kernel·채널·Stride·Padding을 함께 읽어 출력 Shape와 파라미터 수·연산량을 구분.

### 3교시 · Pooling·CNN 구조·Shape 추적

#### Pooling과 Conv 블록

##### Pooling과 CNN 구조를 연결한다 (PDF p.34)

- 공간 크기 축소와 채널 표현 확장을 연결하는 3교시 도입

##### Pooling은 작은 영역을 대표값으로 줄인다 (PDF p.35)

- Max Pooling은 영역의 가장 큰 반응을 대표값으로 선택
- 공간 축소를 통한 연산량·메모리 감소
- 작은 위치 변화에 대한 민감도 완화 가능성
- 과도한 축소에 따른 작은 물체·세부 정보 손실

##### nn.MaxPool2d · 최대값 기반 Downsampling (PDF p.36)

- MaxPool2d의 필수 인자는 kernel_size
- stride=None이면 kernel_size와 같은 이동 간격 적용
- padding은 음의 무한대 채움이며 dilation·return_indices·ceil_mode로 창과 반환 조건 조정
- 출력은 공간 축만 바뀌고 N·C는 유지

##### Conv Block의 기본 패턴 (PDF p.37)

- Conv2d는 국소 패턴을 학습 가능한 Feature Map으로 변환
- BatchNorm2d는 채널별 활성값과 Running 통계를 관리
- ReLU는 음수를 0으로 바꾸는 비선형 변환
- MaxPool 또는 stride Conv는 공간 크기 축소 담당

#### Global Pool·Flatten·Head의 연결

##### CNN은 공간을 줄이며 특징을 누적한다 (PDF p.38)

- 공간 해상도를 줄이면서 채널 표현을 누적하는 CNN 구조
- Global Pool 또는 Flatten으로 벡터화한 뒤 Classifier Head에서 Logit 생성

##### CNN의 Shape를 단계별로 추적한다 (PDF p.39)

- 교재 예시는 `[8,3,64,64]` → `[8,16,32,32]` → `[8,32,16,16]`의 두 블록
- Global Pool → `[8,32,1,1]`, Flatten → `[8,32]`, 3클래스 Head → `[8,3]`
- 배포 기본필수는 32×32·2클래스이므로 같은 공간 크기·출력 수를 정답으로 강제하지 않는 구분

##### nn.AdaptiveAvgPool2d · 출력 크기를 직접 지정 (PDF p.40)

- AdaptiveAvgPool2d는 output_size로 목표 공간 크기를 지정하는 모듈
- output_size=1은 각 채널의 공간 정보를 평균 하나로 요약
- 입력 공간 크기와 무관하게 채널 수가 정해진 Head 입력 구성

##### 작은 CNN 클래스 구현 (PDF p.41)

- 특징 추출부·Global Pool·Flatten·fc를 연결한 SmallCNN 예시
- Flatten은 Batch 축을 유지하는 시작 축 1 사용
- 교재 num_classes=3 예시와 실제 두 클래스 실습의 출력 수 구분
- 기본필수는 같은 구조를 제공된 nn.Sequential로 구성하는 범위

##### nn.Sequential·torch.flatten·nn.Linear (PDF p.42)

- Sequential은 모듈을 주어진 순서로 실행하는 컨테이너
- `torch.flatten` 기본 시작 축은 0이며 이미지 분류에서는 Batch를 보존하는 1 지정
- Linear의 in_features는 입력 특성 수, out_features는 출력 점수 수
- Sequential은 명명된 중간 출력을 직접 반환하지 않는 구조

#### Shape 오류 진단과 실습 03

##### CNN에서 자주 발생하는 Shape 오류 (PDF p.43)

- NHWC를 NCHW로 해석한 채널 불일치 진단
- Pooling 뒤 H·W를 누락한 Linear 입력 크기 오류 진단
- Batch 축까지 펼친 Flatten 오류 진단
- 실제 클래스 폴더 수와 Head 출력 수 불일치 진단

##### 실습 03 · Pooling과 작은 CNN 구조 (PDF p.44)

- 기본필수는 두 Conv→ReLU→Pool 블록과 Adaptive Pool의 Shape 추적
- 응용은 MaxPool과 stride Conv의 Shape·파라미터 비교
- 심화는 BatchNorm2d·Dropout2d의 train/eval 출력·Running 통계 비교
- 특심화 03은 leaf Hook의 Shape·통계 기록과 예외 후 Hook·모드·상태 복구
- 완료 기준은 입력부터 클래스 점수까지의 Shape 흐름 설명

##### 3분 퀴즈 · Pooling과 CNN (PDF p.45)

- Pooling의 채널 보존과 Adaptive Pool 출력 크기를 확인하는 퀴즈
- Flatten 시작 축과 Batch 유지의 관계를 점검하는 문항

**핵심:** 공간 축소와 채널 변화를 단계별로 추적하고 Batch 축·실제 클래스 수를 끝까지 유지.

### 4교시 · ImageFolder·Transforms·증강

#### 클래스 폴더와 기본 변환

##### 이미지 폴더와 변환 파이프라인 (PDF p.46)

- 클래스 폴더와 train·평가 변환 분리를 소개하는 4교시 도입

##### ImageFolder가 이해하는 폴더 구조 (PDF p.47)

- 분할별 루트 아래 클래스 폴더를 두고 이미지를 배치하는 ImageFolder 구조
- 폴더 이름의 정렬로 만들어진 class_to_idx와 정수 라벨 확인
- train·valid·test의 클래스 이름·의미 일치 확인
- 분할 전 중복 이미지와 출처 그룹 점검

##### torchvision.datasets.ImageFolder (PDF p.48)

- ImageFolder의 root는 클래스 하위 폴더를 포함한 경로
- transform은 이미지 변환, target_transform은 라벨 변환
- loader·is_valid_file·allow_empty로 파일 읽기·유효성·빈 클래스 허용 조건 설정
- 반환 샘플은 이미지와 class_index이며 Shape는 transform 결과에 의해 결정

##### 이미지 변환을 순서대로 연결한다 (PDF p.49)

- Resize·Crop → 의미를 보존하는 증강 → Tensor → Normalize의 처리 순서
- 무작위 변환은 train에만 적용
- valid/test는 같은 입력에 같은 결과를 주는 결정적 변환

##### Compose·Resize·ToTensor (PDF p.50)

- Compose는 변환 목록의 순서대로 실행
- Resize의 size와 보간·max_size·antialias 설정으로 크기 변환
- ToTensor는 이번 PIL 이미지의 HWC를 CHW 실수 Tensor로 변환하며 값 범위는 보통 0~1

##### Normalize · 채널별 평균과 표준편차로 변환 (PDF p.51)

- Normalize는 Tensor의 채널별 `(input[c] − mean[c]) / std[c]` 변환
- mean·std는 채널 수에 대응하는 Sequence
- inplace=False가 기본이며 모델이 기대한 정규화 설정과의 일치 확인

#### 라벨을 보존하는 증강과 분할 정책

##### Data Augmentation은 같은 의미의 다양한 입력을 만든다 (PDF p.52)

- 증강은 클래스 의미를 유지한 입력 다양성 확보
- Flip·Rotation·Crop·Color 변환의 허용 여부는 라벨 의미 기준으로 판단
- 가로·세로 줄무늬 실습의 90도 회전은 라벨이 뒤집히므로 제외

##### RandomHorizontalFlip·RandomRotation·ColorJitter (PDF p.53)

- RandomHorizontalFlip의 p는 적용 확률이며 기본값은 0.5
- RandomRotation의 degrees는 회전 범위이며 보간·expand·center·fill 선택 가능
- ColorJitter는 밝기·대비·채도·색조의 변화 범위 설정
- 변환 뒤 입력 크기와 라벨 의미 보존 여부 확인

##### train과 valid/test 변환을 분리한다 (PDF p.54)

- train은 무작위 변환으로 Epoch마다 다른 표현을 제공하는 구성
- valid/test는 Resize·CenterCrop 같은 결정적 크기 변환 뒤 Tensor·Normalize 적용
- 이번 배포 코드의 기본 SmallCNN은 주로 32×32·ToTensor, ResNet18은 공식 224×224 변환 사용

#### Batch 구성과 실습 04

##### DataLoader · 이미지 Batch 구성 (PDF p.55)

- DataLoader는 Dataset을 이미지 `[B,C,H,W]`와 라벨 `[B]`로 묶는 iterator
- batch_size·shuffle·num_workers·pin_memory로 묶음·순서·로딩·전송 조건 설정
- drop_last=False는 마지막 작은 Batch를 유지하는 기본값

##### ImageFolder와 DataLoader로 Batch 확인 (PDF p.56)

- ImageFolder → transform → DataLoader → 첫 Batch의 Shape·라벨·클래스 매핑 확인
- 교재 `[16,3,128,128]`은 예시 입력 조건
- 배포 기본필수는 train 12장과 Batch 4·32×32 조건으로 별도 확인

##### 실습 04 · ImageFolder·Transforms·DataLoader (PDF p.57)

- 기본필수는 두 클래스 폴더와 첫 Batch의 Shape·정수 라벨·class_to_idx 확인
- 응용은 train·valid 변환 분리와 동일 이미지의 변환 결과 비교
- 심화는 증강 후보 3개의 라벨 의미 보존 근거 작성
- 특심화 04는 seed·Worker 정책과 순서·마지막 배치·로딩 시간 확인
- 완료 기준은 같은 클래스 순서와 결정적 평가 입력의 확인

##### 3분 퀴즈 · 이미지 데이터 (PDF p.58)

- 폴더 이름과 정수 라벨의 대응을 확인하는 퀴즈
- 평가 변환의 결정성과 Tensor 변환 뒤 Normalize 적용 순서를 점검하는 문항

**핵심:** 학습 증강은 라벨 의미를 보존하고 검증 입력은 동일한 변환으로 비교 가능하게 구성.

### 5교시 · CNN 학습·평가·Best model

#### Batch 학습과 표본 가중 지표

##### CNN 학습·평가·Best model (PDF p.59)

- ANN의 학습 루프를 유지하면서 입력과 모델 구조를 CNN으로 확장하는 5교시 도입

##### 이미지 분류 학습의 한 Batch (PDF p.60)

- 이미지·라벨 장치 이동 → Logit 계산 → loss → backward·step → 지표 누적
- Batch별 가중치 갱신과 Epoch 전체 지표 집계의 구분

##### Logit·Loss·예측을 구분한다 (PDF p.61)

- Logit `[B,K]`는 정규화 전 클래스 점수
- CrossEntropyLoss는 별도 Softmax 없이 Logit과 long 정수 라벨을 입력
- argmax(dim=1)은 이미지별 예측 클래스
- Accuracy의 분모는 전체 샘플 수이며 클래스별 오류도 별도 확인

##### CNN 한 Epoch 학습 함수 (PDF p.62)

- model.train에서 Batch마다 기울기 초기화·순전파·손실·역전파·갱신 수행
- 평균 loss는 Batch 평균에 해당 Batch 샘플 수를 곱해 누적한 뒤 전체 샘플 수로 나누는 방식
- 마지막 작은 Batch도 동일한 표본 가중 집계
- 정확도는 전체 정답 수를 전체 표본 수로 나눈 값

##### train()·zero_grad()·backward()·step() (PDF p.63)

- train(mode)는 모듈의 학습·평가 동작을 전환
- zero_grad의 set_to_none 선택은 기존 gradient 정리 방식 결정
- backward는 gradient 계산, step은 Optimizer의 파라미터 갱신
- scalar loss의 backward는 별도 gradient 인자 없이 호출하는 기본 경로

#### 평가 모드와 오류 분석

##### 평가 함수 · gradient 없이 loss와 accuracy 계산 (PDF p.64)

- model.eval은 Dropout·BatchNorm의 평가 동작 설정
- inference_mode는 Autograd 기록 비활성화
- 평가에서는 Optimizer 갱신 없이 표본 수 기준 loss·accuracy 집계
- valid는 모델 선택에 사용하며 이번 과제의 test는 보관

##### Accuracy만 보고 끝내지 않는다 (PDF p.65)

- 혼동행렬로 실제 클래스와 예측 클래스의 혼동 유형 확인
- 클래스별 Recall과 실제 오분류 이미지로 놓친 사례·라벨 품질 진단
- 클래스 불균형에서는 Macro-F1·가중치·Sampler 검토
- 높은 전체 정확도만으로 오류 분석을 대체하지 않는 평가

#### Best 저장·복원과 실습 05

##### 학습곡선과 Best model 기록 (PDF p.66)

- Epoch별 train loss·valid loss·valid accuracy 기록
- 미리 정한 valid 기준으로 best epoch와 상태 저장
- best 모델 복원 뒤 선택 지표 재확인
- seed·분할·변환·설정의 재실행 조건 기록

##### Best model 저장과 복원 (PDF p.67)

- PDF 코드는 valid accuracy 개선 시 모델 상태와 classes·image_size·Normalize 저장
- 배포 코드는 valid loss 최소 기준이므로 실제 사용한 선택 지표를 명시
- 메모리에서 best 상태를 보관할 때 후속 학습과 독립된 복사 사용
- 동일 구조로 상태를 복원하고 클래스 순서·전처리를 재현하는 확인
- 모델 구조·라이브러리 버전은 README 기록

##### 실습 05 · CNN 학습·평가와 Best model (PDF p.68)

- 기본필수는 SmallCNN 3~5 Epoch 학습과 train/valid 지표 기록
- 응용은 혼동행렬과 클래스별 정답 수로 어려운 클래스 확인
- 심화는 같은 분할에서 증강 또는 폭 후보 비교와 best epoch 저장
- 특심화 05는 AMP·불균등 기울기 누적·clipping과 표본 가중 평가·상태 보존 검증
- 완료 기준은 선택 기준에 따른 best 모델 복원과 지표 설명

##### 3분 퀴즈 · CNN 학습 (PDF p.69)

- Logit과 CrossEntropyLoss의 입력 관계를 확인하는 퀴즈
- eval과 inference_mode의 역할 차이 및 마지막 Epoch와 best 모델의 구분 점검

**핵심:** 학습과 평가 동작을 구분하고 실제 선택 지표에 따른 best 상태를 독립 저장·복원.

### 6교시 · 전이학습·Freeze·Fine-tuning

#### 사전학습 표현과 가중치 전처리

##### 사전학습 CNN의 표현을 재사용한다 (PDF p.70)

- 사전학습 CNN의 표현을 활용해 Head부터 학습하는 6교시 도입
- 필요한 경우 제한된 깊은 층으로 학습 범위 확장

##### Feature Extractor와 Fine-tuning (PDF p.71)

- Feature Extractor는 사전학습 Backbone을 고정하고 새 Head만 학습
- Partial fine-tuning은 앞쪽 표현을 보존하며 layer4와 Head를 학습
- 데이터 규모·도메인 차이·과적합을 근거로 범위 선택
- BatchNorm의 Running 통계와 affine 파라미터 고정 여부는 별도 정책

##### 처음부터 학습과 전이학습 비교 (PDF p.72)

- Scratch는 무작위 초기화에서 전체 파라미터 학습
- Head-only는 사전학습 표현을 고정해 역전파 비용을 줄이는 구성
- Partial은 일부 깊은 층을 새 도메인에 적응시키는 구성
- 필요 데이터·시간·과적합 위험은 구조·학습률·데이터 조건에 따른 비교

##### torchvision.models.resnet18 (PDF p.73)

- resnet18의 weights=None 기본값은 사전학습 가중치 미사용
- 실제 전이학습에서는 공식 가중치를 명시하는 모델 생성
- 마지막 fc의 출력 수를 실제 클래스 수에 맞게 구성

##### Weights 객체와 전처리 (PDF p.74)

- Weights 객체는 사전학습 가중치와 대응 전처리를 연결
- weights.transforms는 Resize·Crop·Rescale·Normalize를 포함하는 변환
- 공식 가중치 실행에는 네트워크 또는 사전 캐시 필요
- 무작위 weights=None 결과를 전이학습 성능으로 대신 기록하지 않는 구분

#### Head 교체와 부분 미세조정 정책

##### ResNet18의 분류 Head 교체 (PDF p.75)

- 기존 Backbone을 동결한 뒤 클래스 수에 맞는 새 fc로 Head 교체
- Optimizer에는 학습할 fc 파라미터만 전달
- 매 Epoch model.eval과 fc.train으로 Backbone BN 통계를 고정하는 정책
- 뒤이은 무조건적 model.train은 BN 정책을 해제할 수 있는 호출
- eval 상태에서도 gradient 계산과 Head 역전파 가능

##### 부분 미세조정 순서 (PDF p.76)

- Head-only 기준 성능·오류 확인 뒤 마지막 Stage 등 제한된 층 개방
- 사전학습 층에는 Head보다 작은 학습률 적용
- valid 과적합과 BatchNorm 상태를 확인하며 best 모델 저장

##### 학습률을 Parameter Group으로 분리 (PDF p.77)

- Parameter Group으로 layer4와 fc의 학습률 분리
- 교재 예시는 layer4 1e-4·fc 1e-3이며 열지 않은 층은 학습 대상에서 제외
- 학습 모드를 설정한 뒤 모든 BN을 eval로 되돌려 Running 통계 고정
- 특심화 06의 BN affine 추가 동결은 기본 실습과 다른 정책으로 명시

#### 모델 비교·오류 점검·실습 06

##### 모델 비교표에 반드시 남길 항목 (PDF p.78)

- 모델·학습 범위·학습 가능 파라미터 수·best epoch·valid 지표 기록
- 시간·VRAM과 입력 크기·전처리·학습량 차이를 함께 남기는 비교표
- 서로 다른 조건의 결과를 순수한 모델 구조 효과로 단정하지 않는 해석

##### 전이학습에서 자주 발생하는 오류 (PDF p.79)

- 사전학습 가중치와 불일치하는 전처리 점검
- 학습 대상의 Optimizer 누락과 클래스 수에 맞지 않는 fc 점검
- test를 본 뒤 학습률·학습 범위를 고르는 선택 누수 제외

##### 실습 06 · 전이학습·Freeze·Fine-tuning 비교 (PDF p.80)

- 기본필수는 실제 가중치가 준비된 경우 Head-only 학습과 SmallCNN 비교
- 응용은 Head-only·layer4+Head의 학습 범위와 파라미터 수 비교
- 심화는 모델별 입력·Normalize·학습률 조건을 통일하거나 차이 명시
- 특심화 06은 범위 전환 뒤 Optimizer 상태·BN 고정·학습 대상 일치 검증
- 가중치 미준비 시 미실행 사유와 동결·전처리 구조를 설명하는 대체 확인

##### 3분 퀴즈 · 전이학습 (PDF p.81)

- Feature Extractor의 학습 대상과 사전학습 전처리를 점검하는 퀴즈
- Head와 Backbone의 서로 다른 학습률 사용 근거 확인

**핵심:** 실제 사전학습 가중치·전처리·학습 범위·Optimizer·BN 정책이 일치하는 조건에서 전이 결과 판단.

### 7교시 · CPU·GPU 시간·VRAM 비교

#### 장치 특성과 공정한 시간·메모리 측정

##### CPU·GPU 학습시간과 VRAM을 공정하게 측정한다 (PDF p.82)

- 모델·입력·Batch·반복·측정 범위를 통제하는 7교시 도입

##### 병렬 계산과 VRAM의 역할 (PDF p.83)

- CPU의 일반 작업 처리와 GPU의 대규모 Tensor 병렬 연산 구분
- VRAM은 모델·활성값·gradient·Optimizer 상태 저장에 사용
- 작은 모델·Batch에서는 전송·초기화 비용으로 GPU 이득이 작을 수 있는 조건

##### 공정한 시간 비교 조건 (PDF p.84)

- 같은 모델·데이터 순서·Batch·Epoch·입력 크기로 장치 비교
- 데이터 로딩 포함 여부를 명시한 측정 범위 고정
- GPU Warm-up 후 측정 시작·종료의 synchronize 적용
- 시간·images/s·Peak VRAM·환경 정보 동시 기록

##### torch.cuda.synchronize · 비동기 CUDA 완료 대기 (PDF p.85)

- CUDA는 비동기 실행이므로 CPU 타이머와 실제 작업 완료 시점 구분
- synchronize(device)는 해당 장치의 대기 작업 완료까지 대기
- CUDA가 없는 환경에서는 호출 제외

##### GPU Peak Memory 측정 함수 (PDF p.86)

- 측정 구간 시작 직전 reset_peak_memory_stats로 최대값 통계 초기화
- max_memory_allocated는 PyTorch Tensor가 점유한 최대 allocated bytes 반환
- MiB 변환은 bytes ÷ 1024²
- 예약 메모리나 시스템 전체 GPU 사용량과 다른 측정 정의

#### 계측 구현과 Batch별 결과 해석

##### 한 Epoch 시간과 Peak VRAM 측정 (PDF p.87)

- 한 Epoch의 학습 구간을 perf_counter로 측정하는 예시
- 처리량은 실제 처리한 이미지 수 ÷ 경과 초
- CUDA일 때 동기화와 Peak Tensor 메모리 측정
- CPU에서는 VRAM을 None/N/A로 기록하고 CPU 메모리는 별도 도구로 측정
- 모델의 학습·BN 모드 정책은 계측 호출 전에 설정

##### Batch size와 속도·VRAM의 관계 (PDF p.88)

- Batch 크기 변화에 따른 시간·처리량·Peak VRAM 기록
- 큰 Batch의 활용률 향상 가능성과 OOM 위험을 함께 확인
- Batch 비교에서는 다른 실험 조건을 고정하고 갱신 횟수 변화도 구분

##### CPU·GPU 모델 성능표 템플릿 (PDF p.89)

- Device·Model·Batch·Best Valid·시간/Epoch·images/s·Peak VRAM을 함께 기록
- CPU의 VRAM과 GPU 미실행 수치는 N/A
- 모델 선택 표와 장치 속도 비교의 목적 구분

##### 측정값을 과장하지 않고 해석한다 (PDF p.90)

- GPU 속도는 장치·Driver·CUDA·입력·Batch 조건에 의존
- 정확도 차이는 seed·알고리즘·실험 조건 차이와 함께 해석
- GPU 미보유 시 CPU 결과·환경 점검·비교 코드로 기록
- 학습 시간과 서비스 추론 지연을 서로 다른 지표로 구분

#### 실습 07과 성능 측정 확인

##### 실습 07 · CPU·GPU 학습시간과 VRAM 비교 (PDF p.91)

- 기본필수는 SmallCNN 한 Epoch의 CPU 시간·images/s와 조건 기록
- 응용은 GPU 사용 가능 시 같은 설정의 시간·처리량·Peak VRAM 측정
- 심화는 Batch 8·16·32의 속도·메모리 균형 비교
- 특심화 07은 동일 초기 상태의 반복 benchmark와 단계별 profiler를 별도 기록
- 완료 기준은 측정 범위·환경·반복 조건과 미측정 항목의 명시

##### 3분 퀴즈 · 성능 측정 (PDF p.92)

- CUDA 비동기 실행과 synchronize의 관계를 확인하는 퀴즈
- Batch 비교에서 고정할 조건과 allocated 메모리의 측정 범위 점검

**핵심:** 동일한 비교 조건과 명확한 측정 범위로 시간·처리량·Peak allocated VRAM을 해석.

### 8교시 · 이미지 분류 프로젝트·시연

#### 프로젝트 작업 흐름과 단계별 산출물

##### 최종 프로젝트 · 이미지 분류 모델과 성능표 (PDF p.93)

- SmallCNN의 구조·학습곡선·검증 지표를 연결하는 최종 프로젝트
- 준비된 경우 실제 ResNet18 Head 또는 Partial 결과 추가 비교
- CPU/GPU 학습 시간·처리량·Peak VRAM과 선택 근거 기록
- 기본필수 완성 뒤 선택한 단계의 오류 분석·복원 검증으로 확장

##### 심화 참고 · VS Code 프로젝트 구조 (PDF p.94)

- 심화용 모듈 구조는 main·models·data·train과 outputs·reports로 역할 분리
- 기본필수는 제공된 한 파일 골격으로 공통 평가를 충족하는 범위
- 모듈 구조를 모든 단계의 추가 제출 의무로 해석하지 않는 구분

##### 프로젝트 공통 작업 순서 (PDF p.95)

- 클래스 폴더 확인 → 변환 분리 → CNN 학습·best 저장 → 전이학습 비교 → 장치 계측 → 결과표·보고서
- 공식 가중치가 준비되지 않아도 SmallCNN 프로젝트를 독립 완성하는 진행

##### 단계별 제출물 · 기본필수부터 완성 (PDF p.96)

- history는 Epoch별 train/valid 지표와 best 표시 기록
- model_comparison은 모델·학습 범위·학습 가능 파라미터·valid 지표 기록
- hardware_benchmark는 07번의 실제 측정 조건·환경 기록이며 CUDA 미실행은 N/A
- 응용은 실제 오답 CSV, 심화는 오류 이미지로 단계별 확장하며 오답 0건도 정상
- checkpoint는 상태·클래스 순서·입력 크기·Normalize를 함께 보존
- README/report에 실행법·설정·선택 근거·한계·재현 조건 기록
- 기본필수의 직접 생성물과 별도 07번 계측을 README로 연결하는 제출 범위

#### 실습 08·형성평가·경계 검증

##### 실습 08 · 이미지 분류 프로젝트 통합·시연 (PDF p.97)

- 기본필수는 SmallCNN 학습·평가·best 저장·성능표 완성
- 응용은 클래스별 Precision·Recall·F1과 실제 오답 CSV 추가
- 응용 지표의 0분모는 0.0이며 오답 0개는 헤더만 있는 CSV로 기록
- 심화는 표본 가중 평가·호출 전 모드 복구·저장 모델 대조 테스트 추가
- 특심화 08은 연속 4 Epoch와 2 Epoch 저장 후 새 프로세스의 2 Epoch 재개 상태 대조
- 특심화 08의 정확 재개 비교는 동일 CPU·버전·threads=1·workers=0·Epoch 경계 조건에 한정
- 완료 기준은 자신의 결과·선택 근거·한계와 같은 입력의 복원 결과 설명

##### 형성평가 기준 · 기본필수로 100점 (PDF p.98)

- 기본필수만으로 데이터·Transform 20점, CNN·Shape 20점, 학습·평가 25점 충족
- 전이학습 15점은 동결·전처리 설명과 가중치 미준비 기록을 포함
- 시간·VRAM·재현 20점은 CPU 측정·환경·README 설명 기준
- 높은 정확도나 GPU 보유 자체를 공통 평가의 필수 조건으로 두지 않는 기준

##### 정상·경계·실패 상황을 구분한다 (PDF p.99)

- 정상 RGB Batch에서 입력 수·Logit 수·예측 수 일치 확인
- 마지막 작은 Batch는 drop_last와 실제 표본 수 분모 확인
- 클래스 폴더 누락은 학습 전 class_to_idx·클래스 수 점검 단계에서 차단
- CPU-only는 기본 실습 진행과 GPU 항목 N/A 확인
- 복원은 같은 구조·클래스 순서·전처리·동일 입력의 Logit/예측 대조
- Adaptive Pool 사용 모델은 입력 공간 크기 변경 시 후속 fc 입력 Shape 확인

**핵심:** 기본필수의 실행 모델·best 복원·결과표·환경 기록을 완성하고 선택 근거와 한계를 설명.

### 마무리 · 핵심 회수와 다음 수업

#### 오늘의 정리와 다음 구조 연결

##### 오늘의 핵심 정리 (PDF p.100)

- CNN의 국소 연결·가중치 공유와 Conv/Pool 뒤 Shape 추적 정리
- train·평가 변환 분리와 사전학습 표현 재사용 연결
- CPU/GPU 비교는 같은 조건과 측정 범위를 근거로 해석

##### 다음 수업 · 11월 3일 아키텍처 비교 (PDF p.101)

- 다음 수업의 순서 입력·은닉 상태·장기 의존성 예고
- Autoencoder의 압축·재구성과 Transformer의 Attention 연결 예고

### 참고자료 · 공식 문서의 범위

#### PyTorch와 Torchvision 참고 범위

##### 공식 참고자료 · PyTorch Core (PDF p.102)

- Conv·Pooling·DataLoader·Loss·평가 모드의 PyTorch 공식 참고 범위
- CUDA 동기화·메모리 관리·재현성과 모델 저장/복원 참고 범위

##### 공식 참고자료 · Torchvision (PDF p.103)

- ImageFolder·Transforms·Normalize·ResNet18 가중치의 Torchvision 공식 참고 범위
- 전이학습 튜토리얼과 이미지 증강 참고 범위

## 자료 간 차이

- PDF p.39·41의 64×64·3클래스는 구조 예시. 배포 기본필수는 32×32·2클래스이며 ResNet18은 공식 224×224 전처리 사용.
- PDF p.67 코드는 valid accuracy 개선을 기준으로 저장. 배포 `01_basic/05_train.py`·`08_project.py`와 심화 프로젝트 `main.py`는 valid loss 최솟값 기준. 실제 실행의 선택 기준을 기록하는 구분.
- 원본 배포 자료의 PPT 대응표·실습 README의 PPT 쪽수는 이전 93쪽 구성 기준. 현재 PDF에는 도입 10쪽이 추가되어 실습 01~08의 실제 위치는 p.22·32·44·57·68·80·91·97.
- PDF p.96은 단계 전체 산출물 안내. 기본필수 08의 직접 출력은 history.csv·model_comparison.csv·valid_predictions.csv·best_model.pt이며 계측은 별도 07번 결과와 README로 연결. 응용의 실제 오답 CSV·심화 오류 이미지는 선택 확장.
- 원본 배포 자료의 검수 요약에서 실제 ImageNet 가중치·CUDA 실행은 미검증. 미실행을 성능 0이나 무작위 가중치 결과로 대체하지 않는 기록.
