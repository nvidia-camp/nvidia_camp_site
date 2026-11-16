# Day17 강의 구조·핵심 설명

2026-11-10 · 생성형 AI·LLM 및 RAG 엔지니어링 1/18 · FastAPI 입문 · 지식 관리 API → JSON 파일 CRUD → 나만의 일일프로젝트

교시 설명은 PDF p.15 운영표의 교시별 핵심 내용 원문을 옮긴 것이고, 중간 주제는 정리를 위해 편집한 표현이며, 마지막 단계 제목은 원문 슬라이드 제목입니다. 페이지는 PDF 뷰어 기준입니다(전체 94쪽). 인쇄 쪽수는 p.2~11 도입 묶음이 2~11쪽, p.12 이후는 PDF 쪽수에서 10을 뺀 값입니다(p.12 = 2쪽, p.94 = 84쪽). 도입·마무리·참고 부록은 별도 묶음으로 유지했습니다. 실습은 기본필수·응용·심화 중 한 단계를 선택해 같은 API 계약으로 진행하는 구성입니다.

## 강의 목차

```text
도입 · AI Agent 플랫폼 안의 지식 관리 API
├─ 현업 문제와 전체 시스템
│  ├─ FastAPI 입문 · 지식 관리 API (PDF p.1)
│  ├─ AI Agent가 답하기 전에, 지식은 누가 관리할까? (PDF p.2)
│  ├─ 전체 시스템에서 오늘 만드는 부분은 어디인가? (PDF p.3)
│  └─ 지식 관리, RAG, Agent는 서로 다른 책임이다 (PDF p.4)
├─ 서비스에서 변수까지 확대
│  ├─ AI 서비스 → 지식 API → 함수 → 변수까지 확대 (PDF p.5)
│  ├─ GET /api/knowledge/2 한 건은 이렇게 처리된다 (PDF p.6)
│  └─ 코드 네 줄이 API의 어떤 지점에 해당할까? (PDF p.7)
├─ 입력 계약·데이터 수명주기·도구 호출 경계
│  ├─ Agent 시스템도 결국 “검증된 데이터” 위에서 동작한다 (PDF p.8)
│  ├─ CRUD는 Agent가 이용할 지식을 유지하는 기본 기능이다 (PDF p.9)
│  └─ FastAPI 경로를 만든 것만으로 Agent 도구가 되지는 않는다 (PDF p.10)
└─ 오늘의 프로젝트
   └─ 오늘 완성하는 작은 서비스가 Agent 플랫폼의 출발점이다 (PDF p.11)

1교시 · 플랫폼 목적·지식 CRUD 시연·첫 서버
├─ 플랫폼 속 FastAPI와 오늘의 시연
│  ├─ FastAPI는 AI 플랫폼의 요청·응답을 연결한다 (PDF p.12)
│  ├─ 안내문 하나를 등록하고 끝까지 관리한다 (PDF p.13)
│  └─ 한 번의 요청은 어디를 거치는가 (PDF p.14)
├─ 8교시 운영과 세 단계
│  ├─ 8교시 운영 · CRUD를 익히고 일일프로젝트로 완성한다 (PDF p.15)
│  └─ 세 단계 · 핵심 이해에서 실무형 구조까지 (PDF p.16)
├─ 개발환경·첫 앱·서버 실행
│  ├─ 개발환경 · 필요한 것만 설치한다 (PDF p.17)
│  ├─ main.py · 첫 JSON 응답을 만든다 (PDF p.18)
│  ├─ 서버 실행과 접속 주소를 연결한다 (PDF p.19)
│  └─ /docs · API 약속을 읽고 실제 요청을 보낸다 (PDF p.20)
└─ 실습
   └─ 실습 01 · 내 PC에서 첫 요청 성공시키기 (PDF p.21)

2교시 · JSON 파일 읽기·목록·상세 조회·URL
├─ JSON 원본과 저장 보조 함수
│  ├─ 원본 지식 · 제목·본문·분류를 저장한다 (PDF p.22)
│  └─ 파일 읽기·저장은 보조 함수로 감싼다 (PDF p.23)
├─ 목록·상세 조회
│  ├─ GET · 파일 안의 지식 항목 목록을 반환한다 (PDF p.24)
│  └─ GET · ID로 지식 항목 하나를 찾는다 (PDF p.25)
├─ URL·Query·HTTP 메시지
│  ├─ URL에서 서버 위치와 지식 ID를 읽는다 (PDF p.26)
│  ├─ Query · 목록에 조회 조건 하나를 더한다 (PDF p.27)
│  └─ 요청과 응답을 한 쌍으로 읽는다 (PDF p.28)
└─ 실습
   └─ 실습 02 · JSON 목록·상세 조회 완성하기 (PDF p.29)

3교시 · POST·Body 검증·새 ID·파일 저장
├─ 요청 Body와 Pydantic 모델
│  ├─ POST · 새 지식 항목의 값을 Body로 보낸다 (PDF p.30)
│  ├─ Pydantic · 입력과 응답의 모양을 정한다 (PDF p.31)
│  └─ 형식 검증·내용 검토·권한 확인은 다르다 (PDF p.32)
├─ ID 발급과 생성 코드
│  ├─ 새 ID는 목록 길이가 아니라 별도로 관리한다 (PDF p.33)
│  └─ POST · 추가하고 저장한 뒤 201을 반환한다 (PDF p.34)
├─ 생성 검증과 422
│  ├─ 생성 성공은 응답 한 번으로 끝내지 않는다 (PDF p.35)
│  └─ 422 · 잘못된 입력은 저장 전에 막는다 (PDF p.36)
└─ 실습
   └─ 실습 03 · 안내문 등록과 파일 저장 연결하기 (PDF p.37)

4교시 · PUT·ID 유지·전체 필드 교체
├─ PUT 요청과 교체 코드
│  ├─ PUT · 같은 지식의 본문을 갱신한다 (PDF p.38)
│  └─ PUT · 대상 위치를 찾아 값만 교체한다 (PDF p.39)
├─ ID·index 구분과 수정 검증
│  ├─ ID와 목록의 위치는 같은 숫자가 아니다 (PDF p.40)
│  └─ 수정 검증 · 바뀐 값과 그대로인 값을 나눈다 (PDF p.41)
└─ 실습
   └─ 실습 04 · 같은 지식의 본문 수정하기 (PDF p.42)

5교시 · DELETE·204·오류와 파일 보존
├─ 삭제 흐름과 204
│  ├─ DELETE · 불필요한 지식 한 건을 제거한다 (PDF p.43)
│  ├─ DELETE · 삭제 후에는 빈 204 응답을 보낸다 (PDF p.44)
│  └─ 204는 “삭제 완료 JSON”을 담지 않는다 (PDF p.45)
├─ 상태코드와 실패 시 데이터 보존
│  ├─ 지금 사용한 상태코드를 동작에 연결한다 (PDF p.46)
│  └─ 실패한 요청은 기존 파일을 보존해야 한다 (PDF p.47)
└─ 실습
   └─ 실습 05 · 삭제와 실패 후 데이터 보존 확인하기 (PDF p.48)

6교시 · 파일 역할 이해·응용 분리·심화 구조화·Template
├─ 프로젝트 구조와 파일 책임
│  ├─ 심화 · 지식 관리 API의 최소 프로젝트 구조 (PDF p.49)
│  └─ 요청 경로와 파일 책임을 연결한다 (PDF p.50)
├─ main·Router·Repository 연결
│  ├─ main.py · 앱 생성과 Router 등록만 남긴다 (PDF p.51)
│  ├─ Router · HTTP 약속과 저장 호출을 연결한다 (PDF p.52)
│  └─ Repository · 생성 로직을 그대로 옮긴다 (PDF p.53)
├─ 확장 지점과 화면 표현
│  ├─ RAG 처리 코드는 저장 코드와 분리한다 (PDF p.54)
│  └─ Template와 API는 같은 데이터를 다르게 보여준다 (PDF p.55)
└─ 실습
   └─ 실습 06 · 수준에 맞게 파일 역할 이해·분리하기 (PDF p.56)

7교시 · 함께 통합·검증·플랫폼 연결·프로젝트 준비
├─ 플랫폼 API와 최종 계약
│  ├─ 지식 관리·RAG 질의·Agent 작업은 다르다 (PDF p.57)
│  ├─ 최종 API 약속 · 다섯 요청을 통일한다 (PDF p.58)
│  └─ 지식 항목 하나를 끝까지 추적한다 (PDF p.59)
├─ 통합 실습과 검증 기록
│  ├─ 실습 07 · 함께 통합하고 일일프로젝트를 준비한다 (PDF p.60)
│  └─ 검증 기록 · 일일프로젝트에서도 같은 틀을 쓴다 (PDF p.61)
└─ 후속 수업 연결
   ├─ 파일에 저장되는데도 왜 DB를 배우는가 (PDF p.62)
   ├─ 11월 10일 → 11일 → 12일의 연결 (PDF p.63)
   ├─ 그다음 LLM·RAG에서도 같은 API 흐름을 쓴다 (PDF p.64)
   └─ Agent와 API가 연결되는 두 가지 방향 (PDF p.65)

8교시 · 나만의 지식 API·일일프로젝트·공유
├─ 과제 정의와 시작 데이터
│  ├─ 배운 흐름을 나만의 작은 서비스로 연결한다 (PDF p.66)
│  ├─ 나만의 AI 도움말 지식 관리 API (PDF p.67)
│  └─ 지식 3개를 준비하고 실제 ID를 기록한다 (PDF p.68)
├─ 통과 기준과 시간 배분
│  ├─ 하나의 시나리오로 오늘 배운 것을 연결한다 (PDF p.69)
│  ├─ 마지막 50분 · 안내 6분 + 수행 40분 + 공유 4분 (PDF p.70)
│  └─ 일일프로젝트 · 같은 목표를 수준에 맞게 완성한다 (PDF p.71)
├─ 재시작·최종 점검·오류 해결
│  ├─ 재시작 검증 · 파일은 그대로 둔다 (PDF p.72)
│  ├─ 최종 점검 · 정상과 실패를 함께 확인한다 (PDF p.73)
│  └─ 문제가 생기면 가장 가까운 원인부터 본다 (PDF p.74)
└─ 평가·제출·회고
   ├─ 일일프로젝트 평가 · 기본필수만으로 100점 (PDF p.75)
   ├─ 작게 만들고, 실행 근거와 설명을 남긴다 (PDF p.76)
   └─ 마무리 회고 · 내 서비스의 역할을 설명한다 (PDF p.77)

마무리 · 오늘의 완료와 다음 단계
└─ 완료 기준
   └─ 오늘의 완료 · 작은 지식 서비스 한 개를 남긴다 (PDF p.78)

참고 부록 · 구현 보조·선택 확장·참고자료
├─ 부록 지도
│  └─ 참고 부록 · 구현 중 필요할 때만 사용한다 (PDF p.79)
├─ 파일 저장 보조 코드
│  ├─ storage.py · 기준 경로와 읽기 함수 (PDF p.80)
│  ├─ storage.py · 임시 파일을 쓴 뒤 교체한다 (PDF p.81)
│  └─ 참고 · Lock이 보호하는 범위와 한계 (PDF p.82)
├─ HTTP·함수 용어 사전
│  ├─ HTTP·입력 위치 · 헷갈리는 용어 사전 (PDF p.83)
│  ├─ 입력·응답 함수 · 지식 API에서 쓰는 규칙 (PDF p.84)
│  └─ 앱·Router 함수 · 등록과 실행을 구분한다 (PDF p.85)
├─ 선택 확장
│  ├─ 참고 개념 · PUT과 PATCH의 차이 (PDF p.86)
│  ├─ 응용 참고 · 제목·본문의 문자열을 찾는다 (PDF p.87)
│  ├─ 비교 시연 · 같은 지식을 HTML로 보여준다 (PDF p.88)
│  └─ 심화 · 테스트가 실제 지식을 바꾸지 않게 한다 (PDF p.89)
└─ 검수·실행 보조·공식 자료
   ├─ 검수 범위 · 일일프로젝트 추가본 (PDF p.90)
   ├─ Windows · 활성화가 막혀도 Python을 직접 실행한다 (PDF p.91)
   ├─ 공식 참고자료 · FastAPI·RAG·Agent 연결 (PDF p.92)
   ├─ 공식 참고자료 · 파일·실행·검증 (PDF p.93)
   └─ 개편 범위 · 마지막 일일프로젝트까지 연결한다 (PDF p.94)
```

