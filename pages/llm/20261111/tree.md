# Day18 강의 구조·핵심 설명

2026-11-11 · 생성형 AI·LLM 및 RAG 엔지니어링 2/18 · PostgreSQL 입문 · 지식 관리 DB → 접속 → 조회 → 관계·SQL → 검증 → 일일프로젝트

교시 설명은 PDF p.15 운영표의 교시별 중심 활동 원문을 옮긴 것이고, 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준입니다(전체 94쪽). 인쇄 쪽수는 p.2~11 도입 묶음이 2~11쪽, p.12 이후는 PDF 쪽수에서 10을 뺀 값입니다(p.12 = 2쪽, p.94 = 84쪽). 도입·후속 수업 연결·마무리·참고 부록은 교시 표시가 없어 별도 묶음으로 유지했습니다. 실습은 기본필수·응용·심화 중 한 단계를 선택해 같은 두 테이블과 초기 데이터로 진행하는 구성입니다.

## 강의 목차

```text
도입 · AI Agent 플랫폼의 데이터 기반 PostgreSQL
├─ 현업 문제와 플랫폼 속 위치
│  ├─ PostgreSQL 입문 · 지식 관리 DB (PDF p.1)
│  ├─ AI Agent의 답변은 어디에 저장된 지식을 참조할까? (PDF p.2)
│  └─ AI Agent 플랫폼에서 PostgreSQL이 맡는 위치 (PDF p.3)
├─ 서비스에서 값 하나까지 확대
│  ├─ 서비스 → DB → 테이블 → 행 → 값으로 확대한다 (PDF p.4)
│  ├─ 어제 JSON의 지식을 오늘 두 테이블로 표현한다 (PDF p.5)
│  ├─ 테이블의 행 하나와 열 하나를 실제 값으로 읽는다 (PDF p.6)
│  └─ PK·FK·JOIN은 같은 기능이 아니다 (PDF p.7)
├─ 조회·변경·인덱스의 역할 구분
│  ├─ “서버 실행 안내와 분류를 보여 줘”를 SQL로 바꾸면 (PDF p.8)
│  ├─ AI Agent가 사용할 지식의 변경은 어떻게 보호할까? (PDF p.9)
│  └─ 일반 SQL 조회와 의미 검색은 같은 기술일까? (PDF p.10)
└─ 오늘의 프로젝트
   └─ 오늘 완성할 DB가 AI Agent 개발의 어느 부분일까? (PDF p.11)

1교시 · 환경·접속·첫 SQL
├─ 플랫폼 속 DB와 어제의 연결
│  ├─ 오늘은 AI 플랫폼의 데이터 쪽을 만든다 (PDF p.12)
│  └─ 어제의 JSON 파일도 재시작 후 남았다 (PDF p.13)
├─ 하루의 완료 모습과 운영
│  ├─ 하루의 완료 모습부터 확인한다 (PDF p.14)
│  ├─ 8교시 운영 · 설명 130분, 실습·확인 270분 (PDF p.15)
│  └─ 세 단계 · 같은 핵심을 다른 깊이로 (PDF p.16)
├─ DB 구성과 접속 준비
│  ├─ DB·DBMS·접속 도구를 구분한다 (PDF p.17)
│  ├─ DB의 이름 공간과 표의 행·열을 구분한다 (PDF p.18)
│  ├─ 설치보다 먼저 접속 가능한 상태를 확보한다 (PDF p.19)
│  └─ 접속 대상은 다섯 값으로 읽는다 (PDF p.20)
├─ 첫 SQL과 Query Tool
│  ├─ 내가 연결한 서버와 DB부터 확인한다 (PDF p.21)
│  └─ SQL을 한 문장씩 실행하고 결과를 읽는다 (PDF p.22)
└─ 실습
   └─ 실습 01 · 접속과 첫 SQL을 확인한다 (PDF p.23)

2교시 · 지식 데이터 SELECT·조건·정렬
├─ 기준 데이터와 기본 조회
│  ├─ 먼저 읽어 볼 기준 데이터 S0 (PDF p.24)
│  └─ 필요한 열을 고르고 한 행의 뜻을 읽는다 (PDF p.25)
├─ 조건·정렬·NULL
│  ├─ ID와 분류 조건으로 필요한 행만 찾는다 (PDF p.26)
│  ├─ 조건·정렬·개수를 함께 읽는다 (PDF p.27)
│  └─ NULL과 빈 문자열은 다른 값이다 (PDF p.28)
├─ SQL을 읽는 순서
│  └─ SQL을 업무 질문으로 다시 읽는다 (PDF p.29)
└─ 실습
   └─ 실습 02 · 지식 데이터에 작은 질문을 한다 (PDF p.30)

3교시 · 두 테이블·PK/FK·ERD·DDL
├─ 두 테이블 설계와 키
│  ├─ 같은 지식을 두 테이블로 나누는 이유 (PDF p.31)
│  ├─ 분류 하나에는 지식이 0개 이상 연결된다 (PDF p.32)
│  ├─ PK·FK·IDENTITY의 일을 섞지 않는다 (PDF p.33)
│  └─ 자료형과 저장 규칙을 함께 정한다 (PDF p.34)
├─ DDL로 테이블 만들기
│  ├─ categories · 분류의 이름과 키를 만든다 (PDF p.35)
│  └─ knowledge · 지식과 참조 규칙을 만든다 (PDF p.36)
├─ API 약속과 DB 정책
│  └─ 전날의 API 약속과 DB 정책을 연결한다 (PDF p.37)
└─ 실습
   └─ 실습 03 · 두 테이블의 키와 관계를 완성한다 (PDF p.38)

4교시 · INSERT·UPDATE·DELETE·RETURNING
├─ 안전한 변경 순서
│  └─ 변경 SQL은 확인하고, 바꾸고, 다시 확인한다 (PDF p.39)
├─ INSERT·UPDATE·DELETE
│  ├─ 새 지식을 넣고, 발급된 ID를 바로 읽는다 (PDF p.40)
│  ├─ 같은 지식 ID의 본문만 바꾼다 (PDF p.41)
│  └─ 지식 한 행을 삭제하고 취소한다 (PDF p.42)
├─ SQL 결과와 HTTP 응답
│  └─ 0행·오류·HTTP 응답을 구분한다 (PDF p.43)
└─ 실습
   └─ 실습 04 · CRUD를 SQL로 직접 연결한다 (PDF p.44)

5교시 · JOIN·LEFT JOIN·GROUP BY
├─ JOIN으로 분류명 연결
│  ├─ 키로 연결하면 지식에 분류명이 붙는다 (PDF p.45)
│  ├─ 지식 목록에 분류명을 함께 표시한다 (PDF p.46)
│  └─ 지식이 없는 분류도 결과에 남긴다 (PDF p.47)
├─ 집계와 COUNT
│  ├─ 분류별 지식 수를 집계한다 (PDF p.48)
│  ├─ COUNT(*)와 COUNT(k.id)는 무엇을 세는가? (PDF p.49)
│  └─ 행을 세고, 본문 길이를 요약한다 (PDF p.50)
└─ 실습
   └─ 실습 05 · JOIN과 집계로 지식 현황을 읽는다 (PDF p.51)

6교시 · 제약조건·실패·데이터 보존
├─ 검증 위치와 제약조건
│  ├─ API 검증과 DB 제약은 서로 다른 위치다 (PDF p.52)
│  └─ 제약조건의 역할을 정확한 문장으로 읽는다 (PDF p.53)
├─ 실패 시험과 회복
│  ├─ 빈 본문을 보내 DB가 거부하는지 확인한다 (PDF p.54)
│  ├─ 지식 삭제와 분류 삭제는 영향이 다르다 (PDF p.55)
│  └─ 실패 원인과 회복 순서를 함께 기록한다 (PDF p.56)
└─ 실습
   └─ 실습 06 · 실패해도 기존 지식은 보존된다 (PDF p.57)

7교시 · COMMIT/ROLLBACK·INDEX·EXPLAIN
├─ 트랜잭션의 확정과 취소
│  ├─ 트랜잭션은 변경의 확정·취소 단위다 (PDF p.58)
│  ├─ 취소하면 직전 미확정 변경이 사라진다 (PDF p.59)
│  ├─ 확정한 값은 새 연결에서도 다시 읽는다 (PDF p.60)
│  └─ 행이 취소돼도 발급 번호는 되돌아가지 않을 수 있다 (PDF p.61)
├─ 인덱스와 실행계획
│  ├─ 분류 조회를 돕는 인덱스를 검토한다 (PDF p.62)
│  └─ 작은 데이터의 Seq Scan도 정상이다 (PDF p.63)
└─ 실습
   └─ 실습 07 · 취소·확정과 조회 계획을 확인한다 (PDF p.64)

연결 · 후속 수업과 프로젝트 전 정리
├─ 후속 수업 연결
│  ├─ 내일은 같은 지식 API를 PostgreSQL에 연결한다 (PDF p.65)
│  └─ 원본 지식과 검색·생성은 서로 다른 책임이다 (PDF p.66)
└─ 프로젝트 전 정리
   └─ 오늘 배운 것을 한 번에 연결한다 (PDF p.67)

8교시 · 나만의 지식 DB 일일프로젝트
├─ 과제 정의와 대상 상태
│  ├─ 나만의 AI 도움말 지식 DB (PDF p.68)
│  └─ 세 지식의 역할과 실제 ID를 기록한다 (PDF p.69)
├─ 통과 기준
│  ├─ 등록과 조회로 내 지식 목록을 만든다 (PDF p.70)
│  ├─ B를 취소해 보고, 다시 확정한다 (PDF p.71)
│  └─ 거부할 입력과 삭제할 행을 따로 확인한다 (PDF p.72)
├─ 결과 기록과 시간 배분
│  ├─ 결과 기록은 SQL과 실제 결과를 함께 남긴다 (PDF p.73)
│  ├─ 마지막 50분 · 안내 6 + 수행 40 + 공유 4 (PDF p.74)
│  └─ 일일프로젝트 · 같은 목표를 수준에 맞게 완성한다 (PDF p.75)
└─ 평가
   └─ 평가 기준 · 기본필수만으로 100점 (PDF p.76)

마무리 · 오늘의 완료와 다음 단계
└─ 완료 기준
   └─ 오늘 완성한 것은 AI 플랫폼의 지식 관리 DB다 (PDF p.77)

참고 부록 · 준비 SQL·선택 확장·Windows 접속·참고자료
├─ 개인 DB 준비 A01~A05
│  ├─ 개인 학습 DB를 만들고 접속을 바꾼다 (PDF p.78)
│  ├─ 전체 DDL · categories (PDF p.79)
│  ├─ 전체 DDL · knowledge (PDF p.80)
│  ├─ Seed · 분류를 넣고 첫 지식을 연결한다 (PDF p.81)
│  └─ Seed · 나머지 지식과 시작 상태 확인 (PDF p.82)
├─ 연습·응용·심화 SQL
│  ├─ 본 테이블을 건드리지 않고 키를 연습한다 (PDF p.83)
│  ├─ HAVING으로 집계된 분류를 고른다 (PDF p.84)
│  ├─ 생략한 값과 명시한 NULL을 구분한다 (PDF p.85)
│  ├─ 두 번째 변경이 실패하면 첫 변경도 취소한다 (PDF p.86)
│  └─ 지식에 여러 태그가 필요해지면 N:M을 검토한다 (PDF p.87)
├─ Windows·pgAdmin·psql
│  ├─ 설치에서 첫 Query Tool까지 확인하는 순서 (PDF p.88)
│  ├─ 환경 오류는 데이터 오류와 분리한다 (PDF p.89)
│  └─ 터미널 명령과 psql 전용 명령을 나눈다 (PDF p.90)
└─ 이후 연동·검수·공식 자료
   ├─ DB로 바꿀 때 자동으로 해결되지 않는 것 (PDF p.91)
   ├─ 강의 기준과 제작 환경의 검수를 구분한다 (PDF p.92)
   ├─ 공식 참고자료 · 접속·SQL·설계 (PDF p.93)
   └─ 공식 참고자료 · 검증·트랜잭션·인덱스 (PDF p.94)
```

