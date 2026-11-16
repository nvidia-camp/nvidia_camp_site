# Day20 강의 구조·핵심 설명

2026-11-13(금) · 생성형 AI·LLM 및 RAG 엔지니어링 4/18 · LLM 생태계 → Token·Context → Transformer·Attention → 학습·추론·일일프로젝트

교시 설명은 PDF p.15 운영표의 핵심 내용 원문입니다. 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준이며 인쇄 쪽수와 같습니다(전체 100쪽). 도입과 마무리는 교시 표시가 없어 별도 묶음으로 두었습니다. 실습 README의 PPT 장 번호는 90장 기준이라 이 PDF 쪽수보다 10 작습니다(예: 실습 01 = README 15장 = PDF p.25).

## 강의 목차

```text
도입 · 현업 질문에서 오늘의 수업 범위까지
├─ 표지
│  └─ 생성형 AI·LLM 및 RAG 엔지니어링 (PDF p.1)
├─ 현업 질문과 시스템 속 LLM 위치
│  ├─ AI Agent가 실제로 답해야 할 업무 질문 (PDF p.2)
│  ├─ AI Agent 전체 시스템에서 LLM의 위치 (PDF p.3)
│  └─ Agent에서 Attention의 작은 계산까지 (PDF p.4)
├─ 질문에서 Token 출력까지 확대
│  ├─ 질문 하나가 Token 출력이 되기까지 (PDF p.5)
│  ├─ LLM 내부의 Transformer Block을 펼쳐 본다 (PDF p.6)
│  ├─ Q·K·V는 어떻게 서로 다른 일을 하는가 (PDF p.7)
│  └─ 작은 Attention 행 하나를 직접 계산한다 (PDF p.8)
├─ 학습·추론과 시스템 판단
│  ├─ 학습과 추론은 무엇이 달라지는가 (PDF p.9)
│  ├─ 현업에서는 어떤 문제에 무엇을 붙이는가 (PDF p.10)
│  └─ 오늘 배운 작은 계산을 Agent 설계로 다시 합친다 (PDF p.11)
├─ 지난 3일과 플랫폼 경로
│  ├─ 지난 3일 · 지식 관리 플랫폼 기반을 완성했다 (PDF p.12)
│  ├─ AI Agent 플랫폼까지 이어지는 경로 (PDF p.13)
│  └─ 3분 확인 · Backend와 LLM의 역할 (PDF p.14)
└─ 오늘 수업 운영
   ├─ 오늘의 8교시 · 개념과 실습을 교차한다 (PDF p.15)
   ├─ 오늘 배우는 원리와 다음 수업의 경계 (PDF p.16)
   ├─ 오늘의 결과물은 “설명 가능한 모델 내부 흐름” (PDF p.17)
   └─ CPU로 충분한 실습과 선택형 모델 다운로드 (PDF p.18)

1교시 · 생성형 AI·LLM 생태계와 서비스 역할
├─ 용어 관계와 다음 Token 생성
│  ├─ AI·생성형 AI·Foundation Model·LLM의 관계 (PDF p.19)
│  └─ LLM은 다음 Token 후보의 점수를 반복 계산한다 (PDF p.20)
├─ 서비스 계층과 활용 범위
│  ├─ 모델·Runtime·API·데이터는 서로 다른 계층 (PDF p.21)
│  ├─ LLM이 도움 되는 작업과 검증이 필요한 작업 (PDF p.22)
│  └─ LLM의 대표적인 한계 네 가지 (PDF p.23)
├─ 지식 DB와 RAG의 연결
│  └─ 이전에 만든 지식 DB가 왜 필요할까? (PDF p.24)
└─ 실습과 확인
   ├─ 실습 01 · AI 서비스 구성요소를 한 장에 연결 (PDF p.25)
   └─ LLM이 맡는 역할 확인 (PDF p.26)

2교시 · Tokenizer·Token ID·Context Window
├─ Token과 Token ID
│  ├─ 문자열은 Tokenizer를 거쳐 정수 ID가 된다 (PDF p.27)
│  ├─ Token과 Token ID는 무엇이 다를까? (PDF p.28)
│  ├─ 실제 Tokenizer로 Token·ID·개수를 확인한다 (PDF p.29)
│  └─ 일반 Token과 다른 구분용 Token (PDF p.30)
├─ Batch 입력 처리
│  └─ Padding·Truncation·Attention Mask를 분리한다 (PDF p.31)
├─ Context Window와 Token 예산
│  ├─ Context Window는 한 요청에서 모델이 참조하는 Token 범위 (PDF p.32)
│  ├─ 문맥 예산을 예시 숫자로 계산한다 (PDF p.33)
│  ├─ 잘림·패딩·마스크를 코드에서 확인한다 (PDF p.34)
│  └─ Token 수를 확인해야 하는 이유 (PDF p.35)
└─ 실습과 확인
   ├─ 실습 02 · 문장별 Token·ID·Context 길이 분석 (PDF p.36)
   └─ Tokenization과 Context 확인 (PDF p.37)

3교시 · Token/Sentence Embedding·유사도
├─ Token ID에서 벡터로
│  ├─ 정수 Token ID를 계산 가능한 벡터로 바꾼다 (PDF p.38)
│  ├─ 벡터의 차원·행렬 shape를 읽는다 (PDF p.39)
│  ├─ Token Embedding과 Sentence Embedding은 목적이 다르다 (PDF p.40)
│  └─ Position 정보가 필요한 이유 (PDF p.41)
├─ Cosine 유사도와 시각화
│  ├─ Cosine Similarity는 벡터의 방향 유사도다 (PDF p.42)
│  ├─ 작은 2차원 벡터의 Cosine 유사도 계산 (PDF p.43)
│  ├─ 2차원 임베딩 지도 · 가까운 점은 어떻게 보일까? (PDF p.44)
│  └─ 문장 임베딩 모델을 사용하는 참고 코드 (PDF p.45)
└─ 실습과 확인
   ├─ 실습 03 · Embedding 벡터와 유사도 시각화 (PDF p.46)
   └─ Embedding과 위치 정보 확인 (PDF p.47)

4교시 · Transformer Block·Position·FFN
├─ 전체 구조와 모델 유형
│  ├─ Transformer는 Attention과 FFN을 층으로 쌓는다 (PDF p.48)
│  └─ Encoder·Decoder·Encoder–Decoder는 목표가 다르다 (PDF p.49)
├─ Block 구성요소와 Tensor shape
│  ├─ Transformer Block의 핵심 구성요소 (PDF p.50)
│  ├─ 한 Batch의 Tensor shape를 따라간다 (PDF p.51)
│  ├─ Residual과 Normalization은 왜 같이 이야기할까? (PDF p.52)
│  ├─ Attention과 FFN은 서로 다른 계산이다 (PDF p.53)
│  └─ 작은 TransformerEncoderLayer의 shape 확인 (PDF p.54)
├─ Position 방식과 생성형 Decoder
│  ├─ 순서 정보를 반영하는 대표 방식 (PDF p.55)
│  └─ 생성형 Decoder는 미래 Token을 보지 않고 다음 것을 예측한다 (PDF p.56)
└─ 실습과 확인
   ├─ 실습 04 · Transformer Block과 Shape 따라가기 (PDF p.57)
   └─ Transformer의 구성 이해 (PDF p.58)

5교시 · Q/K/V·Self-Attention·Mask
├─ Self-Attention의 역할과 Q/K/V
│  ├─ Self-Attention은 “누구의 정보를 얼마나 섞을지” 계산한다 (PDF p.59)
│  └─ Query·Key·Value를 일상 언어로 구분 (PDF p.60)
├─ Scaled Dot-Product Attention 계산
│  ├─ Scaled Dot-Product Attention 수식 읽기 (PDF p.61)
│  ├─ 작은 Q/K/V로 Attention Weight를 직접 계산 (PDF p.62)
│  └─ Causal Attention 가중치를 숫자로 확인 (PDF p.63)
├─ Mask 종류와 Multi-Head
│  ├─ Padding Mask와 Causal Mask가 막는 것은 다르다 (PDF p.64)
│  └─ Multi-Head Attention이 의미하는 것 (PDF p.65)
├─ Attention Weight 해석의 한계
│  ├─ Self-Attention은 Value를 가중합해 표현을 만든다 (PDF p.66)
│  └─ Attention 분석에서 흔히 발생하는 오해 (PDF p.67)
└─ 실습과 확인
   ├─ 실습 05 · Self-Attention 점수·Mask·가중치 시각화 (PDF p.68)
   └─ Self-Attention 핵심 확인 (PDF p.69)

6교시 · 학습·추론·Logit·Decoding
├─ 학습과 추론의 차이
│  ├─ 학습과 추론은 모델 파라미터를 다루는 방식이 다르다 (PDF p.70)
│  ├─ Causal Language Modeling의 대표 학습 흐름 (PDF p.71)
│  └─ 사전학습 뒤 모델을 활용하는 세 방법 (PDF p.72)
├─ Logit에서 확률로
│  ├─ 마지막 Hidden State에서 어휘 전체 Logit을 얻는다 (PDF p.73)
│  └─ Softmax·Temperature가 분포를 바꾸는지 확인 (PDF p.74)
├─ Decoding과 생성 반복
│  ├─ Greedy·Temperature·Top-k·Top-p 비교 (PDF p.75)
│  ├─ Autoregressive Decoding은 한 Token씩 문맥을 확장한다 (PDF p.76)
│  └─ KV Cache의 이점과 대가 (PDF p.77)
└─ 실습과 확인
   ├─ 실습 06 · 학습·추론 흐름과 Token 확률 비교 (PDF p.78)
   └─ 학습과 추론 차이 확인 (PDF p.79)

7교시 · 모델 한계·검증·RAG/Agent 경계
├─ 실패 위치와 품질 평가
│  ├─ LLM의 답변이 틀릴 수 있는 네 위치 (PDF p.80)
│  └─ 출력 품질은 한 개의 숫자로 끝나지 않는다 (PDF p.81)
├─ Prompt·RAG·Fine-tuning·Agent의 경계
│  ├─ Prompt·RAG·Fine-tuning·Agent가 해결하는 문제 (PDF p.82)
│  ├─ 11/20의 Basic RAG에서 오늘 배운 지식을 다시 쓴다 (PDF p.83)
│  └─ Agent 플랫폼을 만들 때도 필요한 검증 (PDF p.84)
├─ 지식 관리 API 연결 사례
│  └─ 지식 관리 API에 LLM을 연결하면 무엇이 새로 생길까? (PDF p.85)
└─ 실습과 확인
   ├─ 실습 07 · LLM 실패 위치와 보완 방법 매칭 (PDF p.86)
   └─ LLM의 한계와 RAG·Agent의 역할 (PDF p.87)

8교시 · 일일프로젝트·전체 흐름 검증
├─ 프로젝트 흐름과 공통 데이터
│  ├─ 일일프로젝트 · 문장 하나가 LLM 출력이 되기까지 (PDF p.88)
│  └─ 프로젝트 공통 사례: AI 도움말 지식 3건 (PDF p.89)
├─ 작업과 결과 설명
│  ├─ 프로젝트 4개 작업과 남길 증거 (PDF p.90)
│  ├─ 프로젝트 결과를 한 장으로 설명하는 순서 (PDF p.91)
│  └─ 실습 08 · LLM 입력→출력 미니프로젝트 종합 (PDF p.92)
└─ 평가와 진행
   ├─ 평가 기준 · 기본필수만으로 100점 (PDF p.93)
   ├─ 검증할 오류·혼동 사례 (PDF p.94)
   └─ 마지막 50분의 작은 프로젝트 (PDF p.95)

마무리 · 다음 수업과 참고자료
├─ 다음 수업과 정리
│  ├─ 다음은 “모델을 어떻게 지시하고 입력을 구성할까?” (PDF p.96)
│  └─ 오늘의 핵심 개념을 한 번 더 정리한다 (PDF p.97)
├─ 공식 참고자료
│  ├─ 공식 참고자료 · 모델·Token·Attention (PDF p.98)
│  └─ 공식 참고자료 · 문장 임베딩·모델 활용 (PDF p.99)
└─ 마무리
   └─ LLM 원리를 AI 플랫폼의 기능으로 연결한다 (PDF p.100)
```

