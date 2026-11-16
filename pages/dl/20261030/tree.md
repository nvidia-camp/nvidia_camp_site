# Day10 강의 구조와 핵심 설명

교시 설명과 중간 학습 주제는 수업 흐름에 맞춰 편집한 표현. 마지막 단계는 원문 슬라이드 제목이며 페이지는 현재 PDF 뷰어 기준. 도입·마무리·참고자료는 교시 밖에 별도 배치.

기본필수만으로 공통 평가 충족. 응용·심화·특심화는 선택한 단계의 확장 범위. 교재의 설명용 수치와 배포 실습의 실제 실행 결과 구분.

## 강의 목차

```text
도입 · 전체 학습 지도와 실험 원칙
├─ 수업 소개와 업무 적용
│  ├─ 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)
│  ├─ 현업에서 오늘의 기술이 필요한 순간 (PDF p.2)
│  ├─ 전체 지도에서 오늘의 위치 (PDF p.3)
│  ├─ 학습과 검증이 함께 있어야 하는 이유 (PDF p.4)
│  ├─ 한 번의 학습 실행 안의 Epoch와 Batch (PDF p.5)
│  ├─ 한 Batch에서 가중치를 바꾸는 부분 (PDF p.6)
│  ├─ 모델 내부의 Dropout과 BatchNorm (PDF p.7)
│  ├─ 학습곡선에서 과적합의 징후 찾기 (PDF p.8)
│  ├─ Early Stopping과 가장 좋았던 모델 (PDF p.9)
│  ├─ 현업에서는 관찰한 현상으로 다음 실험을 정한다 (PDF p.10)
│  └─ 오늘 완성할 결과물: 학습 안정화 실험표 (PDF p.11)
└─ 선행 학습 복습과 수업 운영
   ├─ 어제 우리가 배운 것 (PDF p.12)
   ├─ 3분 확인 퀴즈 · Day 9 복습 (PDF p.13)
   ├─ 오늘의 목표와 8교시 운영 (PDF p.14)
   ├─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)
   └─ 교재 예시와 단계별 실습 조건을 구분한다 (PDF p.16)

1교시 · Optimizer의 갱신 규칙과 비교
├─ 기울기와 SGD·Momentum
│  ├─ Optimizer는 gradient를 Parameter 갱신으로 바꾼다 (PDF p.17)
│  ├─ Gradient Descent와 Optimizer의 역할 (PDF p.18)
│  ├─ torch.optim.SGD() (PDF p.19)
│  └─ Momentum은 이전 이동 방향을 함께 사용한다 (PDF p.20)
├─ AdamW와 통제된 Optimizer 비교
│  ├─ Adam과 AdamW의 직관 (PDF p.21)
│  ├─ torch.optim.AdamW() (PDF p.22)
│  ├─ SGD와 AdamW를 비교할 때 보는 관점 (PDF p.23)
│  ├─ Optimizer만 바꾸어 같은 학습 루프를 사용한다 (PDF p.24)
│  └─ Optimizer별 validation loss의 흐름 (PDF p.25)
└─ 실습 01의 단계별 비교
   └─ 실습 01 · Optimizer 비교와 갱신 경로 (PDF p.26)

2교시 · 학습률 선택과 Scheduler
├─ 학습률 후보와 학습곡선 진단
│  ├─ 학습률은 한 번의 갱신 크기를 정한다 (PDF p.27)
│  ├─ 학습률에 따른 이동 모습 (PDF p.28)
│  ├─ 학습률 후보를 같은 조건에서 반복한다 (PDF p.29)
│  ├─ 학습률별 validation loss (PDF p.30)
│  └─ 학습률 문제를 의심할 수 있는 신호 (PDF p.31)
├─ ReduceLROnPlateau의 감시 지표와 호출 순서
│  ├─ Scheduler는 학습 중 learning rate를 바꾼다 (PDF p.32)
│  ├─ ReduceLROnPlateau() (PDF p.33)
│  ├─ Validation 이후 Scheduler를 호출한다 (PDF p.34)
│  └─ Scheduler 예시 기록 (PDF p.35)
└─ 실습 02와 개념 확인
   ├─ 실습 02 · 학습률과 Scheduler 실험 (PDF p.36)
   └─ 3분 퀴즈 · Optimizer와 학습률 (PDF p.37)

3교시 · Batch·Iteration·Epoch와 데이터 순회
├─ 데이터 사용 단위와 DataLoader
│  ├─ Dataset을 Batch로 나누고 Epoch 동안 모두 순회한다 (PDF p.38)
│  ├─ Batch·Iteration·Epoch를 구분한다 (PDF p.39)
│  └─ DataLoader() (PDF p.40)
├─ Batch 크기와 순회 정책
│  ├─ Batch size가 바뀌면 gradient와 자원 사용이 달라진다 (PDF p.41)
│  ├─ Batch size만 바꾸어 같은 모델을 비교한다 (PDF p.42)
│  ├─ Batch size 실험표 (PDF p.43)
│  ├─ shuffle과 drop_last를 언제 쓰는가 (PDF p.44)
│  └─ optimizer.zero_grad()와 optimizer.step() (PDF p.45)
└─ 실습 03과 Batch 경계 확인
   ├─ 실습 03 · Batch·Epoch·Iteration 기록 (PDF p.46)
   └─ 3분 퀴즈 · Batch와 Epoch (PDF p.47)

4교시 · 과적합과 학습곡선 진단
├─ 과소적합과 과적합의 관찰 근거
│  ├─ 과적합은 train과 새로운 데이터의 차이에서 보인다 (PDF p.48)
│  ├─ Underfitting · 적절한 학습 · Overfitting (PDF p.49)
│  ├─ 작은 train 자료에서 나타난 과적합 곡선 (PDF p.50)
│  └─ 학습곡선 패턴을 구분한다 (PDF p.51)
├─ 데이터 분리와 재현 가능한 기록
│  ├─ 딥러닝에서도 valid를 선택에 사용한다 (PDF p.52)
│  ├─ Seed를 고정해도 완전히 같은 결과가 아닐 수 있다 (PDF p.53)
│  └─ Epoch별 train·valid 기록을 남긴다 (PDF p.54)
└─ 실습 04와 진단 확인
   ├─ 실습 04 · 학습곡선 진단 (PDF p.55)
   └─ 3분 퀴즈 · 과적합과 학습곡선 (PDF p.56)

5교시 · Dropout과 train·eval 모드
├─ 규제와 Dropout의 확률 동작
│  ├─ Regularization은 train 적합과 일반화 사이를 조절한다 (PDF p.57)
│  ├─ Dropout은 학습 시 일부 연결을 임시로 끈다 (PDF p.58)
│  └─ nn.Dropout() (PDF p.59)
├─ 모드 전환과 ANN 적용
│  ├─ train()과 eval()은 같은 모델의 동작 모드를 바꾼다 (PDF p.60)
│  ├─ model.train() · model.eval() (PDF p.61)
│  ├─ Dropout이 포함된 ANN (PDF p.62)
│  ├─ Dropout·BatchNorm·Weight Decay 실험 요약 (PDF p.63)
│  └─ Dropout에서 자주 발생하는 오류 (PDF p.64)
└─ 실습 05와 모드 확인
   ├─ 실습 05 · Dropout과 train/eval 모드 (PDF p.65)
   └─ 3분 퀴즈 · Dropout과 모드 (PDF p.66)

6교시 · BatchNorm과 Weight Decay
├─ BatchNorm의 통계와 배치 위치
│  ├─ BatchNorm은 Batch 통계로 activation을 정규화한다 (PDF p.67)
│  ├─ nn.BatchNorm1d() (PDF p.68)
│  ├─ BatchNorm의 training과 evaluation 차이 (PDF p.69)
│  ├─ ANN에서 BatchNorm을 배치하는 위치 (PDF p.70)
│  └─ BatchNorm을 포함한 ANN (PDF p.71)
├─ 가중치 감쇠와 Parameter 그룹
│  ├─ Weight Decay는 큰 가중치를 억제한다 (PDF p.72)
│  ├─ Parameter group으로 weight decay를 다르게 줄 수 있다 (PDF p.73)
│  └─ Dropout·BatchNorm·Weight Decay를 구분한다 (PDF p.74)
└─ 실습 06과 규제 구분
   ├─ 실습 06 · BatchNorm과 Weight Decay (PDF p.75)
   └─ 3분 퀴즈 · BatchNorm과 규제 (PDF p.76)

7교시 · Early Stopping과 학습 안정화 통합
├─ 중단 판단과 best 상태 복원
│  ├─ Early Stopping은 valid 개선이 멈추면 학습을 끝낸다 (PDF p.77)
│  ├─ Early Stopping의 핵심 변수 (PDF p.78)
│  ├─ 간단한 Early Stopping 로직 (PDF p.79)
│  ├─ Scheduler와 Early Stopping을 함께 사용할 때 (PDF p.80)
│  └─ Scheduler + Early Stopping 예시 (PDF p.81)
├─ 오류 가설과 통합 프로젝트 설계
│  ├─ 오류 패턴별 우선 처방 (PDF p.82)
│  ├─ 일일 프로젝트 · 학습 안정화 실험표 (PDF p.83)
│  └─ 심화 참고 구조 · 기본필수에는 한 파일만 요구한다 (PDF p.84)
└─ 실습 07의 단계별 통합
   └─ 실습 07 · 학습 안정화 프로젝트 통합 (PDF p.85)

8교시 · 실험표 검증과 오류 처방·재현
├─ 실험 결과 해석과 단계별 산출물
│  ├─ 학습곡선을 보고 먼저 질문할 것 (PDF p.86)
│  ├─ 오류 패턴별 처방 실습 (PDF p.87)
│  └─ 단계별 제출물 · 기본필수는 CSV와 결과 설명 (PDF p.88)
└─ 실습 08의 재실행과 상태 검증
   ├─ 실습 08 · 최종 검증·오류 처방·회고 (PDF p.89)
   ├─ 형성평가 기준 · 100점 (PDF p.90)
   ├─ 정상·경계·실패 상황을 구분한다 (PDF p.91)
   └─ 마무리 3분 확인 퀴즈 (PDF p.92)

마무리 · 전체 정리와 다음 수업
└─ 학습 안정화 원칙과 후속 학습
   ├─ 오늘의 핵심 정리 (PDF p.93)
   └─ 다음 수업 · CNN 합성곱과 이미지 분류 (PDF p.94)

참고자료 · 공식 API와 구현 범위
└─ 함수별 확인 자료
   ├─ 공식 참고자료 · Optimizer와 DataLoader (PDF p.95)
   └─ 공식 참고자료 · Regularization과 Module mode (PDF p.96)

```