## 핵심 설명

### 도입 · AI Agent 플랫폼의 데이터 기반 PostgreSQL

#### 현업 문제와 플랫폼 속 위치

##### PostgreSQL 입문 · 지식 관리 DB (PDF p.1)

- 생성형 AI·LLM 및 RAG 엔지니어링 정규교과 2/18 표지
- RAG·AI Agent 플랫폼의 데이터 기반을 만드는 Day18
- 접속 → 조회 → 관계·SQL → 검증 → 일일프로젝트 순서의 하루 흐름

##### AI Agent의 답변은 어디에 저장된 지식을 참조할까? (PDF p.2)

- 신규 직원의 “개발환경 설정 절차” 질문에는 바뀐 안내문의 최신 내용 확인이 필요
- 이후 AI Agent는 사용자 질문을 이해하고 지식 조회 도구로 업무 자료 탐색
- 오늘은 PostgreSQL로 지식의 제목·본문·분류를 테이블과 규칙으로 관리하고 변경 결과 검증
- 오늘 직접 수행하는 범위는 SQL
- 검색·생성 이전에 사람이 관리하는 원본 지식의 일관성과 추적성이 필요

##### AI Agent 플랫폼에서 PostgreSQL이 맡는 위치 (PDF p.3)

- 사용자·업무 화면 → FastAPI 요청·응답 → 원본 지식 관리·검색·RAG·Agent 실행의 구조
- 원본 지식 관리는 등록·조회·수정·삭제를 맡는 PostgreSQL이며 오늘의 범위
- 검색·RAG는 문서 검색·답변 생성, Agent 실행은 도구 선택·결과 확인을 맡는 이후 단계
- RAG·Agent는 원본 DB를 활용하는 별도 처리 계층

#### 서비스에서 값 하나까지 확대

##### 서비스 → DB → 테이블 → 행 → 값으로 확대한다 (PDF p.4)

- AI Agent 업무 서비스 → 지식 원본 관리 영역 → PostgreSQL 서버 → `knowledge_lab`/`public` → `categories`·`knowledge` → 한 행의 `category_id = 2`의 6단계
- PostgreSQL 서버는 여러 데이터베이스를 관리하는 DBMS
- `knowledge_lab`은 Database, `public`은 Schema 이름 공간
- `category_id = 2`는 한 값이 분류 2번을 참조한다는 뜻
- 상위 개념의 목적을 이해한 뒤 아래 단계의 실제 저장 규칙을 계산·실행하는 학습 순서

##### 어제 JSON의 지식을 오늘 두 테이블로 표현한다 (PDF p.5)

- 11/10은 FastAPI + JSON 파일로 지식 항목 안에 분류 이름 `"category": "api"`까지 함께 저장
- 11/11은 `categories (id, name)`와 `knowledge (id, title, category_id)`의 관계형 구조
- 분류 이름은 JOIN으로 연결해 조회
- 오늘의 S0는 별도의 가상 초기 데이터이며 어제 JSON 파일이 DB로 자동 이관된 것이 아님

##### 테이블의 행 하나와 열 하나를 실제 값으로 읽는다 (PDF p.6)

- 부모 `categories`는 learning·environment·reference 3행
- 자식 `knowledge`는 실습 파일 보관·서버 실행·질문 작성 3행
- 지식 ID 2의 `category_id`는 2이며 분류 ID 2의 이름은 environment
- 한 행(Row)은 지식 한 건, 한 열(Column)은 공통 항목, 한 값은 해당 행·열의 실제 데이터
- 원본의 고유 ID와 분류가 있어야 검색·검토 시 어떤 안내를 참조했는지 추적 가능

##### PK·FK·JOIN은 같은 기능이 아니다 (PDF p.7)

- PRIMARY KEY `categories.id`는 각 분류 행을 고유하게 식별
- FOREIGN KEY `knowledge.category_id`는 존재하는 분류만 참조하도록 검사
- JOIN `c.id = k.category_id`는 조회할 때 두 테이블의 값을 연결
- 참조 규칙은 `FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT`
- 현업에서는 삭제·수정 시 데이터가 연결된 상태로 남는지를 DB 제약조건으로도 검사

#### 조회·변경·인덱스의 역할 구분

##### “서버 실행 안내와 분류를 보여 줘”를 SQL로 바꾸면 (PDF p.8)

- 오늘은 pgAdmin·psql에서 현재 DB 확인 → 조회 조건 지정 → Data Output 읽기 순서로 SQL 직접 실행
- `SELECT k.id, k.title, c.name AS category ... JOIN categories AS c ON c.id = k.category_id WHERE k.id = 2`
- 결과는 id=2 · 서버 실행 · environment
- 내일 FastAPI가 같은 SQL 흐름을 호출해도 HTTP 200·404를 고르는 책임은 API 계층

##### AI Agent가 사용할 지식의 변경은 어떻게 보호할까? (PDF p.9)

- 대상 확인 → 변경 실행 → 제약 검사 → 결과 확정의 4단계
- 대상 확인은 SELECT와 실제 ID로 바꿀 지식 확인
- 변경 실행은 `BEGIN` + `UPDATE`, 변경 결과는 `RETURNING`으로 확인
- 제약 검사는 NOT NULL·CHECK·FK·UNIQUE
- 정상이면 COMMIT으로 변경 유지 후 새 연결에서도 결과 확인
- 실패하면 ROLLBACK으로 미확정 변경 취소 후 오류 원인과 기존 행 보존 확인
- 원문 관리의 안전성과 생성 모델의 사실성은 다른 문제이며 DB 제약과 AI 답변 검증은 별개의 검사

##### 일반 SQL 조회와 의미 검색은 같은 기술일까? (PDF p.10)

- 오늘의 PostgreSQL SQL·Index는 `WHERE category_id = 1`, JOIN으로 분류명 조회, INDEX와 EXPLAIN으로 접근 경로 관찰
- SQL·Index는 조건에 맞는 행과 저장 규칙 관리
- 이후의 Embedding·Vector Search는 문서를 벡터로 변환해 질문과 가까운 근거 후보 검색
- RAG는 선택한 원문을 LLM에 제공하며 원본이 바뀌면 인덱스 갱신 설계 필요
- 일반 B-tree 인덱스를 만들었다고 의미 검색이 되지 않음
- Agent의 근거 관리에는 두 기술이 각각 역할을 가짐