## 핵심 설명

### 도입 · AI Agent 플랫폼 안의 지식 관리 API

#### 현업 문제와 전체 시스템

##### FastAPI 입문 · 지식 관리 API (PDF p.1)

- 생성형 AI·LLM 및 RAG 엔지니어링 정규교과 1/18 표지
- RAG·AI Agent 플랫폼의 기반이 되는 지식 관리 API를 만드는 Day17
- 지식 CRUD → 저장·검증 → 나만의 일일프로젝트 순서의 하루 흐름

##### AI Agent가 답하기 전에, 지식은 누가 관리할까? (PDF p.2)

- 신규 직원의 업무 질문에 AI Agent가 답하려면 근거가 되는 원본 지식이 먼저 필요
- AI Agent는 질문 해석 → 지식 조회 요청 → 근거를 사용한 응답 담당이며 이후 수업 범위
- 오늘의 지식 관리 API는 “가상환경 사용 안내” 같은 지식을 등록·수정·조회하고 JSON 파일에 유지
- 원본 지식이 오래되면 검색·답변 품질도 함께 저하

##### 전체 시스템에서 오늘 만드는 부분은 어디인가? (PDF p.3)

- 사용자·사내 업무 화면 아래 FastAPI가 요청·응답을 받는 서비스 입구
- FastAPI 뒤에 지식 관리 API(CRUD·원본 관리), RAG 검색·생성, Agent 처리가 나란히 연결되는 구조
- 저장소는 오늘 JSON 파일, 이후 Vector DB·모델과 Tool Registry로 확장
- 오늘 구현 범위는 지식 CRUD와 파일 저장이며 AI 모델·RAG·Agent 호출은 산출물에서 제외

##### 지식 관리, RAG, Agent는 서로 다른 책임이다 (PDF p.4)

- Knowledge API는 “안내문을 어떻게 유지하나요?”에 답하는 등록·조회·수정·삭제와 저장 상태 검증
- RAG는 “관련 근거가 어디에 있나요?”에 답하는 문서 검색 → 문맥 제공 → 생성·출처 확인
- AI Agent는 “어떤 도구가 필요한가?”에 답하는 도구 선택·호출 제안과 실행 결과 점검
- 같은 서비스로 연결 가능하지만 원본 저장·근거 검색·도구 실행은 별도 모듈

#### 서비스에서 변수까지 확대

##### AI 서비스 → 지식 API → 함수 → 변수까지 확대 (PDF p.5)

- AI 업무 서비스 → 지식 관리 FastAPI → `GET /api/knowledge/{knowledge_id}` → `get_knowledge(knowledge_id: int)` → `entry["id"] == knowledge_id`의 5단계 확대
- Method + Path가 처리 함수를 선택하고 함수는 받은 값으로 대상 지식 탐색
- “왜 이 함수가 필요한가”를 먼저 알면 매개변수와 조건문이 전체 서비스에 연결

##### GET /api/knowledge/2 한 건은 이렇게 처리된다 (PDF p.6)

- /docs 클라이언트 → Uvicorn 요청 수신 → FastAPI Route의 GET + Path 대조 → 처리 함수 → `storage.py`의 JSON 읽기·목록 탐색 → 200 + 지식 항목의 6단계
- Path의 `2`는 정수 변환에 성공하고 해당 항목이 존재하면 200
- `foo`처럼 정수로 바꿀 수 없는 값은 422
- 존재하지 않는 `9999`는 404
- URL 문자열을 직접 해석하지 않고 Route·타입 검증·함수·저장을 순서대로 연결하는 구조

##### 코드 네 줄이 API의 어떤 지점에 해당할까? (PDF p.7)

- Route `@app.get(...)`은 어떤 요청을 받는지 등록
- Function `get_knowledge(...)`는 요청을 받았을 때 수행할 처리
- Parameter `knowledge_id: int`는 받는 값과 자료형
- Field `entry["id"]`는 비교 대상 자료
- Agent가 나중에 조회 도구를 쓰더라도 실제 저장 데이터를 찾는 일은 이 작은 함수가 담당

#### 입력 계약·데이터 수명주기·도구 호출 경계

##### Agent 시스템도 결국 “검증된 데이터” 위에서 동작한다 (PDF p.8)

- Pydantic이 입력 구조 검증 담당: title 1~80자, content 1~2,000자, category 1~30자
- 필드 누락·빈 문자열은 기본 422
- 안내 내용의 정확성·최신성·수정 권한은 별도 업무 품질 검토 대상
- 형식 통과는 사실성·권한을 보장하지 않음
- 잘못된 입력과 부정확한 원문을 구분해야 Agent도 신뢰 가능한 자료를 사용

##### CRUD는 Agent가 이용할 지식을 유지하는 기본 기능이다 (PDF p.9)

- POST는 새 지식 등록, 새 ID 발급, 201과 저장
- GET은 ID로 원본 반환, 없으면 404
- PUT은 같은 ID를 유지하며 본문과 파일 갱신
- DELETE는 지식 한 건 제거 후 204와 빈 본문
- Agent·RAG의 파생 검색 데이터는 원본과 별개이며 원본 PUT·DELETE가 검색 인덱스를 자동 갱신하지 않음

##### FastAPI 경로를 만든 것만으로 Agent 도구가 되지는 않는다 (PDF p.10)

