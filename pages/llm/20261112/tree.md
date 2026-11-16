# Day19 오후 강의 구조·핵심 설명

2026-11-12(목) 13:30~18:20 · 생성형 AI·LLM 및 RAG 엔지니어링 3/18 오후 · FastAPI–PostgreSQL 연동 지식 관리 API → 연결 → ORM CRUD → 오류·Migration → 통합 검증

오후 강의 PDF만 정리한 문서입니다. 오전은 강의 없이 자율 실습(Day19_01)으로 진행되어 포함하지 않았습니다. 교시 번호는 오후 안의 순서(PDF의 PM 01~PM 05)이고, 교시 설명은 PDF p.14 운영표의 핵심 내용 원문입니다. 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준이며 인쇄 쪽수와 같습니다(전체 82쪽). 도입·후속 연결·마무리·부록은 교시 표시가 없어 별도 묶음으로 두었습니다. 실습은 기본필수·응용·심화 중 한 단계를 골라 같은 API 계약과 두 테이블로 진행하는 구성입니다.

## 강의 목차

```text
도입 · 오전 실습에서 오후 연동으로
├─ 현업 문제와 플랫폼 속 위치
│  ├─ FastAPI–PostgreSQL 연동 지식 관리 API 완성 (PDF p.1)
│  ├─ 현업 사례 | AI 도우미가 쓰는 지식은 누가 관리할까? (PDF p.2)
│  └─ AI Agent 전체 구조에서 오늘의 작업 위치 (PDF p.3)
├─ 플랫폼에서 DB 필드까지 확대
│  ├─ AI 플랫폼에서 DB 필드 하나까지 점점 확대한다 (PDF p.4)
│  └─ 오전의 독립 실습이 오후에는 한 요청으로 연결된다 (PDF p.5)
├─ 요청 하나의 내부 구조
│  ├─ FastAPI 안에서는 Route → 함수 → 매개변수로 들어간다 (PDF p.6)
│  ├─ ORM 클래스에서 테이블·행·외래 키까지 확대한다 (PDF p.7)
│  ├─ Session은 요청 하나의 DB 작업 범위를 관리한다 (PDF p.8)
│  └─ flush 이후에도 COMMIT 전이면 아직 미확정이다 (PDF p.9)
├─ 검증과 오늘의 프로젝트
│  ├─ 운영 개발은 스키마 변경과 API 검증을 나누어 본다 (PDF p.10)
│  └─ 오늘의 일일프로젝트는 Agent의 원본 지식 계층 완성 (PDF p.11)
└─ 오후 시연과 운영
   ├─ 오전에는 각각, 오후에는 하나로 연결한다 (PDF p.12)
   ├─ AI 플랫폼에서 오늘 만드는 부분 (PDF p.13)
   ├─ 오후 5교시 · 먼저 연결하고, 마지막에 완성한다 (PDF p.14)
   └─ 세 단계 모두 DB 연동 CRUD까지 완성한다 (PDF p.15)

1교시 · 설정·ORM 흐름·첫 DB 조회
├─ 연결 대상과 API 계약
│  ├─ 어느 DB를 연결할지 먼저 고정한다 (PDF p.16)
│  └─ 바꾸지 않을 약속 · 경로·입력·응답 (PDF p.17)
├─ 패키지와 접속 설정
│  ├─ 기존 환경에 필요한 패키지만 추가한다 (PDF p.18)
│  ├─ .env · 접속 정보와 코드를 분리한다 (PDF p.19)
│  └─ URL.create · 비밀번호를 문자열로 조립하지 않는다 (PDF p.20)
├─ 구성 요소와 접속 확인
│  ├─ Engine·Driver·ORM·Session을 나누어 읽는다 (PDF p.21)
│  ├─ 같은 DB를 보고 있는지 실제로 확인한다 (PDF p.22)
│  └─ 같은 지식 · 외부 표현과 내부 표현은 다르다 (PDF p.23)
├─ Session Dependency와 첫 ORM 조회
│  ├─ 요청마다 Session을 만들고 끝나면 정리한다 (PDF p.24)
│  └─ 첫 GET · SQL로 넣은 지식이 API에 보인다 (PDF p.25)
└─ 실습
   └─ 실습 01 · 설정부터 실제 DB 목록 조회까지 (PDF p.26)

2교시 · Schema·분류 연결·POST·PUT·DELETE
├─ ORM Model과 Pydantic Schema
│  ├─ ORM Model과 Pydantic은 서로 다른 규칙을 읽는다 (PDF p.27)
│  ├─ Category · 분류 테이블과 맞춘다 (PDF p.28)
│  ├─ Knowledge · 지식의 필드와 FK를 맞춘다 (PDF p.29)
│  └─ 입력 세 필드와 응답 네 필드를 유지한다 (PDF p.30)
├─ 분류 연결과 생성
│  ├─ 분류명은 찾고, 없으면 같은 작업 안에서 만든다 (PDF p.31)
│  └─ POST · 분류와 지식을 저장한 뒤 201을 반환한다 (PDF p.32)
├─ 상세 조회·수정·삭제
│  ├─ PK로 찾고, 없으면 기존 404 계약을 지킨다 (PDF p.33)
│  ├─ PUT · ID를 유지하고 세 필드를 교체한다 (PDF p.34)
│  └─ DELETE · commit 후 본문 없는 204로 끝낸다 (PDF p.35)
└─ 실습
   └─ 실습 02 · 다섯 API를 DB CRUD로 연결한다 (PDF p.36)

3교시 · 트랜잭션·오류·데이터 보존
├─ 트랜잭션 경계와 Session 메서드
│  ├─ 성공과 실패는 서로 다른 종료 경로다 (PDF p.37)
│  ├─ 비슷해 보이는 메서드의 역할을 구분한다 (PDF p.38)
│  ├─ transaction · flush와 commit 실패를 모두 감싼다 (PDF p.39)
│  └─ 새 분류만 남는 불완전한 저장을 막는다 (PDF p.40)
├─ 오류 분류와 HTTP 응답
│  ├─ 오류의 원인과 HTTP 응답을 함께 구분한다 (PDF p.41)
│  └─ IntegrityError를 실제 제약 이름으로 분류한다 (PDF p.42)
├─ 실패 검증과 디버깅
│  ├─ 실패도 서로 다른 두 종류로 검증한다 (PDF p.43)
│  └─ 응답이 이상하면 연결 대상부터 다시 본다 (PDF p.44)
└─ 실습
   └─ 실습 03 · 실패한 요청에서 지식이 보호되는가 (PDF p.45)

4교시 · Migration·API/DB 통합 검증
├─ Migration의 역할과 DB 분리
│  ├─ Model 수정과 실제 DB 변경은 별도다 (PDF p.46)
│  └─ 주 프로젝트·Migration·테스트 DB를 분리한다 (PDF p.47)
├─ Revision 작성과 적용
│  ├─ 작은 변경을 순서대로 적용하고 확인한다 (PDF p.48)
│  ├─ 002_source · 추가와 되돌림을 함께 읽는다 (PDF p.49)
│  ├─ 대상을 확인한 뒤 제공된 변경을 적용한다 (PDF p.50)
│  └─ autogenerate는 초안이고, stamp는 수리가 아니다 (PDF p.51)
├─ API·DB 통합 검증
│  ├─ API 성공은 실제 DB 증거와 함께 확인한다 (PDF p.52)
│  └─ 응답의 id로 Test DB를 다시 조회한다 (PDF p.53)
└─ 실습
   └─ 실습 04 · 작은 Migration과 통합 검증 (PDF p.54)

후속 연결 · RAG·Agent와의 경계
└─ 오늘 만든 서비스와 이후 AI 기능
   └─ 오늘의 서비스는 이후 AI 기능의 기반이다 (PDF p.55)

5교시 · 작은 일일프로젝트·시연
├─ 프로젝트 목표와 통과 기준
│  ├─ 나만의 PostgreSQL 연동 AI 도움말 API (PDF p.56)
│  ├─ A 유지 · B 수정 · C 삭제를 끝까지 추적한다 (PDF p.57)
│  └─ 응답에서 받은 id를 SQL에 연결한다 (PDF p.58)
└─ 진행·수준·평가
   ├─ 마지막 50분 · 안내 6 + 수행 40 + 공유 4 (PDF p.59)
   ├─ 같은 연동 서비스를 수준에 맞게 완성한다 (PDF p.60)
   └─ 기본필수만으로 공통 평가 100점 (PDF p.61)

마무리 · 복습과 다음 단계
├─ 요청 흐름 복습
│  └─ 세 질문으로 요청 한 건의 흐름을 설명한다 (PDF p.62)
└─ 완료 범위와 다음 수업
   └─ 오늘의 완료와 다음 단계의 경계를 남긴다 (PDF p.63)

부록 · 전체 코드·검증·참고자료
├─ 폴더 구조·설정·DB 모듈
│  ├─ 구조는 이해한 책임만큼 나눈다 (PDF p.64)
│  ├─ settings.py · 경로가 고정된 설정 읽기 (PDF p.65)
│  └─ db.py · 연결과 Session의 준비 (PDF p.66)
├─ ORM·main 정의와 경계 사례
│  ├─ models.py · 공통 Base와 import (PDF p.67)
│  ├─ Knowledge의 길이 CHECK와 스키마를 빠뜨리지 않는다 (PDF p.68)
│  ├─ main.py · 연결된 예제의 선행 정의 (PDF p.69)
│  ├─ category 필터 · SQL 조건으로 연결한다 (PDF p.70)
│  └─ 기존 계약을 몰래 바꾸지 않는다 (PDF p.71)
├─ 오류 처리기와 Session 복구 시연
│  ├─ HTTP 변환은 알려진 오류만 정확히 처리한다 (PDF p.72)
│  ├─ 접속 오류도 설정·운영 오류와 구분한다 (PDF p.73)
│  └─ 같은 Session에서 실패 후 rollback을 확인한다 (PDF p.74)
├─ Migration·테스트 DB
│  ├─ 연습 DB 전용 Engine을 Alembic에 전달한다 (PDF p.75)
│  ├─ Migration 예제의 처음·중간·끝 상태 (PDF p.76)
│  ├─ 테스트는 요청마다 Test Session을 주입한다 (PDF p.77)
│  └─ 정상·경계·실패 확인표 (PDF p.78)
└─ 실행 환경·참고자료·검수 범위
   ├─ 실행 위치·가상환경·오전 서버를 구분한다 (PDF p.79)
   ├─ 공식 참고자료 · API·설정·ORM (PDF p.80)
   ├─ 공식 참고자료 · DB·Migration·검증 (PDF p.81)
   └─ 검수한 것과 아직 확인하지 못한 것을 구분한다 (PDF p.82)
```

