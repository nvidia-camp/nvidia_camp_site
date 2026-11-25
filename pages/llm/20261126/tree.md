# Day29 강의구조와 핵심설명 · AI Agent Fundamentals & Tool Calling

- 원자료: `Day29_20261126_AI_Agent.html` · 2026.11.26 (목) · Day 29 · 생성형 AI·LLM 및 RAG 엔지니어링
- 범위: 표지·목차 2개, 8교시 63개 화면. 총 65개 화면
- 교시는 HTML의 Chapter 01~08에 대응하며 교시 제목은 `chapters[].title` 원문 표기
- 교시 아래 학습 주제와 ‘도입’ 묶음은 정리를 위해 붙인 편집 표현. 화면 제목은 원문 유지
- 위치 표시는 HTML 슬라이드 순서 기준 `(화면 N)`

## 강의 목차

```text
AI Agent Fundamentals & Tool Calling
├─ 도입
│  ├─ AI Agent Fundamentals & Tool Calling (화면 1)
│  └─ 목차 (화면 2)
├─ 1교시 · AI Agent Fundamentals
│  ├─ Agent의 위치와 정의
│  │  ├─ 전체지도 · Agent는 기존 RAG 위에서 무엇을 하나요? (화면 3)
│  │  ├─ AI Agent는 무엇인가요? (화면 4)
│  │  └─ 고정 RAG · Workflow · Agent 비교 (화면 5)
│  ├─ 업무 분해와 Agent Loop
│  │  ├─ Agent가 사용되는 실제 업무를 분해합니다 (화면 6)
│  │  └─ Agent Loop를 단계별로 따라가 봅니다 (화면 7)
│  └─ 시연과 실습
│     ├─ 시연 · 같은 질문을 세 처리 방식에 적용하기 (화면 8)
│     └─ 실습 01 안내 · RAG와 Agent 흐름 구분 (화면 9)
├─ 2교시 · Tool Calling Protocol
│  ├─ Tool Calling과 메시지 역할
│  │  ├─ Tool Calling은 어떤 기능인가요? (화면 10)
│  │  └─ Agent 메시지의 네 가지 역할 (화면 11)
│  ├─ 요청과 실행의 분리
│  │  ├─ `bind_tools()`는 실행이 아니라 Tool 목록 전달입니다 (화면 12)
│  │  ├─ Tool Call 요청과 ToolMessage를 연결합니다 (화면 13)
│  │  └─ Harness 없이 실행 경계를 이해하는 최소 예시 (화면 14)
│  └─ 시연과 실습
│     ├─ 시연 · Tool Call → ToolMessage → 최종 답변 (화면 15)
│     └─ 실습 02 안내 · Tool Calling 메시지 추적 (화면 16)
├─ 3교시 · Tool & Schema
│  ├─ Tool 계약과 Schema
│  │  ├─ Tool은 무엇이며 어떤 계약을 가져야 하나요? (화면 17)
│  │  ├─ `@tool`은 일반 Python 함수를 LangChain Tool로 만듭니다 (화면 18)
│  │  ├─ Tool Schema의 실제 JSON 모습 (화면 19)
│  │  └─ Pydantic `Field`로 잘못된 Tool 인수를 걸러냅니다 (화면 20)
│  ├─ 결과 계약과 서버 검증
│  │  ├─ Tool 결과는 무엇을 돌려주어야 하나요? (화면 21)
│  │  └─ 모델의 Tool 선택과 서버 검증은 역할이 다릅니다 (화면 22)
│  └─ 시연과 실습
│     ├─ 시연 · Tool Schema 검사기를 사용해 봅니다 (화면 23)
│     └─ 실습 03 안내 · `@tool`·Schema·검증 (화면 24)
├─ 4교시 · RAG as a Tool
│  ├─ 기존 RAG의 Tool화
│  │  ├─ 기존 Day27 RAG를 `rag_search` Tool로 재사용합니다 (화면 25)
│  │  ├─ RAG를 Tool로 노출할 때 무엇이 달라지나요? (화면 26)
│  │  └─ `rag_search` Wrapper로 실제 RAG를 감쌉니다 (화면 27)
│  ├─ 반환 계약과 설계 선택
│  │  ├─ Tool 결과의 출처 계약을 명확히 합니다 (화면 28)
│  │  ├─ RAG Tool 반환 설계 두 가지를 비교합니다 (화면 29)
│  │  └─ No-answer와 서비스 오류를 구분합니다 (화면 30)
│  └─ 시연과 실습
│     ├─ 시연 · RAG Tool의 반환값을 확인합니다 (화면 31)
│     └─ 실습 04 안내 · 기존 RAG를 Tool로 감싸기 (화면 32)
├─ 5교시 · PostgreSQL Read-only Tool
│  ├─ DB Tool의 역할과 데이터
│  │  ├─ PostgreSQL 조회는 Agent의 두 번째 Tool입니다 (화면 33)
│  │  ├─ `lookup_status`는 무엇을 반환할까요? (화면 34)
│  │  └─ 현업 DB 테이블의 구조와 샘플 행 (화면 35)
│  ├─ 안전한 조회와 신원 주입
│  │  ├─ Parameterized SQL로 읽기 전용 조회를 구현합니다 (화면 36)
│  │  ├─ `ToolRuntime`는 서버 인증 정보를 어떻게 전달하나요? (화면 37)
│  │  └─ `ToolRuntime[UserContext]`로 DB Tool 신원을 고정합니다 (화면 38)
│  └─ 시연과 실습
│     ├─ 시연 · 다른 사용자·과제 ID를 조회해 봅니다 (화면 39)
│     └─ 실습 05 안내 · PostgreSQL Read-only Tool (화면 40)
├─ 6교시 · create_agent Integration
│  ├─ create_agent 구성과 실행
│  │  ├─ `create_agent`는 무엇을 자동으로 관리하나요? (화면 41)
│  │  ├─ 실제 `create_agent()`를 구성합니다 (화면 42)
│  │  └─ `agent.invoke()`가 받는 메시지 구조 (화면 43)
│  ├─ 복합 요청의 실행 흐름
│  │  ├─ 복합 업무 요청의 실제 메시지 실행 순서 (화면 44)
│  │  ├─ VS Code · 파일과 실제 실행 Stage 연결 (화면 45)
│  │  └─ 한 번의 질문에 Tool이 반드시 두 개 호출되나요? (화면 46)
│  ├─ 결과 추출
│  │  └─ 최종 답변을 추출할 때 놓치기 쉬운 부분 (화면 47)
│  └─ 시연과 실습
│     ├─ 시연 · 단일·복합 질문의 Agent 실행 추적 (화면 48)
│     └─ 실습 06 안내 · 단일 Agent에 Tool 2개 등록 (화면 49)
├─ 7교시 · Reliability & Guardrails
│  ├─ 신뢰성 평가 축과 오류 분류
│  │  ├─ Agent Reliability는 무엇을 확인하나요? (화면 50)
│  │  └─ Tool 실패를 하나의 오류로 합치면 안 됩니다 (화면 51)
│  ├─ 실행 제한·권한·검증
│  │  ├─ `ToolCallLimitMiddleware`로 실행 상한을 적용합니다 (화면 52)
│  │  ├─ 권한은 Prompt가 아니라 서버에서 검증합니다 (화면 53)
│  │  └─ Tool 결과를 검증하는 서버 측 Validator (화면 54)
│  ├─ 기록과 회귀 테스트
│  │  ├─ Trace와 Audit Log는 무엇이 다른가요? (화면 55)
│  │  ├─ 시연 · 오류·권한·반복 상한을 적용해 봅니다 (화면 56)
│  │  └─ 11월 27일에 필요한 최소 회귀 테스트 (화면 57)
│  └─ 실습
│     └─ 실습 07 안내 · Agent Reliability 테스트 (화면 58)
└─ 8교시 · End-to-End & Project Bridge
   ├─ API 통합과 데이터 계약
   │  ├─ 최종 아키텍처 · FastAPI에서 Agent까지 (화면 59)
   │  ├─ FastAPI에서 신뢰된 Context를 Agent에 전달합니다 (화면 60)
   │  └─ 개인 프로젝트 전에 확인할 전체 데이터 계약 (화면 61)
   ├─ 개인 프로젝트 기준
   │  ├─ 11월 27일 개인 프로젝트의 최소 완료 기준 (화면 62)
   │  └─ 네 직무의 기술이 하나의 Agent 서비스에서 만납니다 (화면 63)
   └─ 시연과 실습
      ├─ 시연 · 내일 완성할 Agent API 전체 요청 (화면 64)
      └─ 실습 08 안내 · Agent End-to-End·개인 프로젝트 준비 (화면 65)
```