- Agent 판단 → Tool 호출 제안 → 앱 검증·실행 → API·저장소 → 결과 반환의 흐름
- 모델의 제안이 무조건 실행되지 않으며 실제 호출·권한 확인·기록은 애플리케이션 책임
- 오늘 범위는 API 구현만이며 Tool Schema·Agent Loop·LLM 호출은 후속 단계의 별도 작업

#### 오늘의 프로젝트

##### 오늘 완성하는 작은 서비스가 Agent 플랫폼의 출발점이다 (PDF p.11)

- 주제 정하기 → 지식 3건 A·B·C 등록 → 읽기·수정·삭제 → 실패·재시작 확인의 4단계 일일프로젝트
- 오늘은 지식 CRUD + JSON 파일 + 검증, 이후 PostgreSQL → 검색·RAG → AI Agent 도구 연결
- 도입 8~10분 → 기존 FastAPI·CRUD 설명 → 나만의 일일프로젝트로 이어지는 수업 연결

**핵심:** 오늘 만드는 지식 관리 API는 RAG·Agent가 사용할 원본 지식을 검증된 형식으로 유지하는 별도 모듈이며 검색·생성·도구 실행은 포함하지 않음

### 1교시 · 플랫폼 목적·지식 CRUD 시연·첫 서버

#### 플랫폼 속 FastAPI와 오늘의 시연

##### FastAPI는 AI 플랫폼의 요청·응답을 연결한다 (PDF p.12)

- 목표는 RAG·AI Agent를 사용자가 이용하는 서비스로 만드는 것이며 첫 기능이 지식 관리
- 클라이언트는 오늘 /docs, 이후 사용자 화면
- FastAPI는 요청 검증과 함수 연결·응답 담당
- 오늘의 지식 CRUD는 JSON 파일에 저장, 이후 PostgreSQL로 교체
- RAG·Agent의 검색·생성·도구 실행은 별도 처리 코드로 연결
- FastAPI는 AI 모델도 Agent도 아니며 오늘은 PDF·임베딩·LLM 호출 없이 완성

##### 안내문 하나를 등록하고 끝까지 관리한다 (PDF p.13)

- C·R·U·D를 POST·GET·PUT·DELETE에 대응
- 시연 흐름은 실습 환경 안내 등록 → 본문 수정 → 재시작 확인 → 삭제 → 재조회
- 오늘 관리 대상은 AI가 사용할 지식의 원본 데이터이며 검색·답변 생성은 이후 연결

##### 한 번의 요청은 어디를 거치는가 (PDF p.14)

- 클라이언트 요청 → FastAPI의 Route·입력 검증 → 처리 함수의 지식 찾기·변경 → JSON 파일 읽기·저장
- /docs는 임시 클라이언트이며 나중에는 사용자 화면·다른 서버가 같은 API 호출
- Uvicorn은 요청 수신, FastAPI는 Route·검증·함수 연결
- View·Handler는 요청 처리 함수를 가리키는 말

#### 8교시 운영과 세 단계

##### 8교시 운영 · CRUD를 익히고 일일프로젝트로 완성한다 (PDF p.15)

- 1~5교시는 첫 서버, 목록·상세 조회, POST, PUT, DELETE를 한 교시씩 진행
- 6교시는 파일 역할 이해·응용 분리·심화 구조화·Template
- 7교시는 통합·검증과 플랫폼 연결, 8교시는 나만의 지식 API 일일프로젝트와 공유
- 교시별 설명·시연 10~20분, 실습·확인 30~40분
- 50분 × 8교시 = 400분, 설명 110분·실습 290분, 휴식·점심은 별도

##### 세 단계 · 핵심 이해에서 실무형 구조까지 (PDF p.16)

- 기본필수는 단순 구조와 제공 골격으로 CRUD 핵심 동작을 익히고 짧은 TODO 완성 후 /docs로 요청·응답·저장 확인
- 기본필수에는 폴더 재설계·자동 테스트 구현을 요구하지 않음
- 응용은 직접 작성 범위를 조금 늘리고 조회 조건 하나 추가, 반복 코드를 함수·간단한 파일로 분리
- 심화는 Router·Schema·Repository로 역할을 나누고 제공 테스트 틀로 정상·오류·저장 결과 검증
- 심화도 유지보수·재현성은 고려하되 과도한 계층은 만들지 않음
- 공통 목표는 지식 CRUD + 파일 저장 + 재시작 확인, 마지막에 일일프로젝트
- 자기 수준의 한 단계로만 진행하며 기본필수만으로 공통 평가 100점 가능

#### 개발환경·첫 앱·서버 실행

##### 개발환경 · 필요한 것만 설치한다 (PDF p.17)

- `python -m venv .venv`로 가상환경 생성 후 PowerShell에서 `Activate.ps1`로 활성화
- 기본 설치는 `fastapi`와 `uvicorn`
- `sys.executable`과 `pip show`로 실제 사용 중인 Python과 패키지 확인
- `fastapi_knowledge` 폴더를 VS Code로 열고 `.venv`의 Python 선택
- 기존 정상 환경은 불필요하게 재설치하지 않음
- Template 시연은 `jinja2` 추가, 자동 테스트는 심화 범위

##### main.py · 첫 JSON 응답을 만든다 (PDF p.18)

- `FastAPI()`는 앱 객체 생성
- `@app.get()`은 GET 경로 등록
- `health()`는 요청 처리 함수
- `return`은 응답할 Python 값이며 dict는 JSON으로 변환
- `GET /health` → 200과 `{"status":"ok"}`

##### 서버 실행과 접속 주소를 연결한다 (PDF p.19)

- `main.py`가 있는 폴더에서 `.venv` 활성화 후 `python -m uvicorn main:app --reload` 실행
- `main`은 `main.py` 모듈, `app`은 앱 변수 이름
- `127.0.0.1`은 내 컴퓨터, `8000`은 서버 포트
- `--reload`는 개발용 옵션
- 서버는 한 개만 실행하고 종료는 실행 중인 터미널에서 Ctrl+C
- 브라우저 주소창은 GET 확인용, 다른 Method는 /docs에서 요청

##### /docs · API 약속을 읽고 실제 요청을 보낸다 (PDF p.20)

- 경로·입력 약속 읽기 → Try it out → Execute → Server response 확인의 4단계
- 다른 프로그램도 같은 입력·응답 약속을 사용
- Responses 영역은 문서상의 예상 결과
- 실제 실행 결과는 Server response의 Code·Body로 확인

#### 실습

##### 실습 01 · 내 PC에서 첫 요청 성공시키기 (PDF p.21)

- 35분, 세 단계 중 하나 선택
- 기본필수는 `health`의 반환값을 완성하고 `/health`·`/docs`를 열어 200과 JSON 응답 확인
- 응용은 앱 제목과 `/hello` 경로를 직접 작성하고 두 경로의 URL·JSON 응답 비교
- 심화는 실행 명령·작업 폴더·패키지 정보를 README에 기록하고 제공 테스트 틀로 `/health`의 상태·본문 검증
- 완료 기준은 `/health`의 실제 200과 JSON 응답 확인

**핵심:** 요청은 클라이언트 → Uvicorn → FastAPI Route → 처리 함수로 이어지며 실제 동작은 /docs의 Server response Code·Body로 판단

### 2교시 · JSON 파일 읽기·목록·상세 조회·URL

#### JSON 원본과 저장 보조 함수

##### 원본 지식 · 제목·본문·분류를 저장한다 (PDF p.22)

- `data/knowledge.json`은 `next_id`와 `entries`로 구성
- 지식 1건은 `id`·`title`·`category`·`content`
- `entries`는 지식 항목 목록이며 초기 지식은 ID 1·2·3의 3건
- ID는 서버가 발급하는 숫자이며 다음 생성 ID는 4
- `next_id`는 외부 응답에서 제외
- JSON 문자열은 큰따옴표 사용

##### 파일 읽기·저장은 보조 함수로 감싼다 (PDF p.23)

- `main.py`에서 `from storage import LOCK, read_data, write_data`로 사용
- `read_data()`는 파일 → dict, `write_data(data)`는 dict → 파일
- `data`는 파일 전체의 dict, `entries`는 그 안의 지식 목록
- `LOCK`은 읽기·변경·저장 구간 보호
- 지금은 제공 코드를 사용하고 기본필수는 CRUD에 집중
- 실제 구현은 부록 A02~A04에서 확인
- `main.py` + `storage.py` + `data/knowledge.json` 구성이며 데이터 파일은 시작 전에 준비

#### 목록·상세 조회

##### GET · 파일 안의 지식 항목 목록을 반환한다 (PDF p.24)

- 요청마다 `with LOCK:` 안에서 파일을 읽고 `data["entries"]` 반환
- list 반환은 JSON 배열 응답
- GET은 파일을 변경하지 않음
- `GET /api/knowledge` → 200, 초기 상태 지식 항목 3개
- 빈 목록도 200 + `[]`