## 핵심 설명

### 도입 · 현업 질문에서 오늘의 수업 범위까지

#### 표지

##### 생성형 AI·LLM 및 RAG 엔지니어링 (PDF p.1)

- 정규교과 4/18 표지
- 오늘의 흐름은 LLM 생태계 → Token·Context → Transformer·Attention → 학습·추론·일일프로젝트

#### 현업 질문과 시스템 속 LLM 위치

##### AI Agent가 실제로 답해야 할 업무 질문 (PDF p.2)

- 가상의 사내 IT 지원 문의 “FastAPI에서 PostgreSQL 연결이 안 됩니다.” 한 건을 수업 전체에서 추적
- 필요한 답변은 증상 설명·근거 문서·확인 절차
- 실행 권한이 필요한 행동은 별도 승인 대상
- 앞 3일은 FastAPI·DB, 오늘은 LLM 언어 처리, 이후는 RAG·Agent 도구
- 문장을 생성하는 부분과 근거 검색·실제 명령 실행 부분은 서로 다른 계층

##### AI Agent 전체 시스템에서 LLM의 위치 (PDF p.3)

- 사용자 → FastAPI(요청·응답·검증) → Agent 처리(분기·상태·승인) → LLM(문맥을 읽고 다음 Token 생성)의 업무 처리 아키텍처 예시
- RAG는 원본 문서·검색용 벡터 인덱스에서 근거 제공
- Tool은 허용된 API로 업무 시스템을 실행하며 권한·승인·기록 포함
- RAG 근거는 LLM의 Context로 들어가고 Tool 실행 권한은 Backend가 확인
- 실제 서비스의 호출 순서와 수업 진도 순서는 별개

##### Agent에서 Attention의 작은 계산까지 (PDF p.4)

- AI Agent 서비스 → LLM 호출 → Transformer 층 반복 → Transformer Block → Self-Attention → Q/K/V·Mask·Softmax의 여섯 단계 확대
- Transformer Block은 Attention + FFN + Residual / Norm으로 구성
- Self-Attention은 Token 사이 관계를 계산해 표현을 섞는 단계
- 가장 작은 단계는 Score → Weight → Value 가중합
- Tokenizer는 Block 내부가 아니라 모델 입력을 준비하는 별도 단계

#### 질문에서 Token 출력까지 확대

##### 질문 하나가 Token 출력이 되기까지 (PDF p.5)

- 예시 Context는 사용자 질문 + 필요 시 검색된 근거 + 시스템 지시
- 문자열 → Tokenizer → Token ID → Embedding → Transformer → LM Head → Decode의 처리 순서
- 출력 Token은 문맥 끝에 다시 붙고 종료 조건까지 다음 Token 예측 반복
- Token ID는 정수 인덱스이며 임베딩 벡터가 아님
- Logit은 아직 확률이 아닌 점수

##### LLM 내부의 Transformer Block을 펼쳐 본다 (PDF p.6)

- `[B, T, D]` Token 벡터가 Transformer Block 1~N을 차례로 통과
- Block 내부는 Self-Attention(Token 간 정보 교환) → Residual / Norm → Feed-Forward(Token별 비선형 변환) → Residual / Norm
- 마지막 위치의 표현을 LM Head에 넣어 Vocabulary 전체 점수 계산
- Attention 외에 FFN·Residual·Norm이 필요하며 실제 모델별 순서는 다를 수 있음

##### Q·K·V는 어떻게 서로 다른 일을 하는가 (PDF p.7)

- 입력 X에 각각 다른 가중치를 곱해 `Q = XWq`, `K = XWk`, `V = XWv` 계산
- Q는 현재 위치의 질문, K는 비교 대상의 특징, V는 전달할 값
- `QKᵀ / √dₖ`로 관계 점수를 만들고 Mask + Softmax로 참고 비율 결정
- Weight × V로 문맥화된 표현을 만들고 이후 출력 투영·잔차 등과 합산
- Q·K 비교는 참고 비율을 정하고 V는 실제 섞이는 정보를 제공