## 핵심 설명

### 도입

##### AI Agent Fundamentals & Tool Calling (화면 1)

- 기존 RAG와 PostgreSQL을 Tool로 연결하는 Day29 표지

##### 목차 (화면 2)

- AI Agent 개념 → Tool Calling → 코드 → 오류 처리를 한 요청 기준으로 잇는 8개 Chapter 구성

### 1교시 · AI Agent Fundamentals

#### Agent의 위치와 정의

##### 전체지도 · Agent는 기존 RAG 위에서 무엇을 하나요? (화면 3)

- 기본 경로는 사용자 → FastAPI → Agent → Tool(RAG/DB) → Model → Response
- E5(CUDA)·pgvector·GPU Reranker·LangChain RAG, PostgreSQL 조회, FastAPI는 기존 기능으로 유지
- 새로 추가하는 부분은 필요한 Tool을 판단하는 Model과 실행 Harness
- Tool은 서버 쪽 Python 코드가 수행
- 11/27 개인 프로젝트 목표는 단일 Agent에 두 Tool 연결, 필요 시 FastAPI API로 제공
- Tool 선택 횟수와 순서는 질문과 모델 응답에 따라 달라짐

##### AI Agent는 무엇인가요? (화면 4)

- LLM이 작업 상태와 사용 가능한 Tool을 보고 다음 행동(도구 호출 또는 최종 답변)을 선택하는 시스템
- 실행 환경이 그 행동을 수행하고 결과를 다시 모델에 전달
- Model은 Tool 이름·입력을 제안하는 판단 주체
- Tool은 검색·DB 조회처럼 실제 데이터를 가져오는 명시적 함수
- Agent Harness는 모델 호출, Tool Dispatch, 메시지 전달, 한도·오류 처리를 운영하는 실행 환경
- 최종 답변 반환 또는 실행 정책에 따른 중단 시 Agent Loop 종료
- 여러 모델이나 복잡한 Planner가 필수는 아님. 오늘은 단일 모델·두 Tool 구조로 시작

##### 고정 RAG · Workflow · Agent 비교 (화면 5)

- 구분 기준은 다음 단계를 누가 정하는가
- 고정 RAG는 개발자가 Retrieve→Generate 순서를 고정
- Rule-based Workflow는 if/else 등 정의된 조건이 분기를 결정
- Tool Calling Agent는 모델이 Tool 요청과 최종 답변 여부를 제안
- 반복 절차가 명확하고 안정성이 중요하면 고정 Workflow가 더 적합할 수 있음

#### 업무 분해와 Agent Loop

##### Agent가 사용되는 실제 업무를 분해합니다 (화면 6)