##### GET · ID로 지식 항목 하나를 찾는다 (PDF p.25)

- `knowledge_id: int`로 Path 값 수신
- `entries`를 순회하며 `id`가 같은 항목 반환
- 끝까지 없으면 `HTTPException(404, "Knowledge not found")` 발생
- 오류는 `return`이 아니라 `raise`
- `/api/knowledge/2` → 200, `/9999` → 404, `/foo` → 422

#### URL·Query·HTTP 메시지

##### URL에서 서버 위치와 지식 ID를 읽는다 (PDF p.26)

- `http://127.0.0.1:8000/api/knowledge/2`를 통신 방식·서버 주소와 포트·자원 경로·`knowledge_id` 값으로 분해
- Path는 `/api/knowledge/2`의 `2`처럼 대상 지정
- Query는 `/api/knowledge?category=api`처럼 목록의 조건

##### Query · 목록에 조회 조건 하나를 더한다 (PDF p.27)

- 응용 선택 범위이며 기존 목록 Route를 교체
- `category: str | None = None`으로 선택 Query 선언
- 생략하면 전체 목록, `category=api`이면 api 분류만 반환
- 초기 지식 중 `category=api`는 2건
- 단순 값 비교 필터이며 의미 기반 검색이 아님
- 결과 0건도 200 + `[]`

##### 요청과 응답을 한 쌍으로 읽는다 (PDF p.28)

- 요청은 Method `GET`, Path `/api/knowledge/2`, Header(예: `Host`), 이번 조회에서는 Body 없음
- 주소창은 보통 GET 요청 전송
- 응답은 Status 200, `Content-Type: application/json`, Body는 ID 2의 지식 항목
- Status·Header·Body를 함께 확인

#### 실습

##### 실습 02 · JSON 목록·상세 조회 완성하기 (PDF p.29)

- 35분, 세 단계 중 하나 선택
- 기본필수는 목록 반환과 ID 비교의 짧은 TODO 완성 후 목록·ID 2·없는 ID를 /docs에서 확인
- 응용은 대상 탐색을 더 직접 작성하고 category Query 하나로 목록 필터링
- 심화는 목록·상세 조회를 함수로 분리하고 정상·404·422와 GET 전후 파일 불변을 테스트
- 완료 기준은 목록·상세가 파일과 일치하고 GET이 데이터를 바꾸지 않는 것
- 기본필수는 수동 확인으로 충분

**핵심:** 조회는 파일을 바꾸지 않고, 없는 ID는 404·자료형이 맞지 않는 Path는 422·결과 없는 목록은 200 + `[]`로 구분

### 3교시 · POST·Body 검증·새 ID·파일 저장

#### 요청 Body와 Pydantic 모델

##### POST · 새 지식 항목의 값을 Body로 보낸다 (PDF p.30)

- `POST /api/knowledge`, `Content-Type: application/json`, Body에 `title`·`content`·`category`
- Path는 어떤 자원인지, Method는 무엇을 할지, Body는 새로 저장할 내용
- ID는 서버가 발급하며 Body에 넣지 않음
- 세 필드는 모두 필수
- /docs에서 POST → Try it out → Body 입력 → Execute, 정상 결과 201

##### Pydantic · 입력과 응답의 모양을 정한다 (PDF p.31)

- `KnowledgeWrite`는 POST·PUT 공통 입력 모델
- `Field(min_length=..., max_length=...)`로 title 1~80자, content 1~2,000자, category 1~30자 제한
- 기본값이 없으므로 세 필드 모두 필수
- `Knowledge`는 `KnowledgeWrite`에 `id`를 더한 응답 모델
- `model_dump()`는 모델 → dict 변환
- Pydantic 모델은 DB 테이블이 아니며 저장은 별도 코드의 책임

##### 형식 검증·내용 검토·권한 확인은 다르다 (PDF p.32)

- 형식은 필드 존재와 길이이며 Pydantic 검증 실패 시 기본 422, 저장하지 않음
- 내용은 지식 품질 문제이며 JSON 모양이 맞아도 안내 내용이 틀릴 수 있음
- 근거·최신성·답변의 사실성은 별도 검토 대상
- 권한은 운영 서비스 문제이며 형식이 맞아도 누구나 수정·삭제해도 되는 것은 아님
- 인증·권한은 별도 설계이며 오늘은 로컬 학습용
- `response_model`은 반환 구조를 검증·필터링할 뿐 사실성·접근 권한을 보증하지 않음

#### ID 발급과 생성 코드

##### 새 ID는 목록 길이가 아니라 별도로 관리한다 (PDF p.33)

- 초기 1·2·3에서 `len(entries) + 1`과 `next_id` 모두 4
- ID 2 삭제 후 `len(entries) + 1`은 3이 되어 기존 ID 3과 충돌
- `next_id`는 삭제해도 줄이지 않음
- 다음 생성 시 4를 발급하고 `next_id`에 5 저장
- `entries`와 `next_id`를 같은 파일에 함께 저장해 재시작 후에도 다음 번호 유지

##### POST · 추가하고 저장한 뒤 201을 반환한다 (PDF p.34)

- `@app.post(..., status_code=201, response_model=Knowledge)`로 생성 Route 등록
- 순서는 파일 읽기 → `payload.model_dump()`에 새 ID 부여 → 목록에 추가 → `next_id` 증가 → `write_data` 저장 → 생성 항목 응답
- 읽기부터 저장까지 하나의 `with LOCK:` 안에서 수행
- 초기 상태에서 한 번 생성하면 id = 4, 목록 4개, `next_id` = 5

#### 생성 검증과 422

##### 생성 성공은 응답 한 번으로 끝내지 않는다 (PDF p.35)

- POST 응답 201·id=4 → `GET /api/knowledge/4` 상세 재조회 → 목록 3개 → 4개 확인 → 파일의 entry 4와 `next_id` 5 확인
- 초기 3건에서 한 번 등록한 예시이며 실제 응답에서 받은 ID 사용
- Execute를 다시 누르면 새 항목이 하나 더 생성되므로 받은 ID를 기록

##### 422 · 잘못된 입력은 저장 전에 막는다 (PDF p.36)

- 정상 세 필드는 201과 새 ID
- title 누락은 422이며 detail 안의 `body`·`title` 위치 확인
- content가 빈 문자열 `""`이면 최소 길이 1자 위반으로 422
- category 누락은 POST·PUT 공통 필수 필드 위반으로 422
- JSON 문법 오류도 기본 처리로 422이며 쉼표·큰따옴표·괄호 확인
- 검증 실패 후 파일·항목 수·`next_id`가 그대로인지 확인
- 422 검증은 내용의 사실성 검증과 다름

#### 실습

##### 실습 03 · 안내문 등록과 파일 저장 연결하기 (PDF p.37)

- 30분, 세 단계 중 하나 선택
- 기본필수는 추가·다음 번호·저장 호출의 짧은 TODO 완성 후 POST 성공 ID를 GET으로 재조회
- 응용은 지식 항목 dict 생성 부분을 더 직접 작성하고 정상 입력과 필수 값 누락 비교
- 심화는 입력·응답 모델과 생성 함수를 구분하고 제공 테스트 틀로 201·422와 파일 변경 여부 확인
- 완료 기준은 응답·재조회·파일의 일치
- 422 요청은 항목 수와 `next_id`를 바꾸지 않음

**핵심:** 생성은 검증 통과 → `next_id`로 ID 발급 → 저장 → 201 순서이며 성공 여부는 응답이 아니라 재조회와 파일 내용으로 판단

### 4교시 · PUT·ID 유지·전체 필드 교체

#### PUT 요청과 교체 코드

##### PUT · 같은 지식의 본문을 갱신한다 (PDF p.38)

- `PUT /api/knowledge/4`에 세 필드를 담아 본문을 새 안내로 변경하는 예시
- 등록 응답에서 받은 ID 사용
- title·content·category를 모두 보내 내용 전체 교체
- 없는 ID는 새로 만들지 않고 404
- ID·항목 수·`next_id` 유지
- 정상 결과는 200 + 수정된 지식

##### PUT · 대상 위치를 찾아 값만 교체한다 (PDF p.39)

- `enumerate(data["entries"])`로 위치와 값을 함께 받음
- ID가 맞는 위치의 내용을 `payload.model_dump()`에 `id`를 붙인 dict로 교체한 뒤 저장
- `append()`를 쓰면 수정이 아니라 추가
- 찾지 못하면 저장하지 않고 404
- 정상 수정 200, 없는 ID 404, 필수 필드 누락 422

#### ID·index 구분과 수정 검증

##### ID와 목록의 위치는 같은 숫자가 아니다 (PDF p.40)

- index는 현재 배열의 위치, ID는 지식 항목 식별자
- index 0의 지식 ID는 1, ID 2를 지운 뒤 index 1에는 ID 3
- 세 번째 위치 index 2에 ID 4 항목이 놓일 수 있음
- `data["entries"][knowledge_id]`로 찾지 않음

