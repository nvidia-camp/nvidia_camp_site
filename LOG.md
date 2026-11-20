# 진행 기록

작업 단위마다 한 줄. 페이지별 자세한 기록은 각 폴더의 `DESIGN.md`.

| 날짜 | 페이지 | 한 일 | 상태 |
|---|---|---|---|
| 2026-11-09 | vision/all | Day13~16 4일 종합 HTML·PDF 제작 | 완료 |
| 2026-11-09 | ml/all, dl/all | 4일 종합 기획안(구성안.md) 작성 | 확인 대기 |
| 2026-11-09 | (전체) | 요약 산출물을 nvidia_camp에서 site/pages로 이전, 날짜 폴더(YYYYMMDD)로 정리, 요약 PDF 포함 | 완료 |
| 2026-11-09 | 홈 | 과정 전체 일정 띠, 과목별 날짜 카드, 문제 풀이 링크(SWEA·프로그래머스)로 홈 개편. 미리보기 이미지는 넣었다가 뺐다 | 완료 |
| 2026-11-09 | (전체) | 일정 기준을 학습 자료 시트로 변경(lectures.json), 강의 자료 링크 연결, Sequence 개념지도를 20261102-2(Day11-2)로 이동 | 완료 |
| 2026-11-09 | 홈 치트시트 | scikit-learn·PyTorch·OpenCV 공식 로고와 용도 표시, 카드 전체 링크·모바일 세로 배치. 로고는 HTML에 포함 | 완료 |
| 2026-11-09 | 홈 머리말 | 사용자 제공 새싹·NVIDIA 로고를 제목 위에 배치하고 새싹 부트캠프 표시 추가. 375·768·1280px·다크 모드 검증 | 완료 |
| 2026-11-10 | (전체) | Vercel Web Analytics 켜고 모든 페이지에 분석 스크립트 추가(build_site.py) | 배포 대기 |
| 2026-11-10 | llm/20261110 | Day17 구성안 확정: 실습 01~05 순서의 0~11단계, 코드는 실습 07 뼈대를 공식 문서 모양으로, 06은 설명 틀, 08은 제외 | 확정 |
| 2026-11-10 | llm/20261110 | FastAPI 튜토리얼 페이지 0~11단계 완성: PUT·DELETE·재시작 추가, 코드 교체(storage.py 분리), 실제 서버·/docs 재캡처 | 배포 |
| 2026-11-10 | llm/20261110 | FastAPI 튜토리얼에 웹 기초 세 장(API·HTTP 요청·응답·URL) 추가, 상태코드 앞자리 읽기 한 줄 추가 | 배포 |
| 2026-11-10 | llm/20261110 | FastAPI 튜토리얼: 교시 묶음에 Method 표기·단계 이름을 개념으로 통일(Update, 204 No Content), 웹 기초에 REST 카드 추가, 웹 기초 네 장을 세로 스크롤로 | 배포 |
| 2026-11-10 | llm/20261110 | FastAPI 튜토리얼: 웹 기초 네 칸을 "0 웹 기초" 한 칸으로 합치고 아래로 이어 보기 | 배포 |
| 2026-11-10 | llm/20261111 | Day18 Windows PostgreSQL 18·pgAdmin 4 설치 가이드 (설치 마법사 화면별 할 일, Query Tool 설정, 접속 확인, 문제 해결). 1280·375px·다크 모드 확인 | 배포 |
| 2026-11-10 | llm/20261111 | Day18 설치 가이드에 비밀번호 정하기(영문+숫자 8자 이상, 특수문자 제외, 한/영 확인)와 나중에 바꾸기(ALTER USER) 추가 | main만 (배포 전) |
| 2026-11-10 | (deploy) | Day18 설치 가이드가 deploy에 잘못 올라가 deploy를 8c1aaa8로 되돌림(강제 push). 공개 사이트는 가이드 추가 전 상태 | 완료 |
| 2026-11-10 | setup/postgresql | 설치 가이드를 llm/20261111에서 새 섹션 setup/postgresql로 이동. 홈에 '설치 가이드' 섹션, SETUP 공개 여부·--release 빌드 추가. 다운로드 첫 화면·19 버전 안내 반영 | main만 (미공개) |
| 2026-11-10 | setup/postgresql | Windows 실제 설치 사진(Slack 스레드) 기준 수정: 기존 설치 확인·psql 단계 제거(psql은 별도 페이지 예정), pgAdmin 접속·Query Tool에 사진 4장(비밀번호 칸 가림), Master Password·자동 설정은 확인만, Stack Builder 해제 강조, Locale DEFAULT, 확인 SQL 한 줄로 | main만 (미공개) |
| 2026-11-10 | (홈) | 치트시트·설치 가이드 섹션을 없애고 관련 과목 블록 아래 '참고' 한 줄(글자 링크)로 이동. 미공개 표시 제거(공개 구분은 브랜치로) | main만 |
| 2026-11-10 | (홈) | 참고 줄을 공식 로고가 든 작은 칩으로 (너무 안 보인다는 피드백). PostgreSQL 로고 추가 | main만 |
| 2026-11-10 | llm/20261111 | Day18 요약 페이지 틀: 제목·목표·표 2개·오늘의 흐름 01~08(준비 중). 홈 LLM·RAG에 Day18 카드 생김 | main만 |
| 2026-11-10 | (홈) | 과목 제목을 짧은 이름(ML·DL·Vision·LLM·RAG)으로, 전체 과목명은 마우스를 올리면 보이게. 참고 줄 위치는 과목 아래 유지(사용자 선택) | main만 |
| 2026-11-10 | setup/postgresql | "설치하며 정하는 값" 섹션 삭제(기본값 4칸은 입력할 일 없음). 비밀번호 안내는 마법사 Password 줄 한 줄로, 잊었을 때 안내는 막혔을 때 표로 | main만 (미공개) |
| 2026-11-10 | setup/postgresql · llm/20261111 · (홈) | 사용자 요청으로 배포: 설치 가이드 공개 전환, Day18 틀, 참고 칩, 짧은 과목 제목 | 배포 |
| 2026-11-10 | setup/postgresql · setup/psql | 5단계를 사용자 사진 기준으로(두 줄 SQL, 마지막 결과만 보임 안내 + 결과 사진), 15분 문구 삭제. psql 접속 가이드 새 페이지(사진 3장), 두 페이지 서로 링크(data-site) | main만 |
| 2026-11-10 | setup/psql · setup/postgresql | 사용자 요청으로 배포: psql 접속 가이드, 5단계 실제 화면 기준 수정 | 배포 |
| 2026-11-10 | setup/postgresql | 1단계(설치 파일 내려받기)에 EDB 다운로드 표 사진 1장 (18.x 줄 × Windows x86-64 표시) | main만 |
| 2026-11-10 | setup/postgresql | 6단계 "실습 SQL 파일 열기" 추가(Open File·파일 선택·열린 화면 사진 3장, mentor 경로·개인 폴더는 잘라냄). 여기까지만 안내를 6단계 끝으로. 1단계 다운로드 사진과 함께 배포 | 배포 |
| 2026-11-11 | setup/postgresql | 설치·psql 가이드를 'PostgreSQL 가이드' 하나로 묶음: 1 셋업 · 2 pgAdmin 사용법(새 페이지: 서비스 세 층 속 위치, 접속 다섯 값, 화면 구성 그림, knowledge_lab Query Tool, 실행·결과 읽기, 표·구조 보기) · 3 psql(setup/psql에서 이동, knowledge_lab 접속·\dt·\d·SQL 실행·명령 모음 추가, 출력은 임시 서버 실측). 페이지 탭, SETUP_PAGES, 옛 /setup/psql/ 리디렉션. 1280·375px·다크 확인 | 배포 |
| 2026-11-11 | llm/20261111 | Day18 요약 초안: 같은 두 테이블을 카드마다 다시 그려 SQL이 고르고 바꾸는 칸을 표시(조회 4·변경 3·CREATE TABLE·트랜잭션), 큰 그림 지도·종합·더 알아보기. 결과는 capture.py로 S0에서 실측(PostgreSQL 17.10). 1280·375px·다크 확인 | main만 |
| 2026-11-11 | llm/20261111 | 묶음 이름을 공식 용어로: 조회 Queries · 데이터 조작 DML · 데이터 정의 DDL · 트랜잭션 Transaction ("변경" 제거). 사용자 요청으로 배포 | 배포 |
| 2026-11-11 | llm/20261112 · 20261112-2 | Day19를 오전·오후 두 문서로: lectures.json에서 19 → 19-1·19-2 (시트 반영 전 임시). 19-1 오전 실습 가이드(큰 그림 세 실습, 폴더 지도, 파일 관계, 실습 1·2A·2B 진행과 실측 결과, U01·U02 비교, 자주 막히는 곳, 오후 대응표, basic 기준·정답 없음). 19-2 오후 틀(Before/After, PM01~05 준비 중). 1280·375px 확인 | main만 |
| 2026-11-11 | llm/20261112 | 피드백 반영: 제목 "FastAPI · PostgreSQL 실습"으로 줄임, basic 기준 강조 박스, 파일 역할 이름을 문제·참고·실행·제공으로, 파일 관계를 mermaid 그래프 3개(diagrams/, mmdc로 SVG), 실습마다 "생각해 볼 점"과 "이런 화면이 나오면 됩니다"(pgAdmin은 강사 Slack 사진 12장, /docs는 실제 실행 캡처 7장, 원래 크기로), 정답 코드는 접어서 제공. 자주 막히는 곳·오후 대응표 제거. template.html + build.py로 이미지 인라인. 1280·375px 확인 | main만 |
| 2026-11-11 | llm/20261112 | 정답 코드 접기 3곳을 "예시 · 한 문제 풀어 보기"(API-01 · DDL-02 · R01: 받은 코드 → 푼 코드 → 푸는 순서)로 바꿈. 문제 표를 이해 중심으로: FastAPI는 함수·쓸 수 있는 변수·할 일, SQL은 빈칸 모양(▢)·채울 것. 1280·375px 확인 | main만 |
| 2026-11-11 | llm/20261112 | 예시를 실습마다 두 문제로(API-01·02, DDL-01·02, R01·C01) + "이제 직접" 안내. 폴더 지도·파일 관계에 수준 탭(basic·응용·심화, 두 섹션 함께 전환): 응용·심화 파일 역할·문제 수·DB 이름, mermaid 그래프 6개 추가. 그 아래는 basic 기준임을 표시. 1280·375px·탭 전환 확인 | main만 |
| 2026-11-11 | llm/20261112 | 수준 이름을 영어로 통일: 탭 basic · intermediate · advanced, 패널 설명·그래프 제목·안내문도 같은 표기 | main만 |
| 2026-11-11 | llm/20261112 · 20261112-2 | 사용자 요청으로 배포 (main:deploy fast-forward, 28fd3fd). 시트의 Day19는 아직 한 줄: lectures.json 19-1·19-2 분리는 시트 반영 전 임시 | 배포 |
| 2026-11-12 | llm/20261112-2 | Day19-2 오후 FastAPI–PostgreSQL 연동 페이지: 큰 그림(오전·오후 비교, 요청 하나가 DB 행이 되는 7단계를 실제 값으로, 처음 나오는 이름 넷), 연결·CRUD·트랜잭션·Migration 15단계(뜻·코드·실제 결과·핵심), 종합(A·B·C, 재시작 뒤 N+2). code/app = basic 완성본 축약, capture.py가 이 코드를 PostgreSQL 17.10에 연결해 실측(/docs POST 화면 포함). 1280·768·375px·다크 확인 | main만 |
| 2026-11-12 | llm/20261112-2 | 연결을 도식화: 큰 그림의 7줄 목록·이름 카드 넷을 "연결 지도"(/docs → FastAPI → ORM Model → Session → Engine·Psycopg → PostgreSQL 여섯 층, 왼쪽 내려가는 요청·오른쪽 올라오는 응답을 실제 값으로, 층마다 파일·단계 링크)와 "파일 연결"(.env → settings.py → db.py → main.py)로 바꿈. 단계 카드마다 "지금 여기" 띠(그 단계가 다루는 층 표시). 1280·768·375px·다크 확인 | main만 |
| 2026-11-12 | llm/20261112-2 | 텍스트 줄임: 카드마다 뜻·핵심을 맨 위 핵심 한 줄로 합침, 오전·오후 표 → 한 문장, 단계 목록·구역 설명 제거, 2단계 코드 주석(표와 중복) 제거, 12단계 응답 JSON 3개 → 요청 표, 14단계 열 목록 → 새 열 한 줄. 1280px 높이 13,440 → 11,511 | main만 |
| 2026-11-12 | llm/20261112-2 | 4단계에 "같은 요청을 Postman으로" 수업 중 실제 화면(사용자 제공 캡처, 워크스페이스 이름·AI 패널을 잘라 냄, img/postman_list.webp) + 연결 지도 /docs 칸에 "/docs 대신 Postman 같은 도구로 보내도 된다" | main만 |
| 2026-11-12 | llm/20261112-2 | 구역 구분·카드 단순화: 구역 머리를 번호·이름·단계 링크가 든 남색 띠로(종합 포함), 카드의 "지금 여기" 띠 → 제목 옆 층 태그(다루는 층만), "코드/실제 결과" 이름표 제거, 1·3·4·7·8·14단계 코드는 핵심 줄만 보이고 "전체 코드 보기"로 접음, 표 제목·부가 줄 줄임. 1280px 높이 12,353 → 11,414 | main만 |
| 2026-11-12 | llm/20261112-2 | Postman을 4단계에서 빼고 큰 그림에 "/docs와 Postman" 비교 칸(id client): /docs 경로 목록(capture.py로 새로 캡처) ↔ Postman Collection 목록(사용자 캡처에서 목록만 잘라 냄) + 3줄 대조표, 연결 지도 /docs 칸에서 링크. "전체 코드 보기" 수정: 코드 창이 오른쪽 표를 덮던 문제(칸 격자 minmax(0,1fr)), 펼치면 핵심 줄 창을 숨기고 "핵심 줄만 보기"로 | main만 |
| 2026-11-12 | llm/20261112-2 | 사용자 요청으로 종합 구역(일일프로젝트 A·B·C 표와 네 줄 정리) 삭제 | main만 |
| 2026-11-12 | llm/20261112-2 | 단계 제목을 "개념 이름 · 확인하는 것"으로(4~6·8~15단계), 11단계를 트랜잭션 원자성으로 다시 씀(제목·핵심·실험 표 3칸), "전체 코드 보기" 제거(핵심 줄 + …만). 사용자 요청으로 배포 | 배포 |
| 2026-11-12 | llm/20261112 · 20261112/practice | Day19를 한 날로: lectures.json 19-1·19-2(임시 분리) → 시트와 같은 19 한 줄. 오후 연동 요약을 Day19 대표 페이지 /llm/20261112/로, 오전 실습 가이드를 하위 페이지 /llm/20261112/practice/로 옮김(build_site.py DAY_SUBPAGES: 홈 카드 링크 + 상단 경로 Day19 › 오전 실습 가이드). /llm/20261112-2/ → /llm/20261112/ redirect. 사용자 요청으로 바로 배포 | 배포 |
| 2026-11-13 | llm/20261113 | Day20 LLM·Transformer 하루 통합 뷰 main 초안: 큰 그림(날짜 띠, 시스템 속 LLM 위치·AI 용어 관계), 통합 뷰(문장→Token→ID→Embedding→Block×N→Logit→Softmax 흐름 + 반복 고리, Transformer 확대 사다리 모델→Block→Self-Attention→t3 행 계산, 학습·추론 두 갈래, 이름 8개), 세부 6구역 22카드(입력·표현·Block·Attention·출력·바깥, 머리 띠에 위치 표시), 헷갈리기 쉬운 짝 12개, 더 알아보기. 숫자는 슬라이드 코드(p.29·34·43·45·54·62·74)를 capture.py로 실행한 값, build.py가 p.8·63·74 값과 대조. 1280·375px·다크 확인 | main만 |
| 2026-11-13 | llm/20261113 | 피드백 반영 3차: 강사 강조 2교시(Tokenizer·Token ID·Context Window)·7교시(모델 한계·검증·RAG/Agent 경계)를 양 끝에 크게, 3~6교시는 한 덩어리(흐름·Block·Causal Attention 행렬·Logit·학습/추론)로 압축. 첫 화면에 "오늘의 구조" 세 칸. 구역 이름은 p.15 교시 제목 원문, 그림 제목·강조 문장은 슬라이드 원문. 헷갈리기 쉬운 짝·지어낸 구역 이름·코드 상자·중복 그림 삭제, 줄인 내용은 더 알아보기 한 줄씩. 1280px 높이 13,867 → 6,191. 1280·375px·다크 확인 | main만 |
| 2026-11-13 | llm/20261113 | 4차: 그림 세 장으로 다시 그림. 그림 1 시스템 지도 SVG(애플리케이션 경계, 화살표 이름, 날짜 배지, 하려는 일 3경로 버튼, 틀어질 수 있는 곳 핀 1~4) · 그림 2 Context Window 상자(다섯 칸·출처·넘친 Token·실제 Token 17개·PAD/mask) · 그림 3 LLM 안 SVG(Block 펼침, Attention 3×3 실측, Softmax 막대, 반복 고리, 학습 갈래, 좁은 화면용 세로 SVG) · 답 검사 표. 날짜 띠·오늘의 구조 3칸·PDF 원문 문장 삭제, 문장 새로 씀(humanize-scan C-8·I-4·C-11·F-5 0). 1280px 높이 6,191 → 3,661. 1280·375px·다크 확인 | main만 |
| 2026-11-13 | llm/20261113 | 그림 1 시스템 지도에서 LLM을 가운데로: 세 경로(요약·RAG·Agent)가 모두 LLM을 거치게, Agent ⇄ LLM ⇄ Tool 결과를 LLM 옆 순환으로, LLM은 점선 고리와 "모델 · 외부 API로 호출"로 애플리케이션과 구분, 권한 확인은 Agent와 Tool API 사이에 유지. 전체·Agent 경로 설명 문장 수정. 1280px 확인, Agent 경로 버튼 동작 확인 | main만 |
| 2026-11-13 | llm/20261113 | 그림 3 Embedding 추가(그림 4로 LLM 안을 밈): 왼쪽 Token Embedding(9489번 행 → 벡터, 17개 Token → (17, D), 그림 4로), 오른쪽 Sentence Embedding(질문 "실습 파일은 어디에 두나요?"와 일일프로젝트 문서 A·B·C를 multilingual-e5-small로 실측: A 0.906 · C 0.802 · B 0.794, 질문과의 각도 그림 + 순위). 지도의 벡터 인덱스·Retriever에서 그림 3으로 링크, 그림 2 → 3 → 4 연결 문장, 그림 4 Attention에 t3 → [0.75, 0.75] 결과 추가. capture.py에 e5 측정 추가. AI 문체 신호 0. 1280·375px 확인 | main만 |
| 2026-11-13 | llm/20261113 | 그림 1 지도에 Embedding 모델 상자 추가(벡터 인덱스와 구분): PostgreSQL → Chunk → Embedding 모델 → Chunk 벡터 → 벡터 인덱스, Context 조립 → 질문 → Embedding 모델 → 질문 벡터 → Retriever ⇄ 벡터 인덱스(검색) → 문서 발췌 → Context 조립. "그림 3" 링크를 벡터 인덱스에서 Embedding 모델로 옮김, RAG 경로 설명·그림 3 문장 보강. RAG 경로 버튼 확인 | main만 |
| 2026-11-13 | llm/20261113 | 사용자 요청으로 배포 (main:deploy fast-forward, 359ceb3). 라이브 /llm/20261113/ 200·새 지도 반영 확인, 홈 카드 링크 확인 | 배포 |
| 2026-11-14 | setup/opencode · setup/opencode/usage · setup/cli · 홈 | 과정 공통 가이드 신설: 홈 헤더 아래 "공통 가이드" 섹션(묶음 COMMON_GROUPS: 개발 환경·AI 코딩, 묶음마다 한 줄, 보일 가이드가 없으면 섹션도 없음). SETUP의 과목 자리에 묶음 이름을 적으면 이 섹션으로 감. OpenCode 가이드 2쪽(설치 한 페이지: 한눈에·연결 구조·AI 에이전트에게 맡기기·직접 할 3곳·막히면·체크 / 사용법: 꼭 지킬 5가지·화면 읽기·명령·Plan→Build·AGENTS.md·요청 요령·승인 창)과 CLI 도구 1쪽(기본 묶음 5종·gh 로그인·선택 도구·AGENTS.md). 원자료 nvidia_camp/docs/opencode-local-ai, SETUP_FOR_AI.md는 사진 줄·내부 경로를 뺀 사본을 내려받기로 둠(FILES 등록, 원본 바꾸면 다시 복사). 캡처 4장(Ollama 경로의 사용자 이름 가림). 공개 여부 False라 --release 빌드에선 섹션째 빠짐. 1280·375px·다크, 링크 확인 | main만 |
| 2026-11-14 | setup/local-ai · setup/local-ai/usage · setup/cli | 피드백 반영: 중심을 OpenCode → 로컬 AI로. 가이드 이름 "로컬 AI 코딩", 경로 /setup/opencode/ → /setup/local-ai/ (공개 전이라 redirect 없음), 홈 칩 로고 Ollama. 설치 페이지를 직접 따라 하는 설명서로 다시 씀: 0 PowerShell·사양 확인 → 1 Node.js(.msi 마법사 화면별 할 일, winget은 접음) → 2 Ollama → 3 64k·KEEP_ALIVE·재시작 → 4 pull·run·ps 확인표 → 5 OpenCode(npm, 실행 정책) → 6 메모장으로 opencode.jsonc·AGENTS.md → 7 실행·첫 작업, 단계 바로 가기 줄, AI 에이전트에게 맡기기는 맨 아래 한 칸. 캡처 10장(Node.js·Ollama 다운로드, pull, run/ps, 버전, 클라우드 모델 추가). 사용법 맨 위에 "모델과 바로 대화하기"(ollama run·ps·stop). 아직 캡처 없음: Node.js 마법사, PowerShell 열기, node -v 결과, 메모장 저장. 1280·375px·다크, 링크 확인 | main만 |
| 2026-11-14 | setup/local-ai · setup/cli | 2차 피드백: 0단계(사양 확인) 삭제(수업 노트북 동일 사양), 미검증인 메모장 설정 파일 단계 삭제 → 6단계는 /models로 gpt-oss:20b 고르기를 기본 경로로(검증 캡처). "AI 에이전트에게 맡기기"를 맨 위로, 아래 "직접 설치하기" 1~6. 사용법 탭은 빼서 새 가이드 "AI 코딩 도구"(OpenCode·Claude Code·Codex·agy)로 옮길 예정, /setup/local-ai/usage/ 삭제. SETUP_FOR_AI.md 5단계(설정 파일)는 그대로 둠 | main만 |
| 2026-11-14 | setup/ai-coding (+opencode·claude-code·codex·agy) | 새 공통 가이드 "AI 코딩 도구 사용법" main 초안: 0 공통(네 도구 비교, 어떤 도구든 지킬 5가지, 같은 일 다른 이름 표, 요청 요령, AGENTS.md 하나로 같이 쓰기) · 1 OpenCode(로컬 AI 중심: ollama run·ps·stop, 로컬 모델이라 더 지킬 5가지, 화면 읽기, 명령, Plan→Build) · 2 Claude Code · 3 Codex · 4 agy(각각 설치·로그인·명령·권한 모드·안내문 파일). 클라우드 셋은 공식 문서(code.claude.com, developers.openai.com/codex → learn.chatgpt.com, antigravity.google/docs) 2026-11-14 확인 기준, 강사 PC 실행 확인 전. 홈 AI 코딩 줄: 로컬 AI 코딩 · AI 코딩 도구 · CLI 도구 | main만 |
| 2026-11-14 | setup/local-ai · setup/ai-coding · setup/cli | 문장 다듬기: humanize-korean(imnotai.kr 엔진, 로컬 실행) standard 경로로 192개 문장 덩어리 진단·윤문 → 게이트 수렴(문자율 1.8%, golden PASS, 서법 소실 0) → 코드·키·링크·태그가 그대로인 36곳만 반영. 단문 나열 연결, 지시/사실 종결 구분, 무생물 주어("창은 설치된 것을 모릅니다") 정리. CLI 페이지의 없어진 "설치 6-1 설정" 언급 바로잡음. 1시간 유지 보강: 한눈에 보기 "Ollama 설정 두 가지", 3단계 제목·바로 가기, 수업 전 체크(59 minutes), OpenCode 탭 한 줄 | main만 |
| 2026-11-14 | setup/local-ai | "수업 전 체크" 칸 삭제(사용자 요청) | main만 |
| 2026-11-14 | setup/ai-coding | 탭 번호 대신 도구 로고(흰 원 받침): 공통 code.svg · OpenCode 브랜드 페이지 · Claude Code 문서 사이트 파비콘 · OpenAI 개발자 문서 파비콘 · Antigravity 공식 로고. 출처는 assets/logos/README.md | main만 |
| 2026-11-14 | setup/ai-coding | 도구 탭 맨 아래 "이전 · 다음" 줄 삭제(위 탭으로 이동) | main만 |
| 2026-11-14 | 홈 | 맨 위 브랜드 영역을 한 줄 브랜드 바로: 로고 상자 없앰, SeSAC │ NVIDIA 로고 36px + "새싹 부트캠프 · AI 코어 엔지니어 2기", 제목 바로 위에 붙임. 다크 모드에서만 로고 뒤 흰 받침 | main만 |
| 2026-11-14 | 홈 · setup/ai-coding | 참고·공통 가이드 칩의 안쪽 로고 상자 삭제(이중 테두리 없앰): 로고 24px을 칩 안에 바로, 다크 모드에서만 회사 로고 뒤 흰 받침. 직접 그린 code·terminal 아이콘은 두 테마에서 보이는 #4B74A6로 바꾸고 받침 없음 | main만 |
| 2026-11-14 | 홈 | 브랜드 줄 문구 "새싹 부트캠프" → "청년취업사관학교 · AI 코어 엔지니어 2기", DESIGN.md 홈 브랜드 규칙도 새 모양으로 갱신 | main만 |
| 2026-11-14 | 홈 · 모든 페이지 상단 메뉴 | 사이트 이름 "AI 코어 엔지니어 학습 노트" → "학습 아카이브"(홈 제목·브라우저 탭·상단 메뉴 "← 학습 아카이브"). SWEA·프로그래머스 링크에 공식 아이콘(assets/logos/swea.png·programmers.png, 출처 README). Day 페이지 본문의 "새싹 학습 노트" 배지는 PDF와 짝이라 그대로 | main만 |
| 2026-11-14 | 홈 · 과목 목록 | 홈 디자인 개편(로컬 비교 시안 A+ 블루 채택, site/_work/compare): 최근 수업 번호 목록 + "지금 과목" 남색 표지 카드, 100일 일정 선 정리, 참고 문서 모음(개발 환경 · AI 코딩 · 과목 참고 문서 — 과목별 "참고" 칩 줄은 여기로 모음), 과목 = 챕터(번호 · Day 범위 · 요약 수, Day 목록 + PDF·강의 자료 버튼). 포인트 색 #2F66DE, Pretendard(OFL dynamic subset, public/fonts로 복사). --release에서 비공개 가이드 칸은 숨김. 1280·375px, 라이트·다크, 링크 확인 | main만 |
| 2026-11-14 | 홈 | 참고 문서 모음 작게(칸 여백 14·18px, 글자 14px, 로고 18px), 첫 칸 왼쪽으로 삐져나온 세로선과 모음 바로 아래 첫 챕터 윗선 제거. 과목 챕터 왼쪽 열에 그 과목 참고 문서 링크 다시 표시(LLM·RAG → PostgreSQL 가이드, Vision → OpenCV, DL → PyTorch, ML → scikit-learn). 1280·375px, 라이트·다크 확인 | main만 |
| 2026-11-14 | 홈 · 과목 목록 | Day 이름을 짧은 주제 이름으로(SHORT_TITLES: 학습 안정화 기법 · CNN 입문 · RNN·LSTM·Transformer · OpenCV 이미지 전처리 · 전이학습 이미지 분류 · YOLO 객체 탐지 · OCR·VLM 문서 AI · Vision 4일 종합 · FastAPI 입문 · PostgreSQL·SQL 기초 · FastAPI·PostgreSQL 연동). 요약 페이지 안 제목은 그대로. 과목 범위 Day9–11-2 → Day9–11. ML·Python도 챕터로 펼쳐 Day별 "요약 준비 중" + 강의 자료 버튼 | main만 |
| 2026-11-14 | 홈 · 과목 목록 | 요약이 있는 과목도 지난 날 중 요약이 없는 Day를 "요약 준비 중" 줄로 표시(DL Day9 누락 수정) | main만 |
| 2026-11-14 | dl · vision · llm 요약 12쪽 | 페이지 안 <h1>을 홈의 짧은 이름과 같게(학습 안정화 기법 · CNN 입문 · RNN·LSTM·Transformer · OpenCV 이미지 전처리 · 전이학습 이미지 분류 · YOLO 객체 탐지 · OCR·VLM 문서 AI · Vision 4일 종합 · FastAPI 입문 · PostgreSQL·SQL 기초 · FastAPI·PostgreSQL 연동 · LLM·Transformer), <title>은 "DayNN · 이름". template.html·build.py(Day19)도 함께. build_site.py의 SHORT_TITLES 표는 없애고 페이지 <h1>을 유일한 원본으로. 홈 이름 ↔ 페이지 h1 12개 일치 확인. PDF는 아직 옛 제목 | main만 |
| 2026-11-14 | dl · vision · llm 요약 11쪽 · 홈 | 강의 목차(Day*_강의구조_핵심설명.md 교시 제목)를 보고 제목을 장 제목처럼 다시 지음: DL 신경망 학습 기초(Day9, 요약 없음)→최적화와 규제→CNN→Sequence 모델, Vision 이미지 전처리→이미지 분류→객체 탐지와 추적→문서 AI (OCR · VLM), LLM·RAG REST API (FastAPI)→SQL (PostgreSQL)→API와 DB 연동→LLM과 Transformer. 페이지 <h1>·<title>·template·build.py 함께, 홈 이름 12개 일치 확인. Sequence 문서는 Day11-2 수업 문서로 유지(dl/all은 기획안만 있고 미제작) | main만 |
| 2026-11-14 | 전체 | PDF 폐지: 요약 8개·치트시트 2개 PDF를 저장소에서 삭제, build_site.py의 PDF 복사·링크·버튼 제거. 대신 모든 페이지 위쪽 메뉴에 "HTML 받기"(사이트 메뉴·통계를 뺀 원본을 download.html로, 파일 이름은 <title> 기준 예: Day10_최적화와_규제.html). 23쪽 모두 그림이 파일 안에 들어 있어 한 파일로 오프라인 열림 확인. 100일 일정 파란 칸 = 오늘까지 가장 최근 수업일(주말엔 Day20). 다운로드 클릭 시험 3쪽 | main만 |
| 2026-11-14 | llm/20261116/lecture · 홈 · 메뉴 | 강사님 강의 HTML 게시(강사님 허락): sync_lecture_html.py(nvidia_camp 날짜·세션 폴더 바로 아래 *.html → pages/<과목>/<날짜>/lecture/, 바뀐 것만), build_site.py가 /<과목>/<날짜>/lecture/를 원본 그대로 메뉴 아래 전체 화면(iframe)으로 띄움(강의 HTML의 고정 머리·아래 막대와 겹치지 않게). 홈 Day 줄·Day 메뉴에 "바로 보기", 요약 전이라도 강의 HTML이 있으면 Day 줄과 일정 칸이 강의 페이지로 연결. "강의 자료 ↗"는 Slack 링크 그대로. 첫 사례 Day21 Prompt·Context Engineering. 1280·375px 확인 | main만 |
| 2026-11-14 | 홈 · 과목 목록 | 요약 없는 Day에 강의 목차 기준 예정 제목(PLANNED_TITLES) + "요약 준비 중" 배지, 과목마다 맨 위 "종합" 줄(없으면 "<과목> N일 종합 · 요약 준비 중"). 1280·375px, 라이트·다크 확인 | main만 |
| 2026-11-15 | 홈 · 과목 목록 | 요약 준비 중인 "종합" 줄에도 Vision 종합과 같은 연한 파랑 그라데이션. 라이트·다크 확인 | main만 |
| 2026-11-15 | 전체 | 사용자 요청으로 배포: --release 빌드(비공개 가이드 local-ai·ai-coding·cli 제외)를 deploy에 fast-forward push(5c56a02), main에는 merge -s ours로 기록만 합침. 라이브 확인은 아래 행 | 배포 |
| 2026-11-15 | setup/path · setup/venv · setup/docker · 홈 | 개발 환경 가이드 3개 초안(공개 전): Windows 경로와 PATH(경로 읽기·폴더 이동·PATH 확인·추가·막히면), Python 가상환경(py -3.13 -m venv .venv — 수업 자료와 같은 방식, 켜기·pip·VS Code 연결·끄기), Docker(WSL 2 → Docker Desktop → 확인 → 기본 명령 → Compose, Docker·Microsoft 공식 문서 2026-11-15 확인). 캡처 없음, Windows PC 실행 확인 전. 로고 python.png·docker.png(공식 사이트), path.svg(직접 그림). 홈 참고 문서 모음 "개발 환경" 칸에 표시, --release에서는 빠짐. 1280·375px·다크 확인 | main만 |
| 2026-11-15 | setup/path · setup/venv | 피드백 반영 초안 2차: 경로 가이드 제목 "경로 설정 (PATH)", 사용자 Slack 가이드 흐름(Tesseract 예시: Get-Command로 확인 → 실행 파일에서 파일명을 뺀 폴더 → 계정의 환경 변수 편집 → 새 창 확인)으로 다시 씀, 경로 읽기는 참고로 내림. 가상환경은 용도별 이름(gpuenv·backendenv, 예시)으로 실습 저장소 바깥 `C:\workspace\envs`에 두는 방식으로 다시 씀(VS Code는 Enter interpreter path). 캡처 없음, Windows 확인 전 | main만 |
| 2026-11-15 | setup/venv | 명령을 Python 공식 문서와 대조: Set-ExecutionPolicy를 venv 문서 표기로, `py -3.13`이 안 될 때 `py -V:3.13` 안내 추가. `py --list`·Activate.ps1은 문서와 일치 | main만 |
| 2026-11-15 | setup/python-venv | 미리보기에서 /setup/venv/가 404: Vercel이 `venv`라는 이름의 폴더를 기본으로 올리지 않음(같은 배포에서 docker·path는 200). 주소를 /setup/python-venv/로 바꿈. 앞으로 사이트 경로에 `venv`·`node_modules`·`__pycache__` 같은 이름을 쓰지 않는다 | main만 |
| 2026-11-15 | setup/python-venv | 가상환경 가이드를 실제 구성으로 다시 씀: gpuenv(01~04 + 11/13) · backendenv(11/10 · 11/12 · 11/16) 두 환경, 설치 목록 3개(requirements-gpu · backend · all)를 페이지에서 내려받아 `C:\workspace\envs`에 두고 `…\Scripts\python.exe -m pip install -r`로 설치, 통합 환경 `.venv`(실습 저장소 안), 환경 추가 · 갱신 절차. 근거: 01~05의 requirements 116개와 import 전수 조사. 세 목록 모두 Windows · Python 3.13 · wheel만으로 의존성 해석 통과(uv pip compile, gpu 152 · backend 40 · all 166개), all은 두 목록과 버전 동일. 실제 Windows 설치 · 실습 실행은 확인 전. 버전 없던 패키지(transformers 5.23.0 등)는 해석 결과로 고정. 표는 모바일에서 세로로 쌓이게 | main만 |
| 2026-11-15 | setup/python-venv | 통합 환경 .venv를 맨 위 폴더 그림과 환경 표에 추가(전에는 6단계에만 있어 안 보였음), "둘 중 한 가지 방식만" 안내. 1단계를 "먼저 설치할 프로그램"으로: Python 3.13 · Git · VS Code · NVIDIA 드라이버 · Tesseract 5.5.0 · PostgreSQL 18의 버전과 받는 곳(버전은 실습 자료에 적힌 값, Git · VS Code · 드라이버는 최신) | main만 |
| 2026-11-15 | setup/vscode-extensions · 홈 | VS Code 확장 가이드 초안(공개 전): 기본 5개(Python · Pylance · Python Debugger · Jupyter · Korean Language Pack), 추천 8개(Ruff · Error Lens · Rainbow CSV · Data Wrangler · Git Graph · REST Client · WSL · Docker), 설치 방법 · 확인 · 막히면. 확장 ID · 이름 · 게시자는 Marketplace 조회로 확인. Slack 안내(이미지 3장)는 받지 못해 반영 전, 목록은 내 추천. 캡처 없음. 아이콘 extension.svg(직접 그림) | main만 |
| 2026-11-15 | setup/vscode-extensions | 수업(Slack) 안내 확장 3개를 2단계로 추가: Code Runner · Live Server · Material Icon Theme, 사용자가 올린 캡처 3장 포함(ID · 게시자는 Marketplace 확인). Code Runner가 고른 가상환경을 쓰지 않는다는 주의 추가. 단계 번호 1~5로 조정 | main만 |
| 2026-11-15 | setup/vscode-extensions | 확장 수를 줄임: 설치할 것 6개(수업 안내 3 + Python · Jupyter · Korean Language Pack; Pylance · Python Debugger는 Python 확장과 함께 설치되므로 목록에서 뺌), 추천은 8개 → 3개(Error Lens · Rainbow CSV · Git Graph, "이럴 때 설치" 기준). Ruff · Data Wrangler · REST Client · WSL · Docker 제외. "확장은 적을수록 좋다" 안내 | main만 |
| 2026-11-15 | setup/vscode-extensions | 사용자 캡처 6장 추가(Python · Pylance · Python Debugger · Korean Language Pack · Error Lens · Git Graph), 표를 캡처+설명 줄로 바꿈. 추천은 Error Lens · Git Graph 2개(Rainbow CSV 제외), Jupyter는 캡처 없이 글로. 1280 · 375px · 다크 넘침 없음 | main만 |
| 2026-11-15 | 홈 · assets/logos | VS Code 확장 가이드 아이콘을 직접 그린 extension.svg에서 VS Code 공식 아이콘(vscode.png, code.visualstudio.com, 64px)으로 교체. 홈 참고 문서 모음에서 확인 | main만 |
| 2026-11-15 | setup/vscode-extensions · setup/python-venv · 홈 | "VS Code 확장" → "VS Code Extension"으로 이름 변경(제목 · 홈 · 본문). 한국어 메뉴 이름 "확장"은 첫 문장과 아이콘 안내에 한 번씩 병기. 주소는 그대로 /setup/vscode-extensions/ | main만 |
| 2026-11-15 | setup/path | 사용자 캡처 4장 추가: 계정의 환경 변수 편집 검색, 사용자 변수 Path 선택, 환경 변수 편집 창에 추가된 Tesseract 경로, 새 PowerShell의 tesseract --version. 저장소가 공개라 캡처 속 PC 사용자 이름은 회색 칸으로 가림(20곳), 배경이 비친 가장자리는 잘라 냄 | main만 |
| 2026-11-15 | setup/path | 2단계(폴더 찾기)와 3단계(PATH에 추가)를 GUI · 터미널 두 방법으로 나눔. GUI: 파일 탐색기 주소 표시줄 / 환경 변수 창(캡처 3장). 터미널: Get-ChildItem / [Environment]::SetEnvironmentVariable("Path", …, "User") 3줄과 줄별 뜻. 터미널 추가 명령은 Windows에서 실행 확인 전 | main만 |
| 2026-11-15 | setup/path | 가이드를 다시 짬(피드백: 두 방법이 안 드러남, 원리 도식 필요). 맨 위 "왜 필요한가" 도식(추가 전/후 — Windows가 PATH 폴더를 차례로 찾는 모습), "전체 흐름" 5칸(설치 → 폴더 찾기 → PATH에 저장 → 새 창 → 확인), 방법 A GUI · 방법 B 터미널을 큰 선택 카드와 테두리 굵은 별도 섹션으로 분리(A-1 · A-2 / B-1 · B-2), 터미널 3줄은 줄마다 값이 어떻게 바뀌는지 따라가는 도식, 3단계 확인은 "확인하는 것 · 명령 · 기대 결과" 표와 새 창이 필요한 이유. 1280 · 375px · 다크 넘침 없음 | main만 |
| 2026-11-15 | setup/path | 다른 프로그램에도 쓸 수 있게 보완: 예시(tesseract, 설치 폴더)를 색이 다른 글자로 표시하고 "이 부분만 바꾼다"고 안내(변수로 빼지 않음), "내 프로그램에 적용하기" 표 2개(바꿀 것 3가지 / 수업에서 쓰는 프로그램별 명령 이름 · 폴더 · 직접 추가 여부 — 폴더는 사용자 캡처의 Path 목록과 PostgreSQL 가이드 기준), A-1에 파일 탐색기 캡처(유형이 "응용 프로그램"인 파일이 실행 파일; 왼쪽 고정 폴더 이름은 지움)와 확장명 숨김 · 비슷한 이름 · bin 폴더 안내, 저장 명령을 2줄로 줄임, 검색 폴더에 Program Files (x86) 추가 | main만 |
| 2026-11-15 | setup/python-venv | 5단계(VS Code 연결)에 사용자 캡처 2장 추가: 명령 팔레트의 Python: Select Interpreter, Select Interpreter 목록의 Enter interpreter path…. 캡처 속 Workspace 항목(저장소 안 가상환경)이 통합 .venv와 같은 경우라는 설명 추가 | main만 |

