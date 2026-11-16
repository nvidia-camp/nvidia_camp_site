# Day12 강의 구조와 핵심 설명

교재 표기는 Day 12 · 2026.11.03(화). 실제 수업은 2026-11-02(월)로 앞당겨 진행, 학습 자료 시트 표기는 `11-2`. 교시명은 PDF p.14 운영표의 핵심 내용 기준. 중간 학습 주제는 편집한 표현이며 마지막 단계는 원문 슬라이드 제목. 페이지는 103쪽 PDF의 뷰어 기준. 도입·마무리·참고자료는 교시 밖에 별도 배치.

기본필수만으로 형성평가 100점 충족. 응용·심화·특심화는 선택 확장. 이번 정리는 PDF만 근거로 작성했으며 Day12 실습 코드·README는 확인하지 않음. 교재의 예시 수치는 원리 설명용이며 실제 실행 결과가 아님.

## 강의 목차

```text
도입 · Sequence 모델의 전체 지도와 수업 준비
├─ 업무 목적과 모델의 위치
│  ├─ 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)
│  ├─ 센서 기록을 사용하는 두 가지 업무 목적 (PDF p.2)
│  └─ 전체 지도에서 오늘 배우는 모델의 위치 (PDF p.3)
├─ 입력 축과 모델별 핵심 계산
│  ├─ 입력 한 묶음에서 한 시점의 값까지 (PDF p.4)
│  ├─ LSTM 예측 모델의 전체 흐름 (PDF p.5)
│  ├─ LSTM Cell 안에서 기억을 조절하는 Gate (PDF p.6)
│  ├─ Autoencoder의 압축과 복원 (PDF p.7)
│  ├─ Transformer 모델 안의 Encoder와 Attention (PDF p.8)
│  └─ Attention의 Q·K 비교와 V 가중합 (PDF p.9)
├─ 비교 기준과 프로젝트 연결
│  ├─ 모델과 장치를 공정하게 비교하는 방법 (PDF p.10)
│  └─ 일일 프로젝트에서 다시 합치는 전체 흐름 (PDF p.11)
└─ 선행 학습 복습과 수업 운영
   ├─ 지난 수업에서 만든 이미지 분류 흐름 (PDF p.12)
   ├─ 3분 확인 퀴즈 · CNN에서 Sequence 모델로 (PDF p.13)
   ├─ 오늘의 목표와 8교시 운영 (PDF p.14)
   ├─ 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)
   └─ 실습 전 환경과 Sequence 입력을 확인한다 (PDF p.16)

1교시 · Sequence Tensor·Padding·Task 유형
├─ 순서 모델의 역할과 Sequence 데이터
│  ├─ RNN·LSTM·Autoencoder·Transformer의 역할 (PDF p.17)
│  └─ Sequence 데이터는 순서와 길이를 가진다 (PDF p.18)
├─ Sequence Tensor의 축과 Padding
│  ├─ Sequence Tensor의 세 축을 읽는다 (PDF p.19)
│  ├─ Sequence Tensor의 Shape·dtype·device 확인 (PDF p.20)
│  └─ Padding Tensor와 PackedSequence의 입출력 (PDF p.21)
└─ 실습 01의 Padding 검증
   └─ 실습 01 · Sequence Tensor와 Padding (PDF p.22)

2교시 · RNN·Hidden state·순차 예측
├─ 순환 구조와 입출력 유형
│  ├─ RNN은 이전 상태를 다음 시점으로 전달한다 (PDF p.23)
│  ├─ RNN을 시간축으로 펼쳐서 본다 (PDF p.24)
│  └─ Sequence 입력과 출력의 대표 구조 (PDF p.25)
├─ Hidden state 계산과 출력 구분
│  ├─ RNN의 한 시점 계산을 읽는다 (PDF p.26)
│  └─ RNN의 output과 h_n을 구분한다 (PDF p.27)
├─ nn.RNN 사용과 분류 모델
│  ├─ nn.RNN · 기본 순환 신경망 층 (PDF p.28)
│  ├─ RNN forward · 입력과 초기 상태 (PDF p.29)
│  └─ RNN Sequence 분류 모델 (PDF p.30)
└─ RNN의 한계와 실습 확인
   ├─ 기본 RNN의 장기 의존성 한계 (PDF p.31)
   ├─ 실습 02 · RNN 분류와 시점 출력 (PDF p.32)
   └─ 3분 퀴즈 · RNN (PDF p.33)

3교시 · LSTM·Gate·시계열 예측
├─ Gate와 Cell state
│  ├─ Gate와 Cell state로 장기 정보를 제어한다 (PDF p.34)
│  ├─ LSTM은 Cell state와 네 가지 연산을 사용한다 (PDF p.35)
│  ├─ nn.LSTM · 장단기 기억 순환 층 (PDF p.36)
│  └─ LSTM Gate를 역할 중심으로 구분한다 (PDF p.37)
├─ 출력 패턴과 Shape 추적
│  ├─ Sequence-to-one과 Sequence-to-sequence (PDF p.38)
│  ├─ LSTM 시계열 예측의 Shape를 추적한다 (PDF p.39)
│  └─ LSTM의 h_n·c_n과 다층·양방향 Shape (PDF p.40)
├─ 시계열 예측 구현과 오류
│  ├─ LSTM으로 다음 시점 예측 (PDF p.41)
│  ├─ Tensor.unfold · Sliding Window 만들기 (PDF p.42)
│  └─ LSTM에서 자주 발생하는 오류 (PDF p.43)
└─ 실습 03과 LSTM 개념 확인
   ├─ 실습 03 · LSTM 시계열 예측 (PDF p.44)
   └─ 3분 퀴즈 · LSTM (PDF p.45)

4교시 · Autoencoder·재구성·이상 탐지
├─ 압축·복원 구조와 재구성 손실
│  ├─ 입력을 압축하고 다시 복원한다 (PDF p.46)
│  ├─ Encoder·Latent·Decoder의 역할 (PDF p.47)
│  ├─ nn.MSELoss · 재구성 오차 계산 (PDF p.48)
│  └─ Autoencoder의 압축과 복원 (PDF p.49)
├─ 입력=정답 학습과 Latent 활용
│  ├─ TensorDataset·DataLoader로 입력=정답 Batch 만들기 (PDF p.50)
│  ├─ Latent 표현의 활용과 한계 (PDF p.51)
│  └─ 예측과 재구성은 목표가 다르다 (PDF p.52)
├─ 구현과 샘플별 재구성 오류
│  ├─ nn.Sequential·nn.Linear로 Encoder·Decoder 구성 (PDF p.53)
│  ├─ Autoencoder도 학습·선택·평가를 분리한다 (PDF p.54)
│  ├─ reduction="none"으로 샘플별 재구성 오류 계산 (PDF p.55)
│  └─ Autoencoder forward와 재구성 오류 (PDF p.56)
└─ 실습 04와 Autoencoder 개념 확인
   ├─ 실습 04 · Autoencoder 재구성 (PDF p.57)
   └─ 3분 퀴즈 · Autoencoder (PDF p.58)

5교시 · Attention·Transformer Encoder
├─ Attention 흐름과 Query·Key·Value
│  ├─ Attention으로 입력 위치를 직접 비교한다 (PDF p.59)
│  ├─ Transformer Encoder의 한 Batch 흐름 (PDF p.60)
│  └─ Query·Key·Value를 역할로 이해한다 (PDF p.61)
├─ MultiheadAttention과 Encoder Layer
│  ├─ MultiheadAttention으로 Self-Attention (PDF p.62)
│  ├─ nn.MultiheadAttention · 다중 Head Attention (PDF p.63)
│  └─ TransformerEncoderLayer 적용 (PDF p.64)
├─ Mask·Position과 Sequence 분류
│  ├─ Padding Mask와 Causal Mask를 구분한다 (PDF p.65)
│  ├─ Attention에는 순서 정보가 자동으로 들어가지 않는다 (PDF p.66)
│  └─ Transformer Encoder Sequence 분류 (PDF p.67)
└─ 실습 05와 Transformer 개념 확인
   ├─ 실습 05 · Self-Attention과 Transformer Encoder (PDF p.68)
   └─ 3분 퀴즈 · Transformer (PDF p.69)

6교시 · 아키텍처 비교·Mask·미니 모델
├─ 목표에 맞는 구조 선택
│  ├─ 목표·길이·자원에 맞는 구조를 선택한다 (PDF p.70)
│  ├─ Transformer Encoder의 내부 흐름 (PDF p.71)
│  └─ RNN·LSTM·Autoencoder·Transformer 비교 (PDF p.72)
├─ Encoder 구성과 Position Embedding
│  ├─ nn.TransformerEncoderLayer · Encoder 기본 블록 (PDF p.73)
│  ├─ nn.TransformerEncoder · Encoder Layer를 N개 쌓는다 (PDF p.74)
│  └─ 학습 가능한 Position Embedding 연결 (PDF p.75)
├─ 비교 실험 설계와 Mask Pooling
│  ├─ 아키텍처 비교 조건을 고정한다 (PDF p.76)
│  ├─ Padding Mask를 포함한 평균 Pooling (PDF p.77)
│  ├─ 아키텍처 비교표에 반드시 남길 항목 (PDF p.78)
│  └─ Sequence 모델에서 자주 발생하는 오류 (PDF p.79)
└─ 실습 06과 아키텍처 비교 확인
   ├─ 실습 06 · 아키텍처 비교와 Mask 처리 (PDF p.80)
   └─ 3분 퀴즈 · 아키텍처 비교 (PDF p.81)

7교시 · 길이·Padding·CPU/GPU 성능 비교
├─ 가변 길이와 공정한 측정 조건
│  ├─ 길이·Padding·Device가 성능을 바꾼다 (PDF p.82)
│  ├─ 가변 길이 Batch와 Mask (PDF p.83)
│  ├─ 공정한 Sequence 모델 비교 조건 (PDF p.84)
│  └─ pack_padded_sequence·pad_packed_sequence (PDF p.85)
├─ 시간·메모리 측정
│  ├─ GPU 시간·Peak Memory 측정 함수 (PDF p.86)
│  ├─ 한 Batch의 순전파를 반복해 시간 측정 (PDF p.87)
│  └─ Sequence 길이와 속도·메모리의 관계 (PDF p.88)
├─ 결과 기록과 해석
│  ├─ 같은 Device에서 모델별 성능을 비교한다 (PDF p.89)
│  └─ 성능 측정값을 과장하지 않고 해석한다 (PDF p.90)
└─ 실습 07과 성능 측정 확인
   ├─ 실습 07 · Sequence 모델 시간·메모리 비교 (PDF p.91)
   └─ 3분 퀴즈 · Sequence 성능 측정 (PDF p.92)

8교시 · 아키텍처 비교 프로젝트·시연
├─ 프로젝트 목표와 구조
│  ├─ 최종 프로젝트 · 시계열 예측과 재구성 미니 모델 (PDF p.93)
│  ├─ 심화 참고 · 모듈형 프로젝트 구조 (PDF p.94)
│  └─ 프로젝트 흐름과 단계별 확장 (PDF p.95)
├─ 제출물과 통합 실습
│  ├─ 단계별 제출물과 기록 내용 (PDF p.96)
│  └─ 실습 08 · 아키텍처 비교 프로젝트 통합·시연 (PDF p.97)
└─ 평가 기준과 검증 상황
   ├─ 형성평가 · 기본필수만으로 100점 (PDF p.98)
   └─ 정상·경계·실패 상황을 구분한다 (PDF p.99)

마무리 · 정리와 참고자료
├─ 전체 정리와 다음 수업
│  ├─ 오늘의 핵심 정리 (PDF p.100)
│  └─ 다음 수업 · 11월 4일 Vision·OpenCV (PDF p.101)
└─ 공식 참고자료
   ├─ 공식 참고자료 · PyTorch Sequence Layers (PDF p.102)
   └─ 공식 참고자료 · Attention·Transformer (PDF p.103)
```