##### 수정 검증 · 바뀐 값과 그대로인 값을 나눈다 (PDF p.41)

- 존재하는 ID + 세 필드는 200이며 해당 항목만 교체
- 같은 PUT을 다시 보내도 200이며 항목 수·ID·`next_id` 유지
- category를 빼고 보내면 422이며 기존 항목 그대로
- 없는 ID + 정상 Body는 404이며 새 항목이 생기지 않음
- 매번 GET으로 수정 결과 재확인
- 응답만 바뀌고 파일이 그대로면 미완성

#### 실습

##### 실습 04 · 같은 지식의 본문 수정하기 (PDF p.42)

- 35분, 세 단계 중 하나 선택
- 기본필수는 ID 비교·목록 교체·저장의 짧은 TODO 완성 후 같은 ID 조회와 항목 수 대조
- 응용은 수정할 dict와 대상 탐색을 더 직접 작성하고 두 번 수정해도 ID·항목 수 유지 확인
- 심화는 수정 함수를 분리하고 정상·404·422 테스트, 실패 요청 후 파일 불변 자동 확인
- 완료 기준은 대상 ID 유지와 값 변경
- 항목 수와 `next_id`는 증가하지 않음

**핵심:** PUT은 ID로 찾은 위치의 내용을 세 필드 전체로 교체하는 동작이며 항목 수·ID·`next_id`가 그대로여야 수정

### 5교시 · DELETE·204·오류와 파일 보존

#### 삭제 흐름과 204

##### DELETE · 불필요한 지식 한 건을 제거한다 (PDF p.43)

- Path Parameter로 ID 받기 → 지식 ID 비교로 대상 찾기 → 해당 index 제거 → 파일 저장 후 204
- 삭제 대상은 `knowledge.json` 전체가 아니라 ID가 일치하는 항목 하나
- 파일 자체와 나머지 항목, `next_id`는 유지

##### DELETE · 삭제 후에는 빈 204 응답을 보낸다 (PDF p.44)

- `@app.delete(..., status_code=204)`로 삭제 Route 등록
- `pop(i)`로 해당 위치 한 건 제거
- 저장 성공 후 `Response(status_code=204)`로 본문 없는 응답
- 204에 JSON을 함께 보내지 않음
- 대상이 없으면 404
- 삭제 성공 204 → 같은 ID GET 404 → 다시 DELETE도 404

##### 204는 “삭제 완료 JSON”을 담지 않는다 (PDF p.45)

- `DELETE /api/knowledge/4` 성공은 Status 204, Response body 없음
- `{"message":"deleted"}`를 204와 함께 보내지 않음
- 삭제 후 `GET /api/knowledge/4`는 404, 목록에는 ID 4 없음
- `knowledge.json`에서도 ID 4 제거 확인
- 빈 204 응답에 `response.json()`을 호출하지 않음

#### 상태코드와 실패 시 데이터 보존

##### 지금 사용한 상태코드를 동작에 연결한다 (PDF p.46)

- 200은 목록·상세 조회와 정상 수정이며 응답 데이터와 저장값 확인
- 201은 새 항목 생성이며 새 ID와 실제 파일 반영 확인
- 204는 삭제 성공이며 본문 없음과 재조회 404 확인
- 404는 등록되지 않은 경로 또는 없는 항목이며 Path와 대상 ID 구분
- 405는 경로가 지원하지 않는 Method
- 422는 요청의 자료형·필수 값·규칙 오류이며 detail의 위치와 이유 확인
- 500은 서버 처리·파일 접근 오류이며 서버 로그와 저장 파일 확인
- 404·422를 성공 200으로 숨기지 않음
- 연결 자체가 안 되는 상황은 HTTP 오류와 별도로 진단

##### 실패한 요청은 기존 파일을 보존해야 한다 (PDF p.47)

- 422는 함수 본문 실행 전에 입력 검증이 실패하므로 저장 코드가 실행되지 않음
- 404는 대상이 없으면 저장하지 않고 오류를 알리며 새 항목도 만들지 않음
- 파일 읽기 실패를 빈 목록으로 간주해 덮어쓰지 않고 원인 먼저 확인
- 쓰기 실패 시 성공 응답을 만들지 않음
- 임시 파일과 교체 방식은 부록에서 확인

#### 실습

##### 실습 05 · 삭제와 실패 후 데이터 보존 확인하기 (PDF p.48)

- 40분, 세 단계 중 하나 선택
- 기본필수는 대상 삭제와 저장 호출의 짧은 TODO 완성 후 204 본문 없음과 삭제 후 GET 404 확인
- 응용은 삭제 대상 탐색을 더 직접 작성하고 다른 항목과 `next_id` 유지 확인
- 심화는 CRUD 흐름과 204 빈 본문을 테스트하고 404·422 요청 후 파일 불변 확인
- 완료 기준은 세 단계 모두 C·R·U·D 수행
- 기본필수는 /docs 확인으로 충분

**핵심:** 삭제는 대상 한 건만 제거하고 본문 없는 204로 알리며, 404·422 같은 실패 요청은 파일·항목 수·`next_id`를 바꾸지 않아야 정상

### 6교시 · 파일 역할 이해·응용 분리·심화 구조화·Template

#### 프로젝트 구조와 파일 책임

##### 심화 · 지식 관리 API의 최소 프로젝트 구조 (PDF p.49)

- `app/` 아래 `main.py`·`schemas.py`·`routers/knowledge.py`·`repositories/json_knowledge.py`, 루트에 `data/`·`README.md`·`requirements.txt`
- `main`은 앱과 Router 조립
- `schemas`는 입력·응답 규칙
- `routers`는 HTTP 요청·응답
- `repositories`는 지식 읽기·저장
- 기본필수는 단순 구조 유지, 응용은 한 부분만 분리, 심화는 제공 골격으로 역할별 구조 연결

##### 요청 경로와 파일 책임을 연결한다 (PDF p.50)

- `main.py` 앱 조립 → Router의 Method·상태코드 → Repository의 조회·변경·저장 → `knowledge.json` 실제 데이터
- 데이터가 같아도 HTTP 규칙과 저장 방식은 바뀌는 이유가 다름
- Schema는 데이터의 모양, Router는 HTTP, Repository는 저장 담당
- RAG 처리는 이후에 별도로 분리

#### main·Router·Repository 연결

##### main.py · 앱 생성과 Router 등록만 남긴다 (PDF p.51)

- `app/main.py`는 `FastAPI` 앱 생성, `app.include_router(router)`, `/health`만 담당
- 프로젝트 최상위에서 `python -m uvicorn app.main:app --reload` 실행
- `app.main`은 `app/main.py`, `:app`은 그 파일의 앱 변수
- `/health`는 단순 응답 점검이며 데이터 준비 상태 전체를 의미하지 않음

##### Router · HTTP 약속과 저장 호출을 연결한다 (PDF p.52)

- `APIRouter(prefix="/api/knowledge", tags=["knowledge"])`로 관련 Route 묶음
- prefix와 Route Path가 합쳐져 `/api/knowledge` + `""` → `/api/knowledge`
- `tags`는 /docs의 묶음 이름이며 인증·권한 설정이 아님
- Router 함수는 상태코드·`response_model` 등 HTTP 계약을 유지하고 저장 처리는 `repo.create(...)` 호출로 위임
- 같은 Route를 중복 등록하지 않음

##### Repository · 생성 로직을 그대로 옮긴다 (PDF p.53)

- `json_knowledge.py`에 `LOCK`·`read_data`·`write_data`와 `create(fields)` 정의
- 바뀐 것은 코드가 놓인 파일, 유지한 것은 ID 발급·추가·저장 순서
- 데이터 파일 경로 기준은 새 위치에 맞춰 `Path(__file__).resolve().parents[2]`로 프로젝트 루트 계산
- Repository는 저장 방식을 교체하는 지점

#### 확장 지점과 화면 표현

##### RAG 처리 코드는 저장 코드와 분리한다 (PDF p.54)

- 오늘은 Router → Repository → JSON 파일
- 이후 확장은 질의 Router → RAG 처리 함수 → 검색 + LLM
- RAG 처리는 근거 검색·프롬프트·모델 호출 연결
- Repository에는 DB·파일 접근만 유지
- 오늘 Service 계층을 새로 구현하지 않으며 기능이 생길 때 책임이 다른 코드를 분리

##### Template와 API는 같은 데이터를 다르게 보여준다 (PDF p.55)

- JSON API `GET /api/knowledge`는 dict·list를 `application/json`으로 응답하며 관리 화면·다른 서버가 사용
- HTML Template `GET /web/knowledge`는 HTML 틀 + 지식 목록을 `text/html`로 응답
- `{{ entry.title }}`로 제목 표시
- 오늘 직접 구현할 기능은 JSON API이며 Template는 비교 시연만, 코드는 부록 A10

#### 실습

##### 실습 06 · 수준에 맞게 파일 역할 이해·분리하기 (PDF p.56)

