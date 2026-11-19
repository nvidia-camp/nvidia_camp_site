-- Day25 Report Agent v1.4 · DB 사전 점검 (읽기 전용)
-- 실행 순서: 필요하면 postgres DB에서 00_create_database.sql 실행
--            → report_agent_lab에 다시 연결 → 이 파일 → schema.sql → seed.sql
-- pgAdmin에서 report_agent_lab의 Query Tool을 열고 실행하세요.
-- 아래 문장은 SELECT/SHOW만 사용하며 vector 확장 함수를 호출하지 않습니다.

-- 1. correct_database=true, PostgreSQL 18 계열, UTF8인지 확인합니다.
-- correct_database=false이면 report_agent_lab에 다시 연결한 뒤 점검하세요.
SELECT current_database() AS connected_database,
       current_database()='report_agent_lab' AS correct_database,
       current_user AS connected_user,
       current_setting('server_version') AS server_version,
       current_setting('server_encoding') AS server_encoding,
       current_schema() AS current_schema;

-- 2. 기본 실습 스키마는 public입니다.
-- current_schema가 다르거나 public이 검색 경로에 없다면 강사와 연결 설정을 확인합니다.
SHOW search_path;

-- 3. vector_available_to_install=true: 서버가 vector 설치 정보를 인식합니다.
-- false이면 Windows PostgreSQL 서버용 pgvector 설치를 먼저 확인하세요.
-- Python의 pgvector 패키지 설치와 서버 확장 설치는 별도입니다.
-- schema.sql 실행 전에는 vector_active_in_this_database=false도 정상입니다.
-- 실제 활성화 성공은 schema.sql 실행으로 확인합니다.
SELECT EXISTS (
           SELECT 1 FROM pg_available_extensions WHERE name='vector'
       ) AS vector_available_to_install,
       (SELECT default_version FROM pg_available_extensions WHERE name='vector')
           AS vector_default_version,
       EXISTS (
           SELECT 1 FROM pg_extension WHERE extname='vector'
       ) AS vector_active_in_this_database,
       (SELECT extversion FROM pg_extension WHERE extname='vector')
           AS vector_active_version;

-- 4. 처음 만드는 실습 DB라면 아래 결과는 0행이 정상입니다.
-- 결과가 있으면 이전 실습 상태인지 확인하세요. 기존 테이블을 임의로 삭제하지 않습니다.
-- schema.sql의 IF NOT EXISTS는 이미 있는 테이블 구조를 고쳐 주지 않습니다.
SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema='public'
  AND table_name IN (
      'report_categories', 'reports', 'report_embeddings',
      'experiment_reports', 'daily_work_reports', 'research_plans',
      'data_processing_reports', 'prompt_reports', 'meeting_minutes',
      'prompt_versions', 'report_read_view'
  )
ORDER BY table_name;

-- 이 사전 점검은 DB 접속과 확장 준비 상태를 확인합니다.
-- 데이터 적재·180건 E5 인덱싱 완료 여부는 이후 verify.sql로 확인하세요.
-- 이 파일은 실제 강의 PostgreSQL 환경에서 실행 검증하지 않은 제공본입니다.
