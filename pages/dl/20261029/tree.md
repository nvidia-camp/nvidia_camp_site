# Day9 · 강의 구조와 핵심 설명

2026.10.29 · 딥러닝 핵심 아키텍처 및 학습

교시 설명과 중간 주제는 학습 흐름을 위해 구성한 표현. 슬라이드 제목은 원문 유지. 동일 제목의 페이지도 각각 구분.

페이지는 현재 104쪽 PDF의 뷰어 기준. 슬라이드의 인쇄 쪽수와 실습 대응표는 기존 92쪽 기준이 남아 있으므로 제목·실습 번호로 대응. 추가 GPU 도입부는 1교시 라벨 앞의 수업 준비에 배치.

실습 범위는 현재 v2 강사 운영안·PPT 대응표·수강생 README 기준. 기본필수는 정상 20건·CPU·full-batch, 응용 이상은 200건·mini-batch로 구분. 기본필수부터 시작하고 다른 난이도는 선택 경로.

당일 test는 입력 Tensor 생성·모델 전달·평가에 사용하지 않고 보관. 수치·검수 환경은 원문에 기재된 참고 기준.

## 강의 목차

```text
수업 준비
├─ 복습과 수업 범위
│  ├─ 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)
│  ├─ 어제까지 완성한 머신러닝 흐름 (PDF p.2)
│  ├─ 3분 확인 퀴즈 · 머신러닝에서 딥러닝으로 (PDF p.3)
│  ├─ 오늘의 목표와 8교시 운영 (PDF p.4)
│  └─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.5)
├─ 인공신경망과 GPU 연산의 배경
│  ├─ 왜 딥러닝에는 GPU가 유리할까? 인공신경망 구조 (PDF p.6)
│  ├─ 왜 딥러닝에는 GPU가 유리할까? (PDF p.7)
│  ├─ 딥러닝은 같은 계산을 수없이 반복한다 (PDF p.8)
│  ├─ CPU와 GPU의 내부 구성은 무엇이 다를까? (PDF p.9)
│  └─ 딥러닝의 핵심 계산: 행렬 곱셈 (PDF p.10)
├─ 병렬 처리와 메모리 전송의 조건
│  ├─ 같은 일을 나누어 동시에 처리한다 (PDF p.11)
│  ├─ GPU는 학습 과정 중 어디서 사용될까? (PDF p.12)
│  ├─ 그런데 GPU로 옮기는 데도 시간이 든다 (PDF p.13)
│  └─ GPU가 언제나 빠른 것은 아니다 (PDF p.14)
├─ GPU 활용 원리 확인
│  ├─ 2분 확인 퀴즈 · CPU와 GPU (PDF p.15)
│  └─ 한 장으로 정리: 왜 AI 학습에 GPU를 쓸까? (PDF p.16)
└─ 난이도 선택과 전체 학습 흐름
   ├─ 네 난이도 · 같은 주제를 다른 깊이로 (PDF p.17)
   └─ 딥러닝 학습의 큰 흐름 (PDF p.18)

1교시 · GPU·CUDA·PyTorch 환경 점검
├─ GPU 연산 구조와 실행 계층
│  ├─ GPU·CUDA·PyTorch 환경을 먼저 확인한다 (PDF p.19)
│  ├─ CPU와 GPU는 일을 나누는 방식이 다르다 (PDF p.20)
│  └─ GPU 학습 환경의 네 층 (PDF p.21)
├─ 드라이버 조회와 PyTorch 설치 확인
│  ├─ nvidia-smi로 GPU와 드라이버 확인 (PDF p.22)
│  ├─ nvidia-smi 출력에서 오해하기 쉬운 것 (PDF p.23)
│  ├─ PyTorch 설치는 공식 선택기를 기준으로 한다 (PDF p.24)
│  ├─ 가상환경과 설치 명령 확인 (PDF p.25)
│  ├─ PyTorch에서 GPU 사용 가능 여부 확인 (PDF p.26)
│  └─ CUDA 확인 함수 3개 (PDF p.27)
└─ 장치 선택과 환경 실습
   ├─ CPU와 GPU를 모두 지원하는 코드 패턴 (PDF p.28)
   ├─ 실습 01 · GPU·CUDA·PyTorch 동작 점검 (PDF p.29)
   └─ 3분 퀴즈 · GPU 환경 (PDF p.30)

2교시 · Tensor의 모양·자료형·장치
├─ Tensor의 차원과 생성
│  ├─ Tensor·shape·dtype·device를 읽는다 (PDF p.31)
│  ├─ Tensor는 차원을 가진 수치 배열이다 (PDF p.32)
│  ├─ 딥러닝에서 자주 보는 Tensor 모양 (PDF p.33)
│  ├─ torch.tensor로 Tensor 만들기 (PDF p.34)
│  └─ torch.tensor() (PDF p.35)
├─ 초기값 생성과 모양 연산
│  ├─ 무작위·0·1 Tensor 생성 (PDF p.36)
│  ├─ torch.randn() (PDF p.37)
│  ├─ Tensor 연산과 broadcasting (PDF p.38)
│  └─ shape를 바꾸는 주요 연산 (PDF p.39)
└─ 장치 이동과 Tensor 실습
   ├─ Tensor와 모델은 같은 device에 있어야 한다 (PDF p.40)
   ├─ Tensor와 모델을 device로 이동 (PDF p.41)
   ├─ Tensor.to() (PDF p.42)
   ├─ 실습 02 · Tensor 모양과 device 이동 (PDF p.43)
   └─ 3분 퀴즈 · Tensor (PDF p.44)

3교시 · 연산 그래프와 자동 미분
├─ 계산 그래프와 기울기 추적
│  ├─ 연산 그래프·기울기·Gradient Descent (PDF p.45)
│  ├─ 계산 그래프는 연산의 연결을 기록한다 (PDF p.46)
│  ├─ requires_grad가 의미하는 것 (PDF p.47)
│  ├─ 간단한 미분을 자동으로 계산 (PDF p.48)
│  └─ backward() (PDF p.49)
├─ 기울기 누적과 경사하강법
│  ├─ 기울기는 기본적으로 누적된다 (PDF p.50)
│  ├─ Gradient Descent는 손실이 작아지는 방향으로 이동한다 (PDF p.51)
│  ├─ 수동으로 파라미터를 5번 갱신 (PDF p.52)
│  └─ torch.no_grad()와 detach() (PDF p.53)
└─ 미분·갱신 실습과 확인
   ├─ 실습 03 · Autograd와 Gradient Descent (PDF p.54)
   └─ 3분 퀴즈 · Autograd (PDF p.55)

4교시 · ANN 구조와 순전파
├─ 뉴런과 층별 shape
│  ├─ Neuron·Linear·ReLU·순전파 (PDF p.56)
│  ├─ 하나의 인공 뉴런 (PDF p.57)
│  ├─ 2→8→2 ANN의 모양 (PDF p.58)
│  └─ 층을 지날 때 shape가 어떻게 바뀌는가 (PDF p.59)
├─ Linear·ReLU와 모델 구성
│  ├─ nn.Linear (PDF p.60)
│  ├─ nn.ReLU · nn.Sequential (PDF p.61)
│  ├─ 2→8→2 ANN 모델 만들기 (PDF p.62)
│  ├─ 모델의 파라미터를 확인한다 (PDF p.63)
│  └─ nn.Module과 model.to() (PDF p.64)
└─ ANN 순전파 실습과 확인
   ├─ 실습 04 · ANN 구조와 순전파 (PDF p.65)
   └─ 3분 퀴즈 · ANN (PDF p.66)

5교시 · 분류 손실과 mini-batch
├─ logits와 CrossEntropyLoss
│  ├─ Logits·손실함수·Dataset·DataLoader (PDF p.67)
│  ├─ logits·확률·클래스는 다른 값이다 (PDF p.68)
│  ├─ CrossEntropyLoss의 역할 (PDF p.69)
│  └─ nn.CrossEntropyLoss (PDF p.70)
├─ Dataset과 DataLoader
│  ├─ Dataset과 DataLoader의 역할 (PDF p.71)
│  ├─ TensorDataset과 DataLoader 사용 (PDF p.72)
│  ├─ DataLoader (PDF p.73)
│  └─ 전체 데이터를 작은 묶음으로 나누어 학습한다 (PDF p.74)
└─ 손실·배치 집계 실습과 확인
   ├─ 실습 05 · 손실함수와 mini-batch (PDF p.75)
   └─ 3분 퀴즈 · 손실과 데이터 (PDF p.76)

6교시 · 역전파와 SGD 학습 루프
├─ 학습 step의 순서와 준비
│  ├─ 순전파·손실·역전파·Optimizer를 반복한다 (PDF p.77)
│  ├─ 순전파·손실·역전파·Optimizer를 반복한다 (PDF p.78)
│  ├─ 한 번의 학습 step (PDF p.79)
│  ├─ ANN 학습 루프 · 설정과 준비 (PDF p.80)
│  ├─ ANN 학습 루프 · batch 반복 (PDF p.81)
│  └─ SGD · zero_grad · step (PDF p.82)
├─ 평가 모드와 장치·학습곡선
│  ├─ model.train()·model.eval()·torch.no_grad() (PDF p.83)
│  ├─ batch를 GPU로 옮기는 위치 (PDF p.84)
│  └─ 학습곡선 예시 · 매번 감소하는 것은 아니다 (PDF p.85)
└─ 학습 루프 실습과 확인
   ├─ 실습 06 · 순전파·역전파·SGD 학습 루프 (PDF p.86)
   └─ 3분 퀴즈 · 학습 루프 (PDF p.87)

7교시 · ANN 학습 프로젝트 통합
├─ 예측 문제와 프로젝트 구조
│  ├─ GPU 동작 점검표·ANN 학습 프로젝트 (PDF p.88)
│  ├─ 일일 프로젝트 · 2차원 합성 데이터 분류 (PDF p.89)
│  ├─ 심화 프로젝트 구조 · 기본필수는 한 파일 (PDF p.90)
│  └─ 심화 프로젝트 실행 흐름 (PDF p.91)
├─ 모델·학습 함수의 연결
│  ├─ 심화 참조 · model.py의 ANN 구조 (PDF p.92)
│  └─ 심화 참조 · train.py의 한 epoch 학습 (PDF p.93)
└─ 환경·결과 점검과 프로젝트 실습
   ├─ GPU 동작 점검표와 학습 결과 (PDF p.94)
   ├─ 실습 07 · GPU ANN 프로젝트 통합 (PDF p.95)
   └─ 단계별 결과물 · 기본필수는 기존 파일만 (PDF p.96)

8교시 · 최종 재현·시연·회고
├─ 재실행과 단계별 완료 기준
│  ├─ 최종 점검·시연·회고 (PDF p.97)
│  ├─ 실습 08 · 최종 검증·시연·회고 (PDF p.98)
│  └─ 형성평가 · 기본필수만으로 100점 (PDF p.99)
└─ 경계·실패 상황의 확장 검증
   └─ 심화·특심화 확장 · 경계·실패 상황 (PDF p.100)

전체 정리와 참고자료
├─ 학습 정리와 다음 수업
│  ├─ 오늘의 핵심 정리 (PDF p.101)
│  └─ 다음 수업 · 학습을 안정화하고 과적합을 진단한다 (PDF p.102)
└─ 공식 참고자료
   ├─ 공식 참고자료 · 설치와 CUDA (PDF p.103)
   └─ 공식 참고자료 · Tensor·Autograd·신경망 (PDF p.104)
```