- 35분, 세 단계 중 하나 선택
- 기본필수는 기존 `main.py`·`storage.py`에서 요청·저장 코드를 찾고 폴더를 나누지 않은 채 실행 흐름과 파일 역할 설명
- 응용은 입력 모델 또는 조회 함수 한 부분만 파일로 분리하고 import 연결 후 같은 URL·응답 유지 확인
- 심화는 제공 폴더 골격에 Router·Schema·Repository를 연결하고 CRUD를 역할별로 옮긴 뒤 분리 전후 응답 비교
- 완료 기준은 기능과 파일 역할 설명
- 전체 구조 분리는 심화 범위이며 HTML 화면 완성은 필수가 아님

**핵심:** 파일 분리는 Schema·Router·Repository가 바뀌는 이유에 따라 책임을 나누는 일이며 분리 전후 URL·응답·저장 결과는 같아야 함

### 7교시 · 함께 통합·검증·플랫폼 연결·프로젝트 준비

#### 플랫폼 API와 최종 계약

##### 지식 관리·RAG 질의·Agent 작업은 다르다 (PDF p.57)

- 오늘 구현한 지식 관리는 `POST /api/knowledge`와 GET·PUT·DELETE로 원본 지식 등록·관리
- 지식 관리는 AI 모델 없이도 동작
- 후속 수업의 설계 예인 RAG 질의 `POST /api/answers`는 질문 → 관련 근거 검색 → 답변과 출처 반환
- 후속 수업의 설계 예인 Agent 작업 `POST /api/agent-runs`는 작업 → 필요한 도구 선택 → 실행 결과 확인, 필요하면 다시 도구 사용
- 세 기능은 서로 다른 API

##### 최종 API 약속 · 다섯 요청을 통일한다 (PDF p.58)

- `GET /api/knowledge`는 선택 Query `category`, 200과 지식 항목 배열
- `GET /api/knowledge/{knowledge_id}`는 정수 Path ID, 200과 지식 항목 하나
- `POST /api/knowledge`는 title·content·category, 201과 새 ID 포함 항목
- `PUT /api/knowledge/{knowledge_id}`는 Path ID + 세 필드 모두, 200과 수정된 항목
- `DELETE /api/knowledge/{knowledge_id}`는 정수 Path ID, 204와 본문 없음
- 없는 ID는 404, 잘못된 입력은 기본 422
- `/health`·`/docs`는 공통 확인 경로

##### 지식 항목 하나를 끝까지 추적한다 (PDF p.59)

- 초기 파일은 항목 3개·`next_id=4`
- 실습 환경 안내 생성 후 항목 4개·id=4·`next_id=5`
- 같은 ID 수정 후 개수·ID 유지, 본문 변경, 나머지 필드 유지
- 서버 종료 후 같은 파일로 재실행하면 수정 내용 그대로 조회
- 같은 ID 삭제 후 상세 404, 목록에서 제거
- 다시 재실행 후에도 삭제 상태 유지, `next_id=5`
- ID 4는 초기 상태에서 한 번 생성했을 때의 예시이며 실제 받은 ID 사용

#### 통합 실습과 검증 기록

##### 실습 07 · 함께 통합하고 일일프로젝트를 준비한다 (PDF p.60)

- 40분, 세 단계 중 하나 선택
- 기본필수는 다섯 API를 하나의 서비스에서 실행하고 등록→조회→수정→삭제를 같은 ID로 확인
- 응용은 조회 조건 하나와 실패 요청을 추가 확인하고 기본 CRUD와 같은 파일을 읽는지 대조
- 심화는 역할별 프로젝트에서 CRUD·404·422·204를 검증하고 제공된 임시 파일 설정으로 실제 저장 데이터 보호
- 완료 기준은 세 단계 모두 HTTP 응답과 실제 파일 변경 확인
- 단계별 차이는 구조·검증의 깊이

##### 검증 기록 · 일일프로젝트에서도 같은 틀을 쓴다 (PDF p.61)

- 요청·예상·실제·확인한 파일 변화의 4열 기록표
- POST는 201·새 ID, 항목 +1·`next_id` +1
- PUT은 200·수정 항목, 본문 변경·개수 동일
- DELETE는 204·빈 본문, 해당 항목만 삭제
- 재실행 후 삭제한 ID의 GET은 404, 삭제 상태 유지
- 실제 열은 직접 기록하고 예시 ID 4 대신 받은 ID 사용
- 설명에는 Path·Body·저장하는 줄·플랫폼에서의 역할 포함

#### 후속 수업 연결

##### 파일에 저장되는데도 왜 DB를 배우는가 (PDF p.62)

- JSON 저장소도 정상 저장 후 재시작하면 데이터 유지
- 작은 파일 전체를 읽고 다시 저장하는 방식
- 잠금은 한 서버 프로세스 안의 학습용 잠금
- 여러 서버·관계·복합 작업에는 한계
- PostgreSQL에서는 동시 변경, 여러 테이블의 관계, 모두 성공 또는 취소가 필요한 변경을 SQL·제약조건·트랜잭션으로 해결

##### 11월 10일 → 11일 → 12일의 연결 (PDF p.63)

- 11/10은 HTTP로 지식 항목을 CRUD하는 JSON 파일 기반 FastAPI
- 11/11은 테이블·관계·SQL로 SQL CRUD·JOIN·ERD·트랜잭션
- 11/12는 기존 API를 PostgreSQL에 연결하는 ORM·연동 CRUD·설정·통합 테스트
- URL·Method·입력·응답은 가능한 한 유지하고 저장 구현과 DB 연결 처리만 교체

##### 그다음 LLM·RAG에서도 같은 API 흐름을 쓴다 (PDF p.64)

- 11/13 LLM·Token·Attention·Embedding은 모델의 입력과 결과 이해로 연결
- 11/16 Prompt·Context·Structured Output은 JSON 구조와 검증으로 연결
- 11/17 LLM API·Streaming·비용·지연은 HTTP 요청·응답과 실패 처리로 연결
- 11/18 Embedding·Vector DB·Top-k는 조회 조건과 검색 결과로 연결
- 11/19 문서 파싱·Chunking·Metadata는 데이터 저장·구조·검증으로 연결
- 11/20 Retriever–Prompt–Generator·RAG는 검색·생성 결과를 API로 제공하는 단계
- 오늘은 후속 기능을 구현하지 않고 작은 서비스의 요청·저장·응답 완성

##### Agent와 API가 연결되는 두 가지 방향 (PDF p.65)

- 사용자가 Agent를 호출하는 방향은 사용자 → FastAPI → Agent 처리이며 API가 Agent의 서비스 입구
- 이 방향에서 API는 작업 요청을 검증하고 실행 결과·상태 전달
- Agent가 API를 사용하는 방향은 Agent → 도구 함수 → 지식 API
- 도구의 설명·입력·실행 코드는 별도이며 API가 자동으로 도구가 되지 않음
- 처음 연결할 때는 조회부터, 수정·삭제는 별도 권한·승인 정책 검토
- 오늘의 필수 구현 범위가 아닌 예고

**핵심:** 다섯 요청의 URL·Method·입력·응답 계약을 고정하고 응답과 파일 변화를 함께 기록해야 이후 DB·RAG·Agent로 저장 구현만 바꿔 확장 가능

### 8교시 · 나만의 지식 API·일일프로젝트·공유

#### 과제 정의와 시작 데이터

##### 배운 흐름을 나만의 작은 서비스로 연결한다 (PDF p.66)

- 요청과 검증 → 파일 읽기와 대상 찾기 → C·U·D 변경과 저장 → 응답과 재조회의 4단계
- 같은 API를 내 주제에 적용해 지식 3개를 직접 관리
- 새 모델·새 기술 없이 일일프로젝트 완성

##### 나만의 AI 도움말 지식 관리 API (PDF p.67)

- 50분 과제
- 사용자와 주제 하나 결정, 예는 우리 반 학습·팀 온보딩·FAQ
- 주제에 맞는 짧은 안내문 3개를 직접 작성
- 공개해도 되는 가상의 내용만 사용
- 기존 FastAPI 코드와 JSON 저장을 재사용하고 URL·필드·상태코드는 그대로 유지
- A는 유지, B는 수정, C는 삭제
- 응답뿐 아니라 파일과 재시작까지 확인
- 결과물은 원본 지식 관리 서비스이며 LLM·벡터 검색·화면·DB는 새로 구현하지 않음

##### 지식 3개를 준비하고 실제 ID를 기록한다 (PDF p.68)

- A·B·C는 역할 이름이며 A는 끝까지 유지, B는 본문 수정, C는 삭제할 지식
- 세 개 모두 POST로 등록하고 응답의 실제 `id`를 따로 기록
- 시작 목록 수 N 기록 후 3개 생성 시 N+3, C 삭제 후 N+2
- /docs Body에는 `{ }` 안의 JSON만 입력
- 슬라이드의 JSON은 주제와 내용 구성 예시이며 ID·개수는 자신의 실행 결과 기준