##### 작은 Attention 행 하나를 직접 계산한다 (PDF p.8)

- Value 벡터 t1 `[1, 0]`, t2 `[0, 1]`, t3 `[1, 1]`과 Causal Mask 적용 후 Weight 행렬 사용
- 마지막 t3 행 Weight `[0.25, 0.25, 0.50]`으로 Value를 가중합하면 결과 ≈ `[0.75, 0.75]`
- t1 행은 미래 위치 Weight가 0이고 각 행의 합은 1
- 표의 값은 반올림한 교육용 값
- Mask가 미래 정보를 가리고 Softmax가 가중치를 만들며 V의 합성이 출력

#### 학습·추론과 시스템 판단

##### 학습과 추론은 무엇이 달라지는가 (PDF p.9)

- 두 과정 모두 입력 Token → Logit 계산까지는 동일
- Training은 정답 Token과 Loss를 비교하고 `backward()` → `optimizer.step()`으로 가중치 업데이트
- Inference는 디코딩으로 다음 Token을 선택해 붙이는 과정을 반복하며 가중치 고정
- Inference에서는 KV Cache 사용 가능
- 학습 목표는 예측 오차 감소, 추론 목표는 요청에 맞는 다음 Token 생성
- 오늘은 LLM 내부 원리 이해이며 실제 서비스 호출은 이후 API 수업과 연결

##### 현업에서는 어떤 문제에 무엇을 붙이는가 (PDF p.10)

- 문장 요약·정리는 LLM 생성에 내용·형식 검증을 결합
- 사내 규정에 근거한 답변은 Retriever → LLM(RAG)에 출처·최신성 검증을 결합
- 실제 시스템 상태 조회·변경은 Agent → 허용된 Tool API에 권한·승인·감사 기록을 결합
- 필요한 기능과 검증 범위를 함께 설계
- RAG는 근거 검색 + 생성, Agent는 상태·도구 실행을 포함한 처리 시스템
- LLM은 답을 제안하고 실제 실행 권한은 Backend가 판단

##### 오늘 배운 작은 계산을 Agent 설계로 다시 합친다 (PDF p.11)

- 같은 가상 사례로 Token(Token·ID·길이) → Embedding(벡터·Cosine) → Attention(Q/K/V·Mask·행 합) → Output(Logit → 다음 Token) 연결
- 마지막 한 장 설명은 FastAPI·DB → (근거 검색) → LLM Token 생성 → Agent Tool 제어의 흐름
- 학습 결과는 단계별 수치·흐름도·계층별 책임과 한계 기록
- 기본필수는 제공된 작은 CPU 예제로 완성
- LLM 학습과 Agent 도구 실행은 후속 단계

#### 지난 3일과 플랫폼 경로

##### 지난 3일 · 지식 관리 플랫폼 기반을 완성했다 (PDF p.12)

- 11/10 FastAPI의 `/api/knowledge` CRUD와 JSON 파일 저장
- 11/11 PostgreSQL의 knowledge·categories 테이블, PK/FK·SQL·트랜잭션
- 11/12 연동으로 같은 API 요청이 실제 PostgreSQL 행에 반영
- 오늘은 그 플랫폼 위에서 동작할 언어 모델의 원리 이해

##### AI Agent 플랫폼까지 이어지는 경로 (PDF p.13)

- FastAPI(지식 API) → PostgreSQL(원본 지식 DB) → LLM(Token·Attention) → RAG·Agent(검색·생성·도구)의 학습 진도 순서
- 실제 RAG 요청에서는 검색 근거를 먼저 LLM 입력에 제공
- 이후 일정은 11/16 Prompt → 11/18 Embedding → 11/19 Chunking → 11/20 Basic RAG

##### 3분 확인 · Backend와 LLM의 역할 (PDF p.14)

- PostgreSQL은 관계형 저장소이며 문장 의미 생성·추론은 별도 모델 담당
- FastAPI는 요청을 모델 처리에 연결하는 서비스 입구이며 다음 Token을 예측하지 않음
- LLM만 연결해도 Agent가 완성되지 않으며 도구·상태·권한·평가·운영 흐름은 별도 설계

#### 오늘 수업 운영

##### 오늘의 8교시 · 개념과 실습을 교차한다 (PDF p.15)

- 교시마다 설명과 실습을 교차하며 1~7교시는 50분을 설명 20~25분·실습 25~30분으로 배분
- 1교시 생성형 AI·LLM 생태계, 2교시 Tokenizer·Context Window, 3교시 Embedding·유사도, 4교시 Transformer Block
- 5교시 Q/K/V·Self-Attention·Mask, 6교시 학습·추론·Decoding, 7교시 모델 한계·RAG/Agent 경계
- 8교시는 설명 10분·실습 40분의 일일프로젝트

##### 오늘 배우는 원리와 다음 수업의 경계 (PDF p.16)

- 오늘 11/13은 생성형 AI·Foundation Model·LLM, Tokenization·Context Window, Transformer·Self-Attention·Position, Embedding·학습/추론 흐름, LLM 활용·한계·평가
- 다음 11/16은 System/User 메시지, Zero/Few-shot·CoT, Context Engineering, JSON Schema·출력 검증·재시도, Prompt A/B 실험
- 11/17 LLM API → 11/18 Embedding/Vector DB → 11/20 Basic RAG는 오늘 구현하지 않음

##### 오늘의 결과물은 “설명 가능한 모델 내부 흐름” (PDF p.17)

- 개념도는 문장 입력부터 다음 Token 출력까지 6~8단계 연결
- Token 분석은 문장별 Token·ID·개수·잘림 여부 확인
- Embedding 분석은 벡터 차원·Cosine 유사도와 표현 차이 해석
- Attention 분석은 Q/K/V·Mask·Weight를 표와 그림으로 설명
- 공통 목표는 수치·그림·용어가 어떤 코드 동작과 연결되는지 설명

##### CPU로 충분한 실습과 선택형 모델 다운로드 (PDF p.18)

- 공통 실습은 Python·NumPy/PyTorch로 작은 Tensor와 표를 직접 계산
- Transformers tokenizer는 사전 캐시 또는 인터넷 다운로드가 필요한 선택 항목
- Sentence Transformer 가중치 다운로드는 장비·네트워크에 따라 생략 가능
- 결과 숫자보다 shape·mask·입력과 출력의 의미를 확인
- 커리큘럼 기준 버전은 Transformers 5.17 · sentence-transformers 6.1 · PyTorch 2.14

**핵심:** 오늘의 LLM은 지식 API·DB 위에서 문맥을 읽고 다음 Token을 만드는 한 계층이며, 근거 검색과 도구 실행은 다른 계층이 맡음.

### 1교시 · 생성형 AI·LLM 생태계와 서비스 역할

#### 용어 관계와 다음 Token 생성

##### AI·생성형 AI·Foundation Model·LLM의 관계 (PDF p.19)

- AI는 언어·시각·판단 등 넓은 지능적 작업을 수행하는 기술
- 생성형 AI는 학습한 패턴으로 텍스트·이미지·음성 등을 생성
- Foundation Model은 대규모 사전학습 뒤 여러 다운스트림 작업에 활용하는 모델
- LLM은 언어 Token의 통계적 관계를 학습한 대규모 언어 모델

##### LLM은 다음 Token 후보의 점수를 반복 계산한다 (PDF p.20)

- 입력 Token(문맥 구성) → Transformer(은닉 표현) → 출력 Logits(후보 점수) → Token 선택(문맥 갱신)의 한 단계
- 간단화한 autoregressive 언어 생성 과정
- 유창한 출력과 사실 검증은 별개

#### 서비스 계층과 활용 범위

##### 모델·Runtime·API·데이터는 서로 다른 계층 (PDF p.21)

- 모델 계층은 Tokenizer·가중치·Transformer이며 입력을 어떤 표현으로 바꾸는지가 질문
- Runtime 계층은 PyTorch·추론 엔진이며 어디서 어떤 자원으로 실행하는지가 질문
- 서비스 계층은 FastAPI·요청·응답이며 누가 어떻게 기능을 호출하는지가 질문
- 데이터 계층은 PostgreSQL·문서·Metadata이며 어떤 지식과 출처를 보관하는지가 질문
- 운영 계층은 권한·평가·로그·비용이며 어디까지 신뢰하고 통제하는지가 질문
- 모델 설치만으로 서비스의 인증·근거·정확성은 보장되지 않음