## 핵심 설명

### 도입 · 오전 실습에서 오후 연동으로

#### 현업 문제와 플랫폼 속 위치

##### FastAPI–PostgreSQL 연동 지식 관리 API 완성 (PDF p.1)

- 정규교과 3/18 오후 표지
- 오늘의 흐름은 연결 → ORM CRUD → 오류·Migration → 통합 검증
- RAG·AI Agent 플랫폼의 데이터 기반이라는 위치 제시

##### 현업 사례 | AI 도우미가 쓰는 지식은 누가 관리할까? (PDF p.2)

- 가상환경 정책이 바뀐 상황에서 AI 도우미가 무엇을 근거로 답할지 묻는 현업 질문
- 지식 담당자는 관리 화면·/docs에서 안내를 등록·수정하고 FastAPI → ORM·Session → PostgreSQL 경로로 원본을 저장
- AI 도우미는 이후 RAG 검색·LLM 생성·Agent 도구 실행으로 질문에 답하는 별도 업무
- 오늘 만드는 것은 원본 지식 관리이며 검색용 인덱스 반영과 Agent 답변은 이후 단계
- 답변용 지식이 바뀌면 원본을 안전하게 등록·수정하고 반영 여부까지 확인

##### AI Agent 전체 구조에서 오늘의 작업 위치 (PDF p.3)

- 오늘 구현하는 경로는 담당자·/docs → FastAPI API → ORM·Session → PostgreSQL
- 질문 처리 경로는 직원 질문 → Agent 실행·도구 → Retriever·LLM → 답변·출처이며 향후 구성 예시
- 원본 지식은 별도 동기화·인덱싱을 거쳐야 검색 자료가 됨
- API가 존재한다고 Agent 도구로 자동 등록되지 않음
- PostgreSQL은 원본 지식 저장 계층이며 모델·Retriever·Agent와 다른 역할

#### 플랫폼에서 DB 필드까지 확대

##### AI 플랫폼에서 DB 필드 하나까지 점점 확대한다 (PDF p.4)

- AI Agent 서비스 → 지식 관리 서비스 → FastAPI 엔드포인트 → ORM·Session → 테이블·행·필드의 다섯 단계 확대
- 엔드포인트 단계의 예는 `POST /api/knowledge`의 요청·응답 계약
- ORM·Session 단계는 Python 객체를 DB 행으로 처리하고 확정·취소하는 범위
- 가장 작은 단계는 `knowledge.category_id → categories.id` 필드 연결
- 큰 개념에서 작은 개념으로 이동해도 같은 업무 요청 하나를 추적

##### 오전의 독립 실습이 오후에는 한 요청으로 연결된다 (PDF p.5)

- 오전에는 FastAPI → JSON 파일 CRUD와 pgAdmin → PostgreSQL SQL CRUD를 따로 확인
- 오전 상태에서는 API를 호출해도 DB가 자동으로 바뀌지 않음
- 오후에는 `POST /api/knowledge` → 입력 검증 → ORM·Session → PostgreSQL → 201 응답으로 연결
- 완료 증거는 API 응답 id, SQL로 조회한 `knowledge.id`, 다시 GET한 id의 일치
- API 성공 응답만으로 끝내지 않고 같은 ID의 실제 DB 행까지 확인

#### 요청 하나의 내부 구조

##### FastAPI 안에서는 Route → 함수 → 매개변수로 들어간다 (PDF p.6)

- HTTP 요청 `POST /api/knowledge`와 Body의 title·content·category가 출발점
- `@app.post(...)` Route가 요청을 처리 함수에 연결하고 `KnowledgeWrite`로 입력 검증
- 처리 함수는 `payload: KnowledgeWrite`와 `db: DbSession` 두 매개변수를 받아 분류 확인·ORM 저장 호출
- Agent 도구로 쓰려면 Method·Path·입력 스키마·권한을 계약으로 관리

##### ORM 클래스에서 테이블·행·외래 키까지 확대한다 (PDF p.7)

- 요청 JSON의 `category = "learning"`은 ORM에서 `Knowledge.category_id = 1`로 바뀜
- `public.categories`는 분류 테이블, `public.knowledge`는 지식 테이블
- 지식의 `id`는 DB가 실제로 발급한 값
- PK는 행 식별, FK는 참조 검사, JOIN은 분류명 조회로 서로 다른 책임
- 외부 API는 category 문자열, 내부 DB는 `category_id` 외래 키 사용

##### Session은 요청 하나의 DB 작업 범위를 관리한다 (PDF p.8)

- Engine·Pool은 애플리케이션에서 재사용하는 DB 연결 기반
- 요청 A(POST)와 요청 B(GET)는 각자의 Session을 가지며 작업 상태를 공유하지 않음
- Session은 ORM 객체·SQL·트랜잭션의 작업 공간
- Session은 Psycopg Driver를 거쳐 PostgreSQL과 통신
- 요청이 끝나면 Session 자원을 정리하며 `close`는 `commit`이 아님

##### flush 이후에도 COMMIT 전이면 아직 미확정이다 (PDF p.9)

- 분류 확인·추가 → 지식 객체 추가 → `flush()`로 ID 확인까지 같은 Session·같은 트랜잭션에서 진행
- `flush()` 뒤에도 COMMIT 전이면 미확정 상태
- 정상이면 COMMIT으로 새 분류와 지식을 함께 확정
- 오류면 ROLLBACK으로 현재 미확정 변경을 함께 취소
- API의 201 응답은 COMMIT 성공 이후 반환
- DB 제약 오류와 API 입력 422는 서로 다른 단계의 실패

#### 검증과 오늘의 프로젝트

##### 운영 개발은 스키마 변경과 API 검증을 나누어 본다 (PDF p.10)

- 구조 변경은 Alembic으로 ORM Model 열 추가 → Revision 초안·DDL 검토 → 연습 DB에 upgrade → 실제 열·기존 행·이력 확인
- 동작 검증은 POST 201과 응답 id → SQL로 같은 id 조회 → PUT 200·DELETE 204 → 실패 요청·재시작 후 상태 확인
- 주 프로젝트 DB와 Migration·테스트 DB는 분리
- ORM 코드를 수정해도 실제 DB 열은 자동으로 바뀌지 않음

