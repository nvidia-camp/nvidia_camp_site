# 자주 쓰는 명령. site 폴더에서 make <이름>.  (예: make check)
# 날짜를 고정하려면 AS_OF=2026-11-19 를 붙인다. 비우면 지금 시각 기준(18:20부터 다음 수업일).
AS_OF ?=
DATE_ARG = $(if $(AS_OF),--as-of $(AS_OF),)
SNAP ?= .snapshot

.PHONY: build release serve check lint snapshot compare

build:            ## main 빌드: 공개 전 페이지까지 public/에
	uv run --quiet build_site.py $(DATE_ARG)

release:          ## 배포용 빌드: 공개 전 페이지 제외
	uv run --quiet build_site.py --release $(DATE_ARG)

serve:            ## 내 컴퓨터에서 보기: http://localhost:8000
	python3 -m http.server -d public 8000

lint:             ## 코드 검사: 파이썬(ruff) + 자바스크립트 문법
	uvx ruff check build_site.py sitebuild
	@for f in web/*.js; do node --check $$f || exit 1; done; echo "✓ web/*.js 문법 통과"

check: lint       ## 커밋 전 검사: lint → main 빌드 검사 → release 빌드 검사
	uv run --quiet build_site.py $(DATE_ARG) > /dev/null
	uv run --quiet --no-project python -m sitebuild.check
	uv run --quiet build_site.py --release $(DATE_ARG) > /dev/null
	uv run --quiet --no-project python -m sitebuild.check --release

snapshot:         ## 고치기 전 빌드 저장 (결과가 안 바뀌어야 하는 정리 작업용): make snapshot AS_OF=…
	uv run --quiet build_site.py $(DATE_ARG) > /dev/null
	rm -rf $(SNAP) && cp -R public $(SNAP) && echo "✓ $(SNAP)/에 저장"

compare:          ## 고친 뒤 빌드가 snapshot과 같은지: make compare AS_OF=… (같은 날짜로)
	uv run --quiet build_site.py $(DATE_ARG) > /dev/null
	diff -r $(SNAP) public && echo "✓ snapshot과 같음"
