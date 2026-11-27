-- pgAdmin에서 report_agent_lab에 연결한 후 실행. DB/테이블/Seed 생성 절대 금지.
BEGIN TRANSACTION READ ONLY;
SELECT current_database(), current_user;
SELECT extname,extversion FROM pg_extension WHERE extname='vector';
SELECT code,name FROM public.report_categories ORDER BY category_id;
SELECT to_regclass('public.reports'),to_regclass('public.report_embeddings'),to_regclass('public.report_read_view');
SELECT index_status,count(*) FROM public.reports GROUP BY index_status ORDER BY index_status;
SELECT count(*) AS eligible_vectors FROM public.reports r JOIN public.report_embeddings e USING(report_id)
JOIN public.report_read_view v USING(report_id)
WHERE r.index_status='ready' AND e.model_name='intfloat/multilingual-e5-small'
AND e.indexed_revision=r.revision AND public.vector_dims(e.embedding)=384 AND public.vector_norm(e.embedding)>0
AND e.overview_hash=encode(sha256(convert_to(r.overview,'UTF8')),'hex');
SELECT report_id,title,category_code,revision,index_status FROM public.report_read_view
WHERE report_id IN (1,2,16,25,63,64,91,131,137,152,161) ORDER BY report_id;
ROLLBACK;