## 핵심 설명

### 도입 · Sequence 모델의 전체 지도와 수업 준비

#### 업무 목적과 모델의 위치

##### 딥러닝 핵심 아키텍처 및 학습 (PDF p.1)

- Day 12의 Sequence Tensor → RNN·LSTM → Autoencoder → Transformer → 미니 모델 흐름을 소개하는 표지

##### 센서 기록을 사용하는 두 가지 업무 목적 (PDF p.2)

- 설비 센서 관측 기록을 다음 값 예측과 입력 재구성의 두 목적으로 사용하는 가상 업무 예시
- 다음 값 예측은 과거 12개 관측을 LSTM에 넣고 다음 시점의 실제 값을 정답으로 학습
- 입력 재구성은 현재 8개 특성을 Autoencoder로 복원하며 원래 입력이 정답
- 복원 오차가 큰 사례는 점검 후보로 사용
- 수업 실습은 사인파 예측과 8차원 데이터 재구성으로 같은 흐름 연습

##### 전체 지도에서 오늘 배우는 모델의 위치 (PDF p.3)

- 업무 목표와 입력 자료를 먼저 정한 뒤 모델 안의 층과 작은 계산으로 내려가는 구조
- RNN·LSTM은 순환층 안의 한 시점 Cell에서 상태 갱신과 Gate 계산
- Transformer Encoder는 Layer 안의 Self-Attention에서 Q·K 비교와 V 가중합
- 오늘의 Autoencoder는 Linear 층으로 만든 MLP형 Encoder·Latent·Decoder 구성

#### 입력 축과 모델별 핵심 계산

##### 입력 한 묶음에서 한 시점의 값까지 (PDF p.4)

- Batch는 Window B개, Window는 과거 시점 T개, 한 시점은 동시에 관측한 특성 F개
- 이번 LSTM 실습 입력은 `[B,12,1]`로 과거 12개 관측·시점마다 값 1개
- 정답은 다음 값 `[B,1]`
- 관측 주기와 입력 범위를 정해야 예측값을 업무 시간에 연결 가능
- 길이가 다른 자료는 Padding과 실제 길이를 함께 관리하며 실습 01에서 확인

##### LSTM 예측 모델의 전체 흐름 (PDF p.5)

- 과거 Window `[B,12,1]` → LSTM 층 `hidden_size=16` → `[B,12,16]` → 마지막 시점 선택 `[B,16]` → Linear Head → 예측 `[B,1]`
- LSTM은 현재 값과 앞선 흐름을 함께 표현하기 위해 사용
- 학습에서는 다음 실제 값과 예측값의 MSE 비교
- 단방향·고정 길이 예제이며 Padding이 있으면 실제 길이 기준으로 마지막 시점 선택

##### LSTM Cell 안에서 기억을 조절하는 Gate (PDF p.6)

- 한 시점의 LSTM Cell은 이전 상태 h, c와 현재 입력 x로 새 상태 h, c 계산
- 갱신한 기억 c는 Forget gate × 이전 c와 Input gate × 새 후보의 합
- 예시 계산 `0.5×2=1`, `0.4×0.5=0.2`, `1+0.2=1.2`는 원리 설명용 숫자
- 실제 Gate 값은 학습한 가중치로 계산
- 기본 RNN은 h만 갱신하고 LSTM은 h와 c를 함께 전달

##### Autoencoder의 압축과 복원 (PDF p.7)