| 2026-11-15 | setup/path | 마지막 대화의 추가 캡처 3장 반영: test --version 오류 모양(오타·미설치도 같은 오류임을 설명), Program Files에서 설치 폴더 찾기, B-1 검색과 B-2 Path 저장 실행. 계정명·개인 폴더가 있는 2장은 ImageGen 가림 사본 사용, 입력 원본 보존. 새 창 확인 전까지 연결 성공으로 단정하지 않음 | main만 (공개 전) |
| 2026-11-15 | setup/python-venv | 터미널 활성화와 VS Code 인터프리터 선택의 두 실행 경로 도식 추가. 같은 Python·site-packages로 이어짐을 표시하고 새 통합 터미널의 자동 활성화 범위, sys.executable 비교, 경로가 다를 때 조치, 노트북 커널 선택 안내. Code Runner·환경·설치 누락을 구분. 기존 색상·카드 재사용, DESIGN.md 추가 | main만 (공개 전) |
| 2026-11-15 | setup/vscode-extensions · 전체 검증 | 추가 캡처 2장(활동 표시줄의 Extensions 아이콘·상태 표시줄 Go Live)과 설명, 가상환경 확인 링크 추가. 3페이지 × 375·768·1280px × 라이트·다크 18조건 통과, 이미지 확대·Esc 닫기·코드 복사·접기·확인 링크·200% 글자 확대·오프라인 HTML 확인. HTML 구조·aria 참조·중복 ID·JS 문법·git diff --check 통과. Windows 설치·실습 재실행은 미검증 | main만 (공개 전) |
| 2026-11-16 | 전체 | 사용자 요청으로 배포: 경로 설정 · VS Code Extension · AI 코딩 도구(5쪽)를 공개로 바꾸고 --release 빌드를 deploy에 fast-forward push(0a9548e). 가상환경 · Docker · 로컬 AI 코딩 · CLI 도구는 계속 공개 전. 배포용 빌드가 공개 전 가이드로 가는 링크를 글자로 바꾸도록 build_site.py 수정(경로 2 · VS Code 6 · AI 코딩 3개). 라이브 확인: 공개 3종 + PostgreSQL 200, 공개 전 4종 404, 홈 참고 문서 모음에 공개 가이드만 표시 | 배포 |
| 2026-11-16 | llm/20261116 · 홈 | 강의 트리·Colab 연결 첫 적용(Day21만). pages/<과목>/<날짜>/tree.md(작업 폴더 Day21_강의트리.md 복사)를 읽어, 요약이 없는 날은 그날 페이지를 "강의 목차 한눈에 보기"로 만든다(묶음별 접기·펼치기, 흐름 칩, 실습 화면 표시, 원문 제목 그대로). COLAB에 Drive 폴더 주소 등록 → 홈 Day 줄·그날 페이지에 공식 Colab 로고(공유: 링크가 있는 모든 사용자 · 뷰어 확인). 1280·375 × 라이트·다크 가로 넘침 0 | main만 |
| 2026-11-16 | llm/20261116 | 강의 목차를 접기 목록 → 교시 카드 판(시안 A, 사용자 선택)으로 교체. 그날 페이지 = 자료 줄 · "강의 목차 한눈에 보기"(강사님 강의 자료 기준, 기본 접힘, 펼치면 4열 카드에 원문 화면 제목 전부, 실습은 카드 아래 띠) · "요약"(보조강사 해석, 준비 중). 목차 블록은 스타일을 자체 포함(.lt)해 요약 페이지에도 끼울 수 있게 함. 1280·375 × 라이트·다크 가로 넘침 0 | main만 |
| 2026-11-16 | llm/20261116 | 사용자 요청으로 요약 영역의 "요약" 제목과 "보조강사 해석" 표시를 뺌. 요약은 따로 묶는 제목 없이 목차 아래에 바로 이어지고, 지금은 "요약 준비 중" 상자만 둠 | main만 |
| 2026-11-16 | llm/20261113 · 공통 | 요약이 있는 페이지에 첫 적용(Day20): 요약 제목 머리 바로 아래에 자료 줄(Colab) + "강의 목차 한눈에 보기"를 끼움(사이트 화면에만, HTML 받기 원본은 그대로). tree.md = Day20_강의구조_핵심설명.md 복사, COLAB에 11/13 Drive 폴더(링크 공유 · 뷰어 확인) 등록. 요약 페이지 자체 CSS(details·section)가 새어 들지 않게 블록 안에서 초기화, 3단계 트리의 실습도 카드 아래 띠로 모음, · 뒤 줄바꿈 허용. 다크 모드 없는 요약에는 블록도 밝게 두는 처리 포함. Day20·21 × 1280·375 × 라이트·다크 가로 넘침 0 | main만 |
| 2026-11-16 | 전체 Day · 홈 | 학습 자료 시트 재동기화(sync_lectures.py): 강의 자료 링크 5개 추가(Day2만 시트에 링크 없음). 강의 목차를 Day2~21 전부에 적용(Day1 OT는 사이트 과목 없음): 작업 폴더의 강의구조/강의트리 md를 pages/<과목>/<날짜>/tree.md로 복사, 11/02 두 회차는 Day11 파일→20261102, Day12 파일→20261102-2. 요약이 없는 Day2~9는 목차 페이지 생성, Python 과목 페이지도 생김. 요약 페이지 10곳은 제목 머리 감싸개 안쪽 끝에 끼우도록 위치 규칙 보정, 호스트 summary::before 초기화. 20쪽 × 1280·375 × 라이트·다크 가로 넘침 0 | main만 |
| 2026-11-16 | 전체 | 사용자 요청으로 배포: 모든 Day 강의 목차 · Colab 연결(11/13·11/16) · 학습 자료 링크 재동기화를 --release 빌드로 deploy에 fast-forward push(3a029b3). 공개 전 가이드 4종은 계속 제외 | 배포 |
| 2026-11-16 | 홈 | 맨 위 기준을 "요약이 있는 날" → "볼 페이지가 있는 날(요약 또는 강의 목차)"로: 최근 수업 첫 줄 Day21(요약 준비 중 표시), 과목 카드 바로가기 Day21, 수업 칸 띠도 목차 페이지 있는 날을 칠하고 그날로 연결. "요약 N일" 숫자는 실제 요약 수 유지 | main · 배포 |
| 2026-11-16 | llm/20261117 | Day22 강의 HTML을 main에 미리 반영(사용자: 공개 GitHub에 보이는 것은 괜찮음, 사이트 공개는 내일 deploy로). 홈 Day22 줄에 바로 보기 · 미리보기에만 보임 | main만 |
| 2026-11-16 | llm/20261117 · 홈 | Day22 강의 트리 작성(05_LLM_RAG/20261117/Day22_강의트리.md, HTML 내장 데이터 v5 기준 84화면, Day21 형식) → tree.md. 홈 Day22 줄 제목이 비던 문제: 줄 제목을 예정 제목에서만 찾던 것을 교재 제목·강의 HTML 제목까지 보도록 고침. 최근 수업·과목 카드는 오늘까지만(내일 수업 제외). 교시 이름과 같은 화면은 위치와 관계없이 카드에서 뺌 | main만 (공개는 11/17 deploy) |
| 2026-11-16 | setup/local-ai · setup/cli · 빌드 | 사용자 요청으로 로컬 AI 코딩 · CLI 도구 공개(SETUP 플래그 True). 배포용(--release) 빌드는 오늘 이후 날짜의 수업 자료(강의 HTML·목차)를 자동으로 뺌: main에 Day22를 미리 둔 채 다른 변경을 배포해도 Day22는 11/17 배포 때 공개 | main · 배포 |
| 2026-11-16 | setup/cli | 사용자 요청으로 다시 숨김(문서 미완성). SETUP 플래그 False, --release 빌드로 재배포 | main · 배포 |
| 2026-11-16 | setup/ai-coding/agy | 4 모드 카드에 시작 옵션 `agy --dangerously-skip-permissions`(모든 도구 권한 요청 자동 승인, agy 1.5.9 --help로 확인)과 결과 직접 확인 안내 추가. 명령은 한 줄 유지. _work 원본도 같이 수정 | main · 배포 |
| 2026-11-16 | setup/cli | 추천란을 "에이전트에게 연결하면 유용한 CLI"로 변경: Context7 · Playwright CLI · MarkItDown · ripgrep · jq의 작업 보조 용도와 GitHub · Docker · AWS · Google Cloud · Vercel의 서비스 활용을 상황·효과·공식 링크로 소개. 설치 명령 목록을 설명으로 교체, 머리말·메타 설명 갱신. 기존 스타일 재사용, 모바일 200% 글자 확대의 가로 넘침 수정. 빌드·375/768/1280px 라이트/다크·오프라인 HTML·구조 검사 통과. 공개 플래그 True로 전환. main·deploy push, 공개 페이지 200·홈 링크, Day22·비공개 가이드 404 확인 | main · 배포 |
| 2026-11-16 | setup/ai-coding 공통·4개 도구 | 공통 페이지 상단에 OpenCode auto · Claude Code Skip · Codex YOLO · agy Skip 실행 명령과 복사 버튼을 모으고 각 도구 페이지 상단에도 표시. OpenCode의 deny 유지와 Codex의 샌드박스 해제 차이를 설명, 기존 모드 안내를 상단 명령과 연결. 로컬 CLI help·Codex YOLO 별칭·공식 문서 확인. main·deploy 반영, 공통·개별 5쪽 200 및 배포본 일치 확인 | main · 배포 |
| 2026-11-16 | setup/ai-coding 공통·4개 도구 | 자동 승인 안내 강조 축소: 공통 페이지와 개별 페이지 상단의 실행 카드를 제거하고, 각 도구의 기존 권한·모드 설명 안에 명령과 짧은 설명만 유지. main·deploy 반영 및 공개 5쪽 배포본 일치 확인 | main · 배포 |
| 2026-11-16 | setup/python-venv | 초보자용으로 `pip install -r 설치목록.txt` 짧은 명령을 4단계(환경 켠 뒤 gpuenv · backendenv)·6단계·7단계에 추가하고 3단계에 핵심 한 줄 설명 추가. 긴 경로 형태만 있어 안 보이던 문제 | main만 (공개 전) |
| 2026-11-16 | setup/ai-coding/agy · opencode | 자동 승인 명령을 작은 보조 문구에서 기존 모드·승인 표의 정규 행으로 이동. 명령어를 표 본문 크기로 표시하고 기능을 함께 설명. 모바일 가로 넘침 없음·main/deploy 반영·공개 2쪽 배포본 일치 확인 | main · 배포 |
| 2026-11-16 | setup/python-venv | 초보자용으로 구성 재편: 환경 폴더를 practice_assignment\envs 아래(.venv 포함)로 통일하고 명령을 상대경로로. 0 pip로 설치되지 않는 프로그램 · 1 설치 목록(버튼만) · 2 가상환경 만들고 설치(명령 두 줄 강조) · 3 터미널·VS Code 연결(도식 한 장, 캡처 2장에 빨간 네모) · 참고 확인. 통합 환경 6단계·환경 추가 7단계·막히면·명령으로 받기 삭제. vscode-extensions 링크를 #s3로 | main만 (공개 전) |
| 2026-11-16 | site 배포 | site 저장소의 수정만 main·deploy에 push. VS Code Extension 안내 변경을 공개 배포, Python 가상환경·Docker·Day22는 기존 공개 전 설정 유지. 공개 페이지 배포본 일치 및 미공개 경로 404 확인 | main · 배포 |
| 2026-11-16 | setup/python-venv | 사용자 요청으로 가상환경 가이드를 공개로 바꾸고 --release 빌드를 deploy에 반영. Docker · 로컬 AI 외 공개 전 가이드와 11/17 자료는 계속 공개 전 | 배포 |
| 2026-11-16 | setup/python-venv | 명령 입력창 선택(PowerShell · Git Bash) 추가: 맨 위 고정 선택 막대, 고르면 폴더 만들기 · 환경 만들기 · 설치 · 켜기 명령이 그 창에 맞게 바뀜(Git Bash는 / 경로, source …/Scripts/activate). 선택은 브라우저에 기억. Git Bash 명령은 Windows에서 실행 확인 전 | main만 |
| 2026-11-16 | setup/python-venv | PowerShell · Git Bash 선택을 맨 위 막대에서 각 명령 블록(2단계 환경 3개 · 3단계 켜기)의 머리글 탭으로 이동. 한 곳에서 바꾸면 모든 블록이 같이 바뀜. 명령이 같은 블록은 "터미널" 라벨 | main만 |
| 2026-11-16 | setup/path | PowerShell · Git Bash 선택을 명령 블록 머리글 탭으로 추가(지금 상태 확인 · B-1 폴더 찾기 · B-2 PATH 저장 · 임시 시험 · 폴더 이동). Git Bash는 find · ~/.bashrc에 export 한 줄(Git Bash에만 적용, 나머지는 방법 A) · /c/ 경로. 본문의 PowerShell 표현을 터미널로. 선택은 가상환경 가이드와 같은 키로 공유. Git Bash 명령은 Windows 실행 확인 전 | main만 |
| 2026-11-16 | setup/vscode-extensions | 캡처 정리: Go Live 캡처에서 관계없는 채팅 화면을 빼고 상태 표시줄만 남겨 Go Live에 빨간 네모, Code Runner 캡처의 잘린 긴 설명 목록 제거, 확장 카드 캡처 11장을 같은 배율로 표시(캡처마다 폭이 달라 글자 크기가 들쭉날쭉하던 문제) | main만 |
| 2026-11-16 | setup/vscode-extensions | Go Live 캡처의 빨간 네모 위치 수정(Go Live 항목 둘레로), 캡처 아래에 따로 있던 설명을 다른 항목처럼 오른쪽 설명 칸으로 이동하고 구분선 맞춤 | main만 |
| 2026-11-16 | setup/vscode-extensions | 가상환경 실행 주의(Run Code vs Python 실행 버튼)를 아래 별도 박스에서 Code Runner 항목의 오른쪽 설명으로 이동. 항목 사진은 위쪽 정렬 | main만 |
| 2026-11-16 | setup/vscode-extensions | Go Live는 별도 Extension이 아니라 Live Server의 버튼이므로 별도 항목을 없애고 Live Server 항목 안(카드 캡처 아래)으로 이동, 설명도 Live Server 설명에 합침 | main만 |
| 2026-11-16 | llm/20261116 | Day21 요약 초안: 강사 핵심요약 6구역 그림을 흐름 그림 위에 얹고, 개념 사이 구분(≠)을 이음새로 배치. 끝에 증상→의심할 곳→수단 표. 구성안 포함. 코드·실측 없음 | main만 |
| 2026-11-16 | llm/20261116 | Day21 초안 수정: 구역을 번호 박스로 나누고 머리에 흐름상 위치 표시, 설명을 합니다체로 풀고 전문 용어에 원어 병기, 마지막 증상 표 삭제 | main만 |
| 2026-11-16 | llm/20261116 | Day21 초안: 각 구역의 "구분할 것" 블록 삭제 | main만 |
| 2026-11-16 | llm/20261116 | Day21 초안: A/B 평가 구역을 실험 도식으로 재구성(고정 → 한 가지 변경 → 실행 → 첫 응답 원문 보존 → 검사·평가 → 기록, 고정/변경 패널, 질문×A/B 기록 슬롯, D → 고정 → H 순서) | main만 |
| 2026-11-16 | llm/20261116 | Day21 초안: A/B 평가 구역 단순화(고정 + 바꾸는 것 1개 → 기록 표 3칸 그림 하나, 기록 → 입력 개선, D → 고정 → H 한 줄). 6단계 줄·저장 항목·구분 줄 삭제 | main만 |
| 2026-11-16 | llm/20261116 | Day21 초안: 기록 표 칸 글자를 "미실행"에서 "첫 응답"으로(미실행·미평가 설명은 캡션에만) | main만 |
| 2026-11-17 | llm/20261117 | Day22 Colab 실습 폴더 링크 추가 | main |
| 2026-11-17 | llm/20261117 | Day22 요약 초안: 강사님 핵심요약 6구역(모델 호출·입력/출력 검사·Streaming·오류/재시도·비용/시간·캐시/모델 선택)을 내용 그대로 두고 Day21 디자인으로 배치 | main만 |
| 2026-11-17 | llm/20261118 | Day23 준비: 강의 HTML·강의 목차 추가, 강사님 핵심요약 6구역을 Day22 디자인으로 배치한 요약 초안 | main만 |
| 2026-11-17 | 요약 페이지 전체 | 요약·가이드 페이지 글꼴을 Pretendard로 통일(홈·목록과 동일 /fonts, --font-body 앞에 지정, 템플릿 포함) | main만 |
| 2026-11-17 | llm/20261117·20261118 | Day22·Day23 요약 하단 문구를 출처 한 줄로 단순화 | main만 |
| 2026-11-17 | 전체 | 상단 메뉴줄(cn-nav) 스티키 고정: 스크롤해도 ← 학습 아카이브·LLM·RAG 항상 표시, 앵커 이동 여백, 모바일은 한 줄 가로 스크롤 | main만 |
| 2026-11-17 | 전체 | 글꼴 통일 장치: 빌드가 요약·가이드 페이지의 본문 글꼴 선언 앞에 Pretendard를 붙이고 링크를 보장(코드 글꼴·강의 원본 lecture 제외), 못 고치는 경우는 빌드 끝에 ⚠ 경고(빌드는 계속). cheatsheet opencv·sklearn, 12일 실습 도식 반영 | main만 |
| 2026-11-17 | 전체 | 강의 자료(Slack) 링크의 화살표를 Slack 로고로 교체: 홈 Day 줄은 로고만, Day 페이지 자료 줄·상단 메뉴는 로고+강의 자료 | main만 |
| 2026-11-17 | 전체 | 라이트/다크 전환 버튼: 다크 모드가 있는 페이지(홈·과목·Day·LLM 요약·설치 가이드 34개)에만 해·달 아이콘 버튼. 홈은 SWEA·Programmers 옆, 그 밖은 상단 메뉴 오른쪽 끝(모바일은 오른쪽 고정). 고른 값은 localStorage, OS 설정과 같은 쪽을 고르면 다시 OS를 따름. 다크 모드 없는 페이지(vision·치트시트·강의 원본)는 버튼 없음 | main만 |
| 2026-11-17 | llm/20261117 | Day22 강의 자료(Slack) 링크 반영: lectures.json 동기화(시트 PDF 링크 1건 추가) | main |
| 2026-11-17 | 전체 | '바로 보기' → '강의 자료'(사이트 안 강의 HTML). 강의 HTML이 있는 날·강의 자료 화면에서는 Slack 링크를 로고만, 없는 날은 Slack 링크가 '강의 자료' | main만 |
| 2026-11-17 | 홈 | SWEA·Programmers 링크의 ↗ 화살표 제거 | main → 배포 |
| 2026-11-17 | llm/20261118 · 홈 | Day23 Colab 폴더(Drive, 링크 공유·뷰어 확인, 노트북 3개) 등록: 홈 Day 줄·그날 페이지에 Colab 로고 | main만 |
| 2026-11-17 | 전체 | 다크 모드 로고 받침 통일: 참고 칩·Colab·Slack의 흰 받침/흰 바탕 제거(투명). SeSAC·NVIDIA 브랜드 묶음만 흰 판 유지(공식 다크 버전 없음, NVIDIA 가이드상 로고 변형 불가). Ollama는 다크 모드에서 공식 다크 로고(ollama/ollama docs/images/logo-dark.png) | main → 배포 |
| 2026-11-17 | 전체 | 상단 메뉴를 아이콘으로 통일: HTML 받기→다운로드, 강의 자료→문서, Slack은 흰 사각 배경 로고, 달과 같은 2rem 크기. 설명은 마우스를 올리면(title)·aria-label로. ‹ Day · Day › 글자는 그대로. 1000·375 가로 넘침 0 | main만 |
| 2026-11-17 | 전체 | 상단 메뉴 Slack 로고를 흰색 단색(slack-white.svg)으로: 흰 배경 상자 제거, 다른 아이콘과 같은 톤. 홈·자료 줄의 컬러 로고는 그대로 | main만 |
| 2026-11-17 | 전체 | 상단 메뉴 아이콘 설명을 기본 title 대신 CSS 툴팁(data-tip)으로: 마우스를 올리면 바로 아래에 어두운 말풍선, 키보드 포커스에서도 표시, aria-label은 유지 | main만 |
| 2026-11-17 | 전체 | 상단 메뉴의 강의 자료 아이콘을 문서 → 눈(홈 Day 줄·자료 줄의 강의 자료와 같은 아이콘)으로 | main만 |
| 2026-11-17 | 전체 | 자료 링크 표기 정리(f6ef81f)를 되돌림: 상단 메뉴는 5446f06 상태(다운로드·눈·흰색 Slack 아이콘 + 말풍선). 홈 화면 표기는 논의 후 결정 | main만 |
| 2026-11-17 | 전체 | 상단 메뉴에 Colab 흰색 단색 아이콘(colab-white.png) 추가(Slack 오른쪽, 말풍선 포함, Colab 폴더가 있는 날만). 요약·Day 페이지 제목 아래 자료 줄(강의 자료·Slack·Colab) 제거 — 강의 목차 블록만 남김. 홈 화면 표기는 논의 중이라 그대로. 1000·375 가로 넘침 0 | main만 |
| 2026-11-17 | 홈 | Day 줄 자료 버튼: 테두리 제거, 옅은 면만(강의 자료=파란 옅은 면, Slack·Colab=회색 옅은 면), 호버 시 얇은 윤곽선. Slack·Colab은 로고만 두고 마우스 올리면 말풍선. 1100·375 × 라이트·다크 가로 넘침 0 | main만 |
| 2026-11-17 | 강의 화면 | 강사님 강의 HTML의 사이트 화면(view.html)만 본문 글꼴을 Pretendard 96%(PretendardLecture)로 변경. 받기(download.html)는 원본 그대로. 강의 CSP에 self 허용, font: 줄임 표기·inherit 처리 보정. 11/16·17·18 244장 비교: 줄바꿈 변화 1장, 도식 넘침 0 | main만 |
| 2026-11-17 | setup/git | Git · GitHub 가이드 초안: Part 1 기본(0 큰 그림 ~ 7 치트시트) + Part 2 실전 세팅(강사님 저장소에서 폴더 골라 받기, nvidia-camp/practice 기준). 움직이는 그림 4개(작업 폴더→Staging→로컬 저장소→GitHub, fork·upstream, 브랜치·머지, 폴더 골라 받기). 명령은 임시 저장소에서 실행 확인. 1280·390 × 라이트·다크 가로 넘침 0. SETUP 공개=False | main만 (미공개) |
| 2026-11-17 | setup/git | 한 페이지 나열 → 탭 5쪽(기본 · 원본 따라가기 · 브랜치 · 머지 · 되돌리기 · .gitignore · 실전 세팅)으로 나눔. ④에 되돌리기 그림 추가(stash 선반, .env 튕김, revert 커밋) | main만 (미공개) |
| 2026-11-17 | python/20261020~20261022 · 홈 | Python Day 2~4 Colab 실습 폴더(Drive, 노트북 10개) 등록: 홈 Day 줄·그날 페이지에 Colab 로고 | main → 배포 |
| 2026-11-17 | setup/git | ① 기본 탭의 '처음 한 번만 하는 설정'을 접힌 토글로(이미 설정을 마친 수강생 기준). 1280·390 열고 닫기 · 가로 넘침 0 | main만 (미공개) |
| 2026-11-17 | setup/git | ② 탭 이름 '원본 따라가기' → 'upstream'(용어 그대로). 제목·탭·상단 경로·⑤ 탭의 참조 문구 함께 수정 | main만 (미공개) |
| 2026-11-17 | setup/git | ③ 탭 이름 '브랜치 · 머지' → 'branch · merge'(용어 그대로). 제목·탭·상단 경로 함께 | main만 (미공개) |
| 2026-11-17 | setup/git | ④ 탭 이름 → 'undo · .gitignore'. SETUP 공개=True로 전환(배포 준비) | main |
| 2026-11-17 | setup/git/practice | 머리말의 예시 저장소(nvidia-camp/practice · GIT_ROUTINE.md) 안내 문구 삭제 | 배포 |
| 2026-11-17 | setup/docker | Git 가이드처럼 탭 4쪽(기본 · Dockerfile · build · port · volume · compose)으로 다시 씀. 쪽마다 움직이는 그림, 설치는 접힌 토글, 막히면 표 삭제. 명령·출력은 Docker 29에서 실행 확인 | main만 (미공개) |
| 2026-11-17 | ml/20261023~28 | Colab 실습 폴더 링크 등록 | main |
| 2026-11-18 | llm/20261118 · 홈 | Day23(2026-11-18) 요약 · 강의 자료 · Colab 폴더 공개 배포 (Docker 제외) | main → 배포 |
| 2026-11-18 | setup/pgvector | Day23 pgvector 설치 안내(Windows 11 · PostgreSQL 18.6 · pgvector 0.8.7)를 LLM·RAG 과목 참고 문서로 등록. PostgreSQL 가이드 옆. 인쇄 버튼을 사이트 메뉴 아래로(top 62px) | 배포 |
| 2026-11-18 | llm/20261119 | Day24 준비: 강의 HTML·강의 목차(8교시 78화면 원문 제목) 추가, 강사님 핵심요약 6구역을 Day23 디자인으로 배치한 요약 초안 | main만 |
| 2026-11-18 | setup/pgvector | 실제 화면 4장(Slack DM) 추가: 2단계 pg_config 결과(사용자 이름 가림, PROGRA~1 설명) · 3단계 Build Tools 다운로드 · 설치 관리자 준비 · 설치 진행. 누르면 크게 보기 | main만 |
| 2026-11-18 | setup/pgvector | 단계마다 카드로 구획: 번호 배지·실행 도구 표시, 맨 위 단계 목차, 준비·빌드·DB 활성화·Python 연결·마무리 묶음 띠, 실행 위치 줄 강조. 본문 글자는 그대로(태그 제거 비교 일치). 인쇄 버튼은 머리띠와 함께 스크롤 | main만 |
| 2026-11-18 | setup/pgvector | 사진은 확신이 필요한 화면 3장만(3단계 다운로드 페이지 · 4단계 시작 메뉴 x64 Native Tools · 8단계 pgAdmin 결과), 잘라서 원래 크기로. CMD 결과(2·4·5·6단계)는 사진 대신 정상 출력 글자 + 확인 줄 강조. 설치 대기·진행 사진 2장 제외 | main만 |
| 2026-11-18 | setup/pgvector | 명령·SQL·코드 블록 18개에 복사 버튼(정상 출력 상자 4개는 제외). 누르면 복사됨 표시 | main만 |
| 2026-11-18 | setup/pgvector | 두 쪽으로 나눔: 설치(A·1–8단계) /setup/pgvector/ · 실행(9–12단계) /setup/pgvector/run/. 탭·쪽마다 단계 목차, 1단계 결과표의 단계 안내를 링크로, 설치 쪽 끝에 다음 쪽 안내. 홈 이름 pgvector 설치 안내 → pgvector 가이드. 본문 글자 그대로 | main만 |
| 2026-11-18 | setup/pgvector | 11단계부터 셋째 쪽으로: 문제 해결 · 체크리스트(/setup/pgvector/check/, 11 오류별 해결 · 12 체크리스트 · 공식 참고 자료). 실행 쪽은 9–10단계, 끝에 다음 쪽 안내. 본문 글자 그대로 | main만 |
| 2026-11-18 | setup/python-venv | 가상환경 이름을 점으로 시작하게 통일: gpuenv → `.gpuenv`, backendenv → `.backendenv` (`.venv`와 같은 규칙). 명령·폴더 구조·설치 목록 파일 머리말·홈 설명까지 바꿈 | main만 |
| 2026-11-18 | llm/20261119 | Day24 Colab 실습 폴더 등록(Drive `03. 실습/20261119`, 노트북 01–07 basic). 홈 Day 줄·그날 페이지·강의 보기에 Colab 로고 | main만 |
| 2026-11-18 | 배포 | 다음 수업일 자료를 전날 18:20에 공개: 사이트 기준일이 18:20부터 다음 수업일(`--as-of`로 지정 가능), 자동 배포 `auto_release.sh` + launchd 매일 18:20 (공개 전 페이지 있으면 중단) | main만 |
| 2026-11-19 | 전체 | Google Analytics 4(G-9743VJ73E0) 추가: 실제 주소에서만 전송, 공통 값 content_group·page_type·day_label, 이벤트 section_view·toc_open·details_open·site_click(link_type)·theme_toggle·slide_view·lecture_progress. Vercel Analytics 유지, download.html·view.html 제외 | 배포 |
| 2026-11-19 | 전체 | 구조 개편(refactor/structure → main): 설정 site.toml, CSS·JS·아이콘 web/, 빌드 코드 sitebuild/ 7개 모듈, AGENTS.md·README·Makefile·빌드 검사(sitebuild/check.py). 사이트 결과는 GA 코드 모양 외 동일(바이트 비교). 안 쓰는 파일 7개 삭제 | main (deploy는 18:20 자동 배포에 함께) |
| 2026-11-19 | 배포 | release 7bfaa5f: 구조 개편 후 첫 배포(내용 같음, GA 코드 모양만). 실제 사이트 확인: Colab 링크 12/12 · GA 전송 204 · /setup/docker/ 404 | 배포 |
| 2026-11-19 | dl·vision | Colab 실습 폴더 8개 등록(site.toml [colab], Drive `03. 실습/03. DL`·`04. Vision`). Day11-2는 Drive 폴더 이름 20261103(Sequence 노트북) | 배포 |
| 2026-11-19 | 전체 | 다크 모드 코드(web/theme.js)를 영역별로 나누고 설명 추가. 동작 변경 없음: ego-browser로 6개 페이지 27단계(OS 밝음·어두움, 버튼, 새로고침, 이동, 저장 지움) 상태가 정리 전과 같음, 화면 확인 | 배포 |
| 2026-11-19 | llm/20261119 | 강의 목차 한눈에 보기(`tree.md`)의 실습 01–08 표기를 `Basic / Intermediate / Advanced` 대신 실제 실습 주제(원본 수집·Parsing·정제·Chunk·검증·Metadata·pgvector·일일프로젝트)로 보완하고 재빌드 | 배포 |
| 2026-11-19 | 전체 | `강의 목차 한눈에 보기` 실습 띠(`sitebuild/tree.py` `lab_row`)에서 앞 번호(`01 · ` 등)를 제거해 설명만 표시하도록 일괄 수정(23개 페이지 재빌드) | 배포 |
| 2026-11-19 | 배포 | release e2160f8: Day24 강의 목차 실습 이름·전체 실습 띠 앞 번호 제거 배포 (Docker 제외) | 배포 |