##### 오늘의 일일프로젝트는 Agent의 원본 지식 계층 완성 (PDF p.11)

- A는 POST 201 → SQL로 같은 ID 확인 → 재시작 뒤 보존
- B는 PUT 200 → DB의 같은 ID·변경값 확인 → 기존 행·분류 보존
- C는 DELETE 빈 204 → DB 조회 0행 → GET 404
- API 다섯 경로, Session·트랜잭션, 같은 DB 행 검증을 하나로 묶은 결과물
- 별도 연습 DB에서 Migration 한 건 적용
- 기본필수는 /docs·pgAdmin 수동 검증으로 완료
- RAG 인덱싱·Agent 도구·권한 정책 연결은 이후 단계

#### 오후 시연과 운영

##### 오전에는 각각, 오후에는 하나로 연결한다 (PDF p.12)

- 오전은 FastAPI → JSON 파일, SQL → PostgreSQL을 각각 확인한 상태
- 오후는 FastAPI → ORM·Session → DB로 연결하고 SQL로 같은 ID를 다시 조회
- API의 새 지식과 DB의 새 행이 일치해야 완료
- 시연 순서는 POST 한 번 → 응답 id 확인 → pgAdmin에서 같은 id 조회 → API 재조회

##### AI 플랫폼에서 오늘 만드는 부분 (PDF p.13)

- 클라이언트(오늘은 /docs) → FastAPI(입력·응답 약속) → ORM·Session(조회·변경·확정) → PostgreSQL(지식·분류·제약)의 네 구성
- 지식 관리 기능을 먼저 연결하고 검색·생성·도구 실행은 이후에 추가
- API·DB 연동만으로 AI 답변이 생성되지 않으며 RAG·Agent 처리 코드는 후속 수업

##### 오후 5교시 · 먼저 연결하고, 마지막에 완성한다 (PDF p.14)

- 13:30~14:20 설정·ORM 흐름·첫 DB 조회, 설명·시연 25분과 실습 25분
- 14:30~15:20 Schema·분류 연결·POST·PUT·DELETE, 설명·시연 25분과 실습 25분
- 15:30~16:20 트랜잭션·오류·데이터 보존, 설명·시연 20분과 실습 30분
- 16:30~17:20 Migration·API/DB 통합 검증, 설명·시연 20분과 실습 30분
- 17:30~18:20 작은 일일프로젝트·시연, 설명·시연 10분과 실습 40분
- 수업 250분은 설명·시연 100분과 실습·확인 150분이며 쉬는 시간 10분씩 별도

##### 세 단계 모두 DB 연동 CRUD까지 완성한다 (PDF p.15)

- 기본필수는 제공 설정·Model·저장 골격에서 핵심 호출을 완성하고 /docs와 SQL로 요청·응답·DB 행 확인
- 응용은 조회 조건 하나와 직접 작성할 로직을 늘리고 반복 코드를 함수·간단한 파일로 분리
- 심화는 Router·Schema·Service·Repository로 책임을 나누고 제공 테스트 틀에서 오류·DB 반영·격리 검증
- 수준은 하나만 선택
- 기본필수만으로 공통 평가 100점 가능

### 1교시 · 설정·ORM 흐름·첫 DB 조회

#### 연결 대상과 API 계약

##### 어느 DB를 연결할지 먼저 고정한다 (PDF p.16)

- 주 연결 대상은 오전 CRUD DB이며 기본필수 `day19_crud_b`, 응용 `day19_crud_a`, 심화 `day19_crud_h`
- 오전 CRUD DB에서는 공통 두 테이블과 기존 행 보존
- `knowledge_lab` 등 다른 정상 DB는 구조를 확인한 뒤 명시적으로 선택하고 DB명과 실제 초기 개수 기록
- `day19_build_*` 구축 연습 DB는 비었거나 미완성일 수 있어 주 연결 대상으로 자동 선택 금지
- `day19_migration_lab`·`day19_api_test`는 Migration·자동 테스트 전용
- 기존 DB를 DROP·재초기화하지 않음
- API 시작 시 `create_all`·Seed 자동 실행을 넣지 않음

##### 바꾸지 않을 약속 · 경로·입력·응답 (PDF p.17)

- `GET /api/knowledge`는 입력 없이 200과 id 오름차순 배열 반환, 응용부터 category 조건 추가
- `GET /api/knowledge/{knowledge_id}`는 정수 Path ID로 200과 지식 하나 반환
- `POST /api/knowledge`는 title·content·category를 받아 201과 DB가 발급한 id 포함 결과 반환
- `PUT /api/knowledge/{knowledge_id}`는 Path ID와 세 필드 모두를 받아 200과 같은 id의 수정 결과 반환
- `DELETE /api/knowledge/{knowledge_id}`는 204와 본문 없음
- 없는 지식은 404 `{"detail":"Knowledge not found"}`
- 잘못된 입력은 FastAPI 기본 422

#### 패키지와 접속 설정

##### 기존 환경에 필요한 패키지만 추가한다 (PDF p.18)

- 오전의 정상 가상환경을 재사용하고 fastapi·pydantic·uvicorn 설치 여부부터 확인
- 추가 설치는 `sqlalchemy>=2.0,<2.1`, `psycopg[binary]>=3,<4`, `pydantic-settings`, `alembic`
- `httpx`·`pytest`는 심화 자동 테스트에만 필요
- 오전 서버는 종료하고 오후 서버는 8001 포트로 구분
- 실행은 오후 앱의 프로젝트 최상위에서 `python -m uvicorn main:app --port 8001 --reload`
- 오후 문서 주소는 `127.0.0.1:8001/docs`
- 설치 명령은 예시이며 실제 검증 조합은 부록에서 구분
- GPU·CUDA는 필요 없음

##### .env · 접속 정보와 코드를 분리한다 (PDF p.19)

- `.env`에 DB_HOST·DB_PORT·DB_NAME·DB_USER·DB_PASSWORD 다섯 값 기록
- 값은 pgAdmin에서 쓰던 서버·포트·DB·계정과 정확히 일치
- 실제 값이 든 `.env`는 제출·Git에 넣지 않음
- `.gitignore`에 `.env`, `.env.*`, `.venv/`, `__pycache__/`를 넣고 `!.env.example`만 예외 처리
- `.env.example`에는 빈 예시만 둠
- `.env`는 암호화 저장소가 아님
- 같은 이름의 환경변수가 있는지도 확인
- DB 이름이 틀리면 다른 데이터를 보게 됨

##### URL.create · 비밀번호를 문자열로 조립하지 않는다 (PDF p.20)

- `URL.create("postgresql+psycopg", ...)`에 username·password·host·port·database를 구성요소로 전달
- `@`·`%`가 들어간 비밀번호도 URL.create가 처리
- 비밀번호는 `settings.db_password.get_secret_value()`로 꺼냄
- `create_engine`은 연결을 빌리는 기반을 만들 뿐이며 생성만으로 접속 성공은 아님
- `pool_pre_ping=True`는 연결 생존 점검
- `hide_parameters=True`와 `connect_args={"connect_timeout": 5}` 함께 지정
- Engine은 앱에서 재사용하고 Session은 요청마다 생성

#### 구성 요소와 접속 확인

##### Engine·Driver·ORM·Session을 나누어 읽는다 (PDF p.21)

- Engine·Pool은 연결 생성·재사용
- Psycopg는 PostgreSQL과의 통신을 맡는 Driver
- ORM Model은 클래스와 테이블의 대응
- Session은 객체·SQL·트랜잭션의 작업 공간
- 네 이름은 같은 기능의 다른 이름이 아님
- 오늘은 동기 `def`와 일반 Session 사용
- 이 그림은 역할 비교이며 요청의 실행 순서는 앞의 연결 흐름으로 확인

##### 같은 DB를 보고 있는지 실제로 확인한다 (PDF p.22)

- `check_database.py`에서 `engine.connect()`로 `current_database()`, `current_user`, `public.knowledge` 행 수 조회
- 확인 순서는 DB·사용자 확인 → `public.knowledge` 읽기 → pgAdmin 결과와 대조
- 오전 변경이 남아 있을 수 있어 행 수를 3으로 고정하지 않음
- 접속만 성공한 것과 구조가 일치하는 것은 다르므로 실제 테이블도 확인
- 이 확인은 로컬 터미널에서만 실행