- Encoder가 8차원 입력을 4차원 은닉층을 거쳐 2차원 Latent z로 압축
- Decoder가 2차원 표현을 4차원 은닉층을 거쳐 8차원 복원 x̂로 변환
- Shape 흐름은 `[B,8]` → `[B,4]` → `[B,2]` → `[B,4]` → `[B,8]`
- 학습 정답은 원래 입력 x이며 x와 x̂의 MSE 계산
- 복원 오차가 큰 사례는 점검 후보이며 정상·이상 기준은 별도 검증

##### Transformer 모델 안의 Encoder와 Attention (PDF p.8)

- 각 위치가 떨어진 위치의 정보를 참고해 함께 읽을 문맥 생성
- 입력 + Position `[B,T,16]` → Transformer Encoder `[B,T,16]` → 실제 위치만 평균 Pooling `[B,16]` → 분류 Head logits `[B,2]`
- Encoder Layer에는 Self-Attention 외에 FFN·잔차 연결·LayerNorm 포함
- 현업에서는 문장·로그·센서 기록의 문맥을 읽는 모델에 활용

##### Attention의 Q·K 비교와 V 가중합 (PDF p.9)

- Q는 찾을 정보, K는 비교할 위치, V는 합산할 내용
- 한 Query가 Key들을 비교해 얻은 비율로 Value 내용을 모으는 연산
- 예시 가중치 0.2·0.3·0.5와 Value 10·20·30의 가중합은 23
- 예시 숫자는 원리 설명용이며 실제 가중치는 Q·K에서 계산
- Position은 순서 표시, Padding Mask는 채움 Key 제외, Pooling에서도 채움 출력 제외

#### 비교 기준과 프로젝트 연결

##### 모델과 장치를 공정하게 비교하는 방법 (PDF p.10)

- 모델 비교는 자료·분할·목표·Device를 고정하고 RNN·LSTM·Transformer만 변경
- 장치 비교는 모델·가중치·입력·측정 구간을 고정하고 CPU·GPU만 변경
- 재구성 실험은 입력·분할·전처리를 고정하고 Latent 크기 등을 변경
- 예측은 예측끼리, 분류는 분류끼리 같은 지표로 비교
- Autoencoder 재구성 결과는 별도로 기록
- 실습 07은 반복 순전파 측정이며 CPU만으로 기본필수 수행 가능

##### 일일 프로젝트에서 다시 합치는 전체 흐름 (PDF p.11)

- 제공 자료의 분할·입력 Shape 확인 후 LSTM 다음 값 예측과 Autoencoder 입력 재구성으로 분기
- 각 결과는 목적별 결과표에 저장하고 README로 설명
- 기본필수는 제공 골격에서 LSTM 예측·Autoencoder 재구성·결과표 저장 완성
- 확장은 자기 단계 README의 모델 비교·복원·검증 범위 기준
- 실습 순서는 01 입력·02 RNN·03 LSTM·04 AE·05 Attention·06 비교·07 측정·08 통합

#### 선행 학습 복습과 수업 운영

##### 지난 수업에서 만든 이미지 분류 흐름 (PDF p.12)

- CNN은 국소 패턴을 Feature Map으로 만들고 공간 크기를 단계적으로 축소
- train·valid 변환 분리와 Best model·오류 사례 기록
- 사전학습 특징 추출부를 재사용하고 Head 또는 일부 깊은 층 학습
- 오늘은 공간 구조에서 시간·순서·재구성·Attention 구조로 확장

##### 3분 확인 퀴즈 · CNN에서 Sequence 모델로 (PDF p.13)

- 순서 자체가 입력 정보이므로 셔플 위치와 단위를 구분하는지 확인
- 모델 구조가 바뀌어도 train·valid·test 분리 원칙이 유지되는지 확인
- 길이가 다른 입력을 Batch로 만들 때 Padding과 길이 또는 Mask로 실제 위치와 채움 위치를 구분하는지 확인

##### 오늘의 목표와 8교시 운영 (PDF p.14)

- 1교시 Sequence Tensor·Padding·Task 유형, 설명·시연 30분·실습 20분
- 2~7교시는 RNN, LSTM, Autoencoder, Attention·Transformer, 아키텍처 비교, CPU/GPU 성능 비교 순서로 각 설명 25분·실습 25분
- 8교시 아키텍처 비교 프로젝트·시연, 설명 20분·실습 30분

##### 오늘 배우는 범위와 다음 수업의 경계 (PDF p.15)

- 오늘 범위는 RNN·LSTM의 순서·장기 의존성, Autoencoder 압축·재구성과 오류 해석, Transformer Encoder의 Attention·Mask, 아키텍처 비교도와 미니 모델
- 다음 수업은 OpenCV 이미지 표현·색공간·리사이즈, 필터·형태학 처리와 영상 입출력, 프레임 처리·증강 파이프라인, 전처리 결과 검증

##### 실습 전 환경과 Sequence 입력을 확인한다 (PDF p.16)

- `torch` import와 CPU/GPU 장치 확인 후 PyTorch 실제 설치 버전 기록
- Sequence Tensor 기본 Shape는 `[Batch, Time, Feature]`로 통일
- 서로 다른 길이는 Padding·lengths·Mask로 실제 값과 채움 위치 구분
- 정상 설치 환경 유지, 기본 실습은 CPU로 수행하고 GPU 비교는 사용 가능할 때만 진행

**핵심:** 업무 목적을 예측·재구성·문맥 분류로 먼저 나누고 그에 맞는 입력 Shape·정답·비교 조건을 정하는 것이 오늘 모든 모델 선택의 출발점.

### 1교시 · Sequence Tensor·Padding·Task 유형

#### 순서 모델의 역할과 Sequence 데이터

##### RNN·LSTM·Autoencoder·Transformer의 역할 (PDF p.17)

- RNN은 이전 Hidden state를 다음 시점으로 전달해 순서 처리
- LSTM은 Gate와 Cell state로 긴 의존성을 더 안정적으로 보존
- Autoencoder는 입력을 작은 Latent 표현으로 압축한 뒤 복원
- Transformer는 Attention으로 입력 위치들을 직접 비교해 문맥 생성

##### Sequence 데이터는 순서와 길이를 가진다 (PDF p.18)

- 표 데이터·고정 크기 이미지는 한 행 또는 한 이미지가 독립 샘플
- 센서·문장·로그·오디오는 시점·토큰 순서가 의미에 직접 관여
- Sequence 데이터는 고정 길이와 가변 길이 모두 가능
- 현재 출력이 이전 상태나 다른 위치를 참조
- 표본 간 순서와 표본 내부 순서를 구분

#### Sequence Tensor의 축과 Padding

##### Sequence Tensor의 세 축을 읽는다 (PDF p.19)

- 축 순서는 B·Batch → T·Time → F·Feature
- 예시 `[32, 50, 8]`은 Sequence 32개·길이 50·시점별 특성 8개

##### Sequence Tensor의 Shape·dtype·device 확인 (PDF p.20)

- `torch.randn(4, 6, 3)`은 Sequence 4개·최대 길이 6·특성 3개
- `lengths`는 Shape `[4]`로 샘플별 실제 길이 저장
- `arange`와 `lengths` 비교로 Padding 위치 Mask를 만들고 `masked_fill`로 0 채움
- dtype `float32`는 모델 가중치와 같은 실수형
- Padding을 쓰면 T는 Batch 안의 최대 길이

##### Padding Tensor와 PackedSequence의 입출력 (PDF p.21)

- `pad_sequence`는 가변 길이 Tensor 목록을 Padding Tensor로 변환
- `pack_padded_sequence`는 Padding된 Tensor와 각 샘플의 실제 `lengths`로 PackedSequence 생성
- `batch_first`는 기본 False이며 True면 `[B,T,F]`
- `padding_value`는 채움 값, `enforce_sorted`는 길이 정렬 여부
- Packed의 `data`는 `[Σ길이,F]` 형태

#### 실습 01의 Padding 검증

##### 실습 01 · Sequence Tensor와 Padding (PDF p.22)

