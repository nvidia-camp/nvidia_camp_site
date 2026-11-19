# Day24 강의 하이라키

- 원자료: [Day24_20261119_v2.html](./Day24_20261119_v2.html)
- 수업: 2026.11.19 (목) · Day 24 · 생성형 AI·LLM 및 RAG 엔지니어링
- 범위: 표지·목차 2개, 8교시 76개 화면. 총 78개 화면의 원문 제목과 진행 순서 보존
- ‘도입’은 표지·목차를 구분하기 위해 붙인 편집 묶음. 교시 제목과 화면 제목은 원문 표기 유지
- 코드·데모·체크리스트·핵심 확인은 해당 화면의 원문 제목 그대로 배치하며 부속 설명을 별도의 교시나 화면으로 추가하지 않음
- 실습 01–08은 원문 슬라이드 제목이 `Basic / Intermediate / Advanced`로만 적혀 있어, 각 실습의 실제 주제(`mentee/README.md`·슬라이드 수준별 목표 기준)를 반영해 표기함

## 강의 진행 구조

```text
Document Parsing · Chunking · Indexing
├─ 도입
│  ├─ Document Parsing · Chunking · Indexing
│  └─ 목차
├─ 1교시 · Document Collection
│  ├─ 어제의 검색은 문서가 이미 정리되어 있었습니다
│  ├─ Document Ingestion은 무엇을 하는가?
│  ├─ 오늘 사용할 가상 교육센터 문서 5건
│  ├─ Raw File과 Derived Data는 나누어 보관합니다
│  ├─ Python pathlib로 수집 파일을 열거합니다
│  ├─ 수집 Manifest에 원본 해시를 기록합니다
│  ├─ 수집 성공과 파싱 성공을 분리합니다
│  ├─ 실습 01 · 원본 파일 수집과 Manifest·해시 기록
│  └─ 핵심 확인 · Document Collection
├─ 2교시 · Document Parsing
│  ├─ Parsing은 텍스트 추출보다 넓은 개념입니다
│  ├─ 파일 형식마다 보존할 구조가 다릅니다
│  ├─ TXT는 UTF-8을 명시적으로 디코딩합니다
│  ├─ Markdown은 Heading과 본문 경계를 함께 봅니다
│  ├─ HTML에서는 main 본문과 표를 구분합니다
│  ├─ 표를 읽을 때는 행과 열의 관계가 중요합니다
│  ├─ PDF는 페이지별 raw_text와 locator를 남깁니다
│  ├─ PDF의 화면 배치가 텍스트 순서를 보장하지 않습니다
│  ├─ 형식별 Parsing 입력과 추출 결과를 비교합니다
│  ├─ 실습 02 · 형식별 Parsing과 구조 추출
│  └─ 핵심 확인 · Document Parsing
├─ 3교시 · Text Cleaning
│  ├─ Cleaning은 문서를 짧게 만드는 작업이 아닙니다
│  ├─ NFC와 NFKC는 다른 정규화 규칙입니다
│  ├─ 일반 본문 전용 clean_prose()를 구현합니다
│  ├─ Cleaning 규칙별 Before / After를 직접 비교합니다
│  ├─ Cleaning 후의 Offset은 원본 파일 바이트 위치가 아닙니다
│  ├─ 정제 규칙·해시·길이 변화를 기록합니다
│  ├─ 실습 03 · 의미 보존 정제와 변경 이력 기록
│  └─ 핵심 확인 · Text Cleaning
├─ 4교시 · Chunking Strategies
│  ├─ Chunk는 검색과 출처의 기본 단위입니다
│  ├─ 주요 Chunking Strategies를 비교합니다
│  ├─ Character Window는 시작·끝·Overlap이 핵심입니다
│  ├─ 종료 조건이 있는 Character Chunker
│  ├─ Chunk Size와 Overlap을 바꿔 봅니다
│  ├─ E5-small의 입력 규칙은 어제와 동일합니다
│  ├─ 실제 Embedding 입력의 Token 수를 확인합니다
│  ├─ Structure-aware Chunking을 우선 고려합니다
│  ├─ Heading·접두어를 추가하면 입력이 달라집니다
│  ├─ 문장·목록·표를 한 Chunk로 보존하는 기준
│  ├─ Overlap과 Chunk Size의 Trade-off
│  ├─ 실습 04 · Chunk 분할과 Overlap·Token 길이 확인
│  └─ 핵심 확인 · Chunking Strategies
├─ 5교시 · Chunk Validation
│  ├─ 검색 가능한 Chunk가 되려면 검증을 통과해야 합니다
│  ├─ 중간 Span(text)을 CleanUnit과 대조합니다
│  ├─ Coverage는 고유한 문자 위치를 계산합니다
│  ├─ Coverage·중복·누락을 직접 비교합니다
│  ├─ Coverage를 구간 병합으로 계산합니다
│  ├─ 검증 실패를 원인별로 분류합니다
│  ├─ 인덱싱 전 검증 결과표를 만듭니다
│  ├─ 조건과 결과가 같은 청크에 있어야 합니다
│  ├─ 실습 05 · Span·Coverage 검증과 누락·중복 분류
│  └─ 핵심 확인 · Chunk Validation
├─ 6교시 · Metadata & Filtering
│  ├─ Metadata는 근거의 위치와 처리 조건입니다
│  ├─ doc_id · chunk_id · content_hash의 역할을 구분합니다
│  ├─ Chunk Metadata를 명시적으로 구성합니다
│  ├─ 같은 입력에서 같은 Chunk ID를 생성합니다
│  ├─ Metadata Filter는 Top-k 이전에 검색 범위를 정합니다
│  ├─ Category·Version Filter가 결과를 바꿉니다
│  ├─ PostgreSQL에서 공개 버전과 Category를 함께 필터링합니다
│  ├─ 실습 06 · 출처 Metadata와 공개 버전 필터링
│  └─ 핵심 확인 · Metadata & Filtering
├─ 7교시 · pgvector Indexing Pipeline
│  ├─ Indexing Pipeline과 DB Index는 다릅니다
│  ├─ 문서·버전·청크를 PostgreSQL에 저장합니다
│  ├─ 검증 통과 Chunk만 E5로 Embedding합니다
│  ├─ UPSERT는 이전 판의 사라진 Chunk를 자동 삭제하지 않습니다
│  ├─ 완전 적재를 검증하고 한 Transaction에서 새 버전을 공개합니다
│  ├─ v1 / v2 공개 전환과 실패를 시연합니다
│  ├─ 현재 공개된 Chunk만 Top-k 검색합니다
│  ├─ 실습 07 · pgvector Stage·Publish와 Top-k 검색
│  └─ 핵심 확인 · pgvector Indexing Pipeline
└─ 8교시 · End-to-End Integration
   ├─ 하나의 문서를 끝까지 추적합니다
   ├─ Python Pipeline의 단계별 함수를 연결합니다
   ├─ 기본 5개 문서 + 오류 검증 1건의 처리 흐름
   ├─ 실무 Pipeline은 오류의 범위를 구분합니다
   ├─ 내일 RAG가 받을 Retriever Contract
   ├─ 실습 08 · 일일프로젝트 · 전체 Ingestion 통합
   └─ 핵심 확인 · End-to-End Integration
```