## 핵심 설명

### 도입 · 전체 학습 지도와 실험 원칙

#### 수업 소개와 업무 적용

##### 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)

- Day 10의 Optimizer·학습률·Batch·Epoch와 과적합 제어 범위를 소개하는 표지
- 부제는 ‘Day 10 · Optimizer·학습률·Batch·Epoch → 과적합 → Dropout·BatchNorm·Early Stopping’

##### 현업에서 오늘의 기술이 필요한 순간 (PDF p.2)

- 새 업무 요청의 처리 결과를 예측하는 가상 사례로 학습 조건 선택의 목적 확인
- 시간과 메모리 제약 안에서 별도 검증 자료로 사용할 모델 선택

##### 전체 지도에서 오늘의 위치 (PDF p.3)

- 업무 목적에서 모델 개발을 거쳐 학습·검증 실험과 Batch 내부 계산으로 이어지는 위치 확인

##### 학습과 검증이 함께 있어야 하는 이유 (PDF p.4)

- train은 가중치 학습용 자료
- valid는 설정과 중단 시점 선택용 자료
- test는 최종 평가를 위해 보관하며 오늘은 사용 제외

##### 한 번의 학습 실행 안의 Epoch와 Batch (PDF p.5)

- Epoch는 train 전체를 한 번 순회하는 단위
- Batch size는 한 번에 처리하는 표본 수
- Epoch 말에 같은 모델의 train·valid 결과 기록