- 기본필수는 길이 4·2·5인 Tensor 3개를 Padding해 `[3,5,3]` Shape 확인
- 응용은 Padding 위치 Mask를 만들고 실제 값의 평균만 계산
- 심화는 PackedSequence로 변환한 뒤 Padding Tensor와 lengths 복원
- 특심화는 정렬·Packing·역순열 복원을 구현하고 값·길이·gradient 동등성 확인

**핵심:** Sequence 입력은 `[B,T,F]` Shape만으로 끝나지 않고 실제 길이와 Padding 위치를 함께 보관해야 이후 상태 선택·평균·Attention이 올바름.

### 2교시 · RNN·Hidden state·순차 예측

#### 순환 구조와 입출력 유형

##### RNN은 이전 상태를 다음 시점으로 전달한다 (PDF p.23)

- 같은 Cell을 시간축에 반복 적용해 Sequence를 읽는 구조를 소개하는 구분 슬라이드

##### RNN을 시간축으로 펼쳐서 본다 (PDF p.24)

- 각 시점에서 입력 xₜ와 이전 Hidden state hₜ₋₁을 함께 사용
- 같은 가중치를 모든 시점에 공유
- `output`은 마지막 층의 각 시점 출력, `h_n`은 모든 층·방향의 최종 상태
- Sequence 길이가 길어질수록 오래된 정보의 영향이 약해질 수 있음

##### Sequence 입력과 출력의 대표 구조 (PDF p.25)

- Many-to-one은 전체 Sequence를 읽고 최종 클래스·값 하나 예측
- Many-to-many는 각 시점마다 태그·상태·예측 출력
- Next-step은 과거 Window로 다음 시점의 값 예측
- Encoder–Decoder는 입력 Sequence를 다른 길이의 출력 Sequence로 변환

#### Hidden state 계산과 출력 구분

##### RNN의 한 시점 계산을 읽는다 (PDF p.26)

- `hₜ = tanh(Wₓxₜ + Wₕhₜ₋₁ + b)`
- xₜ는 현재 시점 입력, hₜ₋₁은 이전 시점까지의 요약 상태
- hₜ는 현재까지 읽은 정보를 고정된 `hidden_size`로 요약
- 가중치 공유 덕분에 길이가 달라도 같은 Cell 반복 적용 가능

##### RNN의 output과 h_n을 구분한다 (PDF p.27)

- `output`은 모든 시점의 마지막 층 출력, `batch_first=True`에서 `[B,T,D×H]`
- `h_n`은 모든 층·방향의 마지막 상태, `[L×D,B,H]`
- `output`은 시점별 태깅·Attention 입력에 사용
- `h_n`은 Sequence 분류의 최종 표현으로 사용 가능
- `output`에서는 유효 시점 선택·Packing·Mask 구분
- bidirectional이면 방향 수 D=2

#### nn.RNN 사용과 분류 모델

##### nn.RNN · 기본 순환 신경망 층 (PDF p.28)

- 필수 인자는 `input_size`(시점별 입력 Feature 수)와 `hidden_size`(Hidden state Feature 수)
- 선택 인자 `num_layers`·`batch_first`·`bidirectional`은 층 수·축 순서·양방향 지정
- 선택 인자 `nonlinearity`·`dropout`·`bias`는 활성화·층 사이 Dropout·Bias 지정
- 입력 `[B,T,F]` → `output [B,T,D×H]`, `h_n [L×D,B,H]`

##### RNN forward · 입력과 초기 상태 (PDF p.29)

- `output, h_n = rnn(input, hx=None)` 형태로 호출
- `input`은 Sequence Tensor 또는 PackedSequence
- `hx`는 초기 Hidden state이며 생략하면 0
- `hx` Shape는 `batch_first`와 무관하게 `[L×D,B,H]`
- `batch_first`는 input·output에만 적용되고 `h_n` 축 순서는 고정

##### RNN Sequence 분류 모델 (PDF p.30)

- `nn.RNN(3, 8, batch_first=True)`와 `nn.Linear(8, 2)`로 구성
- `[B,T,3]` → `output [B,T,8]` → `h_n[-1] [B,8]` → logits `[B,2]`
- 마지막 층의 최종 상태 `h_n[-1]`을 분류 Head 입력으로 사용

#### RNN의 한계와 실습 확인

##### 기본 RNN의 장기 의존성 한계 (PDF p.31)

- 역전파가 긴 시간축을 지나며 Gradient가 작아지거나 커질 수 있음
- 초기 시점 정보가 많은 갱신을 거치며 희미해질 수 있음
- Sequence가 길수록 순차 계산 때문에 병렬화 제한
- LSTM·GRU의 Gate 또는 Transformer Attention이 대안

##### 실습 02 · RNN 분류와 시점 출력 (PDF p.32)

- 기본필수는 `[B,6,3]` 입력을 RNN에 넣고 `output`·`h_n` Shape와 분류 Logit 확인
- 응용은 Many-to-one과 Many-to-many 출력 사용법을 코드로 비교
- 심화는 Padding 입력과 PackedSequence의 마지막 상태 차이 분석
- 특심화는 같은 가중치의 `RNNCell` 반복과 `nn.RNN`의 출력·초기상태·gradient 대조

##### 3분 퀴즈 · RNN (PDF p.33)

- `batch_first=True`일 때 입력 Shape가 `[Batch, Time, Feature]`임을 확인
- `output`은 모든 시점, `h_n`은 마지막 상태로 서로 다른 Tensor임을 확인
- 긴 Sequence에서 Gradient·정보 보존이 어렵고 순차 계산이 필요한 이유 확인

**핵심:** RNN에서는 `output`과 `h_n`의 의미·Shape를 구분해 과제 유형에 맞는 표현을 꺼내 쓰는 것이 분류·예측 구현의 기준.

### 3교시 · LSTM·Gate·시계열 예측

#### Gate와 Cell state

##### Gate와 Cell state로 장기 정보를 제어한다 (PDF p.34)

- 기억을 지울지·쓸지·출력할지를 학습하는 LSTM을 소개하는 구분 슬라이드

##### LSTM은 Cell state와 네 가지 연산을 사용한다 (PDF p.35)

- Forget gate는 이전 Cell state에서 남길 비율 결정
- Input gate·Candidate는 새 정보를 얼마나 쓸지 결정
- Cell state는 장기 정보를 비교적 직접적인 경로로 전달
- Output gate는 현재 Hidden state로 노출할 정보 결정

##### nn.LSTM · 장단기 기억 순환 층 (PDF p.36)

- 필수 인자는 `input_size`와 `hidden_size`
- 선택 인자는 `num_layers`·`batch_first`·`bidirectional`·`dropout`
- `proj_size`는 출력 Hidden 크기를 투영할 때 사용
- forward 반환은 `output, (h_n, c_n)`

##### LSTM Gate를 역할 중심으로 구분한다 (PDF p.37)

- Forget gate fₜ는 이전 기억 cₜ₋₁의 유지 정도를 0~1로 조절
- Input gate iₜ는 새 Candidate gₜ를 기억에 쓰는 정도 조절
- Cell update는 `cₜ = fₜ⊙cₜ₋₁ + iₜ⊙gₜ`
- Output gate oₜ는 `hₜ = oₜ⊙tanh(cₜ)`로 현재 출력 생성

#### 출력 패턴과 Shape 추적

##### Sequence-to-one과 Sequence-to-sequence (PDF p.38)

- Sequence-to-one은 마지막 Hidden state로 전체 Sequence의 클래스·값 예측
- Sequence-to-sequence는 각 시점 output으로 태그·복원·다음 값 예측
- 마지막 index를 사용할 때 실제 길이와 Padding 위치 구분
- 양방향은 주어진 Window 내부를 양쪽으로 읽는 구조이며 미래 관측이 입력에 섞였는지 확인

