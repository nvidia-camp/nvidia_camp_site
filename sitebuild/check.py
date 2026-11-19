"""빌드 결과(public/) 검사. 사용: uv run --no-project python -m sitebuild.check [--release]

make check가 main 빌드와 --release 빌드 뒤에 각각 돌린다. 하나라도 어기면 종료 코드 1.
  1. 사이트 화면(index.html)마다 GA 측정 ID가 한 번 들어 있다
  2. 원본(download.html)과 강의 화면(view.html)에는 통계 코드가 없다
  3. --release 빌드에는 공개 전 가이드(site.toml public = false)의 폴더도, 그쪽으로 가는 링크도 없다
"""
import re
import sys

from .config import PUBLIC, SETUP, web

RELEASE_CHECK = "--release" in sys.argv
GA_ID = re.search(r"GA_ID = '([^']+)'", web("analytics.js")).group(1)


def main():
    problems = []
    pages = sorted(PUBLIC.rglob("*.html"))
    if not pages:
        sys.exit("public/이 비어 있음: 먼저 빌드하세요")
    for p in pages:
        text = p.read_text(encoding="utf-8")
        rel = p.relative_to(PUBLIC)
        if p.name in ("download.html", "view.html"):
            if "googletagmanager" in text or "_vercel/insights" in text:
                problems.append(f"{rel}: 원본·강의 화면에 통계 코드가 들어감")
        elif p.name == "index.html" and text.count(GA_ID) != 1:
            problems.append(f"{rel}: GA 측정 ID가 {text.count(GA_ID)}번 (1번이어야 함)")
    if RELEASE_CHECK:
        for key, (*_, public) in SETUP.items():
            if public:
                continue
            if (PUBLIC / "setup" / key).exists():
                problems.append(f"setup/{key}/: 공개 전 가이드가 --release 빌드에 있음")
            for p in pages:
                if re.search(rf'href="[^"]*setup/{re.escape(key)}/', p.read_text(encoding="utf-8")):
                    problems.append(f"{p.relative_to(PUBLIC)}: 공개 전 가이드 setup/{key}/로 가는 링크")
    kind = "release" if RELEASE_CHECK else "main"
    if problems:
        print(f"✗ {kind} 빌드 검사 실패 {len(problems)}건")
        for x in problems:
            print("  -", x)
        sys.exit(1)
    print(f"✓ {kind} 빌드 검사 통과: HTML {len(pages)}개")


if __name__ == "__main__":
    main()