##### 한 Batch에서 가중치를 바꾸는 부분 (PDF p.6)

- zero_grad → forward → loss → backward → step 순서로 Batch 처리
- backward는 기울기 계산 단계
- step은 Optimizer 규칙과 학습률에 따른 가중치 갱신 단계

##### 모델 내부의 Dropout과 BatchNorm (PDF p.7)

- BatchNorm은 forward 중간값을 배치 통계로 정규화
- Dropout은 일부 중간값을 무작위로 0으로 만들어 특정 특징에 대한 의존 완화
- 기본 설정의 eval 모드에서 BatchNorm은 저장 통계 사용
- eval 모드에서 Dropout 비활성화

##### 학습곡선에서 과적합의 징후 찾기 (PDF p.8)

- 같은 Epoch 말의 eval 조건에서 train·valid loss 비교
- train 개선과 valid 악화가 함께 나타나면 과적합 가능성 점검
- 그림은 개념 설명용 곡선이며 실제 실험 측정값과 구분

##### Early Stopping과 가장 좋았던 모델 (PDF p.9)

- 개선 없는 평가가 patience에 도달하면 학습 중단
- 중단 시점과 best 시점은 서로 다른 기록
- best 상태 저장·복원은 중단 판단과 별도로 구현

##### 현업에서는 관찰한 현상으로 다음 실험을 정한다 (PDF p.10)

- 느린 감소와 큰 진동 등 관찰한 현상에서 원인 가설 설정
- 같은 split·seed·평가 기준에서 조건 하나씩 변경
- 변경 조건과 실측 결과를 다음 실험의 근거로 기록

##### 오늘 완성할 결과물: 학습 안정화 실험표 (PDF p.11)

- 기준선과 학습률·Dropout 실험의 best valid loss 및 best epoch 비교
- valid accuracy는 선택한 best epoch의 값으로 기록
- 기본필수 산출물은 history CSV와 비교표 및 학습곡선과 설명

#### 선행 학습 복습과 수업 운영

##### 어제 우리가 배운 것 (PDF p.12)

- Tensor와 device 및 Autograd를 이용한 ANN 학습 루프 복습
- 같은 학습 루프가 잘 학습되는 조건을 실험하는 방향으로 확장

##### 3분 확인 퀴즈 · Day 9 복습 (PDF p.13)

- step 이전의 기울기 계산 여부 확인
- eval 모드 전환과 기울기 추적 비활성화의 차이 확인
- 장치가 달라도 유지되는 데이터 분리 원칙 확인

##### 오늘의 목표와 8교시 운영 (PDF p.14)

- Optimizer에서 시작해 학습률·Batch·과적합·규제를 거쳐 통합 실험과 검증으로 이어지는 8교시 운영
- 1교시는 설명·시연 30분과 실습·리뷰 20분
- 2~7교시는 설명·시연과 실습·리뷰를 각각 25분 배정
- 8교시는 설명·시연 20분과 실습·리뷰 30분 배정

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)

- 오늘의 범위는 ANN 학습 조건과 일반화 진단 및 안정화 실험
- 다음 수업의 CNN 이미지 분류에도 같은 학습·평가 원칙 적용

##### 교재 예시와 단계별 실습 조건을 구분한다 (PDF p.16)

- 기본필수는 정상 데이터 20건을 train 12건·valid 4건·test 4건으로 구분
- 응용 이상은 400건을 train 240건·valid 80건·test 80건으로 구분
- 일부 특심화 실험의 train 60건 부분집합은 해당 README 기준 적용
- test는 오늘의 학습·선택·추론에서 사용 제외
- 교재의 설명 예시 수치와 배포 CSV의 실행 결과 구분

### 1교시 · Optimizer의 갱신 규칙과 비교

#### 기울기와 SGD·Momentum

##### Optimizer는 gradient를 Parameter 갱신으로 바꾼다 (PDF p.17)

- 기울기를 Parameter 갱신으로 변환하는 Optimizer의 역할
- 갱신 경로는 학습률과 momentum 및 weight decay 설정에 따라 변화

##### Gradient Descent와 Optimizer의 역할 (PDF p.18)

- Gradient Descent는 loss 증가 방향의 반대쪽으로 Parameter 이동
- Optimizer는 기울기의 누적·보정·적용 규칙 결정
- Optimizer 교체만으로 잘못된 분할이나 loss 구현 해결 불가

##### torch.optim.SGD() (PDF p.19)

- `params`는 학습할 Parameter iterable이며 보통 `model.parameters()` 전달
- `lr`은 갱신 크기 조절
- `momentum`은 이전 이동 방향 누적
- SGD의 `weight_decay`는 L2 형태의 항을 갱신에 반영

##### Momentum은 이전 이동 방향을 함께 사용한다 (PDF p.20)

- 현재 기울기와 이전 이동량을 결합해 새 갱신 방향 결정
- 일관된 방향의 이동 누적과 진동 완화 가능성 확인

#### AdamW와 통제된 Optimizer 비교

##### Adam과 AdamW의 직관 (PDF p.21)

- Adam은 기울기의 1차·2차 이동평균으로 Parameter별 갱신 크기 조절
- AdamW는 적응적 갱신과 가중치 감쇠를 분리
- 빠른 초기 수렴만으로 일반화 성능 우위 판단 불가

##### torch.optim.AdamW() (PDF p.22)

- `betas`는 두 이동평균의 계수
- `eps`는 분모의 수치 안정성을 위한 값
- AdamW의 기본 `weight_decay=0.01`이므로 감쇠 제외 비교에서는 0 명시
- Optimizer의 `state_dict()`에는 갱신에 필요한 내부 상태 포함

##### SGD와 AdamW를 비교할 때 보는 관점 (PDF p.23)

- 같은 데이터 분할과 모델 및 seed·epoch에서 갱신 규칙 비교
- 같은 lr이 두 알고리즘 각각의 최적 학습률이라는 의미는 아님
- valid loss와 accuracy를 함께 확인