##### LSTM 시계열 예측의 Shape를 추적한다 (PDF p.39)

- Window는 과거 12개 값 `[B,12,1]`
- LSTM `hidden=16`은 `[B,12,1]` → `[B,12,16]`
- 마지막 시점 선택은 `[B,12,16]` → `[B,16]`
- Head `Linear 16→1`은 `[B,16]` → `[B,1]`
- Loss는 예측·정답 `[B,1]`의 MSE로 스칼라 산출
- epoch loss는 Batch 반복 결과를 샘플 수로 가중 평균

##### LSTM의 h_n·c_n과 다층·양방향 Shape (PDF p.40)

- `output, (h_n, c_n) = lstm(input, hx=None)` 형태로 호출
- `input`은 `[B,T,F]` 또는 PackedSequence
- `hx=(h_0, c_0)`이며 생략하면 둘 다 0
- 기본 `proj_size=0`에서 `h_n`·`c_n`은 모두 `[L×D,B,H]`
- `proj_size=0`일 때 `output`은 `[B,T,D×H]`

#### 시계열 예측 구현과 오류

##### LSTM으로 다음 시점 예측 (PDF p.41)

- `nn.LSTM(1, 16, batch_first=True)`와 `nn.Linear(16, 1)`로 구성
- `output[:, -1]`로 마지막 시점 `[B,16]`을 선택해 예측 `[B,1]` 생성
- 고정 길이 예제이며 Padding이 없는 조건에서만 `output[:, -1]` 사용

##### Tensor.unfold · Sliding Window 만들기 (PDF p.42)

- `tensor.unfold(dimension, size, step)`의 세 인자 모두 필수이며 선택 인자 없음
- `dimension`은 Window를 만들 축, `size`는 Window 길이, `step`은 시작점 간격
- 반환 Tensor는 Window 차원이 추가되며 원본과 메모리를 공유하는 view
- 길이 20·`size=5`·`step=1`이면 Window 16개
- 시간 구간을 먼저 train·valid·test로 나눈 뒤 각각 Window 생성

##### LSTM에서 자주 발생하는 오류 (PDF p.43)

- `h_n`과 `c_n`을 하나의 Tensor로 취급하거나 Shape 순서를 잘못 해석하는 오류
- Padding된 마지막 열을 실제 마지막 시점으로 사용하는 오류
- bidirectional 출력의 두 방향을 합치는 방법을 설명하지 않는 오류
- 시계열 분할에서 미래 데이터를 train에 섞는 누수

#### 실습 03과 LSTM 개념 확인

##### 실습 03 · LSTM 시계열 예측 (PDF p.44)

- 기본필수는 사인파 Window `[B,12,1]`로 다음 값 하나를 예측하고 Shape 설명
- 응용은 RNN과 LSTM의 valid MSE를 같은 분할·epoch에서 비교
- 심화는 가변 길이 Sequence를 PackedSequence로 학습하고 Padding 결과와 비교
- 특심화는 LSTM gate를 직접 계산하고 실제 시점만 집계해 `nn.LSTM` 수치·미분과 대조

##### 3분 퀴즈 · LSTM (PDF p.45)

- LSTM이 Hidden state h와 함께 Cell state c를 유지하는지 확인
- Padding이 있으면 `output[:, -1]`이 실제 마지막 시점이 아니며 lengths 또는 packed 입력이 필요함을 확인
- 양방향 LSTM의 미래 예측에서는 예측 시점 이후 관측의 입력 여부 확인, 과거 Window 안의 역방향 읽기 자체는 누수가 아님

**핵심:** LSTM 예측의 정확성은 Gate 구조보다 Window 생성 전 시간 분할과 실제 마지막 시점 선택이 올바른지에서 먼저 결정됨.

### 4교시 · Autoencoder·재구성·이상 탐지

#### 압축·복원 구조와 재구성 손실

##### 입력을 압축하고 다시 복원한다 (PDF p.46)

- 정답이 입력 자체인 재구성 학습을 소개하는 구분 슬라이드

##### Encoder·Latent·Decoder의 역할 (PDF p.47)

- Encoder는 입력을 더 작은 Latent 표현 z로 압축
- Latent는 입력의 주요 패턴을 제한된 차원에 저장
- Decoder는 z로부터 원래 입력을 재구성
- 재구성 오류는 압축 정보의 손실과 입력의 비정상성을 함께 반영

##### nn.MSELoss · 재구성 오차 계산 (PDF p.48)

- `loss = loss_fn(input, target)`에서 `input`은 재구성 결과, `target`은 같은 Shape의 원본 입력
- `reduction`은 `"none"`·`"mean"`·`"sum"` 중 선택하며 기본 `"mean"`
- `size_average`·`reduce`는 이전 호환용 인자
- Autoencoder에서는 reconstruction과 input의 Shape 일치 필요

##### Autoencoder의 압축과 복원 (PDF p.49)

- 입력 차원보다 작은 Bottleneck으로 단순 복사 제한
- Latent 차원이 너무 작으면 중요한 정보도 잃어 Underfitting 발생
- 너무 큰 모델은 입력을 거의 그대로 복사해 일반화가 약해질 수 있음
- 분류 모델이 아니므로 Latent의 의미는 별도 분석 필요

#### 입력=정답 학습과 Latent 활용

##### TensorDataset·DataLoader로 입력=정답 Batch 만들기 (PDF p.50)

- `TensorDataset(*tensors)`는 첫 차원 길이가 같은 Tensor들을 묶음
- `DataLoader`의 필수 인자는 `dataset`
- 선택 인자는 `batch_size`·`shuffle`·`num_workers`·`pin_memory`·`drop_last`·`generator`·`persistent_workers`
- Autoencoder Batch는 `(x,)` 한 개짜리 Tuple로 반환될 수 있음

##### Latent 표현의 활용과 한계 (PDF p.51)

- 차원 축소 흐름은 입력 → Encoder → Latent → Decoder → 재구성
- Denoising은 노이즈 입력과 깨끗한 target을 사용하며 정답과 입력의 역할 구분
- 이상 탐지에서 큰 오류는 이상 후보이며 확정이 아님
- 정상 train으로 학습하고 valid에서 임계값 선택
- test는 계획 확정 후 선택 과제에서만 평가

##### 예측과 재구성은 목표가 다르다 (PDF p.52)

- LSTM Forecasting은 과거 Window로 미래 값 또는 클래스 예측
- Autoencoder는 현재 입력을 압축하고 같은 입력 복원
- Forecasting은 미래 정답과의 오차, Autoencoder는 재구성 오차로 평가
- 두 결과는 같은 지표로 평균내지 않고 목적별로 별도 보고

#### 구현과 샘플별 재구성 오류

##### nn.Sequential·nn.Linear로 Encoder·Decoder 구성 (PDF p.53)

- `nn.Sequential`은 순서대로 실행할 Module 목록
- `nn.Linear`의 필수 인자는 `in_features`·`out_features`, 선택 인자 `bias=True`
- Linear는 입력 마지막 차원을 `in_features`에서 `out_features`로 변환
- Sequential은 중간 출력을 자동 반환하지 않음

##### Autoencoder도 학습·선택·평가를 분리한다 (PDF p.54)

- train에서 정상 패턴을 학습할 자료 정의
- Normalize·Scaler는 train에서 fit
- 노이즈를 추가하면 입력만 변형하고 target은 깨끗한 원본 사용
- 이상 자료를 train에 섞을지 정책 명시
- valid·test에는 같은 전처리 규칙으로 재구성 오류 계산
- 임계값은 valid에서 정하고 test는 최종 평가에만 사용
- 오류 분포와 실제 이상·정상 사례를 함께 확인
- 모델 선택 후 test 반복 조회 금지

##### reduction="none"으로 샘플별 재구성 오류 계산 (PDF p.55)