## 핵심 설명

### 수업 준비

#### 복습과 수업 범위

##### 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)

- GPU 환경 점검에서 Tensor·연산 그래프를 거쳐 ANN 학습 프로젝트로 이어지는 Day9 교재

##### 어제까지 완성한 머신러닝 흐름 (PDF p.2)

- 예측 시점의 입력과 정답을 구분하는 문제 정의 복습
- train·valid·test 분리 원칙의 딥러닝 실습 적용
- 전처리와 모델을 연결했던 재현 가능한 실험 흐름 복습

##### 3분 확인 퀴즈 · 머신러닝에서 딥러닝으로 (PDF p.3)

- test를 모델 선택에 사용했을 때의 평가 누수 확인
- 전처리 fit 범위와 딥러닝에서도 유지되는 데이터 분리 원칙 확인

##### 오늘의 목표와 8교시 운영 (PDF p.4)

- 50분씩 8교시로 구성한 총 400분 수업
- 설명·시연 200분과 실습·리뷰 200분 배분
- 환경 → Tensor → Autograd → ANN → 손실·배치 → 학습 루프 → 통합 → 재현의 순서

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.5)

- 당일 범위는 환경 점검과 Tensor 연산에서 작은 ANN 학습까지
- Optimizer 비교와 과적합 제어 기법은 다음 수업의 본격 실험 범위