#### 통과 기준과 시간 배분

##### 하나의 시나리오로 오늘 배운 것을 연결한다 (PDF p.69)

- 1단계 시작은 목록 수 N과 현재 저장 파일 확인, 기존 항목 보존
- 2단계 생성·조회는 POST 3회 → A·B·C ID 기록 → GET, 201·200과 전체 N+3
- 3단계 수정·재시작은 B를 PUT → 서버 종료·재실행 → GET, B의 바뀐 본문과 ID·개수 유지
- 4단계 실패 입력은 `content=""`인 POST 한 번, 422와 기존 지식·`next_id` 변경 없음
- 5단계 삭제·재시작은 C를 DELETE → 서버 재실행 → GET, 204 빈 본문·C 404·A와 B 200
- PUT은 title·content·category를 모두 전송
- 최종 N+2개이며 기존 지식과 A도 그대로 유지

##### 마지막 50분 · 안내 6분 + 수행 40분 + 공유 4분 (PDF p.70)

- 0~6분 과제 안내·공통 기준·난이도 선택
- 6~11분 사용자·주제 결정과 지식 3개 작성
- 11~26분 기존 CRUD 연결과 생성·조회·수정, 실제 ID와 요청 결과 기록
- 26~41분 실패 입력·삭제·두 번의 재시작 확인
- 41~46분 README와 확인 결과 정리
- 46~50분 대표 시연·한 문장 회고·마무리
- 추가 교시가 아니라 기존 8교시 안에서 진행
- 미완성자는 공통 CRUD부터 완성

##### 일일프로젝트 · 같은 목표를 수준에 맞게 완성한다 (PDF p.71)

- 수행 40분, 세 단계 중 하나로 진행
- 기본필수는 현재 단순 구조에서 내 지식 3개를 작성·등록하고 CRUD·오류·재시작을 /docs로 확인·기록
- 응용은 공통 과제에 category 필터 하나를 추가하고 일치하는 목록과 결과 없는 `[]` 확인
- 심화는 기존 역할별 구조에서 임시 파일 테스트를 보완하고 CRUD·422·삭제 후 404 검증, 실제 재시작도 별도 확인
- 공통 기준은 A 유지·B 수정·C 삭제, 오류 확인, 재시작 후 유지
- 기본필수로도 만점 가능

#### 재시작·최종 점검·오류 해결

##### 재시작 검증 · 파일은 그대로 둔다 (PDF p.72)

- GET과 파일로 현재 값 확인 → Ctrl+C로 서버 종료 → 같은 폴더·같은 명령으로 재실행 → 같은 ID 재조회
- B의 수정값을 먼저 확인하고 C 삭제 후에는 A·B 잔존 확인
- 서버 시작은 데이터 초기화가 아님
- 초기화는 서버를 끄고 명시적으로 실행하는 별도 작업

##### 최종 점검 · 정상과 실패를 함께 확인한다 (PDF p.73)

- 목록·상세 조회는 200, 저장 데이터 변경 없음
- 정상 생성은 201 + 새 ID, 항목 +1
- 정상 수정은 200 + 같은 ID, 대상 필드 교체
- 정상 삭제는 204 + 빈 본문, 대상만 제거
- 없는 ID의 조회·수정·삭제는 404, 변경 없음
- 필수 값 누락·`content=""`는 422, 변경 없음
- 재실행 후 조회는 수정 항목 200·삭제 항목 404, 기존 변경 상태 유지
- 없는 ID 테스트의 Body는 정상값으로 보내 오류 조건을 하나씩만 확인

##### 문제가 생기면 가장 가까운 원인부터 본다 (PDF p.74)

- 서버 접속 불가는 터미널·포트·실행 명령 확인, HTTP 오류 응답과 구분
- 404·405는 /docs의 Path·Method·ID 확인, 없는 자원과 다른 Method 구분
- 422는 detail의 `loc`·`msg` 확인, Path·Query·Body 중 위치 구분
- 파일 없음·JSON 오류는 파일 경로·괄호·큰따옴표 확인, 빈 데이터로 덮어쓰지 않음
- 재실행 후 값이 달라지면 자동 초기화·다른 파일 경로 확인, 서버 재시작과 seed 복사 구분

#### 평가·제출·회고

##### 일일프로젝트 평가 · 기본필수만으로 100점 (PDF p.75)

- CRUD 동작 40점은 지식 3개 생성·조회, B 수정, C 삭제 동작
- 파일 저장·재시작 25점은 재시작 후 B 수정·C 삭제 유지와 A·기존 지식 보존
- 입력·오류 응답 15점은 201·204·404·422와 실패 시 데이터 보존
- 흐름·파일 역할 설명 10점은 서비스 목적·요청 흐름·플랫폼 내 역할 설명
- 실행·확인 기록 10점은 실행 명령·실제 ID·예상/실제 검증 결과 기록
- 기본필수만으로 공통 100점 가능
- 구조 분리·자동 테스트는 심화 학습이며 공통 만점의 조건이 아님

##### 작게 만들고, 실행 근거와 설명을 남긴다 (PDF p.76)

- 실행되는 서비스는 기존 프로젝트 코드 + `data/knowledge.json`이며 내가 쓴 지식과 실제 API 동작이 연결된 상태
- 짧은 README에 대상·목적, 실행 위치·명령, A·B·C의 실제 ID, 요청·예상·실제 결과, 저장 위치와 현재 한계 기록
- 확인한 증거는 B 수정 유지·C 삭제 유지·422 전후 데이터 보존, A와 기존 지식 잔존
- 1분 설명은 한 요청이 검증·저장·응답으로 이어지는 경로
- 오늘은 원본 지식 관리이며 검색·답변 생성은 다음 단계라는 범위 설명 포함
- 긴 보고서·별도 화면 제작은 요구하지 않음

##### 마무리 회고 · 내 서비스의 역할을 설명한다 (PDF p.77)

- 공유 4분 안에서 세 질문 중 하나 선택
- Q1은 내 지식 관리 API의 사용자와 목적
- Q2는 B 수정과 C 삭제가 저장됐다는 근거이며 실제 파일과 재시작 후 GET의 B 수정값·C 404·A 보존으로 확인
- Q3은 이 서비스로 RAG·Agent까지 완성되는지이며 원본 지식 관리까지만 해당
- 별도 퀴즈 시간은 추가하지 않음

**핵심:** 일일프로젝트의 통과 기준은 응답 코드가 아니라 두 번의 실제 재시작 후에도 B 수정·C 삭제가 유지되고 A와 기존 지식이 남는 파일 상태

### 마무리 · 오늘의 완료와 다음 단계

#### 완료 기준

##### 오늘의 완료 · 작은 지식 서비스 한 개를 남긴다 (PDF p.78)

- 완료는 내 주제의 지식 3개를 API로 등록하고 조회·수정·삭제까지 연결한 상태
- 증거는 재시작 후 B 수정값과 C 삭제 상태 유지, A와 기존 지식 잔존
- 설명은 요청→검증→저장→응답 경로이며 오늘 결과물은 로컬 학습용 지식 관리 API
- 다음은 PostgreSQL로 저장 확장, 검색·답변 생성·Agent 연결은 후속 수업

### 참고 부록 · 구현 보조·선택 확장·참고자료

#### 부록 지도

##### 참고 부록 · 구현 중 필요할 때만 사용한다 (PDF p.79)

- A02~A04는 파일 저장의 경로·읽기·쓰기·잠금 범위
- A05~A07은 HTTP 입력·함수 인자·Router 사전
- A08~A11은 PATCH·문자열 검색·Template·테스트 선택 확장
- A12~A16은 검수 기록·Windows 실행·공식 자료

#### 파일 저장 보조 코드

##### storage.py · 기준 경로와 읽기 함수 (PDF p.80)

- `BASE = Path(__file__).resolve().parent`로 현재 Python 파일이 있는 폴더를 기준 경로로 사용
- `DATA`는 `BASE / "data" / "knowledge.json"`
- `read_data()`는 UTF-8로 열어 `json.load()`로 JSON → dict·list 변환
- 누락·손상 파일은 예외로 알리고 빈 데이터로 자동 복구하지 않음
- `data/knowledge.json`은 사전 준비 대상
- `main`에서 같은 `LOCK`을 import하고 잠금 범위는 호출자가 관리

##### storage.py · 임시 파일을 쓴 뒤 교체한다 (PDF p.81)

- 같은 폴더의 `.tmp` 임시 파일에 `json.dump(..., ensure_ascii=False, indent=2)`로 기록
- 파일을 닫은 뒤 `temp.replace(DATA)`로 실제 데이터 파일과 교체
- `finally`에서 남은 임시 파일 정리
- 호출은 반드시 같은 `LOCK` 안에서 수행
- 한 프로세스·한 저장 파일 전제
- 쓰기 실패는 호출자에게 전달
- DB 트랜잭션의 대체물이 아님