- `nn.MSELoss(reduction="none")`으로 요소별 오류 유지
- `.mean(dim=1)`로 Feature 축 평균
- Shape는 `[B,F]` → `[B]`로 샘플별 reconstruction error 산출

##### Autoencoder forward와 재구성 오류 (PDF p.56)

- `Linear(8,4)` → `Linear(4,2)` → `Linear(2,4)` → `Linear(4,8)` 사이에 ReLU를 둔 Sequential 구성
- 입력과 재구성 Shape 일치
- 학습 target은 x 자체
- `loss`는 Batch 평균, `score`는 샘플별 오류 `[B]`

#### 실습 04와 Autoencoder 개념 확인

##### 실습 04 · Autoencoder 재구성 (PDF p.57)

- 기본필수는 8차원 정상 데이터를 2차원 Latent로 압축하고 재구성 MSE 기록
- 응용은 Latent 크기 1·2·4를 비교해 압축률과 valid 오류를 표로 작성
- 심화는 Denoising Autoencoder로 노이즈 입력과 깨끗한 target 분리
- 특심화는 Padding 제외 MSE와 valid 임계값 선택 구현, 별도 test 평가는 선택 확장

##### 3분 퀴즈 · Autoencoder (PDF p.58)

- 기본 Autoencoder의 target은 입력 자체, Denoising은 깨끗한 원본임을 확인
- 재구성 오류가 커도 모델 용량·전처리·학습 분포의 영향이 있어 반드시 이상은 아님을 확인
- 이상 탐지 임계값은 valid에서 고정하고 test는 최종 평가에 사용함을 확인

**핵심:** Autoencoder의 재구성 오류는 이상 확정이 아닌 점검 후보 점수이며 임계값은 valid에서만 정하고 예측 지표와 섞지 않음.

### 5교시 · Attention·Transformer Encoder

#### Attention 흐름과 Query·Key·Value

##### Attention으로 입력 위치를 직접 비교한다 (PDF p.59)

- 순차 전달 대신 위치 간 관계를 가중합으로 계산하는 Transformer를 소개하는 구분 슬라이드

##### Transformer Encoder의 한 Batch 흐름 (PDF p.60)

- Token·Feature 입력 → Embedding + Position → Self-Attention → FFN·잔차 정규화 → Pooling·Head 순서

##### Query·Key·Value를 역할로 이해한다 (PDF p.61)

- Query는 현재 위치가 찾는 정보를 나타내는 벡터
- Key는 각 위치가 가진 정보를 비교할 벡터
- Value는 Attention 가중치로 실제 합산할 내용 벡터
- `Softmax(QKᵀ/√d)·V`로 위치별 가중합 생성

#### MultiheadAttention과 Encoder Layer

##### MultiheadAttention으로 Self-Attention (PDF p.62)

- `nn.MultiheadAttention(embed_dim=16, num_heads=4, batch_first=True)`에 `x`를 query·key·value로 전달
- `output`은 `[B,T,E]`로 문맥이 섞인 표현
- `weights`는 `[B,T,T]`로 Head 평균 Attention
- Self-Attention은 query=key=value=x
- `need_weights=False`면 가중치 반환 생략 가능

##### nn.MultiheadAttention · 다중 Head Attention (PDF p.63)

- 필수 인자는 `embed_dim`(입력·출력 Embedding 차원)과 `num_heads`(병렬 Head 수)
- 선택 인자는 `dropout`·`bias`·`batch_first`·`kdim`·`vdim`·`add_bias_kv`·`add_zero_attn`
- forward 반환은 `attn_output`, `attn_output_weights`
- `embed_dim`은 `num_heads`로 나누어떨어져야 함

##### TransformerEncoderLayer 적용 (PDF p.64)

- `d_model=16`, `nhead=4`, `dim_feedforward=32`, `dropout=0.1`, `batch_first=True` 예시
- 구성 요소는 Self-Attention, Residual + LayerNorm, Feedforward Network
- 입력·출력 Shape `[B,T,E]` 유지

#### Mask·Position과 Sequence 분류

##### Padding Mask와 Causal Mask를 구분한다 (PDF p.65)

- Padding Mask `[B,T]`는 Attention에서 Padding key 제외
- MultiheadAttention은 `key_padding_mask`·`attn_mask`, Encoder는 `src_key_padding_mask`·`mask` 인자 사용
- Causal Mask는 미래 위치를 보지 못하게 하며 다음 토큰 예측에 사용
- `nn.MultiheadAttention`의 bool `True`는 차단
- padded query는 Mask와 별도로 집계에서 제외

##### Attention에는 순서 정보가 자동으로 들어가지 않는다 (PDF p.66)

- Token·Feature Embedding에 Position Encoding·Embedding을 더해 순서 정보 추가
- Residual 연결은 입력과 변환 결과를 더해 Gradient 경로 보조
- LayerNorm은 각 위치의 Feature 차원 분포 정규화
- Encoder는 동일 차원의 표현을 여러 층 쌓아 문맥 강화

##### Transformer Encoder Sequence 분류 (PDF p.67)

- `nn.Embedding(64, 16)`으로 위치 표현을 만들어 입력 `[B,T,16]`에 더함
- `src_key_padding_mask`로 key Padding Mask 전달
- 실제 query만 평균해 `[B,16]` 생성 후 Head로 logits `[B,2]` 산출
- 평균 Pooling의 분모가 0이 되지 않도록 각 길이 ≥ 1 조건 유지

#### 실습 05와 Transformer 개념 확인

##### 실습 05 · Self-Attention과 Transformer Encoder (PDF p.68)

- 기본필수는 `[B,5,16]` 입력으로 Attention output·weight Shape 확인
- 응용은 Padding Mask 적용 전후 출력 차이를 비교하고 Mask 위치 시각화
- 심화는 RNN·LSTM·Transformer 분류를 같은 분할·파라미터 범위에서 비교
- 특심화는 Padding·Causal Mask와 head별 통계 구현, padded query는 따로 제외

##### 3분 퀴즈 · Transformer (PDF p.69)

- Self-Attention의 query·key·value는 같은 입력 표현 x를 각각 선형 투영해 사용함을 확인
- Attention 자체는 입력 순서를 구분하지 않아 Position 정보가 필요함을 확인
- Padding 위치는 key padding mask로 Batch별 표시함을 확인

**핵심:** Attention은 순서와 Padding을 스스로 알지 못하므로 Position 추가·key Padding Mask·실제 query만의 Pooling 세 가지가 함께 있어야 올바른 문맥 표현이 됨.

### 6교시 · 아키텍처 비교·Mask·미니 모델

#### 목표에 맞는 구조 선택

##### 목표·길이·자원에 맞는 구조를 선택한다 (PDF p.70)

- 점수 하나가 아니라 입력 구조와 학습 비용을 함께 비교하는 아키텍처 선택을 소개하는 구분 슬라이드

##### Transformer Encoder의 내부 흐름 (PDF p.71)

- Embedding을 Q·K·V로 투영하고 여러 Head가 서로 다른 관계 학습
- Attention 결과를 합친 뒤 Residual·Norm·Feedforward 적용
- 입력 위치를 직접 비교하지만 길이 T가 커지면 Attention 비용 증가
- Reference 구현은 개념 학습용이며 최신 대규모 모델은 추가 최적화 사용

##### RNN·LSTM·Autoencoder·Transformer 비교 (PDF p.72)

- 핵심 연결은 RNN·LSTM의 Hidden·Gate 반복, Autoencoder의 Encoder–Latent–Decoder, Transformer의 Self-Attention
- 주 목표는 RNN·LSTM 분류·예측, Autoencoder 압축·재구성, Transformer 문맥 분류·예측
- 병렬화는 RNN·LSTM 시간축 순차, Autoencoder 층 내부 병렬, Transformer 높음
- 길이 비용은 RNN·LSTM O(T), Autoencoder 입력 차원 의존, Transformer Attention O(T²)
- 핵심 표현은 Hidden·Cell state, Latent z, 위치별 Embedding
- 대표 지표는 RNN·LSTM Accuracy·MSE, Autoencoder Reconstruction error, Transformer Accuracy·AUC·MSE

