# Day27 강의 하이라키

- 원자료: `Day27_20261124.html`
- 수업: 2026.11.24 (화) · Day 27 · 생성형 AI·LLM 및 RAG 엔지니어링
- 범위: 표지·목차 2개, 8교시 81개 화면. 총 83개 화면의 원문 제목과 진행 순서 보존
- ‘도입’은 표지·목차를 구분하기 위해 붙인 편집 묶음. 교시 제목과 화면 제목은 원문 표기 유지
- 코드·시연·실습 안내·이해 확인·핵심 확인은 해당 화면의 원문 제목 그대로 배치하며 부속 설명을 별도의 교시나 화면으로 추가하지 않음

## 강의 진행 구조

```text
LangChain RAG · Query Optimization & Reranking
├─ 도입
│  ├─ LangChain RAG & Reranking
│  └─ 목차
├─ 1교시 · LangChain RAG Orientation
│  ├─ 전체지도에서 RAG 검색 개선 위치를 찾습니다
│  ├─ LangChain은 무엇이며 왜 사용하나요?
│  ├─ LangChain을 쓰면 누가 실제로 일을 하나요?
│  ├─ Document와 Runnable, Prompt와 Model은 어떻게 다를까요?
│  ├─ RunnableLambda와 | 를 처음부터 실행해 봅니다
│  ├─ Prompt.invoke()와 Chat Model.invoke()는 무엇이 다를까요?
│  ├─ 한 질문의 State가 어떻게 이동하는지 추적합니다
│  ├─ 왜 검색 결과의 순서가 답변에 영향을 줄까요?
│  ├─ 검색 실패는 발생 위치에 따라 구분합니다
│  ├─ Rewrite와 Rerank는 문제를 해결하는 위치가 다릅니다
│  ├─ LangChain Runnable로 기존 검색과 새 Reranking의 경계를 찾습니다
│  ├─ 시연 · 실패 원인을 선택해 적용 위치를 찾습니다
│  ├─ 실습 01 · 검색 실패 위치 진단
│  └─ 이해 확인 · 검색 개선의 위치
├─ 2교시 · Conversational Query Rewrite
│  ├─ Query Rewrite는 무엇을 어떻게 다시 쓰는 기술일까요?
│  ├─ 후속 질문에서 무엇을 복원해야 할까요?
│  ├─ 먼저 Rewrite의 성공 기준을 함수로 확인합니다
│  ├─ Query Rewrite가 변경해서는 안 되는 것
│  ├─ LangChain으로 독립 질문 생성을 요청하는 구조
│  ├─ Rewrite 결과는 무엇을 확인해야 할까요?
│  ├─ 검색용 질문과 답변용 질문을 구분합니다
│  ├─ 시연 · 대화 내용에 따라 독립 질문을 선택합니다
│  ├─ 실습 02 · 대화 후속 질문의 독립 질의 변환
│  └─ 이해 확인 · Rewrite의 경계
├─ 3교시 · Expansion & Multi-query
│  ├─ Query Expansion은 단어를 더 넣는 기술일까요?
│  ├─ Rewrite·Expansion·Multi-query의 차이를 한눈에 비교합니다
│  ├─ 질문 후보 목록을 만들 때 원문을 반드시 포함합니다
│  ├─ Multi-query는 여러 번 검색한 문서를 합치는 전략입니다
│  ├─ Multi-query 후보 통합을 LangChain Runnable로 연결합니다
│  ├─ 질문을 더 많이 만들면 무엇이 늘어날까요?
│  ├─ 시연 · 질의 수를 바꾸며 후보 합집합을 확인합니다
│  ├─ 실습 03 · Query Expansion과 Multi-query 후보 통합
│  └─ 이해 확인 · Multi-query 결과
├─ 4교시 · Candidate Retrieval
│  ├─ Candidate Retrieval은 왜 Reranking 이전의 별도 단계인가요?
│  ├─ 기존 E5·pgvector 검색 계약을 그대로 지킵니다
│  ├─ Day26 Retriever 계약을 유지하고 E5 실행 장치를 GPU로 전환합니다
│  ├─ Candidate가 LangChain Document로 바뀌어도 ID는 남겨 둡니다
│  ├─ Candidate 수와 Context 수는 같을 필요가 없습니다
│  ├─ 시연 · 검색 후보 수와 필터를 변경합니다
│  ├─ 실습 04 · Candidate Retrieval 계약 확인
│  └─ 이해 확인 · 검색 후보의 한계
├─ 5교시 · Cross-Encoder Reranking
│  ├─ Reranking은 검색된 후보의 순서를 다시 정합니다
│  ├─ Bi-Encoder와 Cross-Encoder는 무엇이 다를까요?
│  ├─ Bi-Encoder와 Cross-Encoder의 입력·출력을 비교합니다
│  ├─ CUDA GPU에서 다국어 Cross-Encoder를 실행합니다
│  ├─ Document 목록을 모델 입력 쌍으로 바꿉니다
│  ├─ Cross-Encoder의 점수는 정답 확률과 같지 않습니다
│  ├─ Reranker 성능의 상한은 초기 후보 집합이 정합니다
│  ├─ Cross-Encoder를 LangChain Rerank Stage로 연결합니다
│  ├─ 실무 Reranking은 품질과 자원 요구를 함께 설계합니다
│  ├─ 시연 · 후보의 순위가 바뀌는 것을 확인합니다
│  ├─ 실습 05 · Cross-Encoder로 후보를 재정렬하기
│  └─ 이해 확인 · Cross-Encoder의 역할
├─ 6교시 · LangChain Integration
│  ├─ LangChain에서 새로 추가하는 구성요소는 어디에 있을까요?
│  ├─ VS Code에서 파일 구조와 실행 노드의 관계를 봅니다
│  ├─ 실제 Rewrite Chain을 Runnable Stage에 연결합니다
│  ├─ LangChain Pipeline의 실제 실행 순서를 완성합니다
│  ├─ Context Builder를 이어 연결하고 원 질문을 지킵니다
│  ├─ 실무 Pipeline에서는 단계별 출력 이름을 명확히 둡니다
│  ├─ Stage를 연결해도 오류 처리는 Stage별로 구분합니다
│  ├─ 시연 · Chain의 중간값이 어떻게 이어지는지 추적합니다
│  ├─ 실습 06 · 기존 LangChain RAG에 Rewrite와 Reranker 연결
│  └─ 이해 확인 · LangChain 연결의 책임
├─ 7교시 · Compare & Diagnose
│  ├─ 검색 개선은 동일 조건의 Before/After로 확인합니다
│  ├─ 동일한 질문으로 순위를 나란히 비교합니다
│  ├─ 복잡한 평가 지표 전에 Top-k 포함 여부를 확인합니다
│  ├─ 단계별 입력과 소요 시간을 실행 기록으로 남깁니다
│  ├─ 좋은 비교표에는 실패의 종류도 남아야 합니다
│  ├─ 품질이 좋아져도 응답시간이 늘어날 수 있습니다
│  ├─ 시연 · 검색 전후의 Top-k 포함 여부를 계산합니다
│  ├─ 실습 07 · 검색 개선 전후의 차이를 기록합니다
│  └─ 이해 확인 · 결과 비교의 원칙
└─ 8교시 · End-to-End & Agent Bridge
   ├─ 오늘 추가한 단계가 기존 RAG 서비스에 합쳐집니다
   ├─ LangChain을 중심으로 개선된 RAG Service를 조립합니다
   ├─ API 입력 계약에 History와 후보 수를 추가합니다
   ├─ FastAPI Router는 검색 정책과 HTTP 오류 표현을 맡습니다
   ├─ 최종 서비스에서 유지해야 할 검증 경계를 확인합니다
   ├─ 시연 · 질문에서 출처까지 전체 흐름을 추적합니다
   ├─ 실습 08 · Query Optimization RAG 통합
   ├─ 내일은 “좋아 보인다”를 수치·사람 검토로 검증합니다
   └─ 전체 확인 · 개선된 RAG 서비스의 책임
```
