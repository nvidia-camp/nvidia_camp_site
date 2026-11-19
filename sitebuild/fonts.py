"""글꼴 통일: 본문은 Pretendard만, 코드(monospace)는 예외."""
import re

from .config import PUBLIC


# ── 글꼴 통일: 본문은 Pretendard만, 코드(monospace)는 예외 ─────────────────
PRETENDARD_LINK = '<link rel="stylesheet" href="/fonts/pretendard/pretendardvariable-dynamic-subset.css">'
PRETENDARD_STACK = '"Pretendard Variable", Pretendard, '
# 강사님 강의 페이지용: 원래 글꼴(맑은 고딕·Apple SD)과 줄바꿈이 비슷하도록 Pretendard를 96%로 줄인 글꼴 (2026-11-17 비교 확인)
LECTURE_FAMILY = "PretendardLecture"      # 공백·따옴표가 없어야 강의 스크립트 안의 글꼴 문자열에 들어가도 문법이 안 깨진다
LECTURE_SIZE_ADJUST = 96
LECTURE_CSS = "/fonts/pretendard/pretendard-lecture.css"
LECTURE_LINK = f'<link rel="stylesheet" href="{LECTURE_CSS}">'
FONT_DECL = re.compile(r"(font-family|--font[\w-]*|--sans)(\s*:\s*)((?:\"[^\"\n]*\"|'[^'\n]*'|[^;}\"'<\n])+)")
MONO_HINT = re.compile(r"monospace|consolas|menlo|sf mono|sfmono|courier|var\(", re.I)
FONT_WARNINGS = []
FONT_FIXED = []
FONT_SHORT = re.compile(r"((?<![\w-])font\s*:\s*)([^;}\"<]+)")
FONT_FAMILY_TAIL = re.compile(r"\s((?:'[^']*'|\"[^\"]*\"|[A-Za-z][\w-]*)(?:\s*,\s*(?:'[^']*'|\"[^\"]*\"|[A-Za-z][\w-]*))*)\s*$")


def unify_fonts(text, label, lecture=False):
    """페이지 안의 글꼴 선언 중 코드용이 아닌 것은 Pretendard를 맨 앞에 붙이고, 링크가 없으면 넣는다.
    덮어쓸 수 없는 경우(font: 줄임 표기 등)는 경고만 남긴다(빌드는 계속)."""
    stack = f"{LECTURE_FAMILY}, " if lecture else PRETENDARD_STACK
    links = (LECTURE_LINK + "\n" if lecture else "") + PRETENDARD_LINK     # 강의 페이지의 위쪽 메뉴는 원래 Pretendard를 쓴다

    def fix(m):
        value = m.group(3)
        if "pretendard" in value.lower() or MONO_HINT.search(value) or value.strip().lower().startswith("inherit"):
            return m.group(0)     # inherit 앞에 글꼴을 붙이면 선언이 무효가 돼 코드 조각이 기본 monospace로 바뀐다
        return m.group(1) + m.group(2) + stack + value.lstrip()
    text = FONT_DECL.sub(fix, text)
    if lecture:   # 강의 원본의 보안 정책(CSP)은 글꼴·외부 CSS를 막는다: 우리 사이트 것(self)만 허용
        text = text.replace("style-src 'unsafe-inline';", "style-src 'unsafe-inline' 'self';").replace("font-src 'none';", "font-src 'self';")
    if "pretendardvariable" not in text:
        text, n = re.subn(r"</head>", lambda m: links + "\n</head>", text, count=1)
        if not n:
            FONT_WARNINGS.append(f"{label}: <head>가 없어 Pretendard 링크를 못 넣음")
    # font 줄임 표기(font:500 15px/1.6 'Segoe UI',sans-serif): 맨 끝 글꼴 목록 앞에 Pretendard를 붙인다
    def fix_short(m):
        value = m.group(2)
        if "pretendard" in value.lower() or MONO_HINT.search(value) or value.strip().lower().startswith("inherit"):
            return m.group(0)
        fam = FONT_FAMILY_TAIL.search(value)
        if not fam or not re.search(r"\d", value[:fam.start()]):
            return m.group(0)
        FONT_FIXED.append(label)
        return m.group(1) + value[:fam.start(1)] + stack + value[fam.start(1):]
    text = FONT_SHORT.sub(fix_short, text)
    for m in FONT_SHORT.finditer(text):
        value = m.group(2)
        fam = FONT_FAMILY_TAIL.search(value)
        if fam and "pretendard" not in value.lower() and not MONO_HINT.search(value) and not value.strip().lower().startswith("inherit"):
            FONT_WARNINGS.append(f"{label}: font 줄임 표기에 Pretendard 아닌 글꼴 → {fam.group(1).strip()[:60]}")
    return text


def write_lecture_font_css():
    """강의 페이지용 글꼴 CSS: 같은 Pretendard 파일을 다른 이름으로 선언하고 size-adjust로 줄인다."""
    base = (PUBLIC / "fonts/pretendard/pretendardvariable-dynamic-subset.css").read_text(encoding="utf-8")
    css = base.replace("'Pretendard Variable'", f"'{LECTURE_FAMILY}'")
    css = css.replace("font-display: swap;", f"font-display: swap;\n\tsize-adjust: {LECTURE_SIZE_ADJUST}%;")
    assert css.count("size-adjust") == css.count("@font-face") > 0
    (PUBLIC / LECTURE_CSS.lstrip("/")).write_text(css, encoding="utf-8")