##### Optimizer만 바꾸어 같은 학습 루프를 사용한다 (PDF p.24)

- Optimizer 객체를 교체해도 zero_grad부터 step까지의 학습 순서는 유지
- 슬라이드 예시는 lr과 감쇠 설정도 달라 갱신 규칙만의 효과로 해석 불가
- 실제 통제 비교는 각 단계 README의 고정 조건 적용

##### Optimizer별 validation loss의 흐름 (PDF p.25)

- 초기 수렴 속도와 후반 변동을 곡선 전체에서 비교
- 설명용 40 epochs 그래프를 실제 배포 실습의 정답 곡선으로 사용하지 않음

#### 실습 01의 단계별 비교

##### 실습 01 · Optimizer 비교와 갱신 경로 (PDF p.26)

- 기본필수는 SGD와 AdamW를 같은 lr·seed·모델·20 epochs 및 양쪽 weight_decay 0으로 비교
- 응용은 SGD의 momentum 0과 0.9만 변경
- 심화는 AdamW의 weight_decay 0과 0.01에 따른 train_eval·valid loss 비교
- 특심화는 같은 seed 3개로 초기화와 배치 순서를 맞춘 대응 실험 수행
- 비교표와 고정·변경 조건 및 결과의 한계 설명으로 완료 확인
- 특심화는 원시 결과와 평균·표본 표준편차를 함께 기록

**핵심:** Optimizer의 효과는 다른 학습 조건을 통제한 valid 기록으로 판단하며 한 번의 결과를 보편적 우열로 확대하지 않음

### 2교시 · 학습률 선택과 Scheduler

#### 학습률 후보와 학습곡선 진단

##### 학습률은 한 번의 갱신 크기를 정한다 (PDF p.27)

- 너무 작은 lr은 제한된 epoch 안에서 학습 부족 가능
- 너무 큰 lr은 진동이나 발산 가능
- 학습률의 적절성은 Optimizer·Batch size·모델·정규화 조건에 따라 변화

##### 학습률에 따른 이동 모습 (PDF p.28)

- 작은 이동과 안정적 접근 및 최적점 통과의 차이 확인
- 학습률은 후보 범위를 정하고 학습곡선으로 선택하는 하이퍼파라미터

##### 학습률 후보를 같은 조건에서 반복한다 (PDF p.29)

- lr 후보마다 seed를 재설정하고 모델과 Optimizer를 새로 생성
- split·모델·epoch를 고정하고 lr만 변경
- 최소 valid loss와 곡선을 기록하며 test는 선택에 사용 제외

##### 학습률별 validation loss (PDF p.30)

- 초기 감소 속도와 후반 안정성을 전체 validation loss 곡선에서 확인
- 최종 한 점만으로 학습률 적절성 판단 불가

##### 학습률 문제를 의심할 수 있는 신호 (PDF p.31)

- NaN이나 매우 큰 loss는 lr과 입력 스케일 및 loss 구현 점검 근거
- train loss 정체는 작은 lr 외에 gradient 단절과 Parameter 등록 여부 점검 근거
- 큰 진동은 lr·Batch 크기·데이터 이상을 구분하는 관찰 근거
- 초반 개선 뒤 정체하면 Scheduler나 Early Stopping 검토

#### ReduceLROnPlateau의 감시 지표와 호출 순서

##### Scheduler는 학습 중 learning rate를 바꾼다 (PDF p.32)

- Optimizer는 Parameter 갱신 담당
- Scheduler는 Optimizer가 사용할 lr 조정 담당

##### ReduceLROnPlateau() (PDF p.33)

- `optimizer`는 Scheduler가 감쌀 객체
- loss 감소 감시는 `mode="min"` 사용
- accuracy 증가 감시는 `mode="max"` 사용
- `factor`는 감소 배수이며 `patience`와 `threshold`로 정체 판단
- `scheduler.step(metric)`은 validation 이후 호출

##### Validation 이후 Scheduler를 호출한다 (PDF p.34)

- train epoch 수행 후 valid loss 계산
- 현재 valid loss를 `scheduler.step(valid_loss)`에 전달
- 호출 뒤 `optimizer.param_groups`에서 다음 학습에 적용할 lr 확인

##### Scheduler 예시 기록 (PDF p.35)

- 정체 후 factor에 따른 lr 감소를 설명하는 예시 기록
- 실제 감소 epoch는 감시값과 patience 및 threshold에 따라 결정
- ReduceLROnPlateau에 감시 지표 없이 `step()`만 호출하는 사용 제외

#### 실습 02와 개념 확인

##### 실습 02 · 학습률과 Scheduler 실험 (PDF p.36)

- 기본필수는 lr 0.001과 0.01의 첫 5개 loss와 마지막 loss 비교
- 응용은 lr 0.001·0.01·0.1을 같은 조건에서 비교
- 심화는 Plateau를 연결하고 실제 lr 변경 epoch를 표로 기록
- 특심화는 Plateau에 metric을 전달하고 Cosine에는 metric 없이 step 호출
- 특심화는 이번 epoch의 `lr_used`와 다음 epoch의 `lr_next`를 분리
- 곡선과 lr 이력 및 호출 순서 설명으로 완료 확인

##### 3분 퀴즈 · Optimizer와 학습률 (PDF p.37)

- Optimizer 비교의 고정 조건 확인
- Plateau에 전달할 validation metric 확인
- 큰 학습률의 진동·발산 징후와 다른 원인 가능성 확인

**핵심:** 학습률은 곡선의 감소 속도와 안정성으로 비교하며 Scheduler 기록은 적용 시점과 호출 방식까지 확인

### 3교시 · Batch·Iteration·Epoch와 데이터 순회

#### 데이터 사용 단위와 DataLoader

##### Dataset을 Batch로 나누고 Epoch 동안 모두 순회한다 (PDF p.38)

- train 240건을 batch 32로 나누면 마지막 배치는 16건
- 일반적인 실습 루프에서 Batch 한 번의 갱신이 한 Iteration
- train 전체 한 번의 순회가 한 Epoch