#### 오늘의 프로젝트

##### 오늘 완성할 DB가 AI Agent 개발의 어느 부분일까? (PDF p.11)

- 설계 → 구현 → 검증 → 프로젝트의 4단계
- 설계는 categories·knowledge ERD, 구현은 CREATE·SELECT·JOIN, 검증은 FK·CHECK·COMMIT/ROLLBACK
- 프로젝트는 A 유지·B 수정·C 삭제
- 오늘 결과는 지식 3건 등록 → B 수정·확정 → C 삭제 → 최종 N+2건과 기존 지식 보존
- 이후 FastAPI · 원본 갱신 → 검색 인덱스 관리 → Agent의 근거 조회로 연결
- 일일프로젝트는 SQL과 지식 DB까지만 구현하며 Agent 호출·벡터 검색·LLM 생성은 필수 과제가 아님

**핵심:** 오늘 만드는 PostgreSQL 지식 DB는 RAG·Agent가 참조할 원본 지식을 관계와 제약으로 관리하는 계층이며 의미 검색·답변 생성은 포함하지 않음

### 1교시 · 환경·접속·첫 SQL

#### 플랫폼 속 DB와 어제의 연결

##### 오늘은 AI 플랫폼의 데이터 쪽을 만든다 (PDF p.12)

- 지식 API → 원본 지식 DB → 이후 검색·생성·Agent로 이어지는 플랫폼
- 오늘의 클라이언트는 pgAdmin·psql이며 SQL 직접 실행
- PostgreSQL에는 지식·분류 테이블과 규칙·SQL·트랜잭션
- 다음 단계는 11월 12일 FastAPI 연동
- 이후 원본·출처·메타데이터 → 검색용 인덱스 → RAG·Agent 처리로 확장
- 오늘은 HTTP·ORM·벡터 검색을 구현하지 않고 DB를 직접 다루는 기초 완성

##### 어제의 JSON 파일도 재시작 후 남았다 (PDF p.13)

- 11/10에 지식 CRUD와 HTTP 요청·응답, title·content·category, JSON 파일 저장, 재시작 뒤 상태 확인까지 완성
- 11/11은 지식과 분류를 관계로 표현하고 DB에서도 입력·참조 규칙 적용
- SQL로 연결 조회와 집계, 여러 변경의 확정·취소까지 확장
- DB로 옮기는 이유는 “파일은 사라진다”가 아니라 관계·공유 규칙·조회·트랜잭션

#### 하루의 완료 모습과 운영

##### 하루의 완료 모습부터 확인한다 (PDF p.14)

- 두 테이블로 내 지식을 관리하고 SQL 결과와 실제 상태를 설명하는 것이 하루의 완료 모습
- 접속(어느 DB인가) → 조회·설계(지식과 분류) → 변경·검증(키·제약·확정) → 개인 프로젝트(A 유지·B 수정·C 삭제)
- DB 설치만으로는 완료가 아님
- 완료의 근거는 조회 결과·변경 행 수·취소/확정 후 상태

##### 8교시 운영 · 설명 130분, 실습·확인 270분 (PDF p.15)

- 1교시 환경·접속·첫 SQL, 2교시 SELECT·조건·정렬, 3교시 두 테이블·PK/FK·ERD·DDL
- 4교시 INSERT·UPDATE·DELETE·RETURNING, 5교시 JOIN·LEFT JOIN·GROUP BY
- 6교시 제약조건·실패·데이터 보존, 7교시 COMMIT/ROLLBACK·INDEX·EXPLAIN, 8교시 나만의 지식 DB 일일프로젝트
- 교시별 설명·시연 10~20분, 실습·확인 30~40분
- 50분 × 8교시 = 400분
- 마지막 교시는 안내 6분 + 수행 40분 + 공유 4분

##### 세 단계 · 같은 핵심을 다른 깊이로 (PDF p.16)

- 기본필수는 짧은 SQL 골격에서 핵심 키워드·조건을 완성하고 두 테이블·CRUD·JOIN·제약·확정/취소를 직접 확인
- 응용은 작성할 TODO와 조건 조합을 늘리고 빈 결과·추가 조회 확인과 SQL 파일 분리
- 심화는 역할별 SQL과 검증 절차로 재현성을 높이고 제공 구조에서 원자성·실행계획의 근거 설명
- 자기 수준의 한 단계로만 진행
- 기본필수만으로 공통 평가 100점 가능

#### DB 구성과 접속 준비

##### DB·DBMS·접속 도구를 구분한다 (PDF p.17)

- Database `knowledge_lab`은 지식·분류의 구조와 데이터를 담는 업무 공간
- DBMS·RDBMS인 PostgreSQL은 표 형태의 데이터를 관리하고 SQL·규칙 처리
- Client인 pgAdmin·psql은 서버에 SQL을 보내고 결과를 확인하는 도구
- SQL은 구조를 정의하고 데이터를 읽거나 바꾸는 언어
- pgAdmin 창을 닫는 것과 PostgreSQL 서버 종료는 다른 동작

##### DB의 이름 공간과 표의 행·열을 구분한다 (PDF p.18)

- 논리적 이름 공간은 Server(PostgreSQL) → Database(`knowledge_lab`) → Schema(`public`) → Table(`knowledge`)
- 가로 한 행(Row)은 지식 한 건
- 세로 한 열(Column)은 공통 항목 한 종류
- `knowledge_lab`에 접속한 뒤 `public.knowledge` 조회
- Schema는 이름 공간이며 디스크 폴더가 아님

##### 설치보다 먼저 접속 가능한 상태를 확보한다 (PDF p.19)

- 수업은 PostgreSQL 18 계열 기준이며 강사가 검증한 안정 조합 사용, 현재 최신 버전이라는 뜻은 아님
- 구성은 Server·pgAdmin·psql이며 Windows 공식 안내에서 EDB 설치 프로그램으로 연결
- 접속 값은 Host·Port·DB·User, `localhost`·`5432`는 로컬 기본 예시
- 설치한 서버 계정 비밀번호는 소스·Git·제출물·스크린샷에 실제 값 기재 금지
- 사전 설치를 권장하고 1교시에는 실제 접속 확인
- 설치·CLI 상세는 부록 A11~A13

##### 접속 대상은 다섯 값으로 읽는다 (PDF p.20)

- Host `localhost`는 지금 접속하는 컴퓨터의 서버
- Port `5432`는 설치할 때 정한 서버 포트
- Database `knowledge_lab`은 오늘의 개인 학습 DB
- User `postgres`는 설치 확인용 계정이며 운영 앱 계정은 별도
- Password는 본인이 설정한 서버 인증 값이며 수업 결과에서 숨김
- 서버 등록 이름은 화면의 별칭이며 같은 이름을 적어도 DB가 생성되지 않음

#### 첫 SQL과 Query Tool

##### 내가 연결한 서버와 DB부터 확인한다 (PDF p.21)

- Query Tool에서 `SELECT current_database() AS db_name, current_user AS user_name;` 실행
- `SELECT version();`과 `SELECT 1 AS connection_ok;`를 한 문장씩 선택해 실행
- `db_name`이 `knowledge_lab`인지 확인
- `version()`은 서버 버전, `psql --version`은 클라이언트 버전
- 기대 결과는 `db_name: knowledge_lab`, `connection_ok: 1`

##### SQL을 한 문장씩 실행하고 결과를 읽는다 (PDF p.22)

- 실행할 SQL만 선택 → 실행 버튼 설명 확인 → Data Output의 값·행 수 확인 → Messages의 오류·변경 행 수 확인
- 변경 실습 설정은 Auto commit 켬, Auto rollback on error 끔
- BEGIN부터 종료까지 같은 Query Tool 사용
- 오류 뒤에는 ROLLBACK을 따로 실행
- 빈 결과 0행은 정상일 수 있으며 오류 상태와 구분
- DB 직접 실행에는 HTTP 상태코드가 없음

#### 실습

##### 실습 01 · 접속과 첫 SQL을 확인한다 (PDF p.23)

- 30분, 세 단계 중 하나 선택
- 기본필수는 `knowledge_lab`에 접속해 DB 이름과 `SELECT 1` 결과를 확인하고 서버와 Query Tool의 역할을 한 문장으로 구분
- 응용은 pgAdmin과 psql에서 같은 DB 이름·사용자를 비교하고 비밀번호를 제외한 실제 접속 정보 기록
- 심화는 제공 점검 순서를 SQL·도구 확인으로 나누고 접속 실패와 SQL 오류를 구분하는 진단 기록 작성
- `SELECT 1`만 보지 않고 현재 DB 이름도 확인
- 운영 DB·공용 데이터에서는 실습하지 않음

**핵심:** 접속 성공의 근거는 `SELECT 1`이 아니라 `current_database()`가 `knowledge_lab`인지까지 확인한 결과이며 서버·DB·클라이언트의 역할을 구분해 읽음

### 2교시 · 지식 데이터 SELECT·조건·정렬

#### 기준 데이터와 기본 조회

##### 먼저 읽어 볼 기준 데이터 S0 (PDF p.24)

