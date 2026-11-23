# Day28 강의 하이라키

- 원자료: [Day28_20261125.html](./Day28_20261125.html)
- 수업: 2026.11.25 (수) · Day 28 · 생성형 AI·LLM 및 RAG 엔지니어링
- 범위: 표지·목차 2개, 8교시 66개 화면. 총 68개 화면의 원문 제목과 진행 순서 보존
- ‘도입’은 표지·목차를 구분하기 위해 붙인 편집 묶음. 교시 제목과 화면 제목은 원문 표기 유지
- 코드·시연·실습 안내·이해 확인·핵심 확인은 해당 화면의 원문 제목 그대로 배치하며 부속 설명을 별도의 교시나 화면으로 추가하지 않음

## 강의 진행 구조

```text
RAG Evaluation & Debugging · LangChain — 핵심 압축본
├─ 도입
│  ├─ RAG Evaluation & Debugging
│  └─ 목차
├─ 1교시 · Why Evaluate RAG?
│  ├─ 전체지도 · RAG의 어느 부분을 평가할까요?
│  ├─ RAG Evaluation은 무엇이며 왜 필요한가요?
│  ├─ 검색 실패와 생성 실패는 별개의 문제입니다
│  ├─ 평가를 수행하는 네 단계
│  ├─ 평가 기록 하나를 Python dict로 구성합니다
│  ├─ 시연 · 실패 단계를 바꾸면 개선 방법이 달라집니다
│  └─ 실습 01 안내 · RAG 실패 위치 분류
├─ 2교시 · Build a Gold Dataset
│  ├─ Gold Label은 누가 정하고 어디에 사용하는가?
│  ├─ 질문 데이터셋의 필수 필드
│  ├─ Binary Relevance와 Graded Relevance는 어떻게 다를까요?
│  ├─ Gold Dataset을 JSON으로 읽고 기본 계약을 검사합니다
│  ├─ 같은 Corpus에서 질문별 관련 문서는 다릅니다
│  ├─ 정답 문서가 없는 질문도 Dataset에 넣어야 합니다
│  ├─ 시연 · Gold Label을 바꾸면 지표의 기준도 바뀝니다
│  ├─ 현업의 Gold Label 검수는 어떻게 하나요?
│  └─ 실습 02 안내 · Gold Dataset 작성
├─ 3교시 · Recall@k & Precision@k
│  ├─ Recall@k·Precision@k·Hit@k는 무엇인가요?
│  ├─ 세 가지 분모를 정확히 구분합니다
│  ├─ Recall@k를 Python으로 직접 계산해 봅니다
│  ├─ Precision@k와 Hit@k를 같은 입력으로 계산합니다
│  ├─ Candidate Recall과 실제 Context Recall은 왜 다른가요?
│  ├─ 시연 · Top-k를 바꾸며 세 지표를 직접 계산합니다
│  └─ 실습 03 안내 · Recall·Precision·Hit 계산
├─ 4교시 · MRR & nDCG
│  ├─ MRR과 nDCG는 어떤 문제를 해결하나요?
│  ├─ Reciprocal Rank에서 MRR로 넘어가는 계산
│  ├─ MRR을 Python으로 직접 계산합니다
│  ├─ DCG는 왜 로그로 순위에 할인을 적용하나요?
│  ├─ nDCG 계산 · 예시 숫자를 순서대로 따라갑니다
│  ├─ nDCG@k를 Python으로 직접 계산합니다
│  ├─ 시연 · 문서의 순서와 등급을 바꾸며 MRR·nDCG 계산
│  └─ 실습 04 안내 · MRR과 nDCG 계산
├─ 5교시 · Generation Evaluation
│  ├─ Faithfulness · Relevance · Correctness를 비교합니다
│  ├─ Faithfulness를 계산할 때 문장을 주장 단위로 나누는 이유
│  ├─ 같은 질문인데 평가 결과가 다를 수 있습니다
│  ├─ 주장별 지원 여부를 계산해 Faithfulness의 뜻을 확인합니다
│  ├─ LLM-as-a-Judge는 무엇이고 왜 보조 도구인가요?
│  ├─ Pydantic으로 평가 결과의 형태를 정의합니다
│  ├─ 사람 평가표는 어떻게 작성해야 하나요?
│  ├─ 시연 · 답변의 주장별 근거와 질문 적합성을 판정합니다
│  └─ 실습 05 안내 · 답변의 충실성과 적합성 확인
├─ 6교시 · LangChain Evaluation Flow
│  ├─ LangChain RAG 평가에서 무엇을 재사용하나요?
│  ├─ LangChain Stage별 평가용 데이터 계약
│  ├─ 기존 Runnable.invoke()로 질문별 실행을 수집합니다
│  ├─ Trace와 Evaluation Report는 왜 다르나요?
│  ├─ 검색 평가를 RunnableLambda로 감쌀 수 있습니다
│  ├─ VS Code · 데이터가 Target에서 Report까지 이동하는 흐름
│  ├─ LangSmith는 무엇이며 평가에서 어디에 사용할까요?
│  ├─ 시연 · LangChain 평가 Runner의 단계별 입출력 확인
│  └─ 실습 06 안내 · LangChain Evaluation Runner
├─ 7교시 · Debug & Compare
│  ├─ A/B 비교란 무엇이고 왜 필요한가요?
│  ├─ 한 번에 하나씩 바꾸는 실험 매트릭스
│  ├─ 평가 레코드를 버전별로 비교합니다
│  ├─ 낮은 점수에서 실제 수정할 모듈로 이동하기
│  ├─ Latency를 CPU 코드와 GPU 추론에서 구분해 측정합니다
│  ├─ 좋은 평가 리포트는 평균만 보여 주지 않습니다
│  ├─ 질문별 평가 기록을 JSONL로 남기는 방법
│  ├─ 시연 · Baseline과 개선 버전의 지표·속도를 비교합니다
│  └─ 실습 07 안내 · 실패 원인과 A/B 비교
└─ 8교시 · Agent-ready RAG
   ├─ 최종 전체지도 · 평가된 RAG를 Agent Tool로 전달합니다
   ├─ Quality Gate는 무엇이며 왜 필요한가요?
   ├─ Agent에 연결하기 전 RAG 기능의 점검표
   ├─ 평가 결과로 간단한 Release Gate를 구현합니다
   ├─ 네 직무가 평가에서 맡는 역할도 연결합니다
   ├─ 평가 Runner의 전체 실행 순서를 하나로 정리합니다
   ├─ 시연 · 1차 Quality Gate의 통과·실패를 확인합니다
   └─ 실습 08 안내 · RAG Evaluation 통합 리포트
```