##### Batch·Iteration·Epoch를 구분한다 (PDF p.39)

- Batch size는 한 번의 forward·backward에 사용하는 표본 수
- `drop_last=False`에서 240건과 batch 32는 epoch당 8 iterations
- 기울기 누적 확장에서는 micro-batch 횟수와 step 횟수 구분

##### DataLoader() (PDF p.40)

- `dataset`은 DataLoader의 필수 입력
- `batch_size`와 `shuffle`로 묶음 크기와 순서 설정
- `drop_last`는 마지막 불완전 배치 제외 여부 결정
- `sampler`와 `shuffle`의 충돌 조건 확인
- Windows 다중 프로세스 로딩은 시작 방식 확인

#### Batch 크기와 순회 정책

##### Batch size가 바뀌면 gradient와 자원 사용이 달라진다 (PDF p.41)

- 작은 Batch는 기울기 변동이 커질 수 있으나 메모리 부담 감소
- 큰 Batch는 epoch당 iteration 수가 줄지만 step당 계산량과 메모리 사용 증가
- 크기 선택은 학습곡선과 자원 사용의 절충

##### Batch size만 바꾸어 같은 모델을 비교한다 (PDF p.42)

- 같은 split·모델·Optimizer·lr·epoch에서 batch_size만 변경
- 후보마다 seed와 shuffle Generator를 재설정
- 동일 epoch 비교는 동일 optimizer 갱신 횟수 비교와 구분

##### Batch size 실험표 (PDF p.43)

- Batch별 iteration 수와 최소 valid loss 및 마지막 accuracy를 함께 해석
- 표의 수치는 기존 설명 예시이며 이번 실습의 실측값으로 대체 불가

##### shuffle과 drop_last를 언제 쓰는가 (PDF p.44)

- train의 `shuffle=True`는 epoch마다 데이터 순서를 섞는 설정
- validation은 보통 `shuffle=False`로 ID와 예측 대응 순서 유지
- `drop_last=True` 적용 시 해당 epoch에서 일부 train 표본 제외

##### optimizer.zero_grad()와 optimizer.step() (PDF p.45)

- `zero_grad()`는 이전 iteration의 기울기 제거
- `set_to_none=True`의 None과 0 Tensor는 일부 동작에서 차이
- `step()`은 현재 `.grad`와 내부 상태로 Parameter 갱신
- 기울기 누적에서는 zero_grad 위치를 누적 묶음에 맞춰 조정

#### 실습 03과 Batch 경계 확인

##### 실습 03 · Batch·Epoch·Iteration 기록 (PDF p.46)

- 기본필수는 20건을 batch 6으로 순회해 각 shape와 총 iteration 수 출력
- 응용은 train 240건에서 batch 8·32의 iteration 수와 마지막 배치 크기 기록
- 심화는 batch 8·32·240의 loss와 시간 및 total_steps 비교
- 특심화는 큰 batch 64와 16×4 누적의 gradient·갱신 대조
- 불균등 micro-batch 누적은 실제 표본 수를 분모로 사용
- 마지막 작은 누적 묶음도 보존하며 BN·Dropout 포함 모델의 완전 등가를 가정하지 않음

##### 3분 퀴즈 · Batch와 Epoch (PDF p.47)

- 나누어떨어지지 않는 표본 수의 iteration 계산 확인
- drop_last가 표본 사용량에 미치는 영향 확인
- 평가 시 ID 순서를 유지하는 이유 확인

**핵심:** Batch 크기를 비교할 때는 표본 수와 마지막 배치뿐 아니라 실제 갱신 횟수와 자원 사용을 함께 판단

### 4교시 · 과적합과 학습곡선 진단

#### 과소적합과 과적합의 관찰 근거

##### 과적합은 train과 새로운 데이터의 차이에서 보인다 (PDF p.48)

- train loss 감소 중 valid loss가 다시 증가하면 일반화 악화 가능성
- 모델 크기와 epoch 및 데이터 양·노이즈·규제가 과적합에 영향
- 단일 최종 점수보다 epoch별 train·valid 변화 확인

##### Underfitting · 적절한 학습 · Overfitting (PDF p.49)

- train도 충분히 개선되지 않으면 Underfitting 가능성
- train·valid 동반 개선은 적절한 학습의 관찰 근거
- train만 개선되고 valid가 악화하면 Overfitting 가능성
- 모델 복잡도 증가와 장기 학습은 구분되는 원인 후보

##### 작은 train 자료에서 나타난 과적합 곡선 (PDF p.50)

- 작은 train 자료의 예시에서 valid 최저점 이후 train만 계속 개선
- 마지막 epoch와 best epoch를 구분하는 근거 확인
- 설명용 곡선의 약 13 epoch를 배포 데이터의 정답으로 사용하지 않음

##### 학습곡선 패턴을 구분한다 (PDF p.51)

- 둘 다 높은 loss는 모델·lr·학습시간 점검 근거
- train 감소와 valid 증가는 규제·중단 시점·데이터 점검 근거
- 동반 진동은 lr·Batch·입력 스케일 점검 근거
- NaN은 입력·loss·gradient norm 점검 근거

#### 데이터 분리와 재현 가능한 기록

##### 딥러닝에서도 valid를 선택에 사용한다 (PDF p.52)

- train은 gradient 계산과 갱신에 사용
- valid는 epoch와 모델 구조 및 규제 등 선택에 사용
- test는 모든 선택 뒤 최종 평가용이며 오늘은 보관
- 같은 valid를 반복 선택과 보고에 사용하면 선택 편향 잔존

##### Seed를 고정해도 완전히 같은 결과가 아닐 수 있다 (PDF p.53)

- `torch.manual_seed()`는 PyTorch 난수 생성 순서 설정
- shuffle Generator와 worker seed도 재현성에 영향
- GPU 연산과 병렬 처리로 seed만 같아도 완전 동일 결과 보장 불가
- seed·버전·device·batch size·epoch·Optimizer 설정 기록