#### 인공신경망과 GPU 연산의 배경

##### 왜 딥러닝에는 GPU가 유리할까? 인공신경망 구조 (PDF p.6)

- 입력층·여러 은닉층·출력층이 연결된 인공신경망 구조 도식
- 층 사이 다수 연결에서 수치 연산이 반복되는 딥러닝 계산의 배경

##### 왜 딥러닝에는 GPU가 유리할까? (PDF p.7)

- 큰 행렬에 비슷한 계산을 반복하는 딥러닝의 연산 특성
- 복잡한 제어를 맡는 CPU와 대량 수치 계산을 맡는 GPU의 역할 구분

##### 딥러닝은 같은 계산을 수없이 반복한다 (PDF p.8)

- 숫자 입력에서 예측·오차 계산·가중치 수정으로 이어지는 반복
- 데이터 수와 가중치 수 및 epoch 증가에 따른 연산량 확대

##### CPU와 GPU의 내부 구성은 무엇이 다를까? (PDF p.9)

- CPU는 상대적으로 적은 수의 강한 코어를 활용하는 구조
- GPU는 많은 연산 유닛으로 독립적인 수치 연산을 대량 처리하는 구조

##### 딥러닝의 핵심 계산: 행렬 곱셈 (PDF p.10)

- 행렬 곱의 각 결과 원소는 한 행과 한 열의 곱을 더한 값
- 서로 다른 결과 원소 계산의 병렬 처리 가능성

#### 병렬 처리와 메모리 전송의 조건

##### 같은 일을 나누어 동시에 처리한다 (PDF p.11)

- 서로 독립적인 계산을 나누어 동시에 처리하는 병렬 연산
- GPU의 높은 처리량은 동시에 투입할 작업이 충분한 조건과 연결
- CPU도 병렬 처리가 가능하므로 직렬 전용 장치로 단정하지 않음

##### GPU는 학습 과정 중 어디서 사용될까? (PDF p.12)

- 자료 읽기와 전처리는 CPU가 담당하는 학습 흐름 예시
- GPU는 순전파의 행렬 연산과 역전파의 기울기 계산에 활용
- GPU 위 파라미터 갱신을 여러 batch에서 반복하는 구조

##### 그런데 GPU로 옮기는 데도 시간이 든다 (PDF p.13)

- CPU RAM과 GPU VRAM 사이의 자료 전송 비용
- 큰 계산을 묶어서 처리하는 경우와 소량을 자주 이동하는 경우의 차이

##### GPU가 언제나 빠른 것은 아니다 (PDF p.14)

- 큰 행렬 연산과 반복 수치 계산에서의 GPU 이점
- 작은 연산·복잡한 분기·빈번한 전송에서는 CPU가 유리할 가능성
- VRAM 용량과 장치 호환성 및 비용의 제약
- 실제 데이터·모델·batch 조건에서 속도를 측정하는 판단 기준

#### GPU 활용 원리 확인

##### 2분 확인 퀴즈 · CPU와 GPU (PDF p.15)

- GPU의 모든 작업 우위와 CPU의 직렬 전용이라는 오해 확인
- 딥러닝의 행렬 반복 계산과 장치 간 전송 비용 확인

##### 한 장으로 정리: 왜 AI 학습에 GPU를 쓸까? (PDF p.16)

- 대규모 곱셈·덧셈의 반복과 GPU 병렬 처리의 연결
- 충분한 작업량과 낮은 전송 부담이라는 가속 조건
- GPU 존재 확인에서 CUDA·PyTorch 실행 확인으로 이어지는 학습

#### 난이도 선택과 전체 학습 흐름

##### 네 난이도 · 같은 주제를 다른 깊이로 (PDF p.17)

- 기본필수는 정상 20건을 CPU로 처리하는 9개 구현 항목
- 응용은 배치 손실 집계와 실제 오답 기록을 포함한 10개 구현 항목
- 심화는 모듈화와 저장·복원 및 정상 입력 테스트를 포함한 12개 구현 항목
- 특심화는 교시별 독립 실습의 계약·재현성 검증을 포함한 18개 구현 항목

##### 딥러닝 학습의 큰 흐름 (PDF p.18)

- Tensor 입력 → ANN 순전파 → 손실 계산 → 기울기 기반 파라미터 갱신의 연결

### 1교시 · GPU·CUDA·PyTorch 환경 점검

#### GPU 연산 구조와 실행 계층

##### GPU·CUDA·PyTorch 환경을 먼저 확인한다 (PDF p.19)