- 요청 내용을 데이터 출처별로 나눠 Tool 후보 결정
- 정책·매뉴얼·FAQ 같은 비정형 문서는 `rag_search`가 검색
- 과제·주문·예약 상태 같은 최신 구조화 데이터는 `lookup_status`가 조회
- Agent Platform은 의도 해석과 Tool 호출 담당, DB 접속 권한은 모델에 맡기지 않음
- Infra는 API 인증, DB 연결, 실패 상태, GPU·LLM 실행시간 관리
- RAG 결과는 문서 속 규정, DB 결과는 현재 상태. 서로 대체 불가

##### Agent Loop를 단계별로 따라가 봅니다 (화면 7)

- 흐름은 HumanMessage → LLM 판단 → `tool_calls` → Python Tool → ToolMessage → LLM 답변
- 반복의 의미는 Tool 결과를 받은 뒤 새 메시지로 모델을 다시 호출하는 것
- Tool Call이 있으면 Harness가 이름·인수를 검사하고 실행한 뒤 결과를 모델에 반환
- Tool Call이 없는 최종 AIMessage가 생성되면 정상 종료
- 호출 제한·권한 오류·DB 오류 발생 시 정책에 따라 중단 또는 오류 표시
- 한 번에 여러 Tool Call이 반환될 수 있으며 순서는 고정되지 않음

#### 시연과 실습

##### 시연 · 같은 질문을 세 처리 방식에 적용하기 (화면 8)

- 질문 유형과 처리 방식을 바꿔 어느 경로가 충분하고 어디서 추가 Tool이 필요한지 확인

##### 실습 01 안내 · RAG와 Agent 흐름 구분 (화면 9)

- 목표는 질문별 처리 방식, 필요한 Tool 목록과 이유 정리
- Basic은 질문 3개에 고정 RAG 또는 Agent 필요 여부와 이유 한 문장 작성
- Intermediate는 문서 조회·상태 조회·복합 조회를 결정하는 조건 작성
- Advanced는 데이터 소스별 책임, 쓰지 말아야 할 Tool, 실패 사례를 포함한 요구사항 설계
- 규정과 내 제출 상태를 함께 묻는 질문은 현재 상태가 DB에 있으므로 RAG만으로 부족
- 오늘의 Tool은 LLM이 SQL을 작성하지 않고 서버에 미리 작성된 SELECT 사용
- 실제 Agent 구현은 Chapter 06에서 연결

**핵심:** 다음 단계를 모델이 고르는지, 필요한 데이터가 문서인지 DB인지로 RAG·Workflow·Agent를 구분.

### 2교시 · Tool Calling Protocol

#### Tool Calling과 메시지 역할

##### Tool Calling은 어떤 기능인가요? (화면 10)

- 모델이 일반 문장 대신 Tool 이름과 JSON args로 된 구조화 호출 요청을 반환하는 기능
- 모델은 호출을 제안할 뿐 서버 DB에 직접 접속하지 않음
- 앱은 허용된 Tool인지 확인하고 입력을 검증한 뒤 Python 함수를 실행
- Tool 결과를 ToolMessage로 대화에 추가하면 모델이 다음 행동 또는 답변 결정
- 로컬 Python Tool의 실제 실행 책임은 Agent Harness 또는 애플리케이션

##### Agent 메시지의 네 가지 역할 (화면 11)

- SystemMessage는 개발자·서비스 설정이 만드는 역할·지침·금지 작업
- HumanMessage는 사용자 업무 요청, FastAPI 요청 본문에 대응
- AIMessage는 모델이 만드는 `tool_calls` 또는 최종 content
- ToolMessage는 실행 환경이 만드는 `tool_call_id`와 도구 결과
- `tool_calls`는 AIMessage에 실리고 ToolMessage는 같은 호출 ID로 요청과 연결
- 메시지 내용에 민감한 실행 결과가 포함될 수 있음

#### 요청과 실행의 분리

##### `bind_tools()`는 실행이 아니라 Tool 목록 전달입니다 (화면 12)

- `bind_tools()`는 Tool Schema를 모델에 제공해 호출 요청 생성까지만 담당
- `invoke()`는 모델 API 호출이며 Python Tool은 아직 실행되지 않음
- `response.tool_calls`의 핵심 필드는 `name`, `args`, `id`
- 모델 판단에 따라 `tool_calls`가 비어 있을 수 있음

##### Tool Call 요청과 ToolMessage를 연결합니다 (화면 13)

- 흐름은 AIMessage(`tool_calls`) → Harness의 name·args 검증 → Python 실행 → ToolMessage → 모델 해석
- 같은 call ID로 요청과 결과를 짝지어 여러 호출 결과를 구분
- 서버가 Tool 실행 완료를 확인하기 전에는 결과를 성공으로 단정하지 않음

##### Harness 없이 실행 경계를 이해하는 최소 예시 (화면 14)

- 모델 요청과 Python 실행을 분리해 보여 주는 개념 코드
- 모델이 임의의 함수 이름을 제안할 수 있으므로 허용 목록(`allowed`)에 없는 Tool은 거부
- ToolCall을 `tool.invoke()`에 넣으면 ToolMessage 반환
- 실제 프로젝트에서는 `create_agent`가 이 반복을 관리

#### 시연과 실습

##### 시연 · Tool Call → ToolMessage → 최종 답변 (화면 15)

- 단계와 요청을 바꾸며 모델 요청·실제 실행·응답 재입력 시점 확인

##### 실습 02 안내 · Tool Calling 메시지 추적 (화면 16)

- 목표는 Tool Call ID와 인수·결과의 연결을 설명하는 Trace 표
- Basic은 제공된 Tool Call의 name·args·id를 읽고 결과 메시지와 연결
- Intermediate는 두 Tool Call ID의 순서·결과 매칭과 잘못된 호출 식별
- Advanced는 허용되지 않은 Tool, 응답 누락, 중복 ID를 검사하는 Dispatch Contract 구현
- `bind_tools()` 호출만으로는 DB SELECT가 실행되지 않음
- 결과 확인은 미리 정의한 Fixture로 하며 모델 API 호출과 구분