##### 같은 지식 · 외부 표현과 내부 표현은 다르다 (PDF p.23)

- API는 id·title·content·category 네 필드로 프로그램과 약속
- API의 category는 `"learning"` 같은 문자열
- DB는 `knowledge(id, title, content, category_id)`와 `categories(id, name)` 두 테이블
- POST·PUT의 세 입력 필드는 오전과 동일
- DB는 `category_id`로 연결하고 응답에서는 분류명을 돌려줌
- 입력 모델은 테이블이 아니며 ORM 선언만으로 기존 테이블이 바뀌지 않음

#### Session Dependency와 첫 ORM 조회

##### 요청마다 Session을 만들고 끝나면 정리한다 (PDF p.24)

- `sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)`로 `SessionLocal` 생성
- `get_db()`는 `with SessionLocal() as db: yield db` 구조
- yield 앞에서 요청의 Session 준비, yield 값은 함수 매개변수로 전달, 요청이 끝나면 `Session.close`
- `close`는 성공 저장이 아니며 쓰기 확정은 `commit`이 담당
- `DbSession = Annotated[Session, Depends(get_db)]`로 Route에 주입
- 전역 공유 Session 금지, 요청별로 생성·정리

##### 첫 GET · SQL로 넣은 지식이 API에 보인다 (PDF p.25)

- `select(Knowledge, Category.name)`으로 지식과 분류명 선택
- `.join(Category, Knowledge.category_id == Category.id)`로 FK와 PK 연결
- `.order_by(Knowledge.id)`로 id 오름차순
- `db.execute(stmt).all()`이 실제 조회 실행
- `to_read(row, name)`으로 응답 네 필드로 변환
- 정상 결과는 200과 DB의 실제 목록, 비어 있으면 200과 `[]`
- Model·Schema·`to_read`는 제공 골격

#### 실습

##### 실습 01 · 설정부터 실제 DB 목록 조회까지 (PDF p.26)

- 실습 시간 25분
- 기본필수는 제공 설정·Model 골격으로 접속 대상을 맞추고 API 목록과 pgAdmin의 지식 ID·제목·분류명 대조
- 응용은 목록 조회 함수를 연결하고 category 조건 하나를 추가해 일치 결과와 200·`[]` 직접 확인
- 심화는 설정·DB 수명·조회 역할을 분리하고 테스트 연결을 바꿀 수 있는 지점 설명
- 완료 기준은 /docs의 예시가 아니라 실제 DB의 지식이 API 응답으로 보이는 것

**핵심:** API 목록이 pgAdmin에서 본 같은 DB·같은 행을 보여 줄 때 연결이 완성된 것으로 판단.

### 2교시 · Schema·분류 연결·POST·PUT·DELETE

#### ORM Model과 Pydantic Schema

##### ORM Model과 Pydantic은 서로 다른 규칙을 읽는다 (PDF p.27)

- ORM Model은 DB 쪽 규칙으로 Category·Knowledge 클래스가 열·자료형·PK·FK·CHECK를 표현
- ORM Model은 Session이 객체를 추적하며 DB의 실제 구조와 맞아야 함
- Pydantic은 API 쪽 규칙으로 KnowledgeWrite·KnowledgeRead가 JSON의 필수 값·길이·응답 필드를 표현
- Pydantic의 category는 외부 문자열이며 DB의 내부 열을 그대로 공개하지 않음
- `from_attributes=True` 하나로 `category_id`가 category 문자열로 자동 변환되지 않음

##### Category · 분류 테이블과 맞춘다 (PDF p.28)

- `__tablename__ = "categories"`, `{"schema": "public"}`
- `id`는 `BigInteger`, `Identity(always=True)`, `primary_key=True`로 DDL의 BIGINT·GENERATED ALWAYS와 대응
- `name`은 `String(30)`, `nullable=False`, `unique=True`로 VARCHAR(30)과 UNIQUE에 대응
- `CheckConstraint("char_length(name) BETWEEN 1 AND 30", name="categories_name_length")`로 길이 제약 표현
- 클래스 선언은 CREATE 실행이 아니며 기존 테이블을 다시 생성하지 않음
- DB 규칙은 실제 DB에도 있어야 함

##### Knowledge · 지식의 필드와 FK를 맞춘다 (PDF p.29)

- 제목은 `String(80)`, 1~80자
- 본문은 `Text`, 1~2,000자
- 분류는 필수 BIGINT FK이며 `ForeignKey("public.categories.id", name="knowledge_category_fk", ondelete="RESTRICT")`
- 지식 제목은 중복 허용
- 분류 삭제는 FK가 보호
- 길이 CHECK 2개와 schema 지정을 포함한 전체 정의는 부록 A05
- 같은 클래스를 두 번 선언하지 않음

##### 입력 세 필드와 응답 네 필드를 유지한다 (PDF p.30)

- `KnowledgeWrite`는 title(1~80), content(1~2000), category(1~30) 세 필드를 `Field`로 검증
- POST·PUT 모두 세 입력이 필수
- `KnowledgeRead`는 `KnowledgeWrite`에 DB가 발급한 `id`를 더한 응답 모델
- `to_read(row, category)`가 ORM 행과 분류명을 응답 모델로 변환
- PUT에 content만 보내면 기본 422
- 응답은 id·title·content·category 네 필드만 포함
- 응용부터 Schema를 `schemas.py`로 분리 가능

#### 분류 연결과 생성

##### 분류명은 찾고, 없으면 같은 작업 안에서 만든다 (PDF p.31)

- `get_or_create_category(db, name)`은 `select(Category).where(Category.name == name)`으로 분류 조회
- 이미 있는 분류는 그 ID 재사용
- 없는 분류는 `Category(name=name)`을 `db.add`한 뒤 `db.flush()`로 id만 확보하며 아직 미확정
- 이 도우미 안에서는 commit하지 않고 분류와 지식을 함께 확정
- transaction 안에서만 호출하는 제공 골격
- 외부 입력은 category 문자열, 내부 저장은 `category_id`
- “조회 후 생성”이 동시성 문제 전체를 해결하지 않으며 동시 생성 충돌은 부록의 오류 정책으로 처리

##### POST · 분류와 지식을 저장한 뒤 201을 반환한다 (PDF p.32)

- `@app.post("/api/knowledge", status_code=201, response_model=KnowledgeRead)`
- 처리 순서는 입력 검증 → 분류 ID 결정 → `Knowledge` 객체 `db.add` → `db.flush()`로 DB 발급 id 확인 → commit 성공 후 응답
- 모든 쓰기는 `with transaction(db):` 안에서 실행
- 201의 id는 DB 행의 id와 같음
- `next_id`를 직접 관리하지 않음
- transaction 도우미는 다음 교시에서 확대

#### 상세 조회·수정·삭제

##### PK로 찾고, 없으면 기존 404 계약을 지킨다 (PDF p.33)

- `knowledge_or_404`는 `db.get(Knowledge, knowledge_id)`로 PK 조회
- `db.get`은 없으면 `None`을 반환하고 이때 `HTTPException(404, "Knowledge not found")` 발생
- 상세 조회는 `category_id`로 부모 Category를 찾아 분류명을 응답에 넣음
- 정수가 아닌 Path ID는 기본 422
- 없는 정수 ID는 404
- 목록이 0건이면 404가 아니라 200과 `[]`

##### PUT · ID를 유지하고 세 필드를 교체한다 (PDF p.34)

- 수정은 `knowledge_or_404`로 조회부터 시작해 없는 지식을 먼저 거부
- 없는 지식이면 새 분류도 만들지 않음
- 객체의 title·content·category_id 속성을 바꾸면 flush·commit 때 UPDATE 실행
- id와 지식 개수는 유지
- 없는 ID를 새로 생성하지 않음

##### DELETE · commit 후 본문 없는 204로 끝낸다 (PDF p.35)

- `db.delete(row)`는 삭제 대상으로 표시, 실제 삭제 확정은 commit
- 해당 지식만 삭제하고 부모 분류는 자동 삭제하지 않음
- `Response(status_code=204)`로 본문 길이 0 반환
- `{}`·`null`·메시지도 반환하지 않음
- 삭제 뒤 상세 조회는 404

#### 실습