- `categories`는 learning·environment·reference 분류 3건
- `knowledge`는 실습 파일 보관(분류 1)·서버 실행(분류 2)·질문 작성(분류 1) 지식 3건
- `content`에는 각 안내의 본문 저장
- reference 분류에는 아직 지식이 없음
- S0는 새 DB에 준비한 가상 초기 데이터
- 준비 순서와 전체 SQL은 부록 A01~A05

##### 필요한 열을 고르고 한 행의 뜻을 읽는다 (PDF p.25)

- `SELECT id, title, category_id FROM knowledge ORDER BY id;`와 `SELECT name FROM categories ORDER BY id;`
- SELECT는 볼 열, FROM은 읽을 표, ORDER BY는 볼 순서
- 한 행은 지식 한 건이며 `category_id`는 분류를 가리킴
- S0 기준 knowledge 3행, 분류 3행
- 조회는 내용을 변경하지 않음

#### 조건·정렬·NULL

##### ID와 분류 조건으로 필요한 행만 찾는다 (PDF p.26)

- `WHERE id = 2`는 특정 지식 한 건
- `WHERE category_id = 1`은 같은 분류의 지식
- 같다는 `=`, 문자열은 작은따옴표
- 결과 0행은 조회 실패가 아님
- S0 기준 id=2는 서버 실행, 분류 1은 id 1·3

##### 조건·정렬·개수를 함께 읽는다 (PDF p.27)

- `WHERE category_id = 1 AND title LIKE '%실습%' ORDER BY id DESC LIMIT 2`
- AND는 두 조건을 모두 만족
- `%실습%`는 해당 글자를 포함하는 제목
- DESC는 큰 ID부터, `LIMIT 2`는 최대 두 행
- LIKE 문자 검색은 의미 검색이나 RAG가 아님
- S0 결과는 id 1 한 행

##### NULL과 빈 문자열은 다른 값이다 (PDF p.28)

- `SELECT NULL IS NULL`은 true, `SELECT '' IS NULL`은 false
- `char_length('')`는 0
- NULL은 값이 없거나 모르는 상태, 빈 문자열은 길이가 0인 값
- NOT NULL은 NULL을 막고 빈 본문은 길이 CHECK로 막음
- NULL 확인에는 `IS NULL` 사용
- 필수 값 보장에는 두 규칙을 함께 사용

#### SQL을 읽는 순서

##### SQL을 업무 질문으로 다시 읽는다 (PDF p.29)

- “어느 표에서 어떤 행과 열을 어떤 순서로 보고 싶은가?”로 SQL 해석
- FROM(어느 테이블) → WHERE(어떤 조건) → SELECT(어떤 열) → ORDER BY(어떤 순서)
- 이 순서는 의미를 이해하기 위한 순서
- 실제 DB의 물리적 실행 순서는 실행계획에 따라 달라짐

#### 실습

##### 실습 02 · 지식 데이터에 작은 질문을 한다 (PDF p.30)

- 35분, 세 단계 중 하나 선택
- 기본필수는 제공 SELECT의 열·WHERE·ORDER BY를 완성하고 전체 목록·ID 한 건·분류 조건의 결과 확인
- 응용은 분류와 제목 조건을 AND로 조합하고 정렬·LIMIT 추가, 0행 결과도 기록
- 심화는 예상 ID와 실제 ID를 비교하는 조회 세트를 만들고 NULL·빈 결과·동점 정렬의 차이 설명
- 완료 기준은 실행 성공뿐 아니라 결과 한 행의 의미와 실제 ID·행 수 설명

**핵심:** SELECT는 FROM·WHERE·SELECT·ORDER BY를 업무 질문으로 읽고 결과의 실제 ID·행 수로 확인하며 0행과 오류, NULL과 빈 문자열을 구분

### 3교시 · 두 테이블·PK/FK·ERD·DDL

#### 두 테이블 설계와 키

##### 같은 지식을 두 테이블로 나누는 이유 (PDF p.31)

- 어제의 지식 한 건은 `id`·`title`·`content`·`category: environment`를 함께 저장해 분류 이름이 지식마다 반복
- 오늘은 `categories(id, name)`와 `knowledge(id, title, content, category_id)`로 분리
- 분류 이름은 부모 표에서 관리하고 조회할 때 두 표를 연결
- DB 표현을 바꿔도 외부 API의 `category` 문자열을 반드시 바꿔야 하는 것은 아님

##### 분류 하나에는 지식이 0개 이상 연결된다 (PDF p.32)

- `categories`는 `id BIGINT · PK · IDENTITY`, `name VARCHAR(30) · NN · UNIQUE`
- `knowledge`는 `id BIGINT · PK · IDENTITY`, `title VARCHAR(80) · NN`, `content TEXT · NN`, `category_id BIGINT · NN · FK`
- 관계는 categories 1 : knowledge 0..N, `knowledge.category_id → categories.id`
- 각 지식은 분류 하나를 필수 참조
- NN은 NOT NULL
- ERD는 구조 설명이며 실제 참조 검사는 CREATE TABLE의 FK가 수행

##### PK·FK·IDENTITY의 일을 섞지 않는다 (PDF p.33)

- PK는 각 행을 유일하게 식별하며 NULL 불가, 예는 `knowledge.id`
- FK는 참조하는 부모 값의 존재를 검사, 예는 `knowledge.category_id → categories.id`
- IDENTITY는 값을 생략하면 번호를 발급하며 유일성 규칙은 PK가 담당
- JOIN은 조건에 맞는 행을 함께 조회해 분류 이름을 지식 목록에 연결
- FK가 있다고 JOIN이 자동 실행되지 않음
- ID는 행 수나 목록의 위치가 아님

##### 자료형과 저장 규칙을 함께 정한다 (PDF p.34)

- `id`는 BIGINT + IDENTITY + PK, DB가 발급하고 응답의 실제 ID로 추적
- `title`은 VARCHAR(80) + NOT NULL + CHECK, 1~80자이며 같은 제목 허용
- `content`는 TEXT + NOT NULL + CHECK, 1~2,000자
- `category`는 `categories.name`의 VARCHAR(30), 1~30자이며 분류 이름은 UNIQUE
- `category_id`는 BIGINT + NOT NULL + FK, 등록된 분류만 참조
- 전날 title·content·category 길이 규칙을 그대로 이어 사용
- DB는 내용의 사실성까지 검증하지 않음

#### DDL로 테이블 만들기

##### categories · 분류의 이름과 키를 만든다 (PDF p.35)

- 부모 `categories`를 먼저 생성
- `id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY`로 행 식별
- `name VARCHAR(30) NOT NULL UNIQUE`로 NULL 금지와 같은 분류명 중복 방지
- `CONSTRAINT categories_name_length CHECK (char_length(name) BETWEEN 1 AND 30)`로 1~30자 검사
- 이미 있으면 재실행하지 않음
- 실행 연습은 부록 A06

##### knowledge · 지식과 참조 규칙을 만든다 (PDF p.36)

- `title VARCHAR(80) NOT NULL`, `content TEXT NOT NULL`, `category_id BIGINT NOT NULL`
- `knowledge_title_length`는 1~80자, `knowledge_content_length`는 1~2,000자 CHECK
- `knowledge_category_fk`는 `FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT`
- ON DELETE RESTRICT는 연결된 분류의 삭제 거부
- 지식 1건은 분류 1개를 참조하고 부모 없는 참조는 거부
- 지식 제목은 UNIQUE가 아님

#### API 약속과 DB 정책

##### 전날의 API 약속과 DB 정책을 연결한다 (PDF p.37)

- 전날 API는 `category` 문자열로 새 분류명도 입력 가능, 오늘은 분류를 먼저 등록한 뒤 ID 사용
- 내일 API 연결에서도 외부 필드는 `category` 문자열 유지, DB에서는 기존 분류 조회 또는 새 분류 생성 후 지식 저장
- 지식 수정은 특정 지식 한 건의 값만 변경하며 다른 분류로 이동할 때 `category_id` 변경
- 전날 제목 중복을 금지하지 않았으므로 `knowledge.title`에 UNIQUE를 추가하지 않음
- 분류명 자체를 바꾸면 그 분류를 참조하는 모든 지식의 조회 결과에 영향

#### 실습

##### 실습 03 · 두 테이블의 키와 관계를 완성한다 (PDF p.38)

- 30분, 세 단계 중 하나 선택
- 기본필수는 제공 ERD에 PK·FK와 1:N을 표시하고 연습용 `_try` DDL의 핵심 키워드를 완성해 결과 확인
- 응용은 필수·길이·중복 규칙을 더 직접 작성하고 그림의 규칙과 실제 DB 정의 비교
- 심화는 DDL·Seed·검증의 역할을 나누고 삭제 정책과 키 선택 이유를 설계 기록에 작성
- 부록 A06의 연습용 테이블은 같은 연결에서 ROLLBACK
- 본 데이터에는 DROP을 쓰지 않음

**핵심:** PK는 식별, FK는 부모 존재 검사, IDENTITY는 번호 발급, JOIN은 조회 시 연결로 역할이 다르며 실제 규칙은 ERD가 아니라 CREATE TABLE의 제약이 만듦

### 4교시 · INSERT·UPDATE·DELETE·RETURNING