| 2026-11-19 | llm/20261120 | Day25를 Git·Docker 가이드처럼 탭 구조([day_pages])로 재구성: 홈 Day 줄은 기존처럼 [강의 자료]만 두고, /llm/20261120/ 첫 탭은 사전 준비·파일 내려받기 9종(ZIP·SQL 5·Postman 2·requirements.txt), 둘째 탭(/spec/)은 요구사항 명세서 v1.4 | main만 |

| 2026-11-19 | llm/20261120 | ego-browser 점검 반영: 요구사항 명세서(/spec/)와 사전 준비(/20261120/) 모두 라이트 기본 + 다크 모드 전환 지원, 명세서 긴 JSON·표의 데스크톱/모바일(375px) 가로 넘침 제거(532 → 375px), 사전 준비 표 열 폭·줄바꿈 보정 | main만 |

| 2026-11-19 | llm/20261120 · web/nav.css | Day25 사전준비의 bare `nav` 선택자가 `.cn-nav` 폭을 줄여 좌우 여백이 생기던 문제 수정(`.sec-nav` 분리 + `.cn-nav` `width:100%;max-width:none;margin:0`), 헤더·탭·본문 좌측 정렬선 통일 | main만 |
| 2026-11-19 | llm/20261120 | 사전 준비·요구사항 명세서 탭 통일: 사전 준비의 머리 영역·탭·카드 틀을 명세서와 같게(폭 1180px, 그라데이션 머리, 부제 15px, 카드 시작 위치), 본문 글꼴 `font:` 줄임 표기 → `font-family`로 바꿔 Pretendard 적용, 구역 링크는 카드 안으로, 머리 문구 `2026.11.20 · DAY25 · REQUIREMENTS V1.4`로 통일, 다크 모드 바탕·카드·탭 색 같게. 위쪽 메뉴는 두 탭 모두 `LLM·RAG › Day25 › 탭 이름`. 모바일 카드 위 12px 간격. ego-browser 1440 라이트·다크·375에서 두 탭 위치 일치 | main만 |
| 2026-11-19 | llm/20261120 | 사전 준비·요구사항 명세서 섹션 구분: 큰 카드 하나 → h2 섹션마다 카드, 섹션을 PART 제목 줄로 묶음(사전 준비 3개, 명세서 4개), 명세서에 PART 바로가기 줄 추가. 본문 글자·태그·속성은 원본과 같음(텍스트 조각 483·1741개 비교, 섹션 묶음만 추가). 1440 라이트·다크·375 확인 | main만 |
| 2026-11-19 | 전체 요약 · vision/20261106 | 맨 위로 버튼: 강의 요약 27개 페이지 오른쪽 아래에 꺾쇠 + 읽은 만큼 차는 원(web/totop.*, sitebuild/nav.py add_totop). 한 화면쯤 내려가면 나타나고 다크 모드 있는 페이지만 어두운 색. Day25 명세서의 기존 "맨 위로 ↑" 버튼은 이것으로 대체. Day15에 다크 모드 추가(template.html CSS만, style 밖은 원본과 동일·그래프 글자/선 색 포함). 1440 라이트·다크·375, 클릭 시 맨 위 이동 확인 | main만 |
| 2026-11-19 | llm/20261120 · llm/20261112/practice | 코드 복사 아이콘: `<pre data-copy>`에 복사 아이콘 버튼(web/copy.*, sitebuild/nav.py add_copy), 누르면 체크 표시 1.5초. 대상: Day25 사전 준비 실행 명령 4개(어두운 코드 셀로 변경), 명세서 요청 Body JSON 10개, Day19 오전 실습 터미널 명령 3개. 본문 글자·태그는 원본과 동일(data-copy 표시만 추가) | main만 |
| 2026-11-19 | vision/20261104·05·09·all | 다크 모드 추가(Day13·14·16·Vision 4일 종합): 페이지 CSS 끝에 auto-dark 블록(색만). Day14·16·종합은 template.html에 넣고 build.py로 다시 생성, Day13은 index.html style에. 네 페이지 모두 style 밖은 원본과 동일. 픽셀 값 칸·히트맵 눈금 같은 데이터 색은 그대로 | main만 |
| 2026-11-19 | dl·llm/20261110·cheatsheet·setup/pgvector (+vision 재생성) | 다크 모드 없던 공개 페이지 10개에 다크 모드 추가(DL Day10·11-1·11-2, LLM Day17, 치트시트 3, pgvector 가이드 3). Vision 4개도 같은 규칙으로 다시 만듦(진한 면은 그대로, 반투명 흰 면·코드 칩·남색 띠 처리 보완). 모든 페이지 style 밖은 원본과 동일. 이제 강사님 강의 화면(lecture) 말고는 모든 페이지가 다크 모드를 이어 감 | main만 |
| 2026-11-19 | 전체 · setup/pgvector | 복사 아이콘 통일: 원래 글자 복사 버튼(코드 복사·전체 코드 복사·복사, 30개 페이지 98개)을 숨기고 그 코드 칸에 같은 아이콘(빌드 sitebuild/nav.py link_old_copy_buttons). 아이콘이 원래 버튼을 대신 눌러 복사 방식(줄 번호 빼기·PowerShell/Bash 전환)은 그대로 — 98개 모두 복사 내용이 전과 같음을 확인. pgvector 3쪽: 위 띠(DAY 23 … 설치 안내 + 인쇄/PDF 저장) 삭제, 복사 버튼 만드는 스크립트 대신 data-copy | main만 |
| 2026-11-19 | cheatsheet · setup | 맨 위로 버튼을 치트시트 3개·설치 가이드 전체에도 추가(강의 요약과 같은 버튼). 이제 홈·과목 목록·강의 슬라이드 화면 말고 모든 페이지(55개)에 있음 | main만 |
| 2026-11-19 | 배포 | release eec2f62 (main 780f691, --release --as-of 2026-11-20, Docker 제외): Day25 사전 준비·명세서·섹션 카드, 맨 위로 버튼 55쪽, 복사 아이콘 통일, 다크 모드 15쪽 추가, pgvector 위 띠 삭제. 실제 사이트 확인: Day25 3쪽 200 · /setup/docker/ 404 · 홈에서 다크 켜고 Vision·DL·치트시트·pgvector·Day25 이동 시 다크 유지 | 배포 |
| 2026-11-19 | llm/20261120/spec | 요구사항 명세서에서 PART 4(강의·운영 참고: 9 오전 설명·라이브 시연 설계, 10 구현·운영 제약, 11 단계별 제작물과 추적성, 12 설계 근거, 부록 A) 삭제 + PART 바로가기 링크 삭제 (사용자 요청) | 배포 |
| 2026-11-20 | llm/20261120/basic | 3번 탭 "Basic 완주 안내" 추가: 강사님 안내서.html을 make_page.py로 변환(본문 텍스트 1622노드·태그 동일 확인). 원본 목차 nav→nav.toc로 범위 좁힘(사이트 메뉴 아래 48px에 고정), 탭 줄·다크 모드·접힌 전체 코드 칸 강조(왼쪽 선·화살표) CSS 추가, 작성자 개인 ChatGPT 링크 3개는 글자만 남김. 1·2번 탭에도 3번 탭 링크 | main만 |
| 2026-11-20 | llm/20261120/basic | ego lite 점검 후 화면 수정: 원본 목차 줄을 본문 칸에 맞춤(넓은 화면에서 왼쪽 끝에 붙던 것), 탭 줄 아래 간격, 펼친 코드 위 빈 여백 제거, 휴대폰 폭(≤500px)에서 코드 칸 안쪽 여백 축소·줄바꿈 대신 가로 스크롤(20자마다 꺾이던 것). 본문 텍스트 동일 확인 | main만 |
| 2026-11-20 | llm/20261120/basic | 복사 후 안내 문구("전체 내용을 복사했습니다…" / "자동 복사를 사용할 수 없습니다…") 숨김: 원본 버튼·문구 칸 .code-tools 전체 display:none. 복사는 사이트 아이콘(체크 표시)으로 동작 확인 | main만 |
| 2026-11-20 | llm/20261120/basic | 위쪽 고정 목차에 지금 보는 절 표시(scrollspy): 해당 절 링크가 채운 알약으로 바뀜(다크 포함), 페이지 끝이면 마지막 절. 목차는 모든 폭에서 한 줄(넘치면 가로 스크롤, 1240px 이하 양 끝 흐림, 지금 절을 가운데로 자동 이동), 휴대폰에서도 고정. 사이트 메뉴 높이를 재서 목차 위치·앵커 이동 여백 맞춤. ego lite 1656·1280·1024·390px 확인 | main만 |
| 2026-11-20 | llm/20261120 · spec | 1·2번 탭 nav.sec-nav도 3번 탭과 같은 고정 목차 + 지금 보는 절 표시(알약, 한 줄 띠, 좁은 폭 가운데 이동, 휴대폰 고정). CSS·JS만 추가, 본문 텍스트·태그 동일 확인(493·1516 노드). ego lite 1656px·390px 다크 확인 | main만 |
| 2026-11-20 | 배포 | release 0714ff0 (main cd60a5c, --release --as-of 2026-11-20, Docker 제외): Day25 3번 탭 Basic 완주 안내, 세 탭 고정 목차·지금 보는 절 표시. 실제 사이트 확인: Day25 3쪽 200 · /setup/docker/ 404 · ego lite에서 세 탭 탭 줄 3개·목차 고정(top 48)·현재 절 표시 동작 | 배포 |
| 2026-11-20 | llm/20261120 · spec · basic | 탭을 바꿔도 위쪽이 움직이지 않게: 3번 탭 머리말을 1·2번과 같은 CSS로(여백 34·제목 33px·부제 15px·그라데이션·테두리), 부제 두 줄을 " · "로 한 줄(사용자 승인), 세 탭 모두 부제 자리를 960px 이하 2줄·480px 이하 3줄로 확보, 3번 탭 탭 줄·목차 띠 간격·높이를 1·2번과 같게. 1920~360px 12개 폭에서 머리말·탭 줄·목차 띠 위치·높이 세 탭 동일, 다크 색 동일 확인. 남은 것: 601~759px에서 사이트 메뉴(cn-nav) 두 줄 꺾임이 탭마다 다름(web/nav.css, 별도) | main만 |
| 2026-11-20 | 배포 | release 767baae (main 8309761, --release --as-of 2026-11-20, Docker 제외): Day25 세 탭 머리말·탭 줄·목차 띠 위치 통일. 실제 사이트 확인: Day25 3쪽 200 · /setup/docker/ 404 · 1656·390px에서 세 탭 머리말·탭 줄·목차 위치 동일 | 배포 |