##### Epoch별 train·valid 기록을 남긴다 (PDF p.54)

- epoch별 loss와 accuracy를 구분해 history 저장
- 곡선 비교용 train_loss_eval과 valid_loss는 epoch 종료 후 같은 eval 모델로 측정
- 학습 도중의 train_loss_step을 평가 모드 train loss와 혼용하지 않음
- CSV와 그래프로 best epoch와 마지막 epoch 비교

#### 실습 04와 진단 확인

##### 실습 04 · 학습곡선 진단 (PDF p.55)

- 기본필수는 제공된 20개 loss로 곡선을 그리고 최소 valid loss의 epoch 탐색
- 리스트의 0 기반 위치와 출력 epoch의 1 기반 번호 구분
- 응용은 모델 폭 8·64의 train·valid 차이 설명
- 심화는 폭 64 모델의 Dropout 0·0.3 비교
- 실측 곡선에 과적합이 없으면 과적합으로 단정하지 않음
- 특심화는 seed 5개의 개별 best와 평균 곡선 최저점을 구분
- seed 표준편차 음영을 모집단 신뢰구간으로 해석하지 않음

##### 3분 퀴즈 · 과적합과 학습곡선 (PDF p.56)

- train·valid 변화로 과적합 가능성 확인
- 중단 판단에 사용할 validation metric 확인
- 마지막 모델과 best 모델이 달라지는 이유 확인

**핵심:** 과적합은 모델 크기나 마지막 점수만으로 단정하지 않고 같은 eval 조건의 train·valid 곡선으로 판단

### 5교시 · Dropout과 train·eval 모드

#### 규제와 Dropout의 확률 동작

##### Regularization은 train 적합과 일반화 사이를 조절한다 (PDF p.57)

- Dropout은 activation의 무작위 제거로 특정 특징 의존 완화
- Weight Decay는 Parameter 크기 억제
- Early Stopping은 validation 기반 학습 중단과 best 복원
- BatchNorm은 중간 activation 정규화가 주목적이며 규제 효과와 구분

##### Dropout은 학습 시 일부 연결을 임시로 끈다 (PDF p.58)

- train 모드에서 무작위 mask를 적용하고 남은 값의 scale 보정
- eval 모드에서는 입력 그대로 전달

##### nn.Dropout() (PDF p.59)

- Dropout은 입력 원소마다 확률 p로 0을 적용
- 매번 정확히 p 비율의 원소를 제거한다는 의미는 아님
- 입력과 출력 shape 유지
- `inplace`는 입력의 직접 수정 여부 결정

#### 모드 전환과 ANN 적용

##### train()과 eval()은 같은 모델의 동작 모드를 바꾼다 (PDF p.60)

- train 모드는 Dropout을 활성화하고 BatchNorm이 현재 batch 통계 사용
- 기본 설정의 eval 모드는 Dropout을 끄고 BatchNorm이 running 통계 사용
- eval과 no_grad 또는 inference_mode를 함께 사용해 평가

##### model.train() · model.eval() (PDF p.61)

- `model.eval()`은 `model.train(False)`와 같은 모드 설정
- train과 eval은 self 반환
- eval 호출만으로 gradient 기록 중지 불가

##### Dropout이 포함된 ANN (PDF p.62)

- 은닉층 ReLU 뒤 Dropout을 배치한 ANN 구조 확인
- 모델의 모드 전환에 따라 내부 Dropout도 전환
- 너무 큰 p는 작은 데이터에서 Underfitting 가능성

##### Dropout·BatchNorm·Weight Decay 실험 요약 (PDF p.63)

- best epoch의 최소 valid loss와 마지막 valid loss를 구분해 기법 비교
- 마지막 accuracy를 best epoch의 accuracy로 보고하지 않음
- 기존 설명 예시는 실제 배포 파일의 성능 목표와 구분

##### Dropout에서 자주 발생하는 오류 (PDF p.64)

- eval 누락은 평가 출력 변동의 원인 후보
- 과도한 Dropout은 학습 부족의 원인 후보
- Dropout 외 조건을 동시에 바꾸면 효과 분리 불가

#### 실습 05와 모드 확인

##### 실습 05 · Dropout과 train/eval 모드 (PDF p.65)

- 기본필수는 같은 입력을 train·eval에서 각각 3번 통과시켜 출력 비교
- 응용은 p 0·0.3의 best loss와 best epoch 기록
- 심화는 p 0.1·0.3·0.5의 초기 감소와 마지막 train_eval loss 비교
- 특심화는 Dropout만 켠 반복 확률 예측의 평균·분산 계산
- 특심화는 BN 통계와 기존 gradient 및 하위 모드·난수 상태 보존
- 예측 변동을 보정된 위험도로 단정하지 않음
- 선택 단계의 출력과 모드 차이 및 한계 설명으로 완료 확인

##### 3분 퀴즈 · Dropout과 모드 (PDF p.66)

- 평가 모드 Dropout의 identity 동작 확인
- eval과 no_grad의 역할 차이 확인
- train 출력 변동과 무작위 mask의 관계 확인

**핵심:** Dropout의 적용 효과는 평가 모드에서 비교하며 모드 전환과 기울기 추적 비활성화를 별도로 처리

### 6교시 · BatchNorm과 Weight Decay

#### BatchNorm의 통계와 배치 위치

##### BatchNorm은 Batch 통계로 activation을 정규화한다 (PDF p.67)

- batch activation의 평균·분산으로 정규화한 뒤 학습 가능한 scale·shift 적용
- train 모드에서 running_mean과 running_var 갱신

##### nn.BatchNorm1d() (PDF p.68)

- 2차원 입력 `(N, C)`에서 num_features는 C와 일치
- `eps`는 정규화 분모의 수치 안정성 조절
- BatchNorm의 momentum은 running 통계 갱신 계수이며 Optimizer momentum과 구분
- `affine=True`는 학습 가능한 scale·bias 사용
- running 통계 사용 여부는 `track_running_stats` 설정과 함께 해석

##### BatchNorm의 training과 evaluation 차이 (PDF p.69)