#### Encoder 구성과 Position Embedding

##### nn.TransformerEncoderLayer · Encoder 기본 블록 (PDF p.73)

- 필수 인자는 `d_model`(입력 Feature·Embedding 차원)과 `nhead`(Head 수)
- 선택 인자는 `dim_feedforward`(기본 2048)·`dropout`(기본 0.1)·`activation`·`batch_first`·`norm_first`·`bias`·`layer_norm_eps`
- 반환 객체는 Self-Attention+FFN Encoder Layer
- `d_model`은 `nhead`로 나누어떨어져야 하며 입력·출력 차원 유지

##### nn.TransformerEncoder · Encoder Layer를 N개 쌓는다 (PDF p.74)

- 필수 인자는 복제할 `encoder_layer`와 반복 수 `num_layers`
- 선택 인자 `norm`은 최종 LayerNorm
- `enable_nested_tensor`·`mask_check`는 최적화·Mask 검사 옵션
- `forward(src, mask=None, src_key_padding_mask=None, is_causal=None)`는 같은 Shape의 출력 반환

##### 학습 가능한 Position Embedding 연결 (PDF p.75)

- `nn.Embedding(max_len, d_model)`로 학습 가능한 위치 표현 생성
- 입력 길이 T는 `max_len` 이하
- Position Shape `[T,E]`를 `[1,T,E]`로 늘려 Batch에 Broadcasting
- Padding Mask는 `src_key_padding_mask`로 Encoder에 전달

#### 비교 실험 설계와 Mask Pooling

##### 아키텍처 비교 조건을 고정한다 (PDF p.76)

- 같은 train·valid·test·Window·Feature·Target 사용
- Epoch·Optimizer·주 지표·선택 규칙을 실험 전에 결정
- 파라미터 수·학습 시간·Peak Memory를 성능과 함께 기록
- Autoencoder 재구성과 분류·예측 성능은 별도 표로 보고

##### Padding Mask를 포함한 평균 Pooling (PDF p.77)

- `padding_mask`의 `True` 위치가 Padding
- 모든 위치가 Padding인 샘플이 있으면 `ValueError`로 중단하며 실제 길이는 1 이상
- Padding 위치를 0으로 채운 뒤 합산
- Pooling 분모는 실제 길이
- 출력 `[B,E]`를 Head에 전달
- 길이 0 입력의 처리 정책 명시

##### 아키텍처 비교표에 반드시 남길 항목 (PDF p.78)

- RNN·LSTM·Transformer 각각에 주 목표·Params·Best Epoch·Valid 지표·시간·메모리 기록
- 표의 값은 모두 직접 측정해 채우는 빈 양식

##### Sequence 모델에서 자주 발생하는 오류 (PDF p.79)

- BTF와 TBF 축 순서를 혼동해 Batch·Time이 뒤바뀌는 오류
- Padding 위치를 마지막 상태·평균 Pooling에 포함하는 오류
- 시점별 예측에서 허용하지 않은 미래 관측을 참조하는 오류
- 서로 다른 목표의 지표·데이터 분할을 한 표에서 직접 순위화하는 오류

#### 실습 06과 아키텍처 비교 확인

##### 실습 06 · 아키텍처 비교와 Mask 처리 (PDF p.80)

- 기본필수는 같은 Sequence 분류 자료에서 RNN·LSTM의 Params·valid Accuracy 비교
- 응용은 Transformer를 추가하고 Padding Mask·Position Embedding 적용
- 심화는 세 모델의 Params·시간·성능·오류 사례를 같은 조건의 표로 작성
- 특심화는 배치 가중 평가·Padding 불변성을 구현하고 같은 분할로 세 모델 비교

##### 3분 퀴즈 · 아키텍처 비교 (PDF p.81)

- RNN·LSTM은 현재 상태가 이전 상태에 의존해 시간축 계산이 순차적임을 확인
- Transformer는 모든 위치 쌍의 T×T 점수를 계산해 길이에 따라 비용이 크게 증가함을 확인
- Autoencoder와 분류 모델의 지표는 목표와 단위가 달라 직접 평균내지 않음을 확인

**핵심:** 아키텍처 비교는 같은 분할·지표·선택 규칙 위에서 성능과 Params·시간·메모리를 함께 기록할 때만 의미가 있고 목표가 다른 모델은 별도 표로 다룸.

### 7교시 · 길이·Padding·CPU/GPU 성능 비교

#### 가변 길이와 공정한 측정 조건

##### 길이·Padding·Device가 성능을 바꾼다 (PDF p.82)

- 같은 입력과 측정 범위를 고정한 뒤 비교하는 성능 측정을 소개하는 구분 슬라이드

##### 가변 길이 Batch와 Mask (PDF p.83)

- 짧은 Sequence에 Padding을 추가해 같은 T로 Batch 구성
- Mask는 실제 값과 Padding을 구분해 Attention·Pooling에서 제외
- Padding 비율이 높으면 불필요한 계산과 메모리 증가
- Bucket·PackedSequence·Nested Tensor는 상황에 따라 효율 향상

##### 공정한 Sequence 모델 비교 조건 (PDF p.84)

- 같은 Sequence 길이 분포·Batch size·dtype·Device·Warm-up 사용
- 데이터 로딩·Padding 생성 시간의 측정 포함 여부를 명시
- GPU는 비동기 실행이므로 시간 측정 전후 `synchronize` 적용
- 평균 시간·samples/s·Peak VRAM·환경·Padding 비율을 함께 기록

##### pack_padded_sequence·pad_packed_sequence (PDF p.85)

- `pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True)`로 PackedSequence 생성
- `pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)`로 Padding Tensor와 lengths 복원
- `lengths`는 CPU Tensor 또는 정수 목록
- RNN·LSTM은 PackedSequence를 입력·출력으로 사용 가능

#### 시간·메모리 측정

##### GPU 시간·Peak Memory 측정 함수 (PDF p.86)

- `torch.cuda.synchronize`·`reset_peak_memory_stats`·`max_memory_allocated`는 필수 위치 인자 없음
- 선택 인자 `device`는 측정할 CUDA Device, 기본 current device
- CUDA 사용 가능 환경에서만 호출하고 CPU에서는 호출하지 않고 N/A 기록
- `synchronize`·`reset`은 반환값 없음, `max_memory_allocated`는 byte 반환
- 측정 범위·Warm-up·반복 횟수를 함께 기록

##### 한 Batch의 순전파를 반복해 시간 측정 (PDF p.87)

- 호출 전 `model.eval()`, `torch.inference_mode()` 안에서 측정
- 입력과 모델은 같은 장치에 두고 전송 시간은 측정에서 제외
- 워밍업 2회 후 20회 순전파 시간 측정이며 한 epoch 측정이 아님
- CUDA일 때만 측정 전후 `synchronize`와 Peak 통계 초기화
- `samples/s = B × 20 / seconds`
- CPU의 VRAM은 N/A
- 전체 상태를 보존하는 측정은 특심화 07 범위

##### Sequence 길이와 속도·메모리의 관계 (PDF p.88)

- 길이 T 16·32·64·128에서 RNN/LSTM 시간·Transformer 시간·Peak VRAM을 직접 측정하는 양식
- 16은 짧은 기준, 32는 비용 증가, 64는 Attention T² 영향, 128은 메모리 한도 확인 관점

#### 결과 기록과 해석

##### 같은 Device에서 모델별 성능을 비교한다 (PDF p.89)

- CPU에서 RNN·LSTM·Transformer의 T·Params·Valid·시간을 기록하고 Peak VRAM은 N/A
- GPU는 같은 표 형식으로 별도 측정
- 장치 비교는 같은 모델을 유지한 상태에서 수행