- GPU의 물리적 존재와 PyTorch의 CUDA 사용 가능 여부 구분
- 장치·드라이버·설치 패키지·실제 실행 가능 여부의 단계별 확인

##### CPU와 GPU는 일을 나누는 방식이 다르다 (PDF p.20)

- CPU는 복잡한 제어와 순차 작업 중심의 역할
- GPU는 큰 Tensor의 반복 수치 연산을 병렬 처리하는 역할

##### GPU 학습 환경의 네 층 (PDF p.21)

- GPU 하드웨어·드라이버·CUDA Runtime·PyTorch의 역할 구분
- 한 계층의 정상 동작만으로 전체 GPU 학습 환경의 준비를 단정하지 않음

#### 드라이버 조회와 PyTorch 설치 확인

##### nvidia-smi로 GPU와 드라이버 확인 (PDF p.22)

- `nvidia-smi`로 GPU 이름과 드라이버 정보 조회
- VRAM 사용량과 GPU 사용률 확인
- 실행 중인 프로세스 확인과 출력 형식의 버전별 차이

##### nvidia-smi 출력에서 오해하기 쉬운 것 (PDF p.23)

- Memory-Usage는 사용 중인 VRAM과 전체 용량의 관계
- GPU-Util은 현재 측정 구간의 사용률
- CUDA 지원 표시는 설치된 CUDA Toolkit 버전과 항상 같은 값이 아님

##### PyTorch 설치는 공식 선택기를 기준으로 한다 (PDF p.24)

- 기존 정상 가상환경을 우선 확인하고 불필요한 재설치 지양
- 공식 설치 선택기에서 OS·Python·Compute Platform 조합 확인
- 교재의 CPU 검수 버전과 실제 교실 GPU 환경의 검증 범위 구분

##### 가상환경과 설치 명령 확인 (PDF p.25)

- 실행 Python과 가상환경 확인 후 같은 인터프리터에 설치
- 설치 명령은 강의일 공식 선택기의 해당 플랫폼 명령 사용
- 설치 후 torch import와 버전 확인

##### PyTorch에서 GPU 사용 가능 여부 확인 (PDF p.26)

- PyTorch 버전과 `torch.version.cuda` 빌드 정보 구분
- `torch.cuda.is_available()`로 실제 CUDA 사용 가능 여부 확인
- CUDA 사용 가능 확인 후 GPU 이름·속성 조회
- CUDA가 불가능하면 허용된 CPU 경로로 진행

##### CUDA 확인 함수 3개 (PDF p.27)

- `is_available()`의 반환값은 CUDA 사용 가능 여부를 나타내는 bool
- `get_device_name()`과 `get_device_properties()`는 장치 이름과 속성 조회
- CUDA 사용 가능 확인 전 장치 조회를 호출하지 않음
- 조회 장치의 인덱스는 실제 환경에 맞게 확인하며 0으로 고정된다고 가정하지 않음

#### 장치 선택과 환경 실습

##### CPU와 GPU를 모두 지원하는 코드 패턴 (PDF p.28)

- 사용 가능한 장치에 따라 cuda 또는 cpu를 선택하는 공통 실행 패턴
- 선택한 device에 모델과 입력을 함께 배치

##### 실습 01 · GPU·CUDA·PyTorch 동작 점검 (PDF p.29)

- 기본필수는 `01_environment.py`의 CPU Tensor 계산과 실제 환경 기록
- 응용은 선택 device에서 실제 Tensor 연산과 환경 파일 저장
- 심화는 PyTorch 빌드와 장치·드라이버 정보를 구분한 기록
- 특심화는 cpu·auto·cuda 요청 정책의 성공·실패 계약 검증
- 완료 기준은 선택한 난이도의 실제 결과와 README 대조이며 GPU 미보유는 감점 대상 아님

##### 3분 퀴즈 · GPU 환경 (PDF p.30)

- `nvidia-smi` 성공과 PyTorch CUDA 사용 가능 여부의 차이 확인
- VRAM에 저장되는 계산 자료와 GPU 없이 가능한 CPU 실습 경로 확인

**핵심:** GPU 보유 여부와 CUDA 실행 가능 여부를 따로 확인하고, 선택한 난이도의 실제 연산 장치와 CPU 진행 근거 기록

### 2교시 · Tensor의 모양·자료형·장치

#### Tensor의 차원과 생성

##### Tensor·shape·dtype·device를 읽는다 (PDF p.31)

- Tensor의 값과 함께 shape·dtype·device를 읽는 학습 순서

##### Tensor는 차원을 가진 수치 배열이다 (PDF p.32)

- 스칼라·벡터·행렬을 차원 수와 shape로 구분
- 고차원 Tensor의 축 의미는 데이터 맥락과 함께 해석

##### 딥러닝에서 자주 보는 Tensor 모양 (PDF p.33)

- 표 입력은 `(batch, feature)`, 분류 클래스 정답은 `(batch,)`
- 분류 logits는 `(batch, class)`
- 이미지와 문장 자료는 채널·공간·시퀀스 축의 의미를 추가 확인

##### torch.tensor로 Tensor 만들기 (PDF p.34)

- 입력 특성은 float32 Tensor로 구성
- 이 수업의 분류 클래스 인덱스 정답은 long Tensor로 구성
- 생성 후 shape·dtype·device 확인

##### torch.tensor() (PDF p.35)

- `torch.tensor(data)`는 입력 자료를 복사해 새 Tensor 생성
- dtype·device·requires_grad는 목적에 맞게 지정하는 선택 인자
- 기존 Tensor를 다시 감싸는 경우 복사와 그래프 분리 가능성 구분

#### 초기값 생성과 모양 연산

##### 무작위·0·1 Tensor 생성 (PDF p.36)

- `randn`은 표준정규분포 난수 생성
- `zeros`는 0으로 채운 Tensor 생성
- `ones`는 1로 채운 Tensor 생성
- 스칼라 결과의 `.item()`과 Tensor의 shape 확인