#### 안전한 변경 순서

##### 변경 SQL은 확인하고, 바꾸고, 다시 확인한다 (PDF p.39)

- UPDATE·DELETE 전에 같은 조건의 SELECT로 대상 확인
- 대상 조회(WHERE·실제 ID) → BEGIN(취소 가능한 묶음) → 변경·RETURNING(어느 행이 변했나) → 종료·재조회(COMMIT/ROLLBACK)
- 4교시는 BEGIN으로 보호하고 ROLLBACK으로 종료
- 확정하는 COMMIT은 7교시에 비교

#### INSERT·UPDATE·DELETE

##### 새 지식을 넣고, 발급된 ID를 바로 읽는다 (PDF p.40)

- `BEGIN;` 후 `INSERT INTO knowledge (title, content, category_id) VALUES ('임시 안내', '한 번만 실행합니다.', 1) RETURNING id, title, category_id;`
- 결과의 id를 확인한 뒤 `ROLLBACK;`을 별도로 실행
- S0의 분류 1 존재가 전제이며 다르면 실제 분류 ID 사용
- INSERT는 새 행 추가, RETURNING은 실제 생성 결과
- ROLLBACK 후 새 행은 남지 않음
- ID를 4로 고정하지 않으며 취소해도 번호는 건너뛸 수 있음

##### 같은 지식 ID의 본문만 바꾼다 (PDF p.41)

- `UPDATE knowledge SET content = '실행 전에 가상환경을 확인합니다.' WHERE id = 2 RETURNING id, title, content;`
- SET은 바꿀 열과 값, WHERE는 바꿀 대상, RETURNING은 변경한 행
- ROLLBACK 뒤 `SELECT id, content FROM knowledge WHERE id = 2`로 원래 본문 확인
- ID와 총 행 수는 바뀌지 않음
- S0 기준 변경 1행, ROLLBACK 뒤 원문 복원

##### 지식 한 행을 삭제하고 취소한다 (PDF p.42)

- `DELETE FROM knowledge WHERE id = 3 RETURNING id, title;` 후 ROLLBACK
- DELETE는 행을 삭제하며 테이블 구조는 유지
- WHERE를 생략하면 전체 행이 삭제 대상
- 이 예시는 취소하므로 초기 지식 3번이 다시 조회됨
- 삭제 시 RETURNING 1행, 취소 후 SELECT 1행

#### SQL 결과와 HTTP 응답

##### 0행·오류·HTTP 응답을 구분한다 (PDF p.43)

- 없는 ID를 SELECT하면 0행이며 SQL 자체는 정상, API에서는 상세 404 또는 목록 빈 배열 등의 정책
- 없는 ID를 UPDATE하면 `UPDATE 0`과 RETURNING 0행, API에서 변경 성공으로 응답할지 별도 판단
- 정상 INSERT는 생성된 행과 실제 ID, API에서는 저장 성공 후 HTTP 201
- 잘못된 참조·본문은 DB 오류와 미확정 변경, API에서 예외와 응답 정책을 명시적으로 연결
- SQL이 200·201·204·404·422를 직접 보내지 않으며 HTTP 응답은 FastAPI의 책임

#### 실습

##### 실습 04 · CRUD를 SQL로 직접 연결한다 (PDF p.44)

- 35분, 세 단계 중 하나 선택
- 기본필수는 INSERT·UPDATE·DELETE의 핵심 구문을 완성하고 실제 ID·변경 행 수·취소 후 결과 확인
- 응용은 한 건을 직접 구성해 추가하고 받은 ID로 변경, 없는 ID의 0행 결과도 따로 기록
- 심화는 쓰기 SQL과 검증 SQL의 역할을 나누고 대상·변경 내용·보존해야 할 행 명시
- 4교시는 제공 BEGIN/ROLLBACK 구간에서 연습
- 롤백은 번호의 연속성까지 복원하지 않음

**핵심:** 변경 SQL은 같은 조건의 SELECT로 대상을 먼저 읽고 BEGIN 안에서 RETURNING으로 바뀐 행을 확인하며 SQL의 0행·오류는 HTTP 응답과 별개로 판단

### 5교시 · JOIN·LEFT JOIN·GROUP BY

#### JOIN으로 분류명 연결

##### 키로 연결하면 지식에 분류명이 붙는다 (PDF p.45)

- 분류 표의 ID와 지식 표의 `category_id`를 `c.id = k.category_id`로 연결
- 지식 1 → learning, 지식 2 → environment, 지식 3 → learning
- 연결 후에도 한 행은 지식 한 건
- learning 이름의 반복은 정상적인 관계 결과

##### 지식 목록에 분류명을 함께 표시한다 (PDF p.46)

- `SELECT k.id, k.title, c.name AS category FROM knowledge AS k JOIN categories AS c ON c.id = k.category_id ORDER BY k.id;`
- `k`는 knowledge, `c`는 categories의 별칭
- ON은 맞출 값, `AS category`는 결과 열의 이름
- 결과 한 행은 지식 한 건
- S0 기준 3행, 분류명은 learning·environment

##### 지식이 없는 분류도 결과에 남긴다 (PDF p.47)

- `FROM categories AS c LEFT JOIN knowledge AS k ON k.category_id = c.id ORDER BY c.id, k.id`
- 왼쪽 categories의 모든 분류 유지, 오른쪽은 연결된 지식
- 연결할 지식이 없는 reference 분류도 결과에 남음
- 연결할 지식이 없으면 오른쪽 열은 NULL
- S0 기준 총 4행, reference의 `knowledge_id`는 NULL

#### 집계와 COUNT

##### 분류별 지식 수를 집계한다 (PDF p.48)

- `SELECT c.name AS category, COUNT(k.id) AS knowledge_count ... LEFT JOIN ... GROUP BY c.id, c.name ORDER BY c.id;`
- GROUP BY는 분류별로 묶기
- `COUNT(k.id)`는 실제 지식만 세며 NULL인 지식 ID는 세지 않음
- 결과 한 행은 분류 한 개
- S0 기준 learning 2, environment 1, reference 0

##### COUNT(*)와 COUNT(k.id)는 무엇을 세는가? (PDF p.49)

- learning은 실제 지식 두 행으로 `COUNT(*)`·`COUNT(k.id)` 모두 2
- environment는 실제 지식 한 행으로 둘 다 1
- reference는 오른쪽이 NULL인 보존 행이라 `COUNT(*)`는 1, `COUNT(k.id)`는 0
- 지식이 0개인 분류를 1개로 세지 않으려면 실제 자식 ID를 셈

##### 행을 세고, 본문 길이를 요약한다 (PDF p.50)

- `COUNT(*)`, `SUM(char_length(content))`, `MIN(...)`, `MAX(...)`로 knowledge 요약
- COUNT는 행 개수, SUM은 합계, MIN·MAX는 가장 작은 값·큰 값
- S0 기준 3건, 본문 합계 64자, 최소 20자, 최대 24자
- 이 수치가 본문 내용의 정확성을 보장하지는 않음

#### 실습

##### 실습 05 · JOIN과 집계로 지식 현황을 읽는다 (PDF p.51)

- 35분, 세 단계 중 하나 선택
- 기본필수는 지식과 분류를 JOIN하는 조건을 완성하고 분류별 지식 수에서 빈 분류의 0 확인
- 응용은 추가 조건과 HAVING을 더 직접 작성하고 조건을 바꾸기 전 예상 행을 먼저 기록
- 심화는 JOIN 전후의 결과 단위·행 수를 검증하고 WHERE 위치가 빈 분류에 미치는 영향 비교
- S0 기준 learning 2 · environment 1 · reference 0
- 작업 후에는 실제 현재 상태로 다시 계산

**핵심:** JOIN 결과 한 행은 지식 한 건, GROUP BY 결과 한 행은 분류 한 개이며 빈 분류를 0으로 세려면 LEFT JOIN과 `COUNT(k.id)`를 함께 사용

### 6교시 · 제약조건·실패·데이터 보존

#### 검증 위치와 제약조건

##### API 검증과 DB 제약은 서로 다른 위치다 (PDF p.52)

- 오늘은 pgAdmin·psql의 SQL 직접 실행 → DB 제약(필수·길이·참조) → 저장 또는 오류
- 내일은 JSON 요청 → FastAPI 입력 검증·연결 → DB 제약의 저장 규칙 검사
- 오늘의 SQL은 FastAPI를 통과하지 않으므로 DB 제약이 따로 필요
- 형식 검증은 내용의 사실성·권한·AI 답변 품질 검증을 대신하지 않음

##### 제약조건의 역할을 정확한 문장으로 읽는다 (PDF p.53)

- PRIMARY KEY는 각 행을 유일하게 식별하며 NULL 불가, 예는 `knowledge.id`
- FOREIGN KEY는 참조 대상의 존재 보장, 예는 `knowledge.category_id`
- NOT NULL은 NULL 저장 금지, 예는 title·content
- UNIQUE는 같은 값의 중복 금지, 예는 `categories.name`
- CHECK는 정해진 조건 검사, 예는 본문 길이 1~2,000자
- DEFAULT는 값을 생략할 때 채우는 규칙이며 명시적으로 넣은 NULL을 자동 교정하지 않음