##### 실습 02 · 다섯 API를 DB CRUD로 연결한다 (PDF p.36)

- 실습 시간 25분
- 기본필수는 제공 도우미로 생성·PUT·삭제의 핵심 호출을 완성하고 반환 ID를 SQL로 찾아 API와 DB 값 대조
- 응용은 분류 필터와 함수 분리를 더 직접 작성하고 새 분류·기존 분류 처리와 빈 조회 결과 확인
- 심화는 Router와 저장 로직을 분리하되 트랜잭션 경계는 하나로 두고 API 계약을 바꾸지 않은 채 같은 CRUD 결과 확인
- 완료 기준은 GET 목록·상세, POST, PUT, DELETE 모두가 DB의 실제 상태와 일치

**핵심:** 외부의 category 문자열을 내부 `category_id`로 바꿔 저장하고, 응답 id로 찾은 DB 행이 API 결과와 같을 때 CRUD 연결이 맞은 것으로 판단.

### 3교시 · 트랜잭션·오류·데이터 보존

#### 트랜잭션 경계와 Session 메서드

##### 성공과 실패는 서로 다른 종료 경로다 (PDF p.37)

- 새 분류와 새 지식처럼 함께 맞아야 하는 변경을 하나의 작업으로 묶음
- 성공 경로는 COMMIT으로 함께 확정한 뒤 요청 종료·Session 정리
- 실패 경로는 ROLLBACK으로 함께 취소한 뒤 요청 종료·Session 정리
- COMMIT 뒤 ROLLBACK을 실행해도 이미 확정한 변경은 취소되지 않음

##### 비슷해 보이는 메서드의 역할을 구분한다 (PDF p.38)

- `add(obj)`는 새 객체를 Session에 등록하며 즉시 commit하지 않음
- `flush()`는 변경 SQL을 전송해 id를 확보할 수 있지만 트랜잭션을 확정하지 않음
- `commit()`은 필요한 flush 후 변경을 확정하지만 모든 오류·경쟁을 자동 해결하지 않음
- `refresh(obj)`는 DB 값을 객체에 다시 읽으며 저장 명령이 아님
- `rollback()`은 현재 미확정 변경을 취소하고 실패 상태를 정리하지만 발급된 ID 번호는 되돌리지 않음
- `close()`는 Session의 연결·상태를 정리하며 저장을 자동 확정하지 않음
- 수업 코드 순서는 flush → 응답 객체 준비 → commit → return
- `refresh`는 필요할 때만 사용

##### transaction · flush와 commit 실패를 모두 감싼다 (PDF p.39)

- `db.py`의 `@contextmanager` `transaction(db)`가 요청의 쓰기 경계를 하나로 정함
- with 안의 조회·변경·flush가 끝나면 정상일 때 한 번 `db.commit()`
- 예외가 나면 `db.rollback()`으로 미확정 작업을 취소하고 `raise`로 예외를 다시 전달
- 예외를 성공 응답으로 숨기지 않음
- 한 요청의 쓰기 전체에 한 번 사용
- 도우미 안에서 추가 commit 금지
- transaction 중첩 호출 금지
- HTTP 오류 변환은 이 도우미와 별도
- commit 성공 전에는 201·200·204를 보내지 않음

##### 새 분류만 남는 불완전한 저장을 막는다 (PDF p.40)

- 새 분류 INSERT → 먼저 COMMIT → 지식 INSERT 실패 순서로 나누면 지식 없이 새 분류만 남을 수 있음
- 수업 코드는 새 분류 INSERT·flush → 지식 INSERT·flush → 함께 COMMIT 또는 ROLLBACK
- 도우미 안의 flush는 중간 확정이 아님
- 422 요청은 저장 전 거부이므로 rollback 증거가 아님
- 실제 DB 실패의 rollback은 별도 시연·테스트로 확인

#### 오류 분류와 HTTP 응답

##### 오류의 원인과 HTTP 응답을 함께 구분한다 (PDF p.41)

- 필수 값·길이·Path 형식 오류는 FastAPI 기본 검증의 422이며 쓰기 코드로 들어가지 않음
- 정상 입력이지만 없는 지식 ID는 404 `Knowledge not found`이며 새 지식·분류를 만들지 않음
- 알려진 분류 UNIQUE·FK 충돌은 409 `Data conflict`이며 현재 트랜잭션 rollback
- 확인된 연결 실패·접속 시간초과는 503 `Database unavailable`이며 성공으로 보고하지 않음
- 예상 밖 CHECK·SQL·설정 오류는 500 일반 오류 메시지이며 내부 코드·구조 불일치 점검
- 409·503은 이 교안이 명시한 분류 정책
- 모든 DB 오류를 “중복”으로 바꾸지 않음

##### IntegrityError를 실제 제약 이름으로 분류한다 (PDF p.42)

- `exc.orig`의 `sqlstate`와 `diag.constraint_name`으로 실패 원인 판별
- 23505는 UNIQUE 위반, 23503은 FK 위반
- `("23505", "categories_name_key")`, `("23503", "knowledge_category_fk")` 두 조합만 409
- 그 밖의 IntegrityError는 500 `Database operation failed`
- 같은 예외 종류라도 실패한 제약은 다를 수 있음
- rollback은 쓰기 도우미가 담당
- 지식 제목 중복은 허용이므로 제목 중복 409를 만들지 않음
- 전체 예외 처리기는 부록 A09

#### 실패 검증과 디버깅

##### 실패도 서로 다른 두 종류로 검증한다 (PDF p.43)

- 입력 검증은 `content=""` POST → 422를 확인하고 기존 목록·행 내용 불변 확인
- 입력 검증 결과는 쓰기 전 거부의 확인이며 DB rollback의 증거가 아님
- DB 오류 시연은 별도 DB의 Session에서 제약 위반 → rollback 후 행·후속 조회 확인
- DB 오류 시연은 같은 Session의 회복을 확인하는 것이며 시퀀스 번호는 원복 기준이 아님
- 오류 뒤 정상 POST → 201은 다음 요청의 성공 확인이며 이전 Session 재사용 증거가 아님
- 기본필수는 /docs·SQL 수동 대조와 강사 시연 이해로 충분
- 심화는 별도 DB 테스트로 보완

##### 응답이 이상하면 연결 대상부터 다시 본다 (PDF p.44)

- API 결과와 SQL 결과가 다르면 서버 포트·DB_NAME·schema·실제 ID부터 확인하고 Seed를 무작정 다시 넣지 않음
- DB를 못 찾거나 인증에 실패하면 pgAdmin의 Host·Port·DB·계정과 비교하고 비밀번호·접속 문자열을 공개하지 않음
- 테이블·열 오류는 ORM 매핑과 실제 DDL을 대조하고 `create_all`로 모든 차이를 해결하려 하지 않음
- `PendingRollbackError`는 실패 후 rollback 여부와 경계 중첩을 확인하고 같은 Session을 계속 쓰지 않음
- POST 재시도 후 중복 데이터는 이전 요청의 성공 여부와 실제 DB를 조회하고 실패처럼 보여도 무조건 재전송하지 않음

#### 실습

##### 실습 03 · 실패한 요청에서 지식이 보호되는가 (PDF p.45)

- 실습 시간 30분
- 기본필수는 404·422 전후의 DB 지식과 분류를 비교하고 제공된 rollback 시연에서 취소·정리 위치 설명
- 응용은 알려진 DB 충돌과 예상 밖 오류의 분류를 확인하고 실패 후 정상 요청과 잘못된 분류 추가 여부 점검
- 심화는 별도 DB에서 flush·commit 실패 경로를 테스트하고 같은 Session 복구와 새 요청 성공을 나누어 확인
- 완료 기준은 오류 응답·실제 데이터·트랜잭션 경계가 서로 맞는 것

**핵심:** 실패한 요청 뒤에도 지식과 분류가 그대로이고, 422·404·409·503·500이 실패 원인에 맞게 구분될 때 데이터가 보호된 것으로 판단.

### 4교시 · Migration·API/DB 통합 검증

#### Migration의 역할과 DB 분리

##### Model 수정과 실제 DB 변경은 별도다 (PDF p.46)

- ORM에 새 열을 선언해도 기존 DB는 옛 구조일 수 있음
- `create_all`은 일반적인 기존 열 변경·이력 관리 도구가 아님
- Migration은 Revision에 변경 순서 기록 → 사람이 내용 검토 → 대상 DB에 upgrade → 구조와 기존 데이터 확인
- 이 과정을 Alembic으로 관리
- 오늘은 별도 연습 DB에서 작은 변경 한 건만 확인
- 주 프로젝트 DB는 그대로 둠