##### LLM이 도움 되는 작업과 검증이 필요한 작업 (PDF p.22)

- 활용하기 좋은 예는 FAQ 초안·요약·분류, 자유형 텍스트의 형식 변환, Python 코드 초안·설명·테스트 제안, 대화형 지식 탐색 보조
- 검증 없이 위험한 예는 출처 불명확한 정책·법률 답변, 실시간 운영 상태를 안다는 주장
- 승인 없이 DB를 수정·삭제하는 Agent와 개인정보·비밀 정보의 그대로 전달도 위험한 예
- LLM 출력은 후보 답변이며 정확성·권한·출처 검증은 애플리케이션에서 설계

##### LLM의 대표적인 한계 네 가지 (PDF p.23)

- Hallucination은 틀렸거나 근거 없는 내용을 그럴듯하게 생성하는 현상
- 지식 시점 한계로 학습 이후의 변경과 내부 문서는 자동 반영되지 않음
- Context·비용 한계는 입력 길이·요금·응답시간·장비 자원의 제약
- 보안·권한 판단과 개인정보 보호는 프롬프트만으로 완성되지 않음

#### 지식 DB와 RAG의 연결

##### 이전에 만든 지식 DB가 왜 필요할까? (PDF p.24)

- LLM에 필요한 외부 지식을 검색·수집해 입력에 추가하기 위한 저장소
- 사용자 질문 → Retriever(근거 찾기) → LLM(문맥에 근거 사용) → 응답(출처·검증)의 흐름
- RAG는 검색과 생성을 연결하는 구조
- DB를 만들었다고 자동으로 RAG가 되지 않음

#### 실습과 확인

##### 실습 01 · AI 서비스 구성요소를 한 장에 연결 (PDF p.25)

- 기본필수는 제공된 4개 상자(API·DB·LLM·응답)를 올바른 순서로 연결하고 역할을 한 문장씩 작성
- 응용은 검색 기능과 근거·검증 단계를 추가하고 “저장”과 “생성” 책임 구분
- 심화는 RAG·Agent의 Tool·권한·평가 위치를 표시하되 오늘 구현한 것과 후속 구현을 구분
- 완료 기준은 구성요소를 빠짐없이 설명하고 각 화살표가 전달하는 데이터를 설명
- 결과물은 `architecture.md/.json`

##### LLM이 맡는 역할 확인 (PDF p.26)

- DB는 데이터를 보관·조회하고 LLM은 표현을 계산·생성하므로 같은 저장소가 아님
- 유창한 문장도 사실·근거 검증을 별도로 수행
- 지식 DB에서 검색한 문장은 LLM 학습이 아니라 추론 시 문맥을 구성하는 RAG 방식

**핵심:** LLM의 출력은 검증 전의 후보 답변이며, 저장·생성·검색·실행 책임을 계층별로 나누어 판단.

### 2교시 · Tokenizer·Token ID·Context Window

#### Token과 Token ID

##### 문자열은 Tokenizer를 거쳐 정수 ID가 된다 (PDF p.27)

- 원문 텍스트 → Tokenizer → Token 조각 → Vocabulary ID의 변환 순서
- Token은 언어 모델이 다루는 분할 단위이며 띄어쓰기 단어와 반드시 같지 않음
- 같은 문장도 모델에 따라 Token 수가 달라질 수 있음

##### Token과 Token ID는 무엇이 다를까? (PDF p.28)

- Token은 문자열을 모델 규칙에 따라 나눈 텍스트 조각이며 한글·영어·숫자·기호 조합 가능
- 공백 표식이 Token에 포함될 수도 있음
- Token ID는 Token을 Vocabulary에서 찾은 정수 인덱스
- 번호의 크기 자체는 의미의 크기가 아님
- Token ID는 Embedding Table의 행 선택에 사용하며 임베딩 벡터와 다름
- 슬라이드의 분할 예시는 개념용이며 실제 모델 Tokenizer 출력과 혼동하지 않음

##### 실제 Tokenizer로 Token·ID·개수를 확인한다 (PDF p.29)

- `AutoTokenizer.from_pretrained("bert-base-multilingual-cased")`로 Tokenizer 준비
- `input_ids`는 정수 배열이며 `convert_ids_to_tokens`로 Token 조각 확인
- Tokenizer는 모델마다 다름
- Special Token도 개수에 포함될 수 있음
- 원문 문자 수와 Token 수는 다름
- 최초 실행에 모델 Tokenizer 다운로드가 필요하며 어려우면 제공된 수치 예제로 대체

##### 일반 Token과 다른 구분용 Token (PDF p.30)

- BOS·EOS는 시작·종료 경계를 나타내며 사용하는 모델이 따로 있음
- PAD는 배치의 길이를 맞추는 데 사용
- Chat Role은 system·user·assistant 등의 역할 구분과 형식화 표기
- Special Token의 표기·ID·사용 여부는 모델·Tokenizer에 따라 다름

#### Batch 입력 처리

##### Padding·Truncation·Attention Mask를 분리한다 (PDF p.31)

- Padding은 길이가 다른 문장들을 한 배치로 맞추는 처리이며 짧은 입력 뒤에 PAD 추가
- Truncation은 입력 길이 제한이며 넘친 Token은 잘릴 수 있음
- Attention Mask는 실제 Token과 패딩 Token을 1·0 등으로 구분
- Causal Mask는 미래 Token을 보지 못하게 제한하며 Decoder 생성에서 삼각 형태
- 실제 잘리는 위치와 Special Token 추가 정책은 API 호출 옵션에 따라 다름

#### Context Window와 Token 예산

##### Context Window는 한 요청에서 모델이 참조하는 Token 범위 (PDF p.32)

- System·지시, User·대화, 검색 문맥, 출력 Token이 모두 예산의 일부
- Context Window는 영구 Memory가 아님
- 많이 넣을수록 좋은 구조가 아님

##### 문맥 예산을 예시 숫자로 계산한다 (PDF p.33)

- 예시 배분은 System + 지시 300, 이전 대화 1,200, 검색 근거 2,000, User 질문 150, 출력 예약 850 Token
- 출력에 쓸 Token도 미리 예약하는 구조
- 표는 산술 예시이며 실제 모델의 최대 길이나 과금 정책이 아님

##### 잘림·패딩·마스크를 코드에서 확인한다 (PDF p.34)

- 길이가 다른 두 문장 `["AI", "FastAPI와 PostgreSQL"]`을 `padding=True`, `truncation=True`, `max_length=12`로 처리
- 두 문장의 길이가 달라도 Tensor 길이를 맞춤
- `max_length`는 입력 상한
- `attention_mask`로 유효 Token 위치 확인
- 이 마스크는 Padding 위치 확인용이며 Causal Mask와 다름
- `tok`는 p.29에서 준비한 Tokenizer 재사용

##### Token 수를 확인해야 하는 이유 (PDF p.35)

- 입력 길이와 생성 길이는 계산량과 응답 지연 시간에 영향
- API는 입력·출력 Token 단위 과금이 흔함
- 너무 긴 문맥은 잡음·잘림과 근거 누락을 유발할 수 있음

#### 실습과 확인

##### 실습 02 · 문장별 Token·ID·Context 길이 분석 (PDF p.36)

- 기본필수는 제공된 문장 3개의 Token·Token ID·개수·Special Token 여부 기록
- 응용은 Padding·Truncation을 적용한 두 길이 조건에서 결과와 `attention_mask` 비교
- 심화는 한국어·영어·코드 입력을 비교하고 실제 문맥 예산과 잘림 위험 설명
- 완료 기준은 입력/출력 Token 수와 자르는 규칙의 영향을 구분해 설명
- 기본 실습은 교육용 ToyTokenizer를 사용하며 실제 BERT Tokenizer 결과와 다름
- 결과물은 `token_report.json`

##### Tokenization과 Context 확인 (PDF p.37)

- Token은 단어 하나가 아니라 모델별 Tokenizer의 분할 단위
- ID 크기는 단어의 중요도가 아니라 Vocabulary 인덱스
- Truncation은 요약이 아니라 Token을 잘라내는 처리이며 정보 손실 가능