##### torch.randn() (PDF p.37)

- `torch.randn`의 size는 생성할 Tensor의 모양
- generator·dtype·device 등은 선택 설정
- seed 고정의 동일 환경 재현성과 실제 업무 데이터의 대표성 구분

##### Tensor 연산과 broadcasting (PDF p.38)

- `(2, 3)` 행렬에 `(3,)` bias를 더하는 broadcasting 예제
- 축 크기의 호환성과 결과 shape를 계산 전에 확인

##### shape를 바꾸는 주요 연산 (PDF p.39)

- reshape는 전체 원소 수를 유지한 모양 변경
- view는 메모리 배치가 허용하는 모양 변경
- transpose는 두 축의 순서 교환
- unsqueeze와 squeeze는 크기 1인 차원의 추가·제거

#### 장치 이동과 Tensor 실습

##### Tensor와 모델은 같은 device에 있어야 한다 (PDF p.40)

- 연산에 사용하는 모델·입력·정답을 같은 device에 배치
- CPU와 CUDA 자료 혼합에 따른 장치 불일치 오류 구분

##### Tensor와 모델을 device로 이동 (PDF p.41)

- 선택 device로 모델과 입력을 이동한 뒤 순전파 실행
- Tensor의 `.to()` 반환 결과를 변수에 저장
- 출력 device를 입력·모델과 대조

##### Tensor.to() (PDF p.42)

- `Tensor.to()`는 device 또는 dtype을 바꾼 Tensor 반환
- 조건이 같으면 원본 Tensor를 반환할 가능성
- 장치 이동 호출만으로 끝내지 않고 반환값 사용

##### 실습 02 · Tensor 모양과 device 이동 (PDF p.43)

- 기본필수는 정상 Tensor의 모양·자료형·장치 읽기
- 응용은 reshape와 broadcasting 결과의 원소값 확인
- 심화는 모델·입력·정답의 장치 일치 확인
- 특심화는 이동 전후 값·dtype·gradient 연결 보존 검증
- 완료 기준은 선택 경로의 출력 모양과 실제 연산 근거 설명

##### 3분 퀴즈 · Tensor (PDF p.44)

- 클래스 인덱스 정답의 long dtype 확인
- Tensor 이동 결과의 재할당 확인
- 값뿐 아니라 shape·dtype·device·requires_grad를 확인하는 기준

**핵심:** Tensor의 값·shape·dtype·device를 함께 읽고, 이동한 결과와 모델·입력·정답의 장치 일치 확인

### 3교시 · 연산 그래프와 자동 미분

#### 계산 그래프와 기울기 추적

##### 연산 그래프·기울기·Gradient Descent (PDF p.45)

- 순전파의 연산 연결에서 손실 기울기를 계산한 뒤 파라미터를 갱신하는 흐름

##### 계산 그래프는 연산의 연결을 기록한다 (PDF p.46)

- 연산 그래프는 입력에서 결과까지의 계산 관계 기록
- 역전파는 연결된 연산에 연쇄법칙을 적용하는 기울기 계산

##### requires_grad가 의미하는 것 (PDF p.47)

- requires_grad가 활성화된 Tensor의 연산 추적
- 학습 파라미터와 backward 후 `.grad` 누적의 관계
- 평가에서는 no_grad로 새 gradient 그래프 생성 제어

##### 간단한 미분을 자동으로 계산 (PDF p.48)

- 간단한 다항식의 Tensor 계산과 자동 미분 연결
- Autograd 결과를 해석 미분의 값과 대조

##### backward() (PDF p.49)

- 스칼라 손실의 `backward()`는 추가 시작 기울기 없이 호출 가능
- 기울기는 leaf Tensor·Parameter의 `.grad`에 누적되며 메서드 반환값과 구분
- 비스칼라 출력의 시작 기울기 등은 별도 호출 조건

#### 기울기 누적과 경사하강법

##### 기울기는 기본적으로 누적된다 (PDF p.50)

- 새 순전파 결과로 backward를 반복해도 기존 gradient에 누적
- 일반 학습 step에서는 이전 gradient를 비운 뒤 현재 기울기 사용

##### Gradient Descent는 손실이 작아지는 방향으로 이동한다 (PDF p.51)

- 경사하강법은 손실 기울기의 반대 방향으로 파라미터 이동
- 갱신량은 학습률과 현재 기울기의 곱

##### 수동으로 파라미터를 5번 갱신 (PDF p.52)

- 손실 계산과 backward 뒤 no_grad 안에서 수동 파라미터 갱신
- 다음 반복 전에 gradient 초기화
- 목표값에 접근하는 파라미터 변화와 반복 수 확인

##### torch.no_grad()와 detach() (PDF p.53)

- `torch.no_grad()`는 블록 내부의 새 gradient 그래프 생성 억제
- `detach()`는 현재 그래프에서 분리한 Tensor 반환
- 학습에 필요한 gradient 연결을 끊는 위치와 평가·기록 위치 구분

#### 미분·갱신 실습과 확인

##### 실습 03 · Autograd와 Gradient Descent (PDF p.54)

- 기본필수는 다항식의 값과 기울기를 손계산과 비교
- 응용은 목표값에 접근하는 수동 갱신을 10회 수행
- 심화는 학습률별 변화와 gradient 누적의 차이 기록
- 특심화는 해석 미분·수치 미분·Autograd 결과 대조
- 완료 기준은 선택 경로의 기울기 계산과 갱신 근거 설명

##### 3분 퀴즈 · Autograd (PDF p.55)

- backward의 기울기 누적과 초기화 필요성 확인
- no_grad 안의 수동 갱신과 기울기 반대 방향 이동의 의미 확인

**핵심:** backward의 기울기 계산과 실제 파라미터 갱신을 구분하고, 갱신 그래프 기록과 이전 gradient 누적을 제어