##### 주 프로젝트·Migration·테스트 DB를 분리한다 (PDF p.47)

- 주 프로젝트 DB(`day19_crud_b` 등)는 오전에 사용한 지식·분류 보존
- 주 프로젝트 DB에서는 초기 Revision·DROP·Seed 반복 금지
- Migration 연습 DB(`day19_migration_lab`)는 새 개인 빈 DB와 제공 초기 Revision에서 시작
- Migration 연습의 완료 기준은 001 → 데이터 1건 → 002 → 데이터 보존
- 자동 테스트 DB(`day19_api_test`)는 주 DB와 다른 전용 구조·가상 데이터 사용
- 자동 테스트는 연결 대상 검사 후 실행하고 생성한 항목만 정리
- DB명만 다른 URL인지가 아니라 실제 Host·Port·Database와 접속 결과 확인

#### Revision 작성과 적용

##### 작은 변경을 순서대로 적용하고 확인한다 (PDF p.48)

- 연습 예시는 지식의 출처 표기용 `source_label` 열을 선택 항목으로 추가하는 변경
- 순서는 `001_initial`(두 테이블 생성) → 기준 데이터(가상 지식 1건) → `002_source`(nullable 열 추가) → 검증(열·이력·기존 행)
- `source_label` 추가만으로 RAG 출처 검증이 구현되지 않음
- API 네 필드 계약은 유지

##### 002_source · 추가와 되돌림을 함께 읽는다 (PDF p.49)

- `revision`은 현재 변경 ID, `down_revision`은 바로 앞 변경(`001_initial`)
- `upgrade()`는 `op.add_column`으로 `source_label` `String(120)` `nullable=True` 열을 `public.knowledge`에 추가
- `downgrade()`는 `op.drop_column`으로 그 열 삭제
- 열을 삭제하면 그 열 안의 데이터는 잃음
- NOT NULL 새 필드를 기존 행에 무작정 강제하지 않음
- 자동 생성된 초안도 검토 대상

##### 대상을 확인한 뒤 제공된 변경을 적용한다 (PDF p.50)

- `migration_demo` 폴더에서 `.env.migration`을 사용해 실행
- `alembic current`·`alembic history`로 현재 상태와 이력 확인
- `alembic upgrade 001_initial` 뒤 가상 지식 1건을 추가하고 COMMIT
- `alembic upgrade head` 뒤 `alembic current`로 head 표시 확인
- 주 프로젝트의 `.env`와 Migration용 설정을 구분
- pgAdmin에서 `day19_migration_lab`에 접속해 `information_schema.columns`로 `source_label` 열과 `is_nullable` 확인
- current의 head 표시와 함께 실제 열과 기존 지식 값 유지도 확인

##### autogenerate는 초안이고, stamp는 수리가 아니다 (PDF p.51)

- autogenerate는 현재 DB와 metadata의 차이를 비교한 초안
- rename 의도가 drop·add로 나타나는 등 검토가 필요하므로 자동 생성 후 내용을 읽음
- 기존 DB를 이력에 편입하려면 기존 DDL과 초기 Revision을 대조하고 일치가 검증된 경우에만 별도 절차 설계
- `stamp`는 DDL을 실행하지 않음
- 실패했다고 stamp부터 하지 않음
- 기본필수는 제공 Revision 적용·확인에 집중하고 기존 DB 이력 편입은 참고 설명

#### API·DB 통합 검증

##### API 성공은 실제 DB 증거와 함께 확인한다 (PDF p.52)

- 201과 생성된 id는 같은 id의 지식·분류 관계 조회로 확인
- PUT 200은 같은 id의 본문·분류 반영으로 확인
- DELETE 204와 빈 본문은 대상 0행과 다른 행 보존으로 확인
- 422·404는 기존 데이터 불변으로 확인
- 재시작 후 GET은 새 DB 연결의 값과 동일한지 확인
- 이 확인으로 운영 장애 내구성, 동시 수정 충돌 해결, 미래 벡터 인덱스 자동 삭제, 같은 Session의 DB 오류 복구, DB 서버 장애·백업 복구까지 증명되지는 않음
- 기본필수는 /docs와 pgAdmin으로 충분하고 심화만 제공 자동 테스트 보완

##### 응답의 id로 Test DB를 다시 조회한다 (PDF p.53)

- 심화용 예시이며 `get_db`를 별도 DB로 교체한 제공 fixture 사용
- client가 전용 DB를 사용하는지부터 확인
- `client.post`로 가상 지식을 만들고 `status_code == 201` 확인
- `TestSessionLocal`로 응답 id의 행을 `db.get`해 존재와 content 일치 확인
- `category_id`로 Category를 찾아 분류명이 응답의 category와 같은지 확인
- 상태코드, 응답, DB 행 세 가지를 함께 검사
- 테스트가 만든 행만 정리하고 마지막에 override 해제

#### 실습

##### 실습 04 · 작은 Migration과 통합 검증 (PDF p.54)

- 실습 시간 30분
- 기본필수는 별도 연습 DB에서 제공 Revision을 적용·확인하고 주 API는 /docs·SQL로 CRUD 반영을 수동 대조
- 응용은 변경 전후 열·기존 행을 비교해 설명하고 분류 필터·빈 목록·실패 입력 사례를 하나씩 추가
- 심화는 제공 Test DB·override 골격에 확인문을 보완하고 이력·실제 Schema·API·DB 행을 분리해 검증
- 완료 기준은 적용 대상과 실제 변경을 설명할 수 있는 것
- Migration 연습이 주 프로젝트 데이터를 바꾸면 안 됨

**핵심:** Revision 이력과 실제 열·기존 행을 연습 DB에서 따로 확인하고, API 성공은 같은 id의 DB 행으로 증명할 때 변경과 검증이 끝난 것으로 판단.

### 후속 연결 · RAG·Agent와의 경계

#### 오늘 만든 서비스와 이후 AI 기능

##### 오늘의 서비스는 이후 AI 기능의 기반이다 (PDF p.55)

- 오늘 완성한 것은 지식 원본 CRUD, API 입력·응답 약속, 관계·제약·트랜잭션, 오류와 DB 반영 검증
- 이후 연결할 것은 문서·청크·출처 관리, 검색 결과와 LLM 생성, Agent가 쓰는 읽기 도구, 권한·승인·인덱스 갱신 정책
- ORM 조회와 category 필터는 의미 검색이 아님
- API Endpoint가 자동으로 Agent 도구가 되지 않음

### 5교시 · 작은 일일프로젝트·시연

#### 프로젝트 목표와 통과 기준

##### 나만의 PostgreSQL 연동 AI 도움말 API (PDF p.56)

- 사용자와 주제 하나, 가상의 지식 세 문장을 직접 정함
- 세 지식의 역할은 A 유지, B 수정, C 삭제
- 기존 API·ORM·DB 코드를 재사용하고 새 FastAPI 프로젝트를 다시 만들지 않음
- 오전 내용 재사용 가능
- 확인 순서는 API로 변경 → 같은 ID를 SQL로 확인 → API 재조회·서버 재시작
- LLM·벡터 검색·로그인 화면·추가 테이블은 만들지 않음

##### A 유지 · B 수정 · C 삭제를 끝까지 추적한다 (PDF p.57)

- 시작 단계에서 같은 DB·기존 행·시작 수 N을 기록하고 기존 행 보존
- 생성·조회 단계는 POST 3회로 실제 A·B·C id를 기록하며 API 201·200과 DB N+3이 기준
- 수정 단계는 B를 PUT한 뒤 SQL·GET으로 같은 id의 수정 본문 확인
- 실패 단계는 `content=""` POST로 422, 정상 Body와 없는 ID로 404를 확인하고 기존 지식·분류 불변 확인
- 삭제 단계는 C DELETE 뒤 204 빈 본문, DB 0행, GET 404 확인
- 재실행 단계는 API 재시작과 DB 새 연결로 A·B·기존 행 보존과 최종 N+2 확인
- ID는 실제 응답값 사용
- PUT은 세 필드 모두 전송
- 실패 뒤 ID 번호의 연속성은 검사하지 않음

##### 응답에서 받은 id를 SQL에 연결한다 (PDF p.58)