**핵심:** Token 수는 모델별로 달라지고 System·대화·근거·출력이 같은 Context 예산을 나누어 쓰므로, 잘림과 Mask가 어떤 Token에 적용되는지 확인.

### 3교시 · Token/Sentence Embedding·유사도

#### Token ID에서 벡터로

##### 정수 Token ID를 계산 가능한 벡터로 바꾼다 (PDF p.38)

- Token ID → Embedding 행 조회 → d차원 Vector → Transformer 입력의 흐름
- Embedding은 Token/문장을 숫자 좌표로 표현하는 방법
- Token ID는 숫자 인덱스이고 Embedding은 학습된 연속값 벡터

##### 벡터의 차원·행렬 shape를 읽는다 (PDF p.39)

- ID 한 개는 `()`로 정수 하나
- 한 Token Vector는 `(4,)`로 연속 수치 네 개
- 문장의 Token 벡터는 `(5, 4)`로 Token 5개 × feature 4
- Batch 입력은 `(2, 5, 4)`로 Batch 2 × Token 5 × feature 4
- 작은 교육용 숫자이며 실제 모델의 d_model은 구조마다 다름

##### Token Embedding과 Sentence Embedding은 목적이 다르다 (PDF p.40)

- Token Embedding은 Token 단위 숫자 표현이며 모델 입력에서 여러 Token 벡터 사용
- Token Embedding은 뒤의 Attention 층을 거치며 문맥에 따른 Hidden State로 변환
- Token Embedding의 위치 정보는 별도로 반영
- Sentence Embedding은 문장·문서 전체를 대표하는 하나의 벡터이며 의미적 근접성 비교·검색에 사용
- Sentence Embedding은 Pooling·학습 목적에 따라 표현이 달라지며 11/18 검색·Vector DB로 확장
- Token Vector의 단순 평균이 항상 좋은 의미 벡터가 되지는 않음

##### Position 정보가 필요한 이유 (PDF p.41)

- 순서가 다른 문장을 구분하려면 Token의 위치·상대 위치 반영 필요
- Token 정보 + Position 정보 → Transformer 표현 → 문맥별 Hidden State
- 위치는 새로운 Token이 아니라 벡터 계산에 반영되는 정보

#### Cosine 유사도와 시각화

##### Cosine Similarity는 벡터의 방향 유사도다 (PDF p.42)

- Cosine = 1은 방향이 같은 양의 유사도
- Cosine = 0은 직교이며 방향 관련이 적음
- Cosine = -1은 방향이 반대인 음의 유사도
- 높은 Cosine 유사도가 정답·사실성·출처 적절성을 보장하지 않음

##### 작은 2차원 벡터의 Cosine 유사도 계산 (PDF p.43)

- `a=[1.0, 0.0]`, `b=[0.8, 0.2]`, `c=[-1.0, 0.0]`을 `F.cosine_similarity(..., dim=0)`로 비교
- a와 b는 방향이 비슷하고 a와 c는 반대 방향
- b가 단위 길이가 아니어도 cosine은 방향만 비교
- 결과는 벡터 자체를 비교한 값
- 모델 다운로드 없이 CPU에서 계산 가능

##### 2차원 임베딩 지도 · 가까운 점은 어떻게 보일까? (PDF p.44)

- 실습 안내 A·B는 가까이, 주문 FAQ는 멀리 놓인 교육용 2D 좌표 예시
- 차원 축소 그림과 실제 모델의 의미 품질은 다를 수 있음

##### 문장 임베딩 모델을 사용하는 참고 코드 (PDF p.45)

- `SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")`의 `encode`로 문장 벡터 생성
- `vectors.shape`로 문장 개수 × 벡터 차원 확인
- `model.similarity`로 의미가 가까운 문장 점수 비교
- 사전학습 문장 모델 다운로드가 필요한 선택 시연
- 영어 비교 예시이며 한국어 성능으로 일반화하지 않음
- 공식 문서 기준 all-MiniLM-L6-v2 출력은 384차원

#### 실습과 확인

##### 실습 03 · Embedding 벡터와 유사도 시각화 (PDF p.46)

- 기본필수는 제공된 2D 벡터 3개를 비교하고 cosine 값의 의미 설명
- 응용은 단어 대신 문장별 벡터 후보를 비교하며 2D 점 그래프 작성
- 심화는 Token/Sentence Embedding 차이와 2D 투영 한계를 근거로 결과 해석
- 완료 기준은 차원·벡터·유사도·시각화의 한계 설명
- 교육용 2D 벡터는 사전학습 의미 임베딩이 아님
- 결과물은 `vectors.png`, `cosine_report.json`이며 기준값은 A-B ≈ 0.9701, A-C = -1

##### Embedding과 위치 정보 확인 (PDF p.47)

- Token ID는 정수 인덱스, Token Embedding은 연속 벡터
- Cosine 유사도와 사실·근거 품질은 별개
- 순서가 달라지면 위치 정보와 문맥 처리로 다른 표현이 됨

**핵심:** Embedding은 Token ID를 연속 벡터로 바꾼 표현이고, Cosine은 방향의 가까움만 재므로 사실성이나 근거 품질과 구분.

### 4교시 · Transformer Block·Position·FFN

#### 전체 구조와 모델 유형

##### Transformer는 Attention과 FFN을 층으로 쌓는다 (PDF p.48)

- Decoder-only LLM의 입력 처리 한 묶음을 단순화한 그림
- Token + Position → Masked Attention → FFN·Residual·Norm → 반복 Blocks의 흐름
- Encoder / Decoder / Encoder–Decoder 구조를 구분

##### Encoder·Decoder·Encoder–Decoder는 목표가 다르다 (PDF p.49)

- Encoder는 문장 표현·분류·검색 입력에 쓰이며 Attention은 대체로 양방향
- Decoder-only는 다음 Token 생성·대화에 쓰이며 Attention은 대체로 Causal
- Encoder–Decoder는 번역·요약 등 조건부 생성에 쓰이며 Encoder 양방향 + Decoder Causal
- 기초 수업은 구조별 입력/출력 계약 비교이며 모델 구현 전체는 요구하지 않음

#### Block 구성요소와 Tensor shape

##### Transformer Block의 핵심 구성요소 (PDF p.50)

- Self-Attention은 각 Token이 사용할 문맥 정보를 섞음
- Feed Forward는 각 위치 표현을 비선형 변환
- Residual은 기존 표현을 더해 정보·기울기 흐름을 도움
- LayerNorm은 표현의 스케일을 조절해 학습 안정화

##### 한 Batch의 Tensor shape를 따라간다 (PDF p.51)

- Token IDs `(2, 5)`는 2문장 · 문장당 5 Token
- Token Embedding `(2, 5, 8)`은 각 Token이 8차원 벡터
- Attention output `(2, 5, 8)`은 문맥을 반영한 위치별 표현
- FFN output `(2, 5, 8)`은 Token별 표현 변환 결과
- LM Head logits `(2, 5, 100)`은 Token 위치별 어휘 100개 점수
- 배치/시퀀스/특징 차원과 모델 파라미터 수를 혼동하지 않음

##### Residual과 Normalization은 왜 같이 이야기할까? (PDF p.52)

- 입력 x → Attention 또는 FFN → Skip Add `x + f(x)` → LayerNorm의 순서
- 두 모듈 모두 많은 층을 안정적으로 학습시키는 역할
- Residual은 Attention이 아니라 표현에 기존 정보를 더하는 경로

##### Attention과 FFN은 서로 다른 계산이다 (PDF p.53)

- Attention은 Query·Key·Value로 Token들 사이의 문맥을 섞는 계산
- Attention은 Mask에 따라 볼 수 있는 위치가 달라지고 문장 길이와 Attention 행렬 크기가 연관
- FFN은 각 Token 위치 벡터에 두 개 이상의 선형 변환·활성화를 적용
- FFN은 같은 가중치를 각 위치에 공유하며 Token 간 직접 섞는 단계가 아님
- Self-Attention 하나가 Transformer 전체를 대신하지 않음