### 4교시 · ANN 구조와 순전파

#### 뉴런과 층별 shape

##### Neuron·Linear·ReLU·순전파 (PDF p.56)

- 가중합과 비선형 변환을 여러 층으로 연결하는 ANN의 순전파 구조

##### 하나의 인공 뉴런 (PDF p.57)

- Linear는 가중치와 편향으로 가중합 계산
- activation은 가중합에 비선형성 추가

##### 2→8→2 ANN의 모양 (PDF p.58)

- 입력 특성 2개에서 은닉 표현 8개를 거쳐 클래스 logits 2개 생성
- batch 차원 유지와 마지막 특성 차원의 변화 구분
- argmax로 원시 점수에서 예측 클래스 인덱스 선택

##### 층을 지날 때 shape가 어떻게 바뀌는가 (PDF p.59)

- Linear에서 `(batch, 2)` → `(batch, 8)` → `(batch, 2)` 변환
- ReLU는 해당 입력의 shape 유지
- `argmax(dim=1)`은 클래스 축을 줄여 `(batch,)` 반환

#### Linear·ReLU와 모델 구성

##### nn.Linear (PDF p.60)

- `nn.Linear`는 입력 마지막 축에 affine 변환 적용
- in_features와 out_features가 필수 생성 인자
- weight 모양은 `(out_features, in_features)`
- 입력 마지막 차원과 in_features의 일치 확인

##### nn.ReLU · nn.Sequential (PDF p.61)

- ReLU는 음수 값을 0으로 바꾸는 비선형 변환
- Sequential은 전달한 Module을 순서대로 연결
- 층의 순서와 인접 층의 입출력 크기가 모델 구조를 결정

##### 2→8→2 ANN 모델 만들기 (PDF p.62)

- Linear → ReLU → Linear의 순서로 2→8→2 ANN 구성
- `model(X)`의 순전파 출력은 확률이 아닌 logits
- 입력·출력의 batch 크기와 마지막 차원 확인

##### 모델의 파라미터를 확인한다 (PDF p.63)

- `model.parameters()`로 Optimizer에 전달할 파라미터 조회
- 이름과 원소 수를 이용한 모델 구조 점검
- 교재의 2→8→2 ANN은 학습 파라미터 42개

##### nn.Module과 model.to() (PDF p.64)

- 사용자 정의 신경망은 nn.Module을 상속하고 초기화 수행
- forward에 입력에서 출력까지의 순전파 정의
- 등록한 하위 모듈과 Parameter의 장치 이동 및 조회
- 일반 Python list와 Module 등록 구조의 차이

#### ANN 순전파 실습과 확인

##### 실습 04 · ANN 구조와 순전파 (PDF p.65)

- 기본필수는 Sequential ANN의 출력 shape와 파라미터 수 확인
- 응용은 은닉 너비별 파라미터 수 비교이며 성능 순위 실험과 구분
- 심화는 nn.Module 모델을 같은 가중치의 Sequential과 대조
- 특심화는 출력·gradient 일치와 가중치 메모리 비공유 검증
- 완료 기준은 선택 경로의 층 연결과 순전파 결과 설명

##### 3분 퀴즈 · ANN (PDF p.66)

- Linear weight의 축 순서 확인
- ReLU의 비선형성 역할 확인
- 최종 logits와 확률을 구분하는 기준

**핵심:** Linear와 ReLU를 연결한 층별 shape 및 Parameter를 확인하고, 최종 logits와 예측 클래스를 구분

### 5교시 · 분류 손실과 mini-batch

#### logits와 CrossEntropyLoss

##### Logits·손실함수·Dataset·DataLoader (PDF p.67)

- 모델 출력과 정답으로 손실을 만들고 배치 단위로 자료를 공급하는 흐름

##### logits·확률·클래스는 다른 값이다 (PDF p.68)

- logits는 합이 1일 필요가 없는 클래스별 원시 점수
- softmax 출력은 클래스별 확률
- argmax는 가장 큰 점수의 클래스 인덱스
- 이 수업의 CrossEntropyLoss 입력에는 softmax 전 logits 사용

##### CrossEntropyLoss의 역할 (PDF p.69)

- logits `(batch, class)`와 long 정답 `(batch,)`로 분류 손실 계산
- 학습 목적함수인 loss와 보고 지표인 accuracy 구분

##### nn.CrossEntropyLoss (PDF p.70)

- CrossEntropyLoss 생성과 logits·target을 전달하는 실제 호출 구분
- 기본 reduction=mean은 스칼라 평균 손실 반환
- 이 수업의 클래스 인덱스 target은 long 사용
- class 가중치와 reduction 등은 별도 목적의 선택 인자

#### Dataset과 DataLoader

##### Dataset과 DataLoader의 역할 (PDF p.71)

- TensorDataset은 같은 샘플 위치의 X와 y를 묶는 구조
- DataLoader는 batch 구성과 순회 순서 담당
- Dataset의 샘플 수와 한 batch의 크기 구분

##### TensorDataset과 DataLoader 사용 (PDF p.72)

- TensorDataset에 입력과 정답을 함께 전달
- DataLoader로 정해진 batch 크기만큼 순회
- 마지막 batch는 지정 크기보다 작을 가능성

##### DataLoader (PDF p.73)

- DataLoader의 필수 입력은 dataset
- batch_size와 shuffle로 묶음 크기와 학습 순서 지정
- drop_last가 마지막 작은 batch의 유지 여부 결정
- 초기 실습은 num_workers=0으로 시작하는 실행 조건

##### 전체 데이터를 작은 묶음으로 나누어 학습한다 (PDF p.74)

- 각 mini-batch에서 순전파와 역전파 및 갱신 반복
- batch_size는 메모리 사용과 gradient 변동에 영향
- 교재의 200건·batch32 도식과 실제 train120의 배치 구성을 구분