- 기본 설정의 train에서는 현재 batch 통계를 사용하며 running 통계 갱신
- 기본 설정의 eval에서는 running 통계를 사용하며 통계 갱신 없음
- 작은 batch의 통계 변동을 batch size와 함께 해석

##### ANN에서 BatchNorm을 배치하는 위치 (PDF p.70)

- 대표 배치 순서는 Linear → BatchNorm1d → ReLU
- num_features는 앞 Linear의 out_features와 일치
- 2차원 ANN의 batch_size 1 학습에서는 BatchNorm 통계 계산 문제 가능
- Dropout과 함께 사용하면 목적과 순서를 기록해 비교

##### BatchNorm을 포함한 ANN (PDF p.71)

- Linear 출력 `(batch, 64)`와 BatchNorm1d(64)의 입력 연결 확인
- BatchNorm의 학습 가능한 파라미터와 running buffer를 함께 모델 상태로 보관

#### 가중치 감쇠와 Parameter 그룹

##### Weight Decay는 큰 가중치를 억제한다 (PDF p.72)

- SGD는 gradient에 L2 형태의 항을 더하는 방식
- AdamW는 적응적 갱신과 별도로 Parameter 감쇠
- 너무 큰 weight_decay는 Underfitting 가능성
- 초급 실습의 전체 적용과 확장의 bias·정규화 파라미터 제외 전략 구분

##### Parameter group으로 weight decay를 다르게 줄 수 있다 (PDF p.73)

- BatchNorm 여부는 이름 문자열이 아닌 모듈 유형으로 판별
- bias와 BatchNorm 파라미터를 no_decay 그룹으로 분리
- 슬라이드 코드는 공유·동결 파라미터가 없는 모델을 전제
- 공유·동결 검사는 특심화 확장 범위

##### Dropout·BatchNorm·Weight Decay를 구분한다 (PDF p.74)

- Dropout은 무작위 activation 제거
- BatchNorm은 activation 정규화
- Weight Decay는 Parameter 크기 억제
- Early Stopping은 학습 반복 수와 최종 상태 선택에 관여

#### 실습 06과 규제 구분

##### 실습 06 · BatchNorm과 Weight Decay (PDF p.75)

- 기본필수는 입력 `(4,2)`에서 Linear 출력 `(4,8)`과 running_mean `(8,)` 확인
- 응용은 같은 batch 32에서 BN 유무만 변경하고 train·eval 출력 비교
- 응용의 마지막 16건도 포함하며 BN 학습 batch는 2건 이상 유지
- 심화는 baseline·BN·weight_decay 0.01을 각각 비교
- 특심화는 batch 2·8·32의 BN·LayerNorm 통계와 Weight Decay 그룹 확인
- 통계와 shape 및 기법별 목적 설명으로 완료 확인

##### 3분 퀴즈 · BatchNorm과 규제 (PDF p.76)

- num_features와 앞 층 출력 feature 수의 대응 확인
- eval 모드 BatchNorm의 저장 통계 사용 확인
- 과도한 Weight Decay의 Underfitting 가능성 확인

**핵심:** BatchNorm의 통계·모드·feature 수를 확인하고 Weight Decay와 다른 작용을 분리해 비교

### 7교시 · Early Stopping과 학습 안정화 통합

#### 중단 판단과 best 상태 복원

##### Early Stopping은 valid 개선이 멈추면 학습을 끝낸다 (PDF p.77)

- validation metric을 관측하며 개선 정체 시 학습 중단
- 최종 사용할 모델은 중단 시점이 아닌 best epoch의 상태

##### Early Stopping의 핵심 변수 (PDF p.78)

- best는 관측한 최저 validation loss 기록
- patience는 의미 있는 개선 없이 허용하는 epoch 수
- min_delta는 patience 초기화에 필요한 최소 개선 폭
- best_state는 best 시점 state_dict의 독립 사본

##### 간단한 Early Stopping 로직 (PDF p.79)

- valid_loss가 관측 최소보다 작으면 작은 개선도 best에 저장
- reference보다 min_delta를 넘게 감소한 경우에만 대기 횟수 초기화
- state_dict는 deepcopy로 보관해 이후 학습과 분리
- wait가 patience에 도달하면 중단하고 best_state 복원
- 학습 재개용 현재 상태는 best 상태와 별도로 보관

##### Scheduler와 Early Stopping을 함께 사용할 때 (PDF p.80)

- train epoch 뒤 valid loss를 계산하고 Scheduler 호출
- 이후 best 상태 보관과 Early Stopping 대기 횟수 판단
- lr 감소 뒤 개선할 기회를 주도록 두 patience의 관계 설계

##### Scheduler + Early Stopping 예시 (PDF p.81)

- 설명 예시의 best epoch와 stop epoch를 구분
- 실제 후보별 stop epoch가 다르면 수행한 학습량도 함께 보고
- 최종 사용 상태는 저장한 best epoch 모델

#### 오류 가설과 통합 프로젝트 설계

##### 오류 패턴별 우선 처방 (PDF p.82)

- 학습 부족은 모델 용량과 lr·epoch 점검에서 출발
- train만 개선되면 과적합과 데이터 원인 점검
- 진동과 정체는 서로 다른 처방 후보로 구분
- NaN·Inf는 lr과 입력 및 loss·gradient의 수치 상태 점검

##### 일일 프로젝트 · 학습 안정화 실험표 (PDF p.83)

- split·seed·모델을 고정한 기준선에서 한 조건씩 비교
- valid 지표로 후보 설정 선택
- 실행 조건과 history 및 비교 결과를 저장해 재실행 근거 확보
- 슬라이드의 전체 프로젝트 설계와 단계별 실제 제출 범위 구분

##### 심화 참고 구조 · 기본필수에는 한 파일만 요구한다 (PDF p.84)

- 모듈형 data·model·train·evaluate·experiments 구조는 심화 참고
- 기본필수는 제공된 한 파일에서 학습과 기록 완성
- 심화의 체크포인트와 복원 구조를 기본필수 공통 요구로 확대하지 않음