**핵심:** 모델은 Tool Call을 요청만 하고, 실행과 ID 기반 결과 연결은 애플리케이션 책임.

### 3교시 · Tool & Schema

#### Tool 계약과 Schema

##### Tool은 무엇이며 어떤 계약을 가져야 하나요? (화면 17)

- Tool은 이름·설명·입력 Schema·반환값을 명시한 호출 가능한 기능
- Name은 모델이 선택할 고유 이름. 예: `rag_search`, `lookup_status`
- Description은 언제 이 Tool을 쓰는지 설명하며 모델의 선택에 영향
- Args Schema는 입력 필드·자료형·허용 범위 정의. 예: `task_id`는 양의 정수
- Output Contract는 성공·미존재·권한 실패·서비스 오류를 구분해 반환
- 애매한 Docstring과 무제한 인수는 잘못된 Tool 선택이나 위험한 실행으로 이어짐

##### `@tool`은 일반 Python 함수를 LangChain Tool로 만듭니다 (화면 18)

- Decorator가 함수 이름·Docstring·Type Hint를 읽어 Tool 정의 구성
- Docstring은 모델이 Tool 목적과 사용 시점을 파악하는 근거
- Type Hint(`query: str`)로 기본 입력 Schema 생성
- `.name`, `.args`로 Schema 확인, `.invoke()` 시 Python 함수 실행

##### Tool Schema의 실제 JSON 모습 (화면 19)

- `name`, `description`, `properties`, `required`로 채울 필드를 구조적으로 제공
- `task_id`는 `{"type":"integer","minimum":1}`처럼 범위까지 표현
- JSON Schema는 요청 형식 검증용이며 조회 권한을 대신하지 않음
- 서버는 실행 전 필드를 다시 검증
- 표의 return 행은 입력 Schema 필드가 아니라 개발자가 별도로 정의한 Output Contract 예시

##### Pydantic `Field`로 잘못된 Tool 인수를 걸러냅니다 (화면 20)

- `BaseModel`로 인수 Schema를 정의하고 `@tool(args_schema=...)`로 연결
- `Field(ge=1, strict=True)`로 음수·문자열 `task_id` 차단
- Schema를 통과하지 못한 입력은 Tool 실행 전에 `ValidationError`로 탐지

#### 결과 계약과 서버 검증

##### Tool 결과는 무엇을 돌려주어야 하나요? (화면 21)

- 성공은 `status`, `result`, `sources`를 일관되게 작성. 예: `status=answered`
- 검색 근거가 없으면 `status=insufficient_context`로 표시하고 정보를 만들어 내지 않음
- DB에 대상이 없으면 `status=not_found` 명시
- 권한 위반과 DB 장애는 조회 실패와 별도의 오류로 처리
- 함수 반환이 자동으로 API 성공 응답이 되지 않으며 서버가 결과·출처·상태 재검증

##### 모델의 Tool 선택과 서버 검증은 역할이 다릅니다 (화면 22)

- Schema가 맞는 입력도 권한 없는 데이터를 요청할 수 있음
- 모델의 “조회해도 된다”는 판단은 보안 검증이 아님
- Schema 검사는 자료형과 허용 목록 확인
- 권한 검사는 인증된 사용자가 해당 `task_id`의 소유자인지 서버가 확인
- DB 계정에는 필요한 SELECT 권한만 부여
- 유효성 오류·권한 오류·없는 ID·DB 장애를 분리해 기록
- 모델에게서 받은 `user_id`를 그대로 신뢰하면 타인 정보 노출 위험

#### 시연과 실습

##### 시연 · Tool Schema 검사기를 사용해 봅니다 (화면 23)

- `task_id`·`category`를 바꿔 입력 검증 통과 여부와 실행 전 차단 이유 확인

##### 실습 03 안내 · `@tool`·Schema·검증 (화면 24)

- 목표는 이름·Schema가 명확하고 음수 ID를 거절하는 Tool
- Basic은 `@tool` 함수와 Docstring 완성 후 `.invoke()`로 교육용 결과 확인
- Intermediate는 Pydantic `args_schema`와 입력 오류 테스트 추가
- Advanced는 Schema 검증과 인증·권한 검증을 분리한 Tool Contract 설계
- Type Hint 자료형 검사는 권한 검사를 대체하지 못함
- 실제 DB 작업은 실습 05에서 수행

**핵심:** Schema는 입력 형식을 막고, 권한은 서버가 인증된 신원으로 따로 검증.

### 4교시 · RAG as a Tool

#### 기존 RAG의 Tool화

##### 기존 Day27 RAG를 `rag_search` Tool로 재사용합니다 (화면 25)

- 흐름은 Agent → Tool Wrapper(입력·권한) → E5·pgvector → GPU CrossEncoder → Context+LLM → status·sources
- Day26 Basic RAG, Day27 Rewrite·Reranking, Day28 품질 평가 결과를 그대로 재사용
- 새로 구현하는 부분은 query/category를 받아 기존 RAG를 호출하는 `@tool` Wrapper
- Golden Labels는 오프라인 평가용이며 Agent Tool 입력에 포함하지 않음
- 답변까지 반환하는 Tool을 먼저 배우고 검색 결과만 반환하는 Tool은 비용 최적화 대안으로 비교

##### RAG를 Tool로 노출할 때 무엇이 달라지나요? (화면 26)