#### 실패 시험과 회복

##### 빈 본문을 보내 DB가 거부하는지 확인한다 (PDF p.54)

- `BEGIN;` 후 `INSERT ... VALUES ('오류 확인', '', 1);`로 빈 본문 입력
- 기대 오류는 `knowledge_content_length` 위반, 기대 SQLSTATE는 23514
- 분류 1은 실제로 존재해야 하며 제목 등 나머지 값은 정상으로 두어 실패 원인을 하나로 한정
- 오류 이름과 SQLSTATE를 읽은 뒤 `ROLLBACK;`만 별도로 실행
- 롤백 뒤 `SELECT COUNT(*) FROM knowledge;`로 행 내용·개수 비교
- 실패 행은 저장되지 않음
- ID 다음 번호는 비교 대상이 아님

##### 지식 삭제와 분류 삭제는 영향이 다르다 (PDF p.55)

- `DELETE FROM knowledge WHERE id = …`는 해당 지식 행만 제거하며 부모 categories와 다른 지식은 그대로 유지
- `DELETE FROM categories WHERE name = 'learning'`은 연결된 지식이 있어 RESTRICT로 거부
- 부모 삭제가 자식 삭제로 번지지 않음
- 분류 삭제 전에 먼저 업무 정책 결정
- 이번 공통 설계는 ON DELETE RESTRICT이며 CASCADE를 편리하다는 이유만으로 켜지 않음

##### 실패 원인과 회복 순서를 함께 기록한다 (PDF p.56)

- 필수 title = NULL은 23502, NOT NULL 위반
- 분류 learning 중복은 23505, UNIQUE 위반
- content = 빈 문자열은 23514, 길이 CHECK 위반
- 없는 category_id는 23503, FK 위반이며 부모 확인
- 오류 뒤 계속 SQL을 실행하면 25P02, 현재 트랜잭션 중단 상태이므로 ROLLBACK부터 실행
- 목표는 코드 암기가 아니라 기대한 제약으로 실패했는지와 정리 후 데이터 보존 여부 확인

#### 실습

##### 실습 06 · 실패해도 기존 지식은 보존된다 (PDF p.57)

- 35분, 세 단계 중 하나 선택
- 기본필수는 제공된 빈 본문·없는 분류 입력을 하나씩 실행하고 오류 확인 → ROLLBACK → 기존 행 확인 수행
- 응용은 NULL·분류명 중복·참조 중인 부모 삭제를 추가하고 제약조건과 오류 원인을 대응
- 심화는 실패 검증 SQL과 결과 기록을 분리하고 원인별 기대 오류·데이터 불변·회복 확인
- “오류가 났다”만으로는 통과가 아님
- 의도한 제약으로 실패했는지와 원래 행·값이 남았는지 확인

**핵심:** 실패 시험은 한 번에 원인 하나만 넣어 기대한 제약과 SQLSTATE로 거부되는지 확인하고 ROLLBACK 뒤 기존 행과 값이 그대로인지까지 비교

### 7교시 · COMMIT/ROLLBACK·INDEX·EXPLAIN

#### 트랜잭션의 확정과 취소

##### 트랜잭션은 변경의 확정·취소 단위다 (PDF p.58)

- BEGIN(작업 시작) → 변경·확인(아직 미확정) → COMMIT(변경 확정) 또는 ROLLBACK(미확정 변경 취소)
- BEGIN부터 같은 연결에서 작업하고 현재 변경의 종료 방식 선택
- 이미 COMMIT한 변경은 이어서 ROLLBACK해도 취소되지 않음

##### 취소하면 직전 미확정 변경이 사라진다 (PDF p.59)

- 시작 → 작업 중 → 취소 후의 세 시점에서 `SELECT id, content FROM knowledge WHERE id = 2` 비교
- 시작에는 현재 본문, 작업 중에는 임시 본문 `'취소할 임시 안내입니다.'`, 취소 후에는 시작 본문
- ROLLBACK은 DB 전체를 과거 상태로 돌리는 명령이 아님
- 같은 연결에서 직접 확인
- 행 수와 ID는 그대로 유지

##### 확정한 값은 새 연결에서도 다시 읽는다 (PDF p.60)

- `BEGIN;` → `UPDATE knowledge SET content = '실행 전에 가상환경을 확인합니다.' WHERE id = 2 RETURNING id, content;` → `COMMIT;`
- 연결을 닫고 `knowledge_lab`에 다시 접속한 뒤 id 2 조회
- id 2의 수정 본문 유지가 기대 결과
- DB 서버를 강제로 끄지 않음
- 단순 재접속은 서버 장애 시험이 아님
- 이후 S0의 본문은 달라졌으므로 실제 현재값을 기준으로 확인

##### 행이 취소돼도 발급 번호는 되돌아가지 않을 수 있다 (PDF p.61)

- 어제 API 검증 422는 파일 저장 함수에 도달하지 않아 파일 `next_id`도 그대로
- 오늘 INSERT 뒤 ROLLBACK은 새 행은 남지 않지만 발급한 시퀀스 값은 재사용되지 않을 수 있음
- 오늘 DB 제약으로 INSERT가 실패해도 실패 행은 저장되지 않지만 이미 발급된 번호가 있으면 빈 번호 발생
- 공통 원칙은 행의 ID·내용·개수로 검증하며 `max(id)`를 행 수로 사용하지 않음
- 번호가 1, 2, 5여도 정상일 수 있음
- 다음 ID를 예상하지 않고 RETURNING 값 사용

#### 인덱스와 실행계획

##### 분류 조회를 돕는 인덱스를 검토한다 (PDF p.62)

- `pg_indexes`에서 `schemaname = 'public' AND tablename = 'knowledge'`로 현재 인덱스 먼저 확인
- 같은 이름·정의가 없을 때만 `CREATE INDEX idx_knowledge_category_id ON knowledge (category_id);`를 한 번 실행
- 인덱스는 행을 찾는 별도 탐색 구조이며 분류 조건·JOIN의 접근 후보
- 자식 FK 열에는 인덱스가 자동 생성되지 않음
- 읽기를 도울 수 있지만 쓰기·공간 유지 비용 발생
- 모든 쿼리를 빠르게 하지는 않음

##### 작은 데이터의 Seq Scan도 정상이다 (PDF p.63)

- `EXPLAIN SELECT id, title FROM knowledge WHERE category_id = 1;`은 예상 실행계획
- `EXPLAIN (ANALYZE, BUFFERS)`는 실제 실행
- rows는 예상 행 수와 실제 행 수를 구분해 읽음
- cost는 밀리초가 아님
- 이 수업은 SELECT만 측정
- 계획 이름을 고정 정답으로 요구하지 않으며 작은 데이터의 Seq Scan도 정상

#### 실습

##### 실습 07 · 취소·확정과 조회 계획을 확인한다 (PDF p.64)

- 30분, 세 단계 중 하나 선택
- 기본필수는 같은 지식의 ROLLBACK 전후와 COMMIT 후 재접속을 비교하고 제공 인덱스와 EXPLAIN에서 계획 읽기
- 응용은 변경 SQL을 두 문장으로 묶어 결과를 비교하고 ID 번호가 건너뛰어도 행 검증이 맞는 이유 설명
- 심화는 제공 원자성 검증과 인덱스 전후 기록을 보완하고 SQL·검증·실행 순서를 역할별로 정리
- 취소·확정 결과와 근거를 기록
- 더 빠른 실행계획이나 연속 ID는 필수 정답이 아님

**핵심:** ROLLBACK은 현재 연결의 미확정 변경만 취소하고 COMMIT한 값은 새 연결에서 다시 읽어 확인하며 ID 공백과 Seq Scan은 오류가 아님

### 연결 · 후속 수업과 프로젝트 전 정리

#### 후속 수업 연결

##### 내일은 같은 지식 API를 PostgreSQL에 연결한다 (PDF p.65)

- 11/10은 JSON 파일 지식 CRUD API, title·content·category와 실제 ID
- 11/11은 관계형 지식 DB·SQL·ERD, categories·knowledge와 제약·트랜잭션
- 11/12는 FastAPI–PostgreSQL 연동, 접속 설정·ORM·Migration·통합 검증
- 오늘 SQL을 만들었다고 API가 자동 연결되지 않음
- 연결·예외·트랜잭션 범위는 내일 구현

##### 원본 지식과 검색·생성은 서로 다른 책임이다 (PDF p.66)

- 원본 지식 → 문서·메타데이터 → 검색용 인덱스 → 검색·생성의 4단계
- 원본 지식은 오늘 SQL로 관리
- 문서·메타데이터 처리 연결은 11/19, 검색용 인덱스는 11/18~19, Basic RAG는 11/20
- 원본 수정·삭제가 벡터 인덱스에 자동 반영되지 않음
- Agent 도구 연결도 별도 설계

#### 프로젝트 전 정리

##### 오늘 배운 것을 한 번에 연결한다 (PDF p.67)

- “내 지식을 어떤 구조로 저장하고 어떤 SQL과 근거로 관리할 것인가?”가 정리 질문
- ERD·키(대상과 관계) → SQL·JOIN(입력과 조회) → 제약·트랜잭션(거부·취소·확정) → 결과 기록(행·값·실제 ID)
- 일일프로젝트에서는 새 기술을 추가하지 않고 앞에서 쓰던 DB와 SQL을 이어 나만의 사례 완성