#### 실습 07의 단계별 통합

##### 실습 07 · 학습 안정화 프로젝트 통합 (PDF p.85)

- 기본필수는 두 lr의 기준선·후보 학습과 history CSV 및 비교표·곡선 저장
- 기본필수는 best epoch를 관찰하며 모델 저장·복원은 요구하지 않음
- 응용은 Optimizer·Dropout 후보 비교와 best 모델 복원 연결
- 응용의 클래스별 Recall 분모는 실제 해당 클래스 표본 수
- 심화는 Scheduler와 Early Stopping 및 best 저장·복원 연결
- 특심화는 표본 수로 가중한 loss 평가와 관측 최소 모델 복원 검증
- 선택 단계의 결과 파일과 고정·변경 조건 및 한계 설명으로 완료 확인

**핵심:** 관측 최소 모델과 patience 판정 기준을 구분하며 선택 단계에 맞는 기록과 best 복원으로 통합 실험 검증

### 8교시 · 실험표 검증과 오류 처방·재현

#### 실험 결과 해석과 단계별 산출물

##### 학습곡선을 보고 먼저 질문할 것 (PDF p.86)

- 문제가 train과 valid 중 어디에서 발생하는지 구분
- 초반과 후반의 발생 시점 구분
- loss와 accuracy의 판단 일치 여부 확인
- 변경 조건이 하나인지 확인

##### 오류 패턴별 처방 실습 (PDF p.87)

- 학습 지연은 lr과 gradient 및 입력 스케일부터 점검
- train만 개선되는 상황에서 epoch 추가를 즉시 처방하지 않음
- GPU 메모리 부족은 batch 감소와 기울기 누적 검토
- 평가 변동은 seed·eval 모드·shuffle 설정 점검
- NaN은 lr과 입력 및 loss·gradient norm 점검

##### 단계별 제출물 · 기본필수는 CSV와 결과 설명 (PDF p.88)

- 기본필수는 실험 CSV와 곡선 및 결과 설명 제출
- 설정 JSON과 best_model.pt 및 복원 보고서는 선택한 상위 단계 범위 적용
- best epoch의 값과 마지막 값을 구분해 선택 이유 기록
- 보고서는 관찰과 처방 및 한계·다음 실험을 근거로 구성

#### 실습 08의 재실행과 상태 검증

##### 실습 08 · 최종 검증·오류 처방·회고 (PDF p.89)

- 기본필수는 07번을 같은 설정으로 재실행해 곡선·best epoch·valid loss 대조
- 고정·변경 조건과 best·last 차이 및 한계를 세 문장으로 설명
- 응용은 README만으로 결과를 재생성하고 불일치 시 seed·mode·설정 점검
- 심화는 평가 상태 보존과 작은 개선의 best 저장·복원 테스트 작성
- 특심화는 20회 연속 실행과 10회 뒤 새 프로세스에서 10회 재개 비교
- 재개에는 현재 모델과 Optimizer·Scheduler·EarlyStop 및 RNG·배치 순서 보관
- 특심화 재개 일치 검증은 같은 CPU·버전의 epoch 경계와 num_workers 0 범위
- CUDA 검사 skip이나 빈 CUDA 상태의 일치를 GPU 검증 성공으로 해석하지 않음

##### 형성평가 기준 · 100점 (PDF p.90)

- 실험 설계 20점과 학습 루프 20점으로 조건 통제와 계산 순서 확인
- 곡선 진단 25점으로 best epoch와 패턴 근거 평가
- 안정화 기법 20점으로 목적과 선택 근거 평가
- 재현·설명 15점으로 환경·결과·개인 설명·한계 평가
- 실제 성능 점수 자체를 배점으로 사용하지 않음

##### 정상·경계·실패 상황을 구분한다 (PDF p.91)

- 정상 학습은 실제 수행 epoch와 history 행 수 대조
- 마지막 batch 1건은 모델의 BN 사용 여부와 drop_last 정책에 따라 처리 판단
- best epoch 예측과 복원 예측의 일치 확인은 복원을 구현하는 상위 단계 범위
- Scheduler 정체는 감시 기준과 실제 lr 이력으로 확인
- NaN loss는 학습 중단과 원인 기록 대상
- 기본필수에는 자동 테스트와 복잡한 실패 처리 구현을 공통 요구하지 않음

##### 마무리 3분 확인 퀴즈 (PDF p.92)

- 평가 모드 전환 함수의 역할 확인
- Early Stopping 뒤 사용할 best 상태 확인
- train·valid 동반 진동의 우선 점검 설정 확인

**핵심:** 실험의 완성은 예시 점수 일치가 아니라 조건·곡선·상태·재실행 근거와 해석의 한계를 설명하는 것으로 판단

### 마무리 · 전체 정리와 다음 수업

#### 학습 안정화 원칙과 후속 학습

##### 오늘의 핵심 정리 (PDF p.93)

- Optimizer·lr의 갱신 원리와 Batch·Iteration·Epoch의 데이터 사용 단위 연결
- 같은 조건의 train·valid 곡선을 근거로 안정화 기법 선택
- 좋은 숫자 자체보다 조건 통제와 선택 근거 설명을 평가

##### 다음 수업 · CNN 합성곱과 이미지 분류 (PDF p.94)

- 11월 2일 CNN·전이학습에 학습률과 batch 및 규제 원칙 연결
- 후속 시퀀스·비전 학습으로 shape와 gradient 및 재현 원칙 확장

### 참고자료 · 공식 API와 구현 범위

#### 함수별 확인 자료

##### 공식 참고자료 · Optimizer와 DataLoader (PDF p.95)

- SGD·AdamW와 Optimizer의 zero_grad·step을 확인하는 공식 API 목록
- DataLoader와 ReduceLROnPlateau의 인자·동작 확인 자료

##### 공식 참고자료 · Regularization과 Module mode (PDF p.96)

- Dropout·BatchNorm1d와 Module의 train·eval 동작 확인 자료
- Early Stopping은 validation metric을 감시하는 수업의 사용자 정의 로직