- /docs의 POST Body는 title·content·category 세 필드의 JSON이며 Python 코드가 아님
- POST 응답의 id를 읽어 같은 DB에서 SQL 실행
- SQL은 `knowledge`와 `categories`를 `c.id = k.category_id`로 JOIN하고 `WHERE k.id = 응답 id`로 조회
- 예시의 17은 실제 응답 id로 바꿈
- 제목·본문·분류명을 대조한 뒤 다시 API GET으로 같은 id 조회
- 오후에는 API와 SQL이 같은 DB 행을 읽음

#### 진행·수준·평가

##### 마지막 50분 · 안내 6 + 수행 40 + 공유 4 (PDF p.59)

- 0~6분은 목표·완료 기준·현재 코드 확인, DB 대상과 시작 상태 기록
- 6~11분은 주제·세 문장·A/B/C 역할 결정
- 11~26분은 미완성 CRUD 보완과 생성·조회·B 수정, 실제 ID와 SQL 반영 기록
- 26~41분은 오류·C 삭제·API 재시작·DB 새 조회, 실패 보호와 최종 N+2 확인
- 41~46분은 실행 방법·검증 근거를 작은 README에 정리
- 46~50분은 대표 시연과 플랫폼에서 맡을 역할에 대한 한 문장 회고
- 시간은 운영 기준
- 미완성자는 공통 CRUD부터, 완료자는 선택 확장 하나만 보완

##### 같은 연동 서비스를 수준에 맞게 완성한다 (PDF p.60)

- 기본필수는 제공 골격의 지식 CRUD를 끝내고 A/B/C 시나리오 수행, /docs·pgAdmin 수동 확인과 기존 행 보존 설명
- 응용은 공통 결과 뒤 category 필터 한 개와 함수 분리를 보완하고 일치 결과·빈 배열·잘못된 입력 구분
- 심화는 역할별 구조와 전용 테스트 DB 검증을 보완하고 트랜잭션·오류 변환·DB 반영을 근거로 설명
- 공통 완료가 먼저
- 자동 테스트·복잡한 폴더·추가 기능은 기본필수 만점 조건이 아님

##### 기본필수만으로 공통 평가 100점 (PDF p.61)

- 설정·대상 확인 15점은 Secret 분리와 실제 연결 DB 확인
- API CRUD 25점은 목록·상세·생성·PUT·삭제와 HTTP 계약
- API/DB 모델 연결 15점은 category 문자열 ⇄ FK, 입력·응답·ORM 구분
- 오류·트랜잭션 15점은 404·422 보호와 제공 rollback 시연 설명
- Migration 이해·확인 10점은 별도 DB에서 제공 변경 적용과 실제 열 확인
- 통합 검증·설명 20점은 같은 ID DB 대조, 재실행, N+2, 실행 안내
- 자동 테스트 작성, 새 Revision 직접 설계, 성능 수치, 연속 ID는 공통 만점 조건이 아님

**핵심:** 실제 응답 id로 A 유지·B 수정·C 삭제를 SQL과 재시작 뒤까지 추적해 최종 N+2가 확인될 때 일일프로젝트 완료로 판단.

### 마무리 · 복습과 다음 단계

#### 요청 흐름 복습

##### 세 질문으로 요청 한 건의 흐름을 설명한다 (PDF p.62)

- API가 201을 반환하기 전에 성공해야 하는 작업을 묻는 질문으로 COMMIT 시점 확인
- Pydantic의 category 문자열을 DB에 그대로 넣는지 묻는 질문으로 분류명 → `category_id` 변환 확인
- ORM Model 변경이 기존 DB 열을 자동으로 바꾸는지 묻는 질문으로 Migration의 필요 확인
- 답할 때 실제 HTTP 응답과 같은 ID의 DB 행을 함께 제시

#### 완료 범위와 다음 수업

##### 오늘의 완료와 다음 단계의 경계를 남긴다 (PDF p.63)

- 완료 상태는 API 요청이 PostgreSQL의 같은 ID 행으로 연결되는 것
- 검증은 CRUD·오류·DB 반영·재실행 결과를 근거로 설명
- 한계는 로컬 학습용이라는 점이며 인증·권한·운영 장애·검색 인덱스는 별도
- 다음 수업은 11/13 LLM 기초 → 임베딩·문서 처리 → 11/20 Basic RAG
- FastAPI·DB는 AI 플랫폼의 기반이며 오늘 Agent 자체를 완성한 것은 아님

### 부록 · 전체 코드·검증·참고자료

#### 폴더 구조·설정·DB 모듈

##### 구조는 이해한 책임만큼 나눈다 (PDF p.64)

- 기본필수는 평평한 구조로 `main.py`(Schema·Route·작은 도우미), `settings.py`, `db.py`(Engine·Session·transaction), `models.py`(두 ORM 클래스), `.env`(제출 제외)
- 응용은 `schemas.py`와 조회 함수 분리
- 심화는 `app/routers`·`services`·`repositories`·`models`·`schemas`, `tests/`, `migration_demo/`
- 구조가 달라도 기능과 외부 계약은 동일
- 실행 대상은 기본필수 `main:app`, 심화 `app.main:app`이며 프로젝트 최상위에서 실행

##### settings.py · 경로가 고정된 설정 읽기 (PDF p.65)

- `pydantic_settings`의 `BaseSettings`로 db_host(기본 localhost)·db_port(기본 5432)·db_name·db_user·db_password 정의
- `env_file`은 `settings.py`와 같은 폴더의 `.env`로 고정하고 `env_file_encoding="utf-8"`
- 필수 값이 빠지면 설정 오류
- `SecretStr`은 출력 가림 용도이며 보관 파일 암호화가 아님
- 심화 구조로 옮기면 기준 경로도 수정
- 실제 비밀번호는 출력하지 않고 DB 대상만 로컬에서 확인

##### db.py · 연결과 Session의 준비 (PDF p.66)

- `URL.create`, `create_engine`, `sessionmaker`, `get_db`를 한 모듈에 둠
- 본문의 transaction 도우미도 이 모듈에 둠
- `SessionLocal`은 Factory이며 요청마다 `SessionLocal()` 호출
- Engine은 요청마다 만들지 않음
- 코드가 정상 import돼도 접속 확인은 별도로 필요

#### ORM·main 정의와 경계 사례

##### models.py · 공통 Base와 import (PDF p.67)

- `DeclarativeBase`를 상속한 `Base`가 ORM metadata의 기반
- `Mapped`는 Python 속성의 타입, `mapped_column`은 실제 열 매핑
- Model import와 SQL 실행은 같은 일이 아님
- 대상 테이블은 `public.categories`, `public.knowledge`
- 기존 DB에 연결하는 앱에서는 `create_all`을 호출하지 않음

##### Knowledge의 길이 CHECK와 스키마를 빠뜨리지 않는다 (PDF p.68)

- `__table_args__`에 `knowledge_title_length`(1~80자), `knowledge_content_length`(1~2000자) CHECK 두 개와 `{"schema": "public"}` 포함
- NOT NULL과 CHECK는 다른 제약
- CHECK가 제목·본문의 빈 문자열을 막음
- 공백만인 값은 현재 계약에서 허용
- 제목 UNIQUE는 추가하지 않음
- ORM 선언이 빠져도 기존 DB 제약은 별도로 남아 있을 수 있음

##### main.py · 연결된 예제의 선행 정의 (PDF p.69)

- FastAPI·Depends·HTTPException·Response, Pydantic, `select`, `Session`, `get_db`·`transaction`, `Knowledge`·`Category` import
- `app = FastAPI(title="Knowledge API · PostgreSQL")`와 `DbSession` 정의
- 이어서 KnowledgeWrite·Read, `to_read`, 분류·404 도우미, GET·POST·PUT·DELETE, 예외 처리기 배치
- 같은 경로는 한 번만 등록
- `/health`는 앱 응답 점검이며 DB 전체 준비 상태를 보장하지 않음

##### category 필터 · SQL 조건으로 연결한다 (PDF p.70)

- 응용용으로 기존 목록 함수를 `category: str | None = None` Query를 받는 함수로 교체
- `category`가 있으면 `stmt.where(Category.name == category)` 추가
- Query를 생략하면 전체 목록, 일치 분류면 해당 지식, 결과가 없으면 200과 `[]`
- 비교값은 바인딩되며 SQL 문자열 덧붙이기는 피함
- 문자열 분류 필터이며 벡터 검색·RAG가 아님