### 8교시 · 나만의 지식 DB 일일프로젝트

#### 과제 정의와 대상 상태

##### 나만의 AI 도움말 지식 DB (PDF p.68)

- 50분 일일프로젝트
- 사용자와 주제를 하나 정함, 예는 우리 반 학습·팀 온보딩·FAQ
- 가상의 안내문 3개를 직접 작성하고 등록할 분류 확인
- 현재 `knowledge_lab`과 SQL을 재사용
- A는 유지, B는 수정, C는 삭제
- JOIN·집계로 내 결과를 확인하고 제약·취소·확정·재접속까지 검증
- 새 FastAPI·LLM·벡터 검색·화면·자동 배포는 구현하지 않음

##### 세 지식의 역할과 실제 ID를 기록한다 (PDF p.69)

- 기존 지식은 시작 목록·내용을 보존하며 최종 개수와 내용이 그대로
- A는 내 지식 등록 후 유지하며 원래 내용으로 조회
- B는 본문 수정을 취소 한 번, 확정 한 번 수행하며 확정한 새 본문으로 조회
- C는 등록 후 삭제를 COMMIT하며 상세 SELECT 0행
- 시작 지식 수 N → 생성 3건 COMMIT 후 N+3 → C 삭제 COMMIT 후 N+2

#### 통과 기준

##### 등록과 조회로 내 지식 목록을 만든다 (PDF p.70)

- 시작 단계는 현재 DB·목록 수 N·기존 행 내용 기록, 기준은 `knowledge_lab`과 실제 시작값
- 생성 단계는 내 지식 3건 INSERT·RETURNING·COMMIT, 기준은 서로 다른 실제 A·B·C ID와 N+3
- 목록·상세 단계는 실제 ID로 SELECT하고 분류명 JOIN, 기준은 내 지식과 기존 행 모두 확인
- 집계 단계는 분류별 `COUNT(k.id)` 조회, 기준은 전체 지식 수와 분류별 합계 일치
- 지식 3개는 SQL INSERT로 등록
- 제목은 ID의 대체물이 아니며 중복될 수 있음

##### B를 취소해 보고, 다시 확정한다 (PDF p.71)

- B 원문 기록(SELECT) → 수정 후 취소(BEGIN → UPDATE → ROLLBACK) → 다시 수정·확정(BEGIN → UPDATE → COMMIT) → 새 연결 조회
- 수정 후에도 ID와 총 행 수는 같아야 함
- 확인 기준은 내 프로젝트의 실제 값
- ROLLBACK 뒤에는 B 원문, COMMIT 뒤 재접속에는 B 수정문이 보여야 함

##### 거부할 입력과 삭제할 행을 따로 확인한다 (PDF p.72)

- 빈 본문 INSERT는 길이 CHECK 오류, ROLLBACK 뒤 기존 지식 불변
- 없는 분류 ID INSERT는 FK 오류, ROLLBACK 뒤 기존 지식 불변
- C의 실제 ID로 DELETE·COMMIT하면 삭제 행 1건, A·B·기존 지식 보존
- 새 연결에서 다시 SELECT하면 C는 0행, A·B는 각 1행, 총 N+2와 B 수정 본문 유지
- DB 오류코드와 HTTP 상태코드를 섞지 않음
- 실패 후 ID의 다음 번호는 검사하지 않음

#### 결과 기록과 시간 배분

##### 결과 기록은 SQL과 실제 결과를 함께 남긴다 (PDF p.73)

- 사용자·주제는 누구를 위한 어떤 안내인지 기록하며 실제 개인정보·기관 내부 자료는 제출하지 않음
- ERD·규칙은 두 테이블·PK/FK·삭제 정책을 기록하며 도구 가입 증명·복잡한 그림은 불필요
- SQL·결과는 실제 A·B·C ID·N·변경/조회 결과를 기록하며 예상값만 적은 실행 주장은 제출하지 않음
- 설명은 JOIN 한 행의 뜻·취소/확정·다음 API 연결을 기록하며 비밀번호·접속 비밀은 제외
- 긴 보고서보다 재실행할 수 있는 SQL과 실제 근거가 중요
- 기본필수는 수동 확인으로 충분

##### 마지막 50분 · 안내 6 + 수행 40 + 공유 4 (PDF p.74)

- 0~6분 목표·통과 기준·난이도 선택, 현재 DB와 시작 코드 확인
- 6~11분 사용자·주제·안내 3개 준비, N과 현재 지식·분류 확인
- 11~26분 등록·JOIN·집계·B 수정, 실제 ID와 예상/실제 결과 기록
- 26~41분 취소·확정·실패·C 삭제·재접속, 오류 근거와 최종 N+2 확인
- 41~46분 SQL·ERD·짧은 기록 정리로 재현 가능한 제출물 작성
- 46~50분 대표 시연·한 문장 회고, 플랫폼에서 DB 역할 설명
- 추가 교시가 아님
- 미완성자는 공통 목표부터, 완료자는 선택 확장 하나만 보완

##### 일일프로젝트 · 같은 목표를 수준에 맞게 완성한다 (PDF p.75)

- 40분, 세 단계 중 하나 선택
- 기본필수는 제공 SQL 골격으로 내 지식 3개를 관리하고 JOIN·집계·제약·취소/확정·재접속 직접 확인
- 응용은 직접 작성하는 조건과 검증을 늘리고 분류 두 개와 빈 결과를 비교하며 SQL을 역할별로 분리
- 심화는 기존 스키마·데이터·검증 파일 구성을 활용하고 복합 변경 취소와 실행계획의 근거 보완
- 공통 A 유지·B 수정·C 삭제·N+2와 기존 행 보존이 우선
- 기본필수만으로 만점 가능

#### 평가

##### 평가 기준 · 기본필수만으로 100점 (PDF p.76)

- 접속·관계 설명 15점은 현재 DB·두 테이블·PK/FK·ERD
- CRUD·대상 보존 25점은 A 유지·B 수정·C 삭제·기존 행 보존
- JOIN·집계 20점은 분류명 연결과 분류별 개수의 실제 결과
- 제약·트랜잭션 25점은 의도한 거부·ROLLBACK/COMMIT·재접속
- 실행 기록·설명 15점은 실제 ID·N·SQL·오류 원인·플랫폼 역할
- 추가 테이블·자동 테스트·빠른 실행계획·연속 ID는 공통 만점의 조건이 아님

**핵심:** 일일프로젝트는 같은 `knowledge_lab`에서 시작 N과 기존 행을 기록하고 A 유지·B 취소 후 확정·C 삭제로 최종 N+2와 기존 지식 보존을 실제 ID와 SQL 결과로 증명

### 마무리 · 오늘의 완료와 다음 단계

#### 완료 기준

##### 오늘 완성한 것은 AI 플랫폼의 지식 관리 DB다 (PDF p.77)

- 테이블·PK/FK로 지식과 분류의 관계 설명
- SQL로 지식을 관리하고 JOIN·집계 결과 해석
- 제약조건과 COMMIT·ROLLBACK의 결과를 직접 확인
- 내일 FastAPI와 연결하고 검색·생성·Agent는 이후 단계
- 확인 질문은 “FK와 JOIN은 같은가?”와 “이미 COMMIT한 값을 ROLLBACK으로 취소할 수 있는가?”

### 참고 부록 · 준비 SQL·선택 확장·Windows 접속·참고자료

#### 개인 DB 준비 A01~A05

##### 개인 학습 DB를 만들고 접속을 바꾼다 (PDF p.78)

- `postgres` DB에서 `CREATE DATABASE knowledge_lab;`만 단독 실행
- Auto commit이 켜져 있어야 하며 BEGIN 안에서 실행하지 않음
- 이후 `knowledge_lab`을 선택해 Query Tool을 새로 열고 `SELECT current_database();`로 확인
- 이미 같은 DB가 있으면 내용을 먼저 확인하고 임의로 DROP하지 않음
- A02 → A03 → A04 → A05 순서로 빈 개인 DB에 한 번만 준비

##### 전체 DDL · categories (PDF p.79)

- 부모 `categories`부터 `knowledge_lab`에서 생성
- 분류명은 1~30자·필수·중복 금지
- 정의는 3교시 본문 DDL과 동일
- 이미 생성된 테이블에는 다시 실행하지 않음
- 예상 결과는 `CREATE TABLE`, 다음 단계는 knowledge 생성

##### 전체 DDL · knowledge (PDF p.80)

- 부모 `categories`가 먼저 존재해야 함
- 제목 1~80자, 본문 1~2,000자, 분류는 필수 FK
- 삭제 정책은 RESTRICT
- 정의는 3교시 본문 DDL과 동일한 계약
- 예상 결과는 `CREATE TABLE`, 다음 단계는 가상 Seed 입력

##### Seed · 분류를 넣고 첫 지식을 연결한다 (PDF p.81)

