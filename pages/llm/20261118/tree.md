# Day23 강의 하이라키

- 원자료: [Day23_20261118.html](./Day23_20261118.html)
- 수업: 2026.11.18 (수) · Day 23 · 생성형 AI·LLM 및 RAG 엔지니어링
- 범위: 표지·목차 2개, 8교시 78개 화면. 총 80개 화면의 원문 제목과 진행 순서 보존
- ‘도입’은 표지·목차를 구분하기 위해 붙인 편집 묶음. 교시 제목과 화면 제목은 원문 표기 유지
- 코드·데모·체크리스트·실습 안내·핵심 점검은 해당 화면의 원문 제목 그대로 배치하며 부속 설명을 별도의 교시나 화면으로 추가하지 않음

## 강의 진행 구조

```text
Embedding · pgvector
├─ 도입
│  ├─ Embedding · pgvector
│  └─ 목차
├─ 1교시 · Embedding과 Semantic Search
│  ├─ AI Agent의 전체 요청 흐름에서 검색은 어디에 있을까?
│  ├─ 16·17일의 흐름에서 Semantic Search가 필요한 이유
│  ├─ Embedding은 문장을 숫자 벡터로 표현합니다
│  ├─ 생성 모델과 Embedding 모델은 역할이 다릅니다
│  ├─ FAQ 질문끼리 비교할까, 질문으로 지식 본문을 찾을까?
│  ├─ 기존 지식 101·102·103의 원문을 유지합니다
│  ├─ 오늘 사용할 가상 지식 9개를 구분합니다
│  ├─ 자료 준비와 질문 처리, 두 경로를 전환합니다
│  ├─ 실습 01 · 검색 대상과 ID를 구분합니다
│  └─ 핵심 점검 · Embedding의 역할
├─ 2교시 · Vector · Similarity · Distance
│  ├─ 벡터의 길이(norm)와 두 점 사이 거리(distance)는 다릅니다
│  ├─ Dot Product는 같은 위치의 숫자를 곱해 더합니다
│  ├─ Cosine similarity와 Cosine distance를 구분합니다
│  ├─ L2 distance는 두 벡터 사이의 직선거리입니다
│  ├─ 직접 벡터를 움직여 세 계산값을 비교합니다
│  ├─ 정규화는 벡터의 방향을 유지하면서 길이를 1로 맞춥니다
│  ├─ 영벡터는 Cosine 비교에 사용할 수 없습니다
│  ├─ Python에서 계산값을 직접 확인합니다
│  ├─ 실습 02 · 유사도와 거리 계산
│  └─ 핵심 점검 · Similarity와 Distance
├─ 3교시 · Sentence Transformers로 벡터 생성
│  ├─ Sentence Transformers와 E5 모델을 구분합니다
│  ├─ query / passage 접두어가 실제 입력을 어떻게 바꿀까?
│  ├─ 입력 Token 길이와 Embedding 출력 shape는 다릅니다
│  ├─ 기존 가상환경에서 라이브러리만 추가합니다
│  ├─ Embedding 모델을 로드하고 차원을 읽습니다
│  ├─ 같은 모델 계약으로 자료·질문 Embedding을 만듭니다
│  ├─ 저장 전 검증: 개수·차원·유한값·길이
│  ├─ 실습 03 · 문장 Embedding 생성
│  └─ 핵심 점검 · E5의 입력 계약
├─ 4교시 · PostgreSQL 18.6에 pgvector 설치
│  ├─ pgvector는 PostgreSQL을 교체하지 않습니다
│  ├─ 1단계 · pgAdmin에서 현재 서버와 DB 확인
│  ├─ 2단계 · PostgreSQL 18 설치 위치를 확인합니다
│  ├─ 3단계 · Visual Studio C++ Build Tools가 필요합니다
│  ├─ 4–5단계 · x64 빌드 환경 확인과 PGROOT 지정
│  ├─ 6단계 · 공식 pgvector v0.8.7 소스를 가져옵니다
│  ├─ 7단계 · nmake로 서버 확장을 빌드합니다
│  ├─ 8단계 · PostgreSQL 18 설치 폴더에 확장 파일을 배치합니다
│  ├─ 9단계 · pgAdmin에서 현재 DB에 vector 확장을 활성화합니다
│  ├─ 10단계 · 설치된 연산자로 숫자 벡터를 비교합니다
│  ├─ 11단계 · 임시 테이블로 저장·Top-k를 확인합니다
│  ├─ 12단계 · 기존 가상환경에서 Python 연동을 확인합니다
│  ├─ 13단계 · 실습별 .env를 사용합니다
│  ├─ 14단계 · Python에서 vector 타입과 거리 연산을 확인합니다
│  ├─ 설치 전체 과정의 성공 조건을 단계별로 확인합니다
│  ├─ pgvector Windows 설치 오류를 증상별로 구분합니다
│  ├─ 실습 04 · 서버 확장과 Python 연결 확인
│  └─ 핵심 점검 · pgvector 설치
├─ 5교시 · pgvector 저장과 Top-k Search
│  ├─ 저장할 단위는 원문·ID·Embedding이 연결된 한 행입니다
│  ├─ 검색용 테이블은 기존 지식 테이블과 분리합니다
│  ├─ 원문 순서가 달라지면 벡터와 잘못 연결될 수 있습니다
│  ├─ INSERT · ON CONFLICT로 원문과 벡터를 함께 저장합니다
│  ├─ Top-k의 의미와 Metadata Filter를 직접 확인합니다
│  ├─ Top-k SQL과 Metadata Filter SQL을 비교합니다
│  ├─ 유사도에 맞는 pgvector 거리 연산자를 선택합니다
│  ├─ 실습 05 · 검색용 테이블과 Top-k
│  └─ 핵심 점검 · 저장과 Top-k
├─ 6교시 · Vector Index · HNSW
│  ├─ Exact Search와 HNSW 탐색을 비교합니다
│  ├─ 거리 연산자와 인덱스 설정이 같아야 합니다
│  ├─ HNSW Cosine 인덱스 정의
│  ├─ EXPLAIN으로 실제 실행 계획을 읽습니다
│  ├─ HNSW의 탐색 폭을 크게 하면 무엇이 달라질까?
│  ├─ ANN에 Metadata 필터를 적용하면 k개보다 적을 수 있습니다
│  ├─ 실습 06 · 인덱스와 정확 검색 비교
│  └─ 핵심 점검 · 인덱스의 의미
├─ 7교시 · Retrieval 결과 정성평가
│  ├─ 관련성 기준으로 Retrieval 결과를 평가합니다
│  ├─ 범위 밖 질문에도 Top-k 결과가 나올 수 있습니다
│  ├─ 빈 결과와 검색 시스템 장애는 다릅니다
│  ├─ Top-k 정성평가에서 무엇을 기록할까?
│  ├─ 원문이나 모델이 바뀌면 기존 결과를 그대로 믿지 않습니다
│  ├─ 실습 07 · Top-k 결과의 관련성을 평가합니다
│  └─ 핵심 점검 · 검색 결과 판정
└─ 8교시 · Agent 검색 모듈로 연결
   ├─ 검색 모듈의 입출력 계약과 기존 기능의 연결
   ├─ 검색한 원문을 기존 Context 계약에 맞게 정리합니다
   ├─ 검색된 후보 전체와 실제 전달한 출처 목록은 다릅니다
   ├─ 모델과 전처리를 바꿀 때 검색 집합을 관리합니다
   ├─ 실습 08 · AI Agent용 검색 모듈의 입출력 검증
   ├─ 최종 확인 · 오늘 어디까지 완성했을까?
   └─ 오늘의 검색 기능과 다음 수업의 연결
```

## 부가 자료 · 내장 핵심요약

강의 진행 화면과 별도로 HTML에 내장된 핵심요약의 구역 제목. 아래는 원문 목차만 표시하며, 요약 본문은 새로 작성하지 않음.

```text
핵심요약
├─ 전체 흐름: 검색으로 필요한 지식을 찾는다
├─ Vector · Similarity · Distance
├─ Sentence Transformers: 질문과 지식의 역할 구분
├─ Windows 11 · PostgreSQL 18.6 · pgvector 설치
├─ Exact Top-k · Metadata · HNSW
└─ Retrieval 결과와 RAG 연결
```