##### 기존 계약을 몰래 바꾸지 않는다 (PDF p.71)

- 같은 title로 다시 생성하면 허용되어 새 id의 지식이 생기며 title UNIQUE는 없음
- 새 category 문자열은 길이가 유효하면 분류를 조회·생성하고 분류와 지식을 한 번에 commit
- PUT에 content만 보내면 422이며 세 필드가 모두 필수
- 추가 입력 필드는 기본 Pydantic 정책대로 무시하며 `extra forbid`를 임의로 추가하지 않음
- 공백만인 문자열은 길이 규칙상 허용되며 trim 등 업무 정책은 별도 합의
- DELETE 뒤 부모 분류는 그대로 유지되며 빈 분류 삭제는 별도 기능

#### 오류 처리기와 Session 복구 시연

##### HTTP 변환은 알려진 오류만 정확히 처리한다 (PDF p.72)

- `@app.exception_handler(IntegrityError)`가 sqlstate와 constraint_name으로 409·500을 결정
- 흐름은 transaction에서 rollback → 예외 재전달 → 이 처리기가 HTTP로 변환
- 409의 detail은 `Data conflict`, 500의 detail은 `Database operation failed`
- 원문 SQL·파라미터·진단 문자열을 그대로 응답하지 않음
- 같은 IntegrityError라도 모두 중복·409는 아님

##### 접속 오류도 설정·운영 오류와 구분한다 (PDF p.73)

- `@app.exception_handler(DBAPIError)`로 나머지 DB 오류 처리
- `OperationalError`이면서 연결 계열 SQLSTATE `08*`이거나 `connection_invalidated`가 확인된 경우만 503 `Database unavailable`
- 인증·잘못된 SQL·예상 밖 오류는 500 `Database operation failed`로 같은 것으로 처리하지 않음
- 원인은 로컬에서 안전하게 점검
- 성공처럼 200을 반환하지 않음
- 실제 배포 전 환경별 검증 필요

##### 같은 Session에서 실패 후 rollback을 확인한다 (PDF p.74)

- `day19_api_test` 전용 강사 시연이며 기존 `learning` 분류가 있다는 전제
- 같은 이름의 Category를 add·flush해 UNIQUE 위반을 일으키고 sqlstate 23505 기대
- 예외를 잡아 `db.rollback()` 실행
- 실패가 나지 않으면 rollback 후 AssertionError
- 같은 db 객체로 `func.count(Category.id)` 후속 조회가 되는지 확인
- 관찰할 것은 실패한 제약이 UNIQUE인지, rollback 줄 실행, 같은 db로 조회 가능 여부, 기존 행 유지
- 새 요청이 성공한 것과 같은 Session이 회복된 것은 다름

#### Migration·테스트 DB

##### 연습 DB 전용 Engine을 Alembic에 전달한다 (PDF p.75)

- `migration_demo/migrations/env.py`의 online 핵심은 `.env.migration`으로 만든 `demo_url`을 `create_engine(..., poolclass=pool.NullPool)`에 전달
- 연결 직후 `SELECT current_database()`로 실제 DB명을 확인하고 점검 SELECT의 트랜잭션 종료
- 실제 DB가 `day19_migration_lab`이 아니면 `RuntimeError`로 중단
- Model을 import해 metadata 등록
- URL 객체를 직접 전달해 ini의 `%` 보간과 분리
- 기존 `.env`를 우연히 읽어 주 DB를 바꾸지 않도록 하는 안전장치

##### Migration 예제의 처음·중간·끝 상태 (PDF p.76)

- 시작은 새 `day19_migration_lab`에 사용자 테이블 없음, `alembic current`는 적용 없음
- `001_initial` 적용 뒤 categories·knowledge가 기존 DDL과 같게 생성되고 현재 001_initial
- 기준 데이터로 가상 분류와 지식 1건을 COMMIT하고 id·원래 열 값 기록
- `002_source` 적용 뒤 `source_label VARCHAR(120) NULL` 추가, 현재 002_source·head
- 선택 되돌림 시연은 새 열 삭제이며 그 열 값은 복구되지 않고 001_initial로 돌아감
- 001의 upgrade는 부모 → 자식 순서 생성, downgrade는 자식 → 부모 순서 삭제
- 삭제 시연은 연습 DB에서만 실행

##### 테스트는 요청마다 Test Session을 주입한다 (PDF p.77)

- `TestSessionLocal`은 전용 PostgreSQL DB에 연결
- `override_get_db`가 요청마다 Test Session을 yield
- `app.dependency_overrides[get_db] = override_get_db`로 앱이 쓰는 `get_db` 객체 자체를 교체
- `TestClient(app)` 안에서 API 요청과 Test DB 행 대조
- `finally`에서 `dependency_overrides.pop(get_db, None)`으로 원복
- 준비 코드에서 실제 DB 대상 검사, 테이블·기준 데이터 준비, 테스트가 만든 행만 정리
- TestClient는 실서버 재시작이 아니며 mock 통과는 PostgreSQL 통과가 아님

##### 정상·경계·실패 확인표 (PDF p.78)

- 기존·새 분류로 등록하면 201이며 새 분류 재사용과 같은 id DB 행 확인
- 제목 중복은 201이며 새 id 생성과 원래 지식 보존 확인
- 없는 ID에 정상 PUT은 404이며 새 category도 생성하지 않음
- 길이 초과·null·누락은 422이며 지식·분류 기존 내용 불변
- 알려진 DB 제약 충돌은 409이며 rollback과 내부 정보 미노출
- 예상 밖 CHECK 실패는 500이며 성공으로 위장하지 않음
- 삭제는 204, 이후 GET은 404이며 재실행 뒤 다른 행·B 수정 내용 유지

#### 실행 환경·참고자료·검수 범위

##### 실행 위치·가상환경·오전 서버를 구분한다 (PDF p.79)

- 활성화 정책이 막히면 정책 우회 대신 `.\.venv\Scripts\python.exe -m ...`로 직접 실행
- `main:app`은 루트의 `main.py`, `app.main:app`은 `app/main.py`를 가리킴
- 심화 `app/` 구조는 프로젝트 최상위에서 `python -m uvicorn app.main:app --port 8001 --reload`
- 명령은 터미널에 입력하고 `http://127.0.0.1:8001/docs`는 브라우저에서 엶
- PostgreSQL 포트(예: 5432)와 API 포트(8001)는 목적이 다름
- 기존 서버는 Ctrl+C로 종료
- Windows 직접 실행은 제작 환경에서 미검증

##### 공식 참고자료 · API·설정·ORM (PDF p.80)

- S01 FastAPI Dependencies with yield, S02 SQLAlchemy Session Basics, S03 SQLAlchemy ORM Quick Start
- S04 SQLAlchemy Engine·URL.create, S05·S06 FastAPI Settings·Psycopg Install, S07~S09 FastAPI Errors·Response·Status
- 공식 링크는 각 슬라이드 발표자 노트에 있으며 확인일은 2026-11-08

##### 공식 참고자료 · DB·Migration·검증 (PDF p.81)

- S10·S11 PostgreSQL 18 Constraints·Sequence, S12~S14 Alembic Tutorial·Autogenerate·Operations
- S15 FastAPI Testing Dependencies, S16·S17 SQLAlchemy Exceptions·Psycopg Errors, S18 FastAPI async·await, S19·S20 PostgreSQL 18 Transactions·Error Codes
- 기존 상품·주문 예제 대신 오전 Spec_v2의 지식 API·두 테이블 계약 사용

##### 검수한 것과 아직 확인하지 못한 것을 구분한다 (PDF p.82)

- PPT는 전 슬라이드 렌더링·내용·배치를 점검했으나 최종 산출물 기준 재확인 필요
- 코드·metadata는 Python 문법·PostgreSQL DDL·Revision SQL 생성까지 확인했으며 실행 DB 적용과는 다름
- 모의 API·Session 69항목(입력·응답·정렬·오류 매핑·취소 호출)은 통과했으나 모의 객체 검수
- 실제 PostgreSQL의 접속·CRUD·제약·Migration·재접속은 미검증
- Windows·pgAdmin 설치·UI·버튼 조작은 미검증
- 교실 사전 확인 순서는 실제 DB 대상·구조 → API CRUD → 실패 rollback → 별도 Migration·Test DB