- 질문마다 무조건 실행하던 RAG가 Agent가 필요할 때 호출하는 기능으로 바뀜
- 입력은 query, category 등 필요한 필드만 받고 권한·신원은 서버에서 전달
- 내부 처리는 E5 query Embedding(CUDA) → pgvector → Reranker(CUDA) → Context → LLM
- 출력은 근거 기반 answer, verified sources, status
- Wrapper에서 기존 RAG 응답을 정해진 Tool 결과 계약으로 변환
- Category allowlist는 문서 접근 권한 검사가 아님. RAG 내부에서 인증 사용자 기준으로 문서 필터링

##### `rag_search` Wrapper로 실제 RAG를 감쌉니다 (화면 27)

- `run_existing_rag`는 Day27 RAG 서비스 호출로 교체할 Adapter 자리
- `NotImplementedError`는 연결 전 코드를 완성본으로 오인하지 않게 하는 표시
- 허용되지 않은 category는 `ValueError`로 거부
- 반환은 `status`, `answer`, `sources`만 추린 JSON 문자열
- `sources`는 실제 `included_ids`에 속하는지 검증한 뒤 반환

#### 반환 계약과 설계 선택

##### Tool 결과의 출처 계약을 명확히 합니다 (화면 28)

- 검증되지 않은 출처 ID를 인용한 응답은 그럴듯해도 신뢰 불가
- `status`는 answered / insufficient_context / error 분리
- `answer`는 해당 Context가 사실을 지지하는지 확인
- `sources`는 `included_ids`와 대조해 검증한 출처만 전달
- `missing_information`은 정보 부족 시 누락 요소 표시
- `trace_id`는 오류·원문 점검용 내부 기록 ID
- 최종 Citation Validator는 서버가 보관한 검증 출처 기준으로 동작

##### RAG Tool 반환 설계 두 가지를 비교합니다 (화면 29)

- Answer Tool은 기존 RAG가 내부 LLM까지 호출해 answer+sources 반환, 기존 수업 재사용이 쉬움
- Evidence Tool은 Retriever·Reranker가 선정한 Context와 sources만 반환하고 Agent가 최종 답변 생성
- Answer Tool은 Agent가 다시 LLM을 호출하면 이중 생성 비용 발생 가능
- 오늘은 구현이 단순한 Answer Tool을 사용하고 최적화 설계는 비교만 진행
- 선택 기준은 중복 LLM 호출 여부와 Context·Citation 계약의 측정 결과

##### No-answer와 서비스 오류를 구분합니다 (화면 30)

- 검색 근거 없음은 정상 업무 결과일 수 있지만 CUDA OOM·DB 연결 실패는 시스템 오류
- `answered`인데 `sources`가 없으면 오류
- `insufficient_context`인데 `sources`가 있으면 오류
- 401 인증 오류, DB 오류, GPU 오류는 `RuntimeError`로 실패 유지

#### 시연과 실습

##### 시연 · RAG Tool의 반환값을 확인합니다 (화면 31)

- 질문·Tool 방식·실패 유형을 바꾸며 verified sources, No-answer, 비용 차이 관찰

##### 실습 04 안내 · 기존 RAG를 Tool로 감싸기 (화면 32)

- 목표는 `rag_search(query, category)`의 명확한 성공/오류 출력
- Basic은 기존 RAG 호출부를 `@tool` Wrapper로 연결하고 결과 확인
- Intermediate는 status·answer·sources 검증과 No-answer·오류 분리
- Advanced는 권한·출처 ID·Latency·예외 기록과 이중 생성 비용 비교
- Gold Label은 평가 전용이며 `rag_search` 입력에 넣지 않음
- Retriever가 반환한 문서가 아니라 실제 포함된 Context ID만 인용 근거
- Day27 프로젝트별 함수 이름에 맞춰 Adapter 연결

**핵심:** RAG 내부는 재사용하고 Wrapper에서 검증된 출처·No-answer·오류를 구분한 결과 계약을 제공.

### 5교시 · PostgreSQL Read-only Tool

#### DB Tool의 역할과 데이터

##### PostgreSQL 조회는 Agent의 두 번째 Tool입니다 (화면 33)

- 문서 규정은 RAG, 개인의 현재 상태는 PostgreSQL에서 조회
- 흐름은 Agent → Authorization → DB Tool(SQL 파라미터) → PostgreSQL(SELECT + owner) → ToolMessage
- Tool 내부에서 개발자가 작성한 Parameterized SQL 사용, LLM에 SQL 실행 권한을 주지 않음
- 신원은 로그인 인증을 거친 서버의 `user_id`를 Runtime Context로 전달
- 모델이 생성한 값은 신원으로 신뢰하지 않음
- 전용 읽기 계정은 SELECT만 가능하도록 권한 제한
- FastAPI가 Agent 실행 전에 신원 인증(Authentication), DB Tool이 신원과 `task_id`로 조회 권한 판단(Authorization)

##### `lookup_status`는 무엇을 반환할까요? (화면 34)

- 지정한 과제 ID에 대해 인증된 사용자 자신의 제출 상태만 반환하는 Read-only Tool
- `task_id`는 모델이 선택하는 양의 정수
- `user_id`는 FastAPI 인증 계층에서 확인한 서버 측 값
- 결과는 submitted, pending 같은 상태와 업데이트 시각
- 없는 ID, 타인 데이터, DB 장애를 모두 “제출 안 됨”으로 바꾸지 않음
- 예제 데이터는 교육용 합성 데이터

##### 현업 DB 테이블의 구조와 샘플 행 (화면 35)

- `task_id`(PK), `owner_id`, `submission_status`, `updated_at` 구조의 합성 예시
- `task_id` 101·102는 stu-001, 202는 stu-002 소유
- 실제 테이블 이름·타입은 수강생 프로젝트 스키마에 맞게 조정

##### Parameterized SQL로 읽기 전용 조회를 구현합니다 (화면 36)

