-- report_agent_lab DB가 없을 때만 1회 실행.
-- pgAdmin에서 기본 postgres DB에 연결 후 실행하세요.
-- CREATE DATABASE는 트랜잭션 블록 내부에서 실행하지 마세요.
-- 이미 DB가 존재하면 이 파일을 건너뜁니다. 다른 강의 DB는 삭제하지 마세요.
CREATE DATABASE report_agent_lab WITH ENCODING 'UTF8' TEMPLATE template0;