#### 손실·배치 집계 실습과 확인

##### 실습 05 · 손실함수와 mini-batch (PDF p.75)

- 기본필수는 작은 logits와 long 정답으로 CE 계산
- 응용은 10건을 4·4·2로 공급하고 A09에서 표본 수 가중 평균 계산
- 심화는 마지막 작은 배치를 포함한 전체 손실 집계 대조
- 특심화는 큰 logits의 안정적 CE와 gradient 계약 검증
- 완료 기준은 logits·target의 조건과 선택 경로의 배치 집계 설명

##### 3분 퀴즈 · 손실과 데이터 (PDF p.76)

- CrossEntropyLoss에 softmax를 먼저 적용하지 않는 사용 조건 확인
- 클래스 인덱스 정답의 shape·dtype 확인
- 학습 자료 shuffle의 목적 확인

**핵심:** 분류 logits와 long 정답으로 손실을 계산하고, 마지막 작은 batch를 포함한 표본 수와 손실 집계 의미 확인

### 6교시 · 역전파와 SGD 학습 루프

#### 학습 step의 순서와 준비

##### 순전파·손실·역전파·Optimizer를 반복한다 (PDF p.77)

- 순전파·손실·역전파·Optimizer 갱신을 반복하는 학습 루프

##### 순전파·손실·역전파·Optimizer를 반복한다 (PDF p.78)

- 순전파는 입력층에서 은닉층을 거쳐 출력층으로 진행하는 계산
- 역전파는 출력 쪽에서 입력 쪽으로 기울기를 전달하는 계산
- 앞 페이지의 학습 단계와 신경망 내부의 계산 방향을 연결하는 도식

##### 한 번의 학습 step (PDF p.79)

- 한 step의 순서는 zero_grad → forward → loss → backward → step
- 기울기 초기화·기울기 계산·파라미터 갱신의 서로 다른 역할

##### ANN 학습 루프 · 설정과 준비 (PDF p.80)

- seed·device·데이터·DataLoader·모델·손실함수·Optimizer 준비
- 교재 준비 예제의 모델은 2→8→2 ANN
- SGD에는 모델 파라미터와 수업 학습률 전달

##### ANN 학습 루프 · batch 반복 (PDF p.81)

- 각 batch의 입력·정답을 이동한 뒤 학습 step 반복
- epoch는 자료 순회의 반복 단위
- 마지막 batch loss와 전체 자료의 평균 손실 구분

##### SGD · zero_grad · step (PDF p.82)

- SGD는 파라미터의 gradient를 이용한 값 갱신
- zero_grad는 이전 gradient 초기화
- step은 현재 gradient에 따른 한 번의 갱신
- 학습률의 크기는 변화 속도와 안정성에 영향

#### 평가 모드와 장치·학습곡선

##### model.train()·model.eval()·torch.no_grad() (PDF p.83)

- train·eval은 Dropout·BatchNorm 등 층의 동작 모드 전환
- eval만으로 gradient 기록이 꺼지지는 않음
- 평가는 eval과 no_grad의 역할을 구분해 함께 사용

##### batch를 GPU로 옮기는 위치 (PDF p.84)

- batch의 입력과 정답을 모델과 같은 device로 이동
- CPU에서 결과를 기록할 때 계산 그래프 분리와 CPU 이동 구분

##### 학습곡선 예시 · 매번 감소하는 것은 아니다 (PDF p.85)

- 학습곡선은 전체 추세와 평가 표본 수를 함께 해석
- loss와 accuracy는 서로 다른 지표
- 매 step·epoch 손실 감소를 완료 조건으로 단정하지 않음
- 그림의 예시 곡선과 README의 난이도별 실제 검수 수치 구분

#### 학습 루프 실습과 확인

##### 실습 06 · 순전파·역전파·SGD 학습 루프 (PDF p.86)

- 기본필수는 제공 모델을 CPU full-batch로 학습
- 응용은 mini-batch 갱신 후 train·valid 지표 기록
- 심화는 학습·평가 함수와 online loss의 의미 구분
- 특심화는 평가 전후 가중치·gradient·모드 보존 검증
- 완료 기준은 정확한 학습 순서와 선택 경로의 기록 의미 설명

##### 3분 퀴즈 · 학습 루프 (PDF p.87)

- zero_grad를 생략했을 때의 이전 기울기 누적 확인
- backward는 기울기 계산이며 실제 값 갱신은 step의 역할
- eval과 no_grad의 기능 구분 확인

**핵심:** zero_grad → forward → loss → backward → step을 연결하고, 학습 중 손실·고정 모델 평가·비학습 상태를 구분

### 7교시 · ANN 학습 프로젝트 통합

#### 예측 문제와 프로젝트 구조

##### GPU 동작 점검표·ANN 학습 프로젝트 (PDF p.88)

- 환경 점검에서 데이터·모델 준비와 학습·평가 및 결과 설명까지의 통합

##### 일일 프로젝트 · 2차원 합성 데이터 분류 (PDF p.89)

- 두 수치 특성으로 합성 데이터의 클래스 0·1 예측
- 모델은 Linear(2,8) → ReLU → Linear(8,2)
- 기본필수는 20건 중 train12·valid4 사용이며 test4 보관
- 응용 이상은 200건 중 train120·valid40 사용이며 test40 보관
- 정답 생성 규칙을 직접 예측에 대입하는 방식과 ANN 학습 구분

##### 심화 프로젝트 구조 · 기본필수는 한 파일 (PDF p.90)

- 심화는 환경·모델·학습·전체 실행의 책임을 파일로 분리
- outputs는 실행 결과, reports는 개인 해석 기록
- 기본필수에는 심화용 모듈 구조의 추가 파일 작성 요구 없음

##### 심화 프로젝트 실행 흐름 (PDF p.91)