- 입력을 SQL 문자열로 이어 붙이지 않고 `%s` Placeholder로 값 바인딩
- `WHERE task_id = %s AND owner_id = %s`로 본인 범위 제한
- `DATABASE_URL`은 SELECT만 허용된 전용 계정
- 결과가 없으면 `not_found_or_forbidden` 반환
- 미존재와 권한 밖을 외부에 구분 노출하지 않는 정책도 가능

##### `ToolRuntime`는 서버 인증 정보를 어떻게 전달하나요? (화면 37)

- `ToolRuntime`은 Agent 실행 중 State·Context에 접근하는 LangChain 인터페이스
- `task_id`는 모델이 볼 수 있는 인수
- `runtime`은 Harness가 주입하며 Tool Schema에 신원 필드로 노출되지 않음
- `context_schema`는 Dataclass 등으로 신뢰된 런타임 값 정의
- 로그인하지 않은 요청은 Agent 실행 전에 API에서 거절
- 시연의 `user_id` 드롭다운 변경은 권한 차이 설명용 시뮬레이션

##### `ToolRuntime[UserContext]`로 DB Tool 신원을 고정합니다 (화면 38)

- `UserContext` dataclass에 인증 middleware가 제공한 `user_id` 정의
- 함수 시그니처에서 모델 인수 `task_id`와 주입값 `runtime` 분리
- `task_id < 1`은 `ValueError`로 거부
- 조회는 `runtime.context.user_id`를 owner 조건으로 사용

#### 시연과 실습

##### 시연 · 다른 사용자·과제 ID를 조회해 봅니다 (화면 39)

- 같은 `task_id`라도 인증된 `user_id`에 따라 조회 결과와 권한 판정이 달라지는지 관찰

##### 실습 05 안내 · PostgreSQL Read-only Tool (화면 40)

- 목표는 본인 정보만 조회하고 오류를 명시하는 `lookup_status`
- Basic은 제공 데이터로 `task_id` 101·102 상태 조회 구현
- Intermediate는 Parameterized SQL과 미존재·권한 실패 처리 분리
- Advanced는 ToolRuntime 인증 컨텍스트, SELECT 전용 계정, 권한 회귀 테스트 구성
- `WHERE task_id=%s`만으로는 부족하며 `owner_id` 같은 신뢰된 범위 제한 필요
- 모델이 `user_id`를 지정하게 하지 않음
- Windows 11 PostgreSQL 직접 설치 환경 유지, Docker·WSL 불필요

**핵심:** DB Tool은 미리 작성한 Parameterized SELECT와 서버가 주입한 신원으로 본인 범위만 조회.

### 6교시 · create_agent Integration

#### create_agent 구성과 실행

##### `create_agent`는 무엇을 자동으로 관리하나요? (화면 41)

- Model과 Tools로 Agent 실행 구조를 만들고 Tool Call 요청·실행·결과 재입력·반복 종료 관리
- Model은 Tool Calling 가능한 Chat Model, 이번 과정은 ChatOpenAI
- Tools에 `rag_search`, `lookup_status`를 등록해 Tool Schema 구성
- `system_prompt`로 Tool 사용 시점과 답변 정책 제공
- 권한 검증과 데이터 품질은 대신하지 않으며 Tool 내부 규칙은 개발자 책임

##### 실제 `create_agent()`를 구성합니다 (화면 42)

- `model`, `tools`, `system_prompt`, `context_schema`, `middleware`를 연결
- `context_schema=UserContext`로 ToolRuntime과 연결
- `ToolCallLimitMiddleware(run_limit=4)`로 반복 폭주 제한
- 주석 처리된 Tool import를 프로젝트 실제 경로로 변경
- API Key 인증 필요

##### `agent.invoke()`가 받는 메시지 구조 (화면 43)

- 입력은 `{"messages": [...]}`와 `context=UserContext(user_id=auth_user_id)`
- `auth_user_id`는 로그인 인증에 성공한 FastAPI 서버가 제공
- `result["messages"]`에 Human·AI·Tool 메시지가 누적
- 메시지 타입별로 `tool_calls`, `tool_call_id`, content를 출력해 실행 확인
- 마지막 메시지를 무조건 정답으로 가정하지 않고 결과 검증

#### 복합 요청의 실행 흐름

##### 복합 업무 요청의 실제 메시지 실행 순서 (화면 44)

- “제출 규정 + 내 상태” 요청은 두 Tool이 모두 필요한 사례
- 흐름은 Human → AIMessage(Tool Calls) → Harness 실행 → ToolMessages 2개 → 최종 AIMessage
- 요청 1은 `rag_search(query="과제 제출 규정", category="학사")`
- 요청 2는 `lookup_status(task_id=101)`, `user_id`는 서버가 runtime으로 주입
- 최종 응답은 규정과 현재 상태를 함께 설명하고 실제 확인한 출처만 포함
- 호출 개수·순서·표현은 모델별로 달라질 수 있어 고정 사실로 취급하지 않음

##### VS Code · 파일과 실제 실행 Stage 연결 (화면 45)

- Explorer에서 파일을 고르면 코드, 실행 Stage를 고르면 그 단계의 입력·출력·책임 확인

##### 한 번의 질문에 Tool이 반드시 두 개 호출되나요? (화면 46)

- Agent는 요청과 Tool Description을 바탕으로 Tool을 0개·1개·여러 개 선택
- 일반 인사처럼 외부 데이터가 필요 없으면 0개
- 과제 규정만 물으면 `rag_search` 1개로 충분할 수 있음
- 규정과 현재 상태를 함께 물으면 2개 필요
- DB가 필요한데 RAG만 고르거나 근거 없이 답하면 실패로 평가
- Tool Selection Accuracy와 실제 조회 여부를 Trace로 확인

