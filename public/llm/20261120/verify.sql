-- Report Agent v1.4 · 읽기 전용 검증
-- 1단계: schema.sql + seed.sql 직후에는 벡터 0개, pending 180개가 정상입니다.
-- 2단계: 실제 index_overviews.py 완료 후에는 벡터 180개, ready 180개여야 합니다.
-- CREATE/DELETE, Prompt 버전 생성 후에는 현재 행 수가 초기 기대값과 달라집니다.
-- 아래 expected_seed / expected_indexed는 처음 제공한 시드 상태의 기준입니다.
-- 뒤의 무결성 검사(error_count)는 요청/인덱싱이 끝난 시점에 모두 0이어야 합니다.

SELECT 'report_categories' AS name, COUNT(*) AS actual,
       6 AS expected_seed, 6 AS expected_indexed FROM report_categories
UNION ALL SELECT 'reports',COUNT(*),180,180 FROM reports
UNION ALL SELECT 'experiment_reports',COUNT(*),30,30 FROM experiment_reports
UNION ALL SELECT 'daily_work_reports',COUNT(*),30,30 FROM daily_work_reports
UNION ALL SELECT 'research_plans',COUNT(*),30,30 FROM research_plans
UNION ALL SELECT 'data_processing_reports',COUNT(*),30,30 FROM data_processing_reports
UNION ALL SELECT 'prompt_reports',COUNT(*),30,30 FROM prompt_reports
UNION ALL SELECT 'meeting_minutes',COUNT(*),30,30 FROM meeting_minutes
UNION ALL SELECT 'prompt_versions',COUNT(*),60,60 FROM prompt_versions
UNION ALL SELECT 'report_embeddings',COUNT(*),0,180 FROM report_embeddings;

SELECT c.code,COUNT(*) AS report_count
FROM reports r JOIN report_categories c ON r.category_id=c.category_id
GROUP BY c.code ORDER BY c.code;
SELECT index_status,COUNT(*) AS actual FROM reports GROUP BY index_status;

-- Vector(384), 현재 revision, 명세서의 E5 모델, 실제 개요 내용이 모두 맞아야 합니다.
-- sha256/convert_to/encode는 PostgreSQL 18 내장 함수이며 pgcrypto 설치가 필요 없습니다.
-- Python hashlib.sha256(overview.encode('utf-8')).hexdigest()와 같은 기준입니다.
SELECT 'invalid_vector_dimension' AS check_name, COUNT(*) AS error_count
FROM report_embeddings WHERE vector_dims(embedding)<>384
UNION ALL
SELECT 'stale_vector_revision_or_status',COUNT(*)
FROM report_embeddings e JOIN reports r USING(report_id)
WHERE e.indexed_revision<>r.revision OR r.index_status<>'ready'
UNION ALL
SELECT 'wrong_embedding_model',COUNT(*)
FROM report_embeddings WHERE model_name<>'intfloat/multilingual-e5-small'
UNION ALL
SELECT 'overview_hash_mismatch',COUNT(*)
FROM report_embeddings e JOIN reports r USING(report_id)
WHERE e.overview_hash<>encode(sha256(convert_to(r.overview,'UTF8')),'hex')
UNION ALL
SELECT 'ready_without_valid_vector',COUNT(*)
FROM reports r LEFT JOIN report_embeddings e USING(report_id)
WHERE r.index_status='ready' AND (
    e.report_id IS NULL OR e.indexed_revision<>r.revision
    OR e.model_name<>'intfloat/multilingual-e5-small'
    OR vector_dims(e.embedding)<>384
    OR e.overview_hash<>encode(sha256(convert_to(r.overview,'UTF8')),'hex')
);

-- 한 보고서는 자기 카테고리의 상세 테이블에 정확히 한 행만 있어야 합니다.
WITH all_details AS (
    SELECT report_id,'EXPERIMENT' AS detail_code FROM experiment_reports
    UNION ALL SELECT report_id,'DAILY_WORK' FROM daily_work_reports
    UNION ALL SELECT report_id,'RESEARCH_PLAN' FROM research_plans
    UNION ALL SELECT report_id,'DATA_PROCESSING' FROM data_processing_reports
    UNION ALL SELECT report_id,'PROMPT' FROM prompt_reports
    UNION ALL SELECT report_id,'MEETING' FROM meeting_minutes
)
SELECT 'missing_or_multiple_details' AS check_name,COUNT(*) AS error_count
FROM (
    SELECT r.report_id
    FROM reports r LEFT JOIN all_details d USING(report_id)
    GROUP BY r.report_id HAVING COUNT(d.report_id)<>1
) invalid
UNION ALL
SELECT 'wrong_detail_category',COUNT(*)
FROM all_details d JOIN reports r USING(report_id)
JOIN report_categories c ON c.category_id=r.category_id
WHERE d.detail_code<>c.code
UNION ALL
SELECT 'detail_missing_in_read_view',COUNT(*)
FROM reports r LEFT JOIN report_read_view v USING(report_id)
WHERE v.report_id IS NULL;

-- title/content/author/날짜는 상세 테이블의 값이며 API에서 함께 반환됩니다.
SELECT 'invalid_common_text_or_time' AS check_name,COUNT(*) AS error_count
FROM report_read_view
WHERE title IS NULL OR char_length(btrim(title)) NOT BETWEEN 1 AND 200
   OR content IS NULL OR char_length(btrim(content)) NOT BETWEEN 1 AND 20000
   OR author IS NULL OR char_length(btrim(author)) NOT BETWEEN 1 AND 100
   OR create_at IS NULL OR update_at IS NULL OR update_at<create_at
UNION ALL
SELECT 'invalid_overview_or_revision',COUNT(*) FROM reports
WHERE overview IS NULL OR char_length(btrim(overview)) NOT BETWEEN 10 AND 1000
   OR revision IS NULL OR revision<1
UNION ALL
SELECT 'missing_required_detail_date',
    (SELECT COUNT(*) FROM experiment_reports WHERE experiment_date IS NULL)
  + (SELECT COUNT(*) FROM daily_work_reports WHERE work_date IS NULL)
  + (SELECT COUNT(*) FROM research_plans WHERE target_date IS NULL)
  + (SELECT COUNT(*) FROM meeting_minutes WHERE meeting_at IS NULL);

-- Prompt 생성/활성 전환 후에도 활성 버전이 실제 존재하며 본문과 같아야 합니다.
SELECT 'missing_active_prompt_version' AS check_name,COUNT(*) AS error_count
FROM prompt_reports p LEFT JOIN prompt_versions v
  ON v.report_id=p.report_id AND v.version_no=p.active_version_no
WHERE v.prompt_version_id IS NULL
UNION ALL
SELECT 'active_prompt_content_mismatch',COUNT(*)
FROM prompt_reports p JOIN prompt_versions v
  ON v.report_id=p.report_id AND v.version_no=p.active_version_no
WHERE p.content IS DISTINCT FROM v.prompt_text;

-- 검색 결과의 원문·출처를 확인하는 조회입니다. 출력 건수를 고정 정답으로 삼지 않습니다.
SELECT report_id,title,author,category_code FROM report_read_view
WHERE title ILIKE '%가중치%' ORDER BY report_id LIMIT 10;