##### 참고 · Lock이 보호하는 범위와 한계 (PDF p.82)

- 같은 프로세스 안에서 읽기 → 대상 변경 → 파일 저장을 하나의 `with LOCK:` 안에 두어 보호
- 쓰기 한 줄만 잠그면 동시 요청이 서로의 변경을 덮어쓸 수 있음
- `def` Route도 동시 요청 처리 가능
- 서로 다른 서버 프로세스의 접근은 보장 범위 밖
- 실행 중 외부 편집기의 파일 수정은 보장 범위 밖
- 정전·디스크 고장에 대한 완전한 복구는 보장 범위 밖
- 여러 테이블 변경의 트랜잭션은 보장 범위 밖

#### HTTP·함수 용어 사전

##### HTTP·입력 위치 · 헷갈리는 용어 사전 (PDF p.83)

- Method는 GET·POST·PUT·DELETE의 요청 의도
- Path는 `/api/knowledge/4`처럼 자원의 경로와 대상 ID
- Query는 `?category=api`처럼 목록의 선택 조건
- Header는 `Content-Type: application/json` 등 본문 형식과 부가 정보
- Body는 생성·수정에 보낼 데이터
- Status는 200·201·204·404·422 등 처리 결과
- Response body는 지식 항목 JSON·오류 detail·없음 중 클라이언트가 받는 내용

##### 입력·응답 함수 · 지식 API에서 쓰는 규칙 (PDF p.84)

- `Field(...)`는 `min_length`·`max_length` 지정, 기본값이 없으면 필수 필드
- `payload.model_dump()`는 검증 모델을 dict로 반환하며 파일 저장은 하지 않음
- `HTTPException(...)`은 `status_code`·`detail` 지정, `return`이 아니라 `raise`
- `response_model=Knowledge`는 반환값의 구조·문서·필드 규칙이며 DB Model과 다른 개념
- `Response(status_code=204)`는 본문 없는 HTTP 응답이며 JSON을 함께 반환하지 않음

##### 앱·Router 함수 · 등록과 실행을 구분한다 (PDF p.85)

- `FastAPI(title="Knowledge API")`는 앱 객체 생성, `title`은 선택 설정
- `@app.get("/health")`는 Method·Path를 함수에 등록하며 함수는 요청이 올 때 실행
- `APIRouter(prefix=..., tags=...)`는 관련 Route를 한 모듈로 묶음, `tags`는 문서 그룹
- `app.include_router(router)`는 앱에 Router 연결, prefix와 Route Path 결합
- `main:app`과 `app.main:app`은 실행할 모듈과 앱 변수이며 프로젝트 구조에 맞춰 선택

#### 선택 확장

##### 참고 개념 · PUT과 PATCH의 차이 (PDF p.86)

- 오늘의 필수 PUT은 세 필드를 모두 보내 기존 항목 교체
- PUT의 누락 필드는 422, 없는 ID는 404, ID와 항목 수는 유지
- PATCH는 바꿀 필드만 보내는 추가 참고 개념
- `model_dump(exclude_unset=True)`로 전송한 필드만 추출 가능
- PATCH는 생략과 명시적 `null`을 구분해야 하며 부분 수정 규칙은 별도로 정함

##### 응용 참고 · 제목·본문의 문자열을 찾는다 (PDF p.87)

- `q: str = Query("", max_length=80)`로 검색어 Query 선언, category와 별개인 목록 Route 교체 예시
- `q`가 title 또는 content에 포함된 항목만 반환
- `q` 생략 시 빈 문자열이므로 전체 목록
- `q=서버`이면 초기 지식 1건
- 대소문자를 구분하는 포함 비교이며 의미 유사도를 계산하지 않음
- 0건도 200 + `[]`
- RAG·벡터 검색이 아님

##### 비교 시연 · 같은 지식을 HTML로 보여준다 (PDF p.88)

- `Jinja2Templates(directory=BASE / "templates")`와 `HTMLResponse`로 `/web/knowledge` Route 구성
- `templates.TemplateResponse(request=..., name="knowledge.html", context={"entries": ...})`로 HTML 응답
- `main.py` 단계의 독립 시연이며 `jinja2` 설치 필요
- `main.py` 옆 `templates` 폴더에 `knowledge.html` 작성, `{% for entry in entries %}`와 `{{ entry.title }}`로 목록 표시
- JSON `/api/knowledge`와 HTML `/web/knowledge`는 같은 저장 파일을 읽음

##### 심화 · 테스트가 실제 지식을 바꾸지 않게 한다 (PDF p.89)

- `app/` 구조화 이후 프로젝트 루트 `tests/`의 예시
- pytest가 제공하는 `tmp_path`에 빈 임시 `knowledge.json` 생성
- `monkeypatch.setattr(repo, "DATA", test_file)`로 Repository의 데이터 경로만 교체
- `TestClient(app)`로 없는 ID DELETE 요청 후 404와 파일 바이트 불변 확인
- 실제 `knowledge.json` 보존
- 서버 재시작 검증은 별도로 진행
- 추가 설치는 `pytest`·`httpx`

#### 검수·실행 보조·공식 자료

##### 검수 범위 · 일일프로젝트 추가본 (PDF p.90)

- 수정 범위는 일일프로젝트 안내·시간표·완료 기준이며 기존 API 구현 예제는 변경하지 않음
- 코드는 원본의 Linux 실행 검수 기록 유지, 이번 수정에서 API 런타임 재검수는 하지 않음
- 이번 PPT 검수는 84장 전체 렌더링·배치·장번호·노트·과제와 API 계약의 일치 확인
- 교실 Windows·브라우저 직접 조작·LLM·벡터 DB·Agent·운영 배포는 미검증

##### Windows · 활성화가 막혀도 Python을 직접 실행한다 (PDF p.91)

- 프로젝트 루트에서 `.\.venv\Scripts\python.exe -m pip install ...`과 `... -m uvicorn main:app --reload`로 활성화 없이 실행
- 구조화 후에는 기존 서버 종료 후 `app.main:app` 실행
- /docs 사용이 어려우면 `Invoke-RestMethod`로 GET 확인
- 보안 정책을 임의로 바꾸지 않음
- 가상환경의 Python 경로를 설치와 실행에 똑같이 사용
- 두 서버를 동시에 띄우지 않음
- 실행 위치는 프로젝트 루트
- 포트를 바꾸면 URL도 수정

##### 공식 참고자료 · FastAPI·RAG·Agent 연결 (PDF p.92)

- FastAPI의 First Steps·Path·Query·Request Body·Status Code·Handling Errors·Body Updates 문서
- FastAPI의 Response Model·Bigger Applications·Templates·Security·Settings 문서
- LangChain의 Retrieval·RAG와 Tools 문서
- 새 플랫폼 설명은 개념 참고이며 프레임워크 설치 과제가 아님

##### 공식 참고자료 · 파일·실행·검증 (PDF p.93)

- Python의 json·pathlib·threading·os.replace·venv 문서
- Pydantic의 Models·Fields와 Field constraints 문서
- FastAPI의 Testing·async/await 문서와 Uvicorn Settings
- RFC 9110 HTTP Semantics와 PostgreSQL Transactions
- 실행 검수 환경과 한계는 부록 A12에서 확인

##### 개편 범위 · 마지막 일일프로젝트까지 연결한다 (PDF p.94)

- 디자인 원본은 강의자료 기본 템플릿이며 제목·코드·실습·하단 형식 유지
- 학습 단계는 기본필수 → 응용 → 심화, 핵심 동작에서 역할 분리·검증으로 확장
- 이번 추가는 마지막 50분의 지식 관리 일일프로젝트와 과제·수준·검증·공유 기준
- 이 슬라이드는 제작물이 PPT뿐이고 수강생용 TODO·강사용 정답·참고 MVP는 아직 없다고 설명하지만, 현재 폴더에는 해당 실습 패키지가 후속 산출물로 포함

## 자료 간 표기 차이

- 실습 README·PPT 대응표·자료기준의 “PPT N쪽”은 84장 원본 기준. 현재 PDF는 p.2~11에 도입 10장이 추가되어 원본 2~84쪽이 PDF p.12~94에 해당(PDF 쪽수 = PPT 쪽수 + 10). 예: 실습 01~08은 PPT 11·19·27·32·38·46·50·61쪽, PDF p.21·29·37·42·48·56·60·71. 이 요약의 모든 페이지는 현재 PDF 기준.
- 강사용·수강생용 README의 `cd ".\01_기본필수\..."` 명령과 수준 링크는 `01_기본필수`·`02_응용`·`03_심화` 폴더명을 사용하지만, 실제 폴더는 `01_basic`·`02_intermediate`·`03_advanced`. 명령을 그대로 복사하면 경로 오류.
- 강사용 README의 심화 추가 설치 `requirements-test.txt`는 폴더에 없음. 현재 `requirements.txt`에 `pytest`·`httpx`가 이미 포함.