#### 결과 추출

##### 최종 답변을 추출할 때 놓치기 쉬운 부분 (화면 47)

- Agent result는 문자열이 아니라 messages를 담은 State
- 역순으로 탐색해 `tool_calls`가 없는 AIMessage를 최종 답변으로 선택
- content가 문자열이 아니거나 최종 AIMessage가 없으면 명시적 오류
- 출처 ID 검증·Tool 성공 여부·API 상태 판정은 별도 Validator 담당

#### 시연과 실습

##### 시연 · 단일·복합 질문의 Agent 실행 추적 (화면 48)

- 요청 유형에 따라 AIMessage·ToolMessage 개수와 Tool 선택이 달라지는 교육용 Trace 확인

##### 실습 06 안내 · 단일 Agent에 Tool 2개 등록 (화면 49)

- 목표는 실제 Tool 호출 결과를 포함한 Agent 메시지 실행 로그
- Basic은 `create_agent(tools=[...])` 완성과 Tool 2개 등록
- Intermediate는 0개·1개·2개 Tool 사례 기록과 결과·출처 확인
- Advanced는 파일별 책임 분리·Runtime Context·실행 로그·오류 테스트 추가
- `messages`에 ToolMessage가 없으면 호출을 확인할 수 없으므로 Tool Call·ToolMessage와 서버 로그 대조
- 11/27 개인 프로젝트의 직접적인 기반이 되는 핵심 실습

**핵심:** `create_agent`는 반복을 관리할 뿐이며, Tool 호출 여부는 messages Trace로 확인하고 최종 답변은 따로 검증.

### 7교시 · Reliability & Guardrails

#### 신뢰성 평가 축과 오류 분류

##### Agent Reliability는 무엇을 확인하나요? (화면 50)

- 최종 문장뿐 아니라 올바른 Tool의 안전한 호출, 실패 상태, 운영 비용 관리를 확인
- Tool Selection은 필요한 Tool 호출과 불필요한 남발 여부
- Input Validation은 args 형식과 허용 범위
- Authorization은 인증된 사용자가 허용된 데이터만 읽었는지
- Execution Policy는 오류·지연·과도한 반복 시 중단 가능 여부
- Day28 RAG 평가에 도구 선택·권한·반복 평가 축을 추가

##### Tool 실패를 하나의 오류로 합치면 안 됩니다 (화면 51)

- Schema Error(`task_id=-2`, 잘못된 category)는 인수 오류로 차단·기록
- Authorization(타인 데이터 요청)은 서버에서 403 또는 정책에 따른 비공개 오류
- Not Found는 조회 결과 없음 표시, 추측 금지
- DB/Provider Error(PostgreSQL 연결 실패, LLM 401)는 실행 오류로 분리, 제한된 재시도
- RAG No-answer는 정보 부족 표시와 질문 재확인
- Loop Limit은 중단·로그·요청 축소
- 모델에게 무제한 재시도를 맡기지 않음
- 401 등 인증 실패를 정보 부족 답변으로 위장하지 않음

#### 실행 제한·권한·검증

##### `ToolCallLimitMiddleware`로 실행 상한을 적용합니다 (화면 52)

- 반복 호출에 상한을 두어 비용 폭주·무한 반복 위험 감소
- `run_limit`은 한 Agent 실행에서 허용할 Tool 호출 수
- `tool_name`을 지정하면 Tool별 상한 적용. 예: `lookup_status`는 2회
- `exit_behavior`로 한도 초과 시 error/continue 등 처리 정책 선택
- Agent 전체 종료 시간·LLM 호출 한도는 별도 정책으로 관리

##### 권한은 Prompt가 아니라 서버에서 검증합니다 (화면 53)

- “타인 정보를 보지 마세요” 지시만으로 권한 제어가 완성되지 않음
- 사용자·모델·문서 내용은 서버 인증 결과와 분리된 비신뢰 영역
- DB는 `owner_id=auth_user_id`를 SQL WHERE에 적용
- RAG는 조회 가능한 Category·권한을 Retriever 이전·실행 단계에서 제한
- 검증 실패·도구 요청·조회 범위·결과 상태를 보안 정책에 맞게 Audit 기록
- Prompt Injection·Guardrails는 12/1에 추가로 다룸

##### Tool 결과를 검증하는 서버 측 Validator (화면 54)

- Tool 성공 여부와 근거 출처를 분리해 검증
- Citation은 모델이 제시한 ID가 아니라 서버가 보관한 `verified_source_ids` 기준으로 대조
- `answered`는 출처 누락·중복 ID·검증 Context 밖 인용을 오류 처리
- `insufficient_context`는 출처를 가지면 오류
- DB Tool 상태(`ok`, `not_found_or_forbidden`, `not_found`)도 계약에 맞는지 검사
- 출처 ID가 일치해도 Faithfulness는 별도로 검사

#### 기록과 회귀 테스트

##### Trace와 Audit Log는 무엇이 다른가요? (화면 55)

- Trace는 단계별 실행 재현용 개발 기록, AIMessage·Tool Call·ToolMessage·Latency 관측
- Audit Log는 누가 어떤 접근을 시도했는지 남기는 보안·운영 기록
- Audit에는 익명화된 actor_id, tool_name, 입력 검증 결과, 권한 결정, request_id 기록
- 원문 문서·로그인 토큰·API Key는 Trace에 그대로 남기지 않음
- 필요한 필드만 최소로 남기고 저장 기간·접근 권한 통제

##### 시연 · 오류·권한·반복 상한을 적용해 봅니다 (화면 56)

- 실패 유형과 최대 호출 수를 바꿔 Tool 실행 차단 시점과 반환 상태 확인

##### 11월 27일에 필요한 최소 회귀 테스트 (화면 57)