##### 작은 TransformerEncoderLayer의 shape 확인 (PDF p.54)

- `nn.TransformerEncoderLayer(d_model=8, nhead=2, dim_feedforward=16, batch_first=True, dropout=0.0)`에 `torch.randn(2, 5, 8)` 입력
- `d_model=8`은 Token feature 크기
- `nhead=2`는 Attention Head 수
- `batch_first=True`이면 `(B, T, D)` 형식
- 출력 shape는 입력과 같음
- Encoder Layer 구조의 shape 학습용이며 Decoder-only 생성 모델 구현이 아님

#### Position 방식과 생성형 Decoder

##### 순서 정보를 반영하는 대표 방식 (PDF p.55)

- Sinusoidal은 원 Transformer 논문의 고정된 위치 인코딩
- Learned Position은 위치별 학습 벡터를 사용하는 방식
- RoPE는 Attention 계산에서 상대 위치 정보를 회전 형태로 반영
- 오늘의 범위는 순서 정보를 반영한다는 공통 개념

##### 생성형 Decoder는 미래 Token을 보지 않고 다음 것을 예측한다 (PDF p.56)

- 이전 입력 Token → Causal Attention → 마지막 상태 → LM Head → Logits의 흐름
- Causal Mask가 현재 위치보다 나중의 정답 Token을 가림
- 추론에서는 새 Token을 선택해 입력 끝에 붙이는 과정 반복

#### 실습과 확인

##### 실습 04 · Transformer Block과 Shape 따라가기 (PDF p.57)

- 기본필수는 제공된 구조도의 Token → Attention → FFN → 출력 순서를 채우고 shape 읽기
- 응용은 Residual·LayerNorm을 표시하고 Encoder와 Decoder의 Mask 차이 설명
- 심화는 PyTorch EncoderLayer의 `batch_first`·head 수를 바꾸고 출력 차원과 제약 검증
- 완료 기준은 Block 구성요소의 역할과 `(B,T,D)` 구분
- 결과물은 `transformer_report.json`이며 기준 shape는 2×5 → 2×5×8 → 2×5×8

##### Transformer의 구성 이해 (PDF p.58)

- Self-Attention만으로는 Transformer 전체가 아니며 FFN·Residual·Norm 등이 함께 필요
- Encoder는 대체로 양방향, 자기회귀 Decoder는 Causal
- `(2,5,8)`의 8은 Token 수가 아니라 feature 차원

**핵심:** Transformer Block은 Token 사이를 섞는 Attention과 위치별로 변환하는 FFN, 이를 안정화하는 Residual·Norm의 조합이며 `(B, T, D)` shape를 유지.

### 5교시 · Q/K/V·Self-Attention·Mask

#### Self-Attention의 역할과 Q/K/V

##### Self-Attention은 “누구의 정보를 얼마나 섞을지” 계산한다 (PDF p.59)

- Query·Key·Value → `QKᵀ` 점수 → Mask + Softmax → 가중합 출력의 순서
- 각 Token의 Query가 다른 Token의 Key와 비교되어 Value를 가중합
- 가중치가 크다는 사실만으로 모델의 판단 원인을 모두 설명할 수 없음

##### Query·Key·Value를 일상 언어로 구분 (PDF p.60)

- Query는 지금 이 위치에서 찾고 싶은 정보
- Key는 다른 위치가 가진 특징
- Value는 실제로 섞어 가져올 정보
- 비유는 직관용이며 실제 Q/K/V는 Tensor에 학습 행렬을 곱한 결과

#### Scaled Dot-Product Attention 계산

##### Scaled Dot-Product Attention 수식 읽기 (PDF p.61)

- 1단계 `Q @ K.T`로 Token 위치 간 점수 계산
- 2단계 `/ sqrt(d_k)`로 특징 차원에 따른 Scale 조정
- 3단계 `+ Mask`로 보면 안 되는 위치 제외
- 4단계 `softmax(scores)`로 가중치를 분포로 정규화
- 5단계 `weights @ V`로 Value를 가중합해 출력
- Mask의 불허 위치는 확률을 0으로 만들기 위해 보통 `-inf` 계열 사용

##### 작은 Q/K/V로 Attention Weight를 직접 계산 (PDF p.62)

- `q = [[1,0],[0,1],[1,1]]`, `k`와 `v`는 q의 복사본으로 설정
- `scores = q @ k.T / math.sqrt(2)`는 `(3,3)` 행렬
- `torch.triu(..., diagonal=1)`로 upper triangle을 Mask하고 `masked_fill(mask, float("-inf"))` 적용
- Softmax 뒤 각 행의 합은 1이고 미래 Token 가중치는 0
- CPU만 사용하며 같은 Q/K/V와 Mask이면 항상 같은 값

##### Causal Attention 가중치를 숫자로 확인 (PDF p.63)

- 행은 Query, 열은 Key 위치
- t1 행 `[1.00, 0.00, 0.00]`은 미래 t2/t3를 보지 못한 결과
- t2 행 `[0.33, 0.67, 0.00]`
- t3 행 `[0.25, 0.25, 0.50]`은 앞쪽 2개와 자신을 함께 참고한 결과

#### Mask 종류와 Multi-Head

##### Padding Mask와 Causal Mask가 막는 것은 다르다 (PDF p.64)

- Padding Mask는 Batch 길이 맞춤용 PAD, 즉 실제 내용이 없는 위치를 무시
- Padding Mask는 Tokenizer의 `attention_mask`와 연결되며 보통 입력마다 위치가 다름
- Causal Mask는 현재 Token보다 미래 위치를 가리며 자기회귀 Decoder에서 중요
- Causal Mask는 왼쪽 아래 삼각 형태가 기본이며 출력 생성 순서를 보존
- 같은 Mask라는 이름이어도 목적과 계산 방식이 다름

##### Multi-Head Attention이 의미하는 것 (PDF p.65)

- 한 Head는 Q/K/V 한 묶음과 한 가지 참고 분포
- 여러 Head는 Head별 별도 투영으로 여러 패턴을 함께 학습 가능
- 여러 Head의 출력은 Concat 또는 결합 후 Projection
- 가중치 해석은 제한적이고 Head 수가 많다고 무조건 향상되지 않음
- 현대 LLM은 GQA/MLA 등 변형을 쓰기도 하므로 모두 표준 MHA가 아님

#### Attention Weight 해석의 한계

##### Self-Attention은 Value를 가중합해 표현을 만든다 (PDF p.66)

- Q가 K와 비교 → Attention 분포 → Value 가중합 → 새 Hidden State의 흐름
- 가중치가 높다고 그 단어가 정답을 결정했다고 단정할 수 없음
- 가중치 시각화와 모델 판단의 완전한 설명은 별개

##### Attention 분석에서 흔히 발생하는 오해 (PDF p.67)

- Softmax 전 Score와 Softmax 후 Weight의 혼동
- 행(Query)과 열(Key)을 바꾼 Heatmap 해석
- 서로 다른 PyTorch API에 Mask의 True 의미를 동일하게 적용하는 실수
- 어텐션이 높은 Token 하나를 모델의 유일한 이유로 주장하는 해석

#### 실습과 확인

##### 실습 05 · Self-Attention 점수·Mask·가중치 시각화 (PDF p.68)

- 기본필수는 Q/K/V 3×2 예제에서 Scores·Weights·행의 합 확인
- 응용은 Causal Mask 유무를 비교하고 3×3 Attention Heatmap 작성
- 심화는 Head 수·입력 벡터를 바꾸어 Weight 차이와 해석 한계 설명
- 완료 기준은 Score/Weight/Mask의 의미 설명
- 결과물은 `attention_report.json`이며 확인 기준은 행 합 = 1, 마스크 위치 = 0
- 교육용 Attention은 자연어 모델의 학습된 주의 분포가 아님

##### Self-Attention 핵심 확인 (PDF p.69)

- `QKᵀ`는 Token 위치 사이의 유사·적합 점수
- Causal Mask는 현재 위치보다 나중 Token의 참조를 막음
- Attention Weight는 여러 Head·층·잔차 경로를 포함한 계산의 일부이며 모든 판단 근거가 아님