- `INSERT INTO categories (name) VALUES ('learning'), ('environment'), ('reference') RETURNING id, name;`
- 첫 지식은 `INSERT ... SELECT '실습 파일 보관', '실습 파일은 개인 폴더에 보관합니다.', id FROM categories WHERE name = 'learning'`
- 분류명이 UNIQUE이므로 SELECT로 실제 분류 ID 획득
- 부모가 없으면 INSERT SELECT가 0행일 수 있으므로 RETURNING 결과 확인
- 결과는 분류 3건·지식 1건, 다음 단계는 지식 2건 추가

##### Seed · 나머지 지식과 시작 상태 확인 (PDF p.82)

- ‘서버 실행’은 environment, ‘질문 작성’은 learning 분류를 같은 INSERT SELECT 방식으로 입력
- `SELECT COUNT(*) FROM knowledge;`로 시작 상태 확인
- 정상 기준 S0는 categories 3건, knowledge 3건, learning 2건·environment 1건·reference 0건
- 기존 DB에 Seed를 반복하지 않음
- 전체 준비 뒤 본문 SELECT 실행
- ID는 실제 조회 결과로 확인

#### 연습·응용·심화 SQL

##### 본 테이블을 건드리지 않고 키를 연습한다 (PDF p.83)

- `BEGIN;` 후 `categories_try`·`knowledge_try`를 만들어 PK·FK 연결 확인
- 기준 데이터와 이름을 분리한 구조 학습용 축소 예제
- 연습용 ID는 수동 번호
- 같은 연결에서 ROLLBACK하면 `_try` 테이블 생성도 취소
- 본문의 실제 모델은 IDENTITY·길이 규칙 사용

##### HAVING으로 집계된 분류를 고른다 (PDF p.84)

- `GROUP BY c.id, c.name HAVING COUNT(k.id) >= 2 ORDER BY c.name`
- WHERE는 묶기 전 행 조건, HAVING은 묶은 뒤 그룹 조건
- S0에서는 learning 한 행
- 현재 데이터를 바꿨다면 기대 결과도 달라짐
- 새로운 필수 기능이 아니라 응용의 작은 조회 확장

##### 생략한 값과 명시한 NULL을 구분한다 (PDF p.85)

- `defaults_try (label TEXT DEFAULT '미지정')`에 `DEFAULT VALUES`와 `(NULL)`을 각각 입력
- 값을 생략하면 ‘미지정’, NULL을 입력하면 NULL
- 기대 결과는 ‘미지정’·false와 NULL·true
- 이 표는 NULL을 허용하며 NOT NULL을 추가하면 NULL 입력 거부
- 연습 후 ROLLBACK

##### 두 번째 변경이 실패하면 첫 변경도 취소한다 (PDF p.86)

- 먼저 현재 2·3번 원문 기록
- `BEGIN;` 후 2번 본문을 임시 본문으로 UPDATE, 3번 본문을 빈 문자열로 UPDATE
- 두 번째 문장의 CHECK 오류를 확인한 뒤 ROLLBACK을 별도로 실행
- 같은 묶음의 2번 첫 변경도 남지 않아야 함
- `WHERE id IN (2, 3)` 조회로 두 지식의 시작값 보존 확인
- 원자성 확인은 IDENTITY 연속성과 무관

##### 지식에 여러 태그가 필요해지면 N:M을 검토한다 (PDF p.87)

- knowledge 1→N knowledge_tags N←1 tags 구조
- `knowledge_tags`는 `knowledge_id` FK와 `tag_id` FK, 두 열의 조합이 PK
- 한 지식에 여러 태그, 한 태그에 여러 지식 연결
- 같은 `(knowledge_id, tag_id)` 조합의 중복 방지
- 선택 설계 예시이며 공통 완료 조건은 categories·knowledge 두 테이블 그대로

#### Windows·pgAdmin·psql

##### 설치에서 첫 Query Tool까지 확인하는 순서 (PDF p.88)

- 받기 단계는 공식 Windows 안내 → EDB 설치 프로그램, 강사가 정한 안정 18.x 사용, 기존 데이터 삭제 금지
- 구성 단계는 Server·pgAdmin·Command Line Tools, Stack Builder는 선택, 기관 관리자 승인 확인
- 설정 단계는 서버 비밀번호·Port·Data Directory, 비밀번호 비공개, 실제 Port를 접속 설정에 사용
- 접속 단계는 pgAdmin에서 Server 연결 등록, Host·Port·User·서버 비밀번호로 인증
- DB 선택 단계는 `knowledge_lab` → Query Tool, DB 생성은 A01, 현재 DB 이름 확인
- 실행 단계는 `SELECT 1;`을 선택해 실행하고 Data Output의 1과 Messages 확인
- 기준은 설치 화면의 완료 표시가 아니라 현재 DB에서 SQL 결과를 확인했는지 여부

##### 환경 오류는 데이터 오류와 분리한다 (PDF p.89)

- connection refused는 서버 실행·Host·Port 확인, 서비스 상태와 설치한 포트 점검
- 인증 실패는 사용자·서버 비밀번호 확인, pgAdmin 보호 비밀번호와 구분
- database does not exist는 DB 이름 확인, 개인 학습 DB 생성 여부 점검
- relation does not exist는 현재 DB·스키마·준비 순서 확인, A01~A05 실행 대상과 테이블 점검
- psql 명령을 못 찾으면 Command Line Tools·경로 확인, SQL Shell 또는 설치 bin 경로 사용
- 정상 환경을 임의 삭제·재설치하거나 기관 보안 정책을 우회하지 않음

##### 터미널 명령과 psql 전용 명령을 나눈다 (PDF p.90)

- PowerShell에서 `psql -U postgres -h localhost -p 5432 -d knowledge_lab`로 접속
- 접속한 psql에서 `SELECT current_database();`와 `\conninfo`·`\dt`·`\d knowledge`·`\q` 실행
- `\dt`·`\d`·`\q`는 SQL이 아닌 psql 명령이며 pgAdmin Query Tool에 붙이지 않음
- 같은 서버·DB이면 pgAdmin과 psql에서 같은 테이블 확인 가능

#### 이후 연동·검수·공식 자료

##### DB로 바꿀 때 자동으로 해결되지 않는 것 (PDF p.91)

- 스키마는 Pydantic 모델과 DB 테이블 정의는 다르며 입력·저장·응답 규칙의 일치 확인 필요
- 데이터 이관은 JSON이 DB로 자동 이동하지 않으며 기존 ID·분류 매핑·중복 정책 확인 필요
- 분류 입력은 새 category 문자열 허용 정책에 따라 조회/생성·UNIQUE 충돌·트랜잭션 처리 필요
- 검색 데이터는 원본 수정이 청크·벡터를 자동 갱신하지 않으며 수정·삭제 전파와 출처 추적 필요
- 공개 서비스는 로컬 학습과 운영 환경은 다르며 앱 권한·비밀 설정·백업·관측 필요
- 후속 수업의 연결 지점 목록이며 오늘 구현할 과제가 아님

##### 강의 기준과 제작 환경의 검수를 구분한다 (PDF p.92)

- 교육 기준은 PostgreSQL 18 문서·Windows 11·pgAdmin 중심, psql 보조
- PPT는 전체 슬라이드 렌더링, 문구·표·SQL·번호, 화면 배치 점검
- SQL은 공식 문서 대조·기준값 계산·별도 관계 논리 검산이며 PostgreSQL 실행은 아님
- PostgreSQL 서버 직접 실행·Windows 설치·pgAdmin UI 조작은 미검증
- 강의 전 실제 교실 PostgreSQL에서 DDL·Seed·실패·COMMIT/ROLLBACK 재확인

##### 공식 참고자료 · 접속·SQL·설계 (PDF p.93)

- S01~S05는 PostgreSQL·pgAdmin의 서버·클라이언트·설치·접속·Query Tool
- S06~S10은 PostgreSQL 18의 SELECT·Schema·Constraint·CREATE·Identity
- S11~S13은 RETURNING·UPDATE·DELETE
- S14~S16은 JOIN·Table expressions·Aggregate
- 각 슬라이드 하단의 코드와 발표자 노트에서 공식 링크 확인

##### 공식 참고자료 · 검증·트랜잭션·인덱스 (PDF p.94)

- S17~S18은 Transactions·Sequence functions
- S19~S20은 Indexes·Using EXPLAIN
- S21~S24는 Error codes·NULL·Character·Pattern
- S25~S26은 CREATE DATABASE·Defaults
- 성능 수치·고정 실행계획·ID 연속성은 검증하지 않은 사실처럼 제시하지 않음

## 자료 간 표기 차이

- 실습 README·SQL 머리말·`PPT_대응표.md`의 “PPT N”과 “84장”은 원본 PPT 기준. 현재 PDF는 p.2~11에 도입 10장이 추가된 94쪽이며 원본 2~84쪽이 PDF p.12~94에 해당(PDF 쪽수 = PPT 쪽수 + 10). 예: 실습 01~08은 PPT 13·20·28·34·41·47·54·65쪽, PDF p.23·30·38·44·51·57·64·75. 준비 SQL의 “PPT 68~72”는 PDF p.78~82(부록 A01~A05).
- 실습 README의 S1은 7교시 COMMIT 이후 상태를 가리키는 이름. PDF에는 S1 표기 없이 p.60에서 “S0의 본문은 이제 달라졌다”로만 안내.