##### 성능 측정값을 과장하지 않고 해석한다 (PDF p.90)

- GPU 이점은 모델 크기·길이·Batch·전송 비용·커널 최적화에 따라 달라짐
- Transformer가 항상 빠르거나 RNN이 항상 가벼운 것은 아님
- 작은 입력에서는 Launch·전송 오버헤드가 계산 시간을 지배할 수 있음
- 성능표에는 하드웨어·버전·dtype·Mask·측정 범위를 함께 기록

#### 실습 07과 성능 측정 확인

##### 실습 07 · Sequence 모델 시간·메모리 비교 (PDF p.91)

- 기본필수는 RNN 한 Batch의 CPU 시간과 samples/s를 측정하고 조건 기록
- 응용은 LSTM을 CPU에서 측정하고 GPU가 있으면 같은 LSTM 추가 측정
- 심화는 RNN·LSTM·Transformer를 길이 16·32·64에서 비교해 표 작성
- 특심화는 상태를 보존하는 반복 측정과 Profiler 구간을 구현하고 시간 변동 기록

##### 3분 퀴즈 · Sequence 성능 측정 (PDF p.92)

- CUDA 실행이 비동기여서 실제 완료 시점을 맞추려면 `synchronize`가 필요함을 확인
- Padding 비율이 높으면 실제 정보가 아닌 위치에도 연산·메모리를 쓰는 문제 확인
- 길이를 바꾸며 비교할 때 데이터·Batch·dtype·Device·측정 범위·모델 설정을 고정함을 확인

**핵심:** 속도·메모리 수치는 측정 범위·Warm-up·동기화·Padding 비율을 함께 기록할 때만 비교 근거가 되며 GPU 우위를 일반화하지 않음.

### 8교시 · 아키텍처 비교 프로젝트·시연

#### 프로젝트 목표와 구조

##### 최종 프로젝트 · 시계열 예측과 재구성 미니 모델 (PDF p.93)

- LSTM으로 과거 Window에서 다음 시점 값 예측
- Autoencoder로 입력을 압축·복원하고 재구성 오류 기록
- RNN·LSTM·Transformer 비교는 같은 분할·지표·길이에서 수행
- 기본필수는 한 파일 결과와 README 설명 제출
- 상위 단계는 모델 복원·검증까지 제출

##### 심화 참고 · 모듈형 프로젝트 구조 (PDF p.94)

- `day12_sequence_models/main.py`는 실험 실행과 결과 저장
- `models.py`는 RNN·LSTM·Autoencoder·Transformer 정의
- `data.py`는 Window·Padding·Mask·DataLoader 구성
- `train.py`는 train/evaluate·checkpoint·benchmark 함수
- `outputs/`에 `history.csv`·`comparison.csv`·`predictions.csv`·`best_model.pt` 저장
- `reports/architecture_comparison.md`에 선택 근거·오류 사례·한계 기록
- 심화 단계 참고 구조이며 기본필수 요건이 아님

##### 프로젝트 흐름과 단계별 확장 (PDF p.95)

- 자료·Window 확인 → 길이 확인·가변 길이 Mask → LSTM·AE 학습 → 예측·재구성 결과 기록 → 성능표·보고서 → 상위 단계 저장·복원
- 기본필수는 LSTM 예측·AE 재구성·결과표
- 확장 범위는 자기 단계 README 기준

#### 제출물과 통합 실습

##### 단계별 제출물과 기록 내용 (PDF p.96)

- `history.csv`에 epoch·train/valid loss·주 지표·best 표시
- `architecture_comparison.csv`에 모델·Params·길이·Valid·시간·메모리
- `predictions.csv`에 ID·실제값·예측값 또는 재구성 오류
- `best_model.pt`에 state_dict·모델 설정·Feature·길이 정보
- `mask_or_latent.png`에 Padding Mask 또는 Latent·재구성 시각화
- README·report에 실행법·선택 근거·오류 사례·한계·재현 조건
- 기본필수는 자기 폴더 README 기준이며 저장·복원 등은 해당 상위 단계 범위

##### 실습 08 · 아키텍처 비교 프로젝트 통합·시연 (PDF p.97)

- 기본필수는 제공 골격에서 LSTM 예측·Autoencoder 재구성·결과표 저장 완성
- 응용은 최적 모델을 복원하고 클래스별 Recall·실제 오답 기록 추가, TODO 10개
- 심화는 가변 길이·저장 복원과 평가 상태·Padding 불변 테스트 2개 완성
- 특심화는 4회 연속 학습과 2회 저장 후 새 프로세스 재개 비교, 이전 과제 완료 불필요

#### 평가 기준과 검증 상황

##### 형성평가 · 기본필수만으로 100점 (PDF p.98)

- Sequence·Mask 20점은 BTF Shape·Padding·실제 길이·분할 확인
- 모델 구현 25점은 RNN·LSTM·AE·Transformer 중 목표에 맞는 구조와 Shape 설명
- 학습·평가 25점은 자기 단계의 지표·원문 결과·test 보관 설명
- 비교·성능 15점은 측정 조건·모델별 목적·CPU 환경의 한계
- 재현·설명 15점은 실행법·환경·결과 재생성·개인 설명

##### 정상·경계·실패 상황을 구분한다 (PDF p.99)

- 정상 Sequence Batch는 `[B,T,F]`에서 목표 Shape로 변환되고 loss·예측 개수 일치
- 가변 길이·Padding은 Mask로 채움 위치를 제외하며 Pooling·Attention 분모로 판정
- 길이 1 Sequence는 모델이 명확히 처리하며 마지막 상태·Mask Shape로 판정
- 모든 위치가 Padding이면 중단 또는 정책 적용, 0으로 나누지 않음
- 저장 모델 복원은 동일 입력의 출력 대조이며 구조·설정·Feature 일치 확인
- CPU-only 환경은 기본 실습 정상 수행, GPU 항목은 N/A로 device 분기와 보고서에 기록

**핵심:** 프로젝트 완성 기준은 높은 점수가 아니라 목적별 결과표·Padding 경계 처리·재현 가능한 README를 기본필수 범위에서 설명할 수 있는지 여부.

### 마무리 · 정리와 참고자료

#### 전체 정리와 다음 수업

##### 오늘의 핵심 정리 (PDF p.100)

- RNN은 Hidden state, LSTM은 Gate와 Cell state로 순서 정보 처리
- Autoencoder는 압축·재구성하며 재구성 오류를 별도 목표로 해석
- Transformer는 Attention·Position·Mask로 입력 위치 관계를 직접 계산
- 아키텍처 비교는 데이터·지표·길이·시간·메모리·재현 조건을 함께 기록

##### 다음 수업 · 11월 4일 Vision·OpenCV (PDF p.101)

- NumPy 배열과 BGR·RGB 색공간으로 OpenCV 이미지 표현
- Resize·Blur·Edge·형태학 처리
- 이미지·영상 입출력과 Frame 반복
- 원본 대비 전처리 결과 검증과 CNN 전처리 연결
- Vision 프로젝트의 입력 품질 관리

#### 공식 참고자료

##### 공식 참고자료 · PyTorch Sequence Layers (PDF p.102)

- `nn.RNN`·`RNNCell`, `nn.LSTM`·`LSTMCell` 공식 문서
- `pad_sequence`·`pack_padded_sequence`·`pad_packed_sequence` 공식 문서
- `TensorDataset`·`DataLoader`·`MSELoss` 공식 문서

##### 공식 참고자료 · Attention·Transformer (PDF p.103)

- `nn.MultiheadAttention`, `nn.TransformerEncoderLayer`·`TransformerEncoder` 공식 문서
- PyTorch Transformer tutorial과 masking 예제
- Attention Is All You Need 원 논문