- 정상 RAG는 검증된 출처가 있는 답변
- 정상 DB는 내 `task_id=101`의 기록된 상태 반환
- 복합 요청은 규정과 제출 상태가 모두 답변에 포함
- 타인 과제(`owner_id` 불일치)는 권한 밖 결과 미노출
- 잘못된 인수(`task_id=-1`)는 Schema/Validation 오류
- 서비스 실패(DB Down, Model 401)는 실행 오류와 진단 기록
- 반복 폭주는 Tool Call 상한 초과 시 정책에 따른 중단
- HTML 시연은 합성 Fixture로 검증하며 실제 DB·LLM 테스트는 별도 인프라 필요

#### 실습

##### 실습 07 안내 · Agent Reliability 테스트 (화면 58)

- 목표는 정상·실패가 구분되는 검증 표와 실행 기록
- Basic은 정상 Tool 호출·No-answer·DB 오류 세 사례 구분
- Intermediate는 잘못된 인수·타인 조회·반복 상한 테스트 추가
- Advanced는 오류 정책·감사 기록·민감정보 마스킹·회귀 테스트 분리
- DB 인증 실패를 RAG 근거 부족으로 바꿔 반환하지 않음
- Prompt만으로 타인 조회를 막을 수 없으며 서버·DB 권한 검증 필수
- 전체 Guardrails 프레임워크 구현은 범위 밖, 목표는 개인 프로젝트에 필요한 안전 경계

**핵심:** 오류는 원인별로 분리하고, 권한·호출 상한·출처 검증은 Prompt가 아닌 서버 코드로 강제.

### 8교시 · End-to-End & Project Bridge

#### API 통합과 데이터 계약

##### 최종 아키텍처 · FastAPI에서 Agent까지 (화면 59)

- 흐름은 Client → FastAPI(Auth·Schema) → Agent → RAG/DB → Validator → JSON Response
- 기존 FastAPI·RAG·PostgreSQL에 Agent 실행 계층만 추가
- 오늘은 두 Tool 실행 결과를 콘솔 Trace로 확인
- 11/27 개인 프로젝트에서 FastAPI 연결과 요청·응답·오류 계약 마무리
- 이후 11/30 LangGraph State, 12/01 Security, 12/02 MCP로 확장

##### FastAPI에서 신뢰된 Context를 Agent에 전달합니다 (화면 60)

- 인증된 사용자 ID는 요청 본문이 아니라 서버 인증 계층(`Depends`)의 결과로 전달
- `AgentRequest`는 `question` 길이 1~500 검증
- `get_authenticated_user_id`는 프로젝트의 JWT/Session 검증으로 교체할 자리
- `agent.invoke(..., context=UserContext(user_id=user_id))`로 신원 주입
- 최종 메시지·출처·오류 계약을 서버에서 검증한 뒤 반환
- 인증 Dependency와 출처 Validation을 채우기 전에는 배포하지 않음

##### 개인 프로젝트 전에 확인할 전체 데이터 계약 (화면 61)

- Request의 `question`은 사용자 입력, `user_id`는 인증된 서버 값
- Tool Calling은 `AIMessage.tool_calls` → Python Tool → ToolMessage로 실제 호출 확인
- RAG는 답변·출처·정보 부족·시스템 오류 구분
- DB는 본인 제출 상태·미조회·권한·DB 오류 구분
- 인수인계 시 Tool Name, Args Schema, Output Schema, 오류 코드, 처리시간, 담당자를 표로 정리
- 최종 자연어 응답은 인증·권한·실행 Tool·출처 검증을 거친 뒤 반환

#### 개인 프로젝트 기준

##### 11월 27일 개인 프로젝트의 최소 완료 기준 (화면 62)

- Agent 1개는 `create_agent` 구성과 실제 invoke
- Tool 2개는 `rag_search` + `lookup_status`
- 기존 RAG는 E5·pgvector·GPU Reranker 연결
- PostgreSQL은 인증된 사용자 범위 SELECT
- FastAPI는 Agent 요청·응답 API
- 실행 기록은 질문별 Tool Call·ToolMessage
- 평가·안전은 정상/권한/오류 테스트
- 멀티 Agent·MCP·LangGraph 직접 구현은 11/27 필수 아님

##### 네 직무의 기술이 하나의 Agent 서비스에서 만납니다 (화면 63)

- 주요 학습 목표는 Agent Platform Engineer
- Data Analysis는 문서·메타데이터·평가 Dataset 준비
- AI Core는 E5·Reranker·LLM 품질과 CUDA 실행
- Agent Platform은 Tool 계약·실행 Loop·API·오류·출처 통합
- Infra는 DB·API·GPU·인증·배포 환경·운영 기록 관리
- 개인 프로젝트에서는 새 프레임워크보다 기학습 코드 연결 우선

#### 시연과 실습

##### 시연 · 내일 완성할 Agent API 전체 요청 (화면 64)

- 질문·인증 사용자·DB 장애 상태를 바꿔 Tool 실행 결과와 API 상태 변화 확인

##### 실습 08 안내 · Agent End-to-End·개인 프로젝트 준비 (화면 65)

- 목표는 작동하는 Agent 흐름, 요청/응답, 오류 점검 체크리스트
- Basic은 콘솔에서 두 Tool을 연결하고 실제 호출 결과 확인
- Intermediate는 FastAPI 요청·응답과 No-answer·미조회 결과 분리
- Advanced는 인증된 Runtime·오류·Audit Log·통합 테스트·응답 계약 구현
- 필수 목표는 단일 Agent와 실제 Tool 2개, MCP·Multi-Agent는 필수 아님

**핵심:** 인증된 신원을 서버에서 주입하고 Tool 결과와 출처를 검증한 뒤에만 Agent 응답을 API로 반환.