- device 결정에서 Dataset·Loader·ANN 학습을 거쳐 결과 저장으로 연결
- 입력·모델·손실·Optimizer의 역할을 분리한 뒤 main에서 통합

#### 모델·학습 함수의 연결

##### 심화 참조 · model.py의 ANN 구조 (PDF p.92)

- nn.Module 초기화와 하위 Sequential 등록
- forward의 입력·출력 shape 확인
- CrossEntropyLoss와 연결하는 모델 마지막에는 별도 softmax 미추가

##### 심화 참조 · train.py의 한 epoch 학습 (PDF p.93)

- 한 epoch 안에서 batch별 학습 step 수행
- 각 batch 평균 loss에 실제 표본 수를 곱한 뒤 전체 표본 수로 나누는 집계
- 갱신 중 계산한 online loss와 학습 종료 후 고정 모델 평가 loss의 차이

#### 환경·결과 점검과 프로젝트 실습

##### GPU 동작 점검표와 학습 결과 (PDF p.94)

- GPU·드라이버·PyTorch CUDA 빌드·실제 device의 구분 기록
- 입력·정답 shape와 모델 구조 확인
- 손실 변화와 정확도를 사용 자료의 표본 수와 함께 해석
- CSV·JSON과 실행 방법 및 본인의 학습 흐름 설명 확인

##### 실습 07 · GPU ANN 프로젝트 통합 (PDF p.95)

- 기본필수는 07_project.py의 역전파·갱신과 클래스 선택을 완성
- 응용은 실제 valid 오답만 ID·정답·예측과 함께 저장하며 오답이 없으면 헤더만 생성
- 심화는 모델·학습·main을 나누고 파라미터 상태 저장
- 특심화는 고정 분할과 배치 순서 및 예측 기록의 계약 검증
- 완료 기준은 선택 경로의 결과 재생성과 test 미사용 설명

##### 단계별 결과물 · 기본필수는 기존 파일만 (PDF p.96)

- 기본필수 결과는 환경 기록·학습 이력·최종 지표의 세 파일
- 기본필수 이력은 epoch0부터80까지의 고정 모델 train_loss_eval 기록
- 응용은 고정 모델 평가 손실과 valid 예측·오답 목록 추가
- 심화 이력의 train_loss_online은 학습 중 배치 손실의 표본 수 가중 평균
- README의 실행 방법과 개인 설명을 결과 파일과 함께 확인

**핵심:** 난이도별 데이터·학습 방식·손실 기록을 구분해 결과를 재생성하고, train 학습·valid 확인·test 보관의 경계 유지

### 8교시 · 최종 재현·시연·회고

#### 재실행과 단계별 완료 기준

##### 최종 점검·시연·회고 (PDF p.97)

- 프로그램 재실행과 Tensor·device 및 학습 흐름 설명 중심의 마무리

##### 실습 08 · 최종 검증·시연·회고 (PDF p.98)

- 기본필수는 07번 재실행과 결과 설명이며 별도 테스트·예외처리 작성 없음
- 응용은 README 재현과 배치 가중 손실·실제 오답 수 설명
- 심화는 새 프로세스 모델 복원과 H11·H12의 정상 입력 테스트
- 특심화는 자체 baseline의 80회 연속 학습과 40+40회 재개 비교
- 재개 검증은 동일 CPU 환경·버전·epoch 경계·num_workers=0 범위
- 완료 기준은 선택 경로의 재현 근거와 확인한 한계 기록

##### 형성평가 · 기본필수만으로 100점 (PDF p.99)

- 환경 20점과 Tensor·모델 20점의 구분 기록
- 학습 루프의 순서와 구현 30점
- 결과 해석 15점과 재현·문서화 15점
- 기본필수만으로 공통 100점 충족 가능하며 GPU 미보유나 선택 확장 미완성 자체는 감점 사유 아님

#### 경계·실패 상황의 확장 검증

##### 심화·특심화 확장 · 경계·실패 상황 (PDF p.100)

- CUDA 사용 불가 시 허용된 자동 선택 경로는 CPU 대체
- 특심화의 명시적 cuda 요청은 자동 대체와 다른 실패 정책 적용
- Linear 입력 마지막 차원과 분류 정답의 long dtype 점검
- gradient 초기화 누락과 평가 그래프 생성 누락의 결과 구분
- 경계·실패 상황의 별도 구현은 기본필수 완료 조건에 추가하지 않음

**핵심:** 선택한 난이도의 실행 결과와 학습 원리를 설명하고, 확장 검증의 범위 및 장치·버전 간 재현 한계를 명시

### 전체 정리와 참고자료

#### 학습 정리와 다음 수업

##### 오늘의 핵심 정리 (PDF p.101)

- GPU 존재와 CUDA 실행 가능 여부를 분리하는 환경 판단
- Tensor의 shape·dtype·device·requires_grad 확인
- 순전파·손실·역전파·갱신의 반복 구조
- Linear와 activation이 표현과 분류 규칙을 학습하는 ANN의 역할

##### 다음 수업 · 학습을 안정화하고 과적합을 진단한다 (PDF p.102)

- 다음 수업은 Optimizer·학습률과 Batch·Epoch 비교
- Dropout·BatchNorm·Early Stopping을 통한 과적합 제어
- train·valid 손실 패턴으로 학습 문제를 진단하는 흐름

#### 공식 참고자료

##### 공식 참고자료 · 설치와 CUDA (PDF p.103)

- 플랫폼별 설치와 CUDA 의미 확인을 위한 PyTorch 공식 문서
- GPU 상태 조회를 위한 NVIDIA nvidia-smi 공식 문서

##### 공식 참고자료 · Tensor·Autograd·신경망 (PDF p.104)

- Tensor 생성과 Autograd의 공식 API 확인 경로
- 신경망 층·손실함수·SGD·DataLoader의 공식 API 확인 경로