**핵심:** Attention은 Score → Mask → Softmax → Value 가중합의 순서로 계산되며, Weight는 행 합 1과 마스크 위치 0으로 검증하되 판단 원인의 전부로 해석하지 않음.

### 6교시 · 학습·추론·Logit·Decoding

#### 학습과 추론의 차이

##### 학습과 추론은 모델 파라미터를 다루는 방식이 다르다 (PDF p.70)

- Training은 대량 데이터에서 예측 목표를 정하고 Logits와 정답의 차이로 Loss 계산
- Training은 `backward()`로 기울기를 계산하고 Optimizer가 가중치 업데이트
- Inference는 학습된 가중치로 입력을 Tokenize하고 순전파 수행
- Inference는 Logits에서 다음 Token을 선택하고 선택을 반복해 출력 생성
- 학습 데이터에 원문을 저장하는 것과 추론 시 RAG 근거를 전달하는 것은 다른 작업

##### Causal Language Modeling의 대표 학습 흐름 (PDF p.71)

- 입력 Token 시퀀스 → 다음 Token 대상 → Loss 계산 → Gradient·Update의 순서
- 다음 Token 정답과 예측 점수의 차이를 줄이도록 학습
- Training에서는 θ 업데이트, Inference에서는 θ 고정

##### 사전학습 뒤 모델을 활용하는 세 방법 (PDF p.72)

- Prompting은 모델 가중치를 바꾸지 않고 입력의 지시·예시 조정
- Instruction Tuning은 지시·응답 데이터로 가중치를 추가 학습
- Preference Alignment는 선호 데이터 등으로 응답 행동을 추가 조정
- Prompt는 11/16 수업이며 Fine-tuning 구현은 11/13 필수 범위가 아님

#### Logit에서 확률로

##### 마지막 Hidden State에서 어휘 전체 Logit을 얻는다 (PDF p.73)

- 마지막 Hidden State → Linear LM Head → Vocabulary Logits → Softmax 확률
- Logit은 확률이 아닌 점수이며 확률로 보려면 Softmax 필요
- Logit 수치 크기를 확률 %로 읽지 않음

##### Softmax·Temperature가 분포를 바꾸는지 확인 (PDF p.74)

- 같은 `logits = [2.0, 1.0, 0.0]`에 Temperature 0.5·1.0·2.0을 적용해 `torch.softmax(logits / temp, dim=0)` 비교
- 온도가 낮으면 상위 후보에 확률 집중
- 온도가 높으면 분포가 완만해짐
- 확률 계산만 보여주는 코드이며 실제 LLM 호출·Token 선택은 하지 않음

#### Decoding과 생성 반복

##### Greedy·Temperature·Top-k·Top-p 비교 (PDF p.75)

- Greedy는 매번 점수 최고 후보를 선택하며 반복·다양성 부족 가능
- Temperature는 확률 분포의 날카로움을 조절하며 사실성을 자동으로 높이지 않음
- Top-k는 상위 k개 후보로 제한하며 k 설정에 따라 결과가 달라짐
- Top-p는 누적 확률 p까지 후보를 선정하며 분포에 따라 후보 수가 변함
- Top-k·Top-p를 동시에 적용하는 런타임도 있으며 실제 파라미터 동작은 구현별로 확인

##### Autoregressive Decoding은 한 Token씩 문맥을 확장한다 (PDF p.76)

- Prompt Token → Logits → 다음 Token 선택 → EOS/길이까지 반복
- 선택된 새 Token을 다시 입력에 포함해 다음 점수 계산
- 입력 전체 처리(Prefill)와 이후 한 Token씩 처리(Decode)를 구분

##### KV Cache의 이점과 대가 (PDF p.77)

- 이전 Token의 Key/Value를 재사용해 반복 디코딩의 중복 연산 일부 감소
- 긴 출력의 시간 효율에 도움
- 길어진 문맥만큼 메모리 사용이 늘고 모델·Head 구성에 따라 크기가 변함
- 캐시가 사실 검증을 대신하지 않음
- 여러 요청에는 캐시 정책, 캐시 경계와 멀티 사용자 격리 필요
- KV Cache는 사용자 장기 Memory가 아니며 요청 간 영구 저장소와 역할이 다름

#### 실습과 확인

##### 실습 06 · 학습·추론 흐름과 Token 확률 비교 (PDF p.78)

- 기본필수는 학습과 추론 단계를 분류하고 Logits에서 Softmax 값 확인
- 응용은 Temperature 두 설정을 비교하고 선택된 Token 후보 변화 설명
- 심화는 Top-k/Top-p 개념으로 선택 후보를 검토하고 KV Cache 한계 설명
- 완료 기준은 “학습은 가중치 변경, 추론은 다음 Token 선택” 구분
- 결과물은 `inference_report.json`

##### 학습과 추론 차이 확인 (PDF p.79)

- 일반적인 추론은 가중치를 업데이트하지 않으므로 `optimizer.step()`이 필요 없음
- Logit은 점수이며 Softmax로 확률 분포를 얻음
- KV Cache는 장기 기억이 아니라 한 생성 과정의 과거 Key/Value 재사용

**핵심:** 학습은 Loss로 가중치를 바꾸고 추론은 고정된 가중치의 Logit을 Softmax·Decoding해 다음 Token을 반복 선택.

### 7교시 · 모델 한계·검증·RAG/Agent 경계

#### 실패 위치와 품질 평가

##### LLM의 답변이 틀릴 수 있는 네 위치 (PDF p.80)

- 입력·문맥 단계에서는 질문의 의도나 필요한 제약이 빠짐
- 검색·근거 단계에서는 관련 문서를 못 찾거나 오래된 버전 사용
- 생성·추론 단계에서는 근거 밖 내용을 보충하거나 오해
- 표현·평가 단계에서는 JSON 형식은 맞지만 내용이 틀림

##### 출력 품질은 한 개의 숫자로 끝나지 않는다 (PDF p.81)

- 형식은 필수 필드·JSON 구조 확인이며 증거는 Schema 검증
- 근거는 답변의 각 주장이 문서로 뒷받침되는지 확인이며 증거는 출처·인용
- 정확성은 사실·계산과의 일치 확인이며 증거는 정답 세트
- 재현성은 같은 모델·설정에서의 동작 설명이며 증거는 버전·Seed·로그
- 안전성은 비밀·권한·오염된 근거 대응이며 증거는 거부·승인 규칙
- 근거가 있어도 그 근거가 최신·정확하다는 보장은 없음

#### Prompt·RAG·Fine-tuning·Agent의 경계

##### Prompt·RAG·Fine-tuning·Agent가 해결하는 문제 (PDF p.82)

- 정보·표현 문제에는 Prompt(지시·예시·출력 형식 정리), RAG(외부 지식 검색·근거 제공), Fine-tuning(모델 행동·스타일·과제 적응)
- 각 방법은 장점·비용·한계가 다름
- 실행·제어 문제에는 Agent(도구 선택·작업 단계 실행), FastAPI(기능의 서비스 입구), PostgreSQL(원본·상태·기록 저장)
- 실행 권한·검증은 애플리케이션 담당
- RAG를 넣어도 Agent가 자동 완성되지 않음
- Fine-tuning이 사실성까지 보장하지 않음

##### 11/20의 Basic RAG에서 오늘 배운 지식을 다시 쓴다 (PDF p.83)

- User Question → Retriever(관련 근거) → Prompt+Context → LLM Answer(Source)의 Retriever–Prompt–Generator 경로
- 중간의 검색 근거도 Token 예산에 포함
- 응답에서 출처 확인 필요

##### Agent 플랫폼을 만들 때도 필요한 검증 (PDF p.84)

- 검색된 문서의 명령 문구는 Untrusted Text이며 시스템 지시로 신뢰하지 않음
- 조회·수정·삭제 등 도구별 허용 범위는 애플리케이션에서 확인
- 모델·지시·참고 문서·Tool 결과·오류를 안전하게 기록해 관측·재현 가능하게 유지
- 학습용 지식 관리 API에는 인증·권한이 실제로 구현되어 있지 않음

#### 지식 관리 API 연결 사례

##### 지식 관리 API에 LLM을 연결하면 무엇이 새로 생길까? (PDF p.85)

- 지난 3일에 이미 있는 것은 `/api/knowledge` CRUD, PostgreSQL 원본 지식·분류, HTTP 오류와 DB 트랜잭션, 서버 재시작 후 저장 유지
- 이후 추가할 것은 질문 처리용 LLM 호출과 관련 지식 검색·Chunking·Vector DB
- 근거·사실성 평가와 출처 관리, 필요 시 Agent 도구·권한·상태도 추가 대상
- 원본 지식의 수정·삭제가 검색 인덱스에도 반영되도록 설계

#### 실습과 확인

##### 실습 07 · LLM 실패 위치와 보완 방법 매칭 (PDF p.86)

- 기본필수는 예시 답변 세 개를 읽고 사실·형식·근거 중 부족한 항목 분류
- 응용은 실패마다 Prompt·RAG·DB/API 검증 중 필요한 대응 선택
- 심화는 Agent의 도구 권한·근거 신뢰·평가 체크리스트를 최소 항목으로 정리
- 완료 기준은 방법의 나열보다 어떤 문제가 왜 생겼는지 설명
- 결과물은 `review.json/.md`

##### LLM의 한계와 RAG·Agent의 역할 (PDF p.87)

- RAG 근거는 자동으로 참이 아니며 문서 신뢰성과 답변의 인용 일치도 확인
- Pydantic 응답 검증은 형식 검증이며 사실성 검증과 달라 환각을 없애지 못함
- Agent의 Tool 실행에는 애플리케이션의 인증·권한·승인 필요

**핵심:** 틀린 답변은 입력·검색·생성·평가 중 어디서 생겼는지 먼저 찾고, 그 위치에 맞는 Prompt·RAG·검증·권한 대응을 선택.

### 8교시 · 일일프로젝트·전체 흐름 검증

#### 프로젝트 흐름과 공통 데이터

##### 일일프로젝트 · 문장 하나가 LLM 출력이 되기까지 (PDF p.88)

- Token 분석 → Embedding 비교 → Attention/Mask → 다음 Token·RAG 연결의 네 단계
- 11/10~12의 AI 플랫폼 구조 위에 오늘 배운 모델 흐름을 연결
- 모든 단계에서 CPU 기본 예제와 이미 제공한 코드·그림 재사용 가능

##### 프로젝트 공통 사례: AI 도움말 지식 3건 (PDF p.89)

- A 실습 파일 보관 “실습 파일은 개인 폴더에 보관합니다.”
- B 서버 실행 “프로젝트 폴더에서 서버를 실행합니다.”
- C 질문 작성 “오류 메시지와 시도한 작업을 함께 적습니다.”
- 학습용 텍스트만 사용하며 실제 기관 문서나 비밀값은 포함하지 않음

#### 작업과 결과 설명

##### 프로젝트 4개 작업과 남길 증거 (PDF p.90)

- Token은 문장 1개를 Token/ID/길이로 분석하고 Token 표를 남김
- Embedding은 3개 문장 또는 제공 벡터로 유사도를 비교하고 Cosine 표·간단 그림을 남김
- Attention은 3×3 가중치와 Mask의 의미를 확인하고 Matrix·행 합을 남김
- 출력 흐름은 Logit → Softmax → 선택 → 반복을 설명하고 입출력 흐름도를 남김
- Attention 결과를 모델 실제 답변의 인과적 근거로 주장하지 않음

##### 프로젝트 결과를 한 장으로 설명하는 순서 (PDF p.91)

- 입력 문장 → Token·ID → Embedding+Attention → Token 출력의 순서
- 입력 문자열과 모델 계산을 다른 개념으로 분리
- RAG의 외부 근거 추가 위치, FastAPI의 요청·응답, DB의 원본 관리 위치도 표시

##### 실습 08 · LLM 입력→출력 미니프로젝트 종합 (PDF p.92)

- 기본필수는 제공된 Token·Cosine·Attention 예제로 표와 흐름도 완성
- 응용은 직접 정한 문장 3개로 Token 비교·2D 유사도·Mask 유무 재실행
- 심화는 실행 결과·설계 한계·RAG/Agent 확장 위치를 연결한 설명 자료 작성
- 완료 기준은 Token·Embedding·Attention·Logit의 역할과 후속 서비스 연결 설명
- 결과물은 `daily_project.json`, `one_page_summary.md`
- 08은 01~07 출력물에 의존하지 않고 독립 실행

#### 평가와 진행

##### 평가 기준 · 기본필수만으로 100점 (PDF p.93)

- Token·Context 25점은 Token/ID·입력 길이·잘림 구분
- Embedding 20점은 벡터·유사도·표현 차이 설명
- Attention 25점은 Q/K/V·Mask·Weight·행 합 확인
- 학습·추론 15점은 Logit·확률·다음 Token·반복 설명
- 플랫폼 연결 15점은 FastAPI/DB·RAG/Agent 역할 분리
- 수준 간 차이는 과제 복잡도와 설명의 깊이이며 필수 목표는 모든 수준이 동일

##### 검증할 오류·혼동 사례 (PDF p.94)

- Token ID를 Embedding이라고 설명하면 두 표현의 자료형과 역할을 다시 구분
- Cosine이 크면 RAG 답변이 무조건 정확하다고 하면 근거·사실성을 별도 평가
- Masked Weight가 0이 아니면 Causal Mask 위치와 Softmax 전후 확인
- LLM 추론에서 계속 backward/step을 실행하면 Training과 Inference 구분

##### 마지막 50분의 작은 프로젝트 (PDF p.95)

- 0~5분은 설명·수준 선택·자료 위치 확인으로 과제 목표 파악
- 5~18분은 Token·Context 표 작성으로 Token·ID·길이 기록
- 18~30분은 Embedding 유사도 비교로 Cosine·벡터 관계 기록
- 30~42분은 Attention·Mask·Logit 분석으로 가중치·선택 흐름 기록
- 42~50분은 한 장 설명·공유·회고로 입력 → 출력 구조도 완성
- 학습자별로 난이도 한 가지를 선택하며 미완성자는 기본필수 완료를 우선

**핵심:** 일일프로젝트는 같은 문장이 Token → Embedding → Attention → Logit을 거쳐 출력되는 흐름을 수치와 그림으로 증명하고, 플랫폼의 각 계층 위치까지 표시하는 작업.

### 마무리 · 다음 수업과 참고자료

#### 다음 수업과 정리

##### 다음은 “모델을 어떻게 지시하고 입력을 구성할까?” (PDF p.96)

- 11/16은 Prompt 구조 → Zero/Few-shot → Context Engineering → JSON Schema·재시도
- 오늘은 모델 내부, 다음은 모델의 행동·출력 관리
- 전체 진도는 모델 내부 이해 → 입력 설계 → API 실행 → 검색·문서 → RAG 통합

##### 오늘의 핵심 개념을 한 번 더 정리한다 (PDF p.97)

- 문장 → Token → Token ID → Embedding → Transformer Hidden State의 변환
- Attention은 Q/K/V 점수·Mask·Softmax·Value 가중합으로 계산
- Training은 가중치를 업데이트하고 Inference는 다음 Token을 반복 선택
- 저장(API·DB), 모델(LLM), 검색(RAG), 도구 실행(Agent)은 서로 다른 역할

#### 공식 참고자료

##### 공식 참고자료 · 모델·Token·Attention (PDF p.98)

- Transformer 원 논문, Hugging Face Transformers 문서
- PyTorch `scaled_dot_product_attention`, `TransformerEncoderLayer` API 문서

##### 공식 참고자료 · 문장 임베딩·모델 활용 (PDF p.99)

- Sentence Transformers 문서, Transformers Tokenizer 문서
- Hugging Face Causal LM, Text Generation 문서

#### 마무리

##### LLM 원리를 AI 플랫폼의 기능으로 연결한다 (PDF p.100)

- 오늘 완성한 것은 Token·Embedding·Attention·Logit의 관계 설명
- RAG 검색·출처 검증·Agent 도구 실행은 아직 하지 않은 후속 과정
- 다음 수업은 Prompt와 Context 설계로 같은 모델에 더 좋은 입력 제공
- 최종 목표는 검증 가능한 AI Agent 플랫폼을 만드는 기초 역량 축적
