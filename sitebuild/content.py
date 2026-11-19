"""내용 페이지 복사: pages/의 요약·가이드·강의 HTML을 public/에 옮기며 메뉴·글꼴·통계를 끼운다."""
import html
import posixpath
import re
import shutil

from .config import FILES, HERE, ICON_DL, PUBLIC, RELEASE, SETUP
from .fonts import unify_fonts
from .nav import ANALYTICS, DOWNLOAD_MARK, THEME_MARK, add_theme, add_totop


# 사이트 안 다른 페이지로 가는 링크는 data-site를 붙여 두면 살린다
LOCAL_LINK = re.compile(r'<a\s(?![^>]*data-site)[^>]*href="(?!https?:|#|mailto:|data:)[^"]*"[^>]*>(.*?)</a>', re.S)


SCRIPT_BLOCK = re.compile(r"(<script\b.*?</script>)", re.S | re.I)


def strip_local_links(text):
    """<script> 밖의 상대 링크만 글자로 바꾼다. 스크립트 안의 HTML 문자열은 그대로 둔다."""
    parts = SCRIPT_BLOCK.split(text)
    count = 0
    for i in range(0, len(parts), 2):
        parts[i], n = LOCAL_LINK.subn(r"<span>\1</span>", parts[i])
        count += n
    return "".join(parts), count


HIDDEN_LINK = re.compile(r'<a\b[^>]*\bhref="([^"#]*)(#[^"]*)?"[^>]*>(.*?)</a>', re.S)


def strip_hidden_links(text, dest):
    """--release에서만: 공개 전 설치 가이드로 가는 링크를 글자로 바꾼다 (라이브에서 404가 나지 않게)."""
    if not RELEASE:
        return text, 0
    hidden = {f"setup/{k}" for k, v in SETUP.items() if not v[4]}

    def repl(m):
        href = m.group(1)
        if not href or "://" in href or href.startswith(("mailto:", "/")):
            return m.group(0)
        target = posixpath.normpath(posixpath.join(dest, href)).strip("/")
        if any(target == h or target.startswith(h + "/") for h in hidden):
            return f"<span>{m.group(3)}</span>"
        return m.group(0)

    parts = SCRIPT_BLOCK.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = HIDDEN_LINK.sub(repl, parts[i])
    new = "".join(parts)
    return new, len(HIDDEN_LINK.findall(text)) - len(HIDDEN_LINK.findall(new))


def download_name(text):
    """받는 파일 이름: 페이지 <title>에서 · ( ) 공백을 _로. 예: Day10_최적화와_규제.html"""
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    name = html.unescape(m.group(1)) if m else "page"
    name = re.sub(r"[\\/:*?\"<>|·()\[\]–—|-]+", " ", name)
    name = re.sub(r"\s+", "_", name.strip())[:60].strip("_")
    return f"{name}.html"


def copy_lecture(src, dest, nav):
    """강사님 강의 HTML: 원본은 손대지 않고 download.html로 두고(받기용), 글꼴만 Pretendard로 바꾼 view.html을 사이트 메뉴 아래 화면 전체에 띄운다.
    (강의 HTML은 자체 고정 머리·아래 막대가 있어 메뉴를 끼워 넣으면 겹친다)"""
    original = (src / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<title>(.*?)</title>", original, re.S)
    title = m.group(1).strip() if m else "강의 자료"
    link = (f'<a class="cn-ico cn-dl" href="download.html" download="{html.escape(download_name(original))}" '
            f'data-tip="HTML 파일 하나로 받기 (인터넷 없이 열림)" aria-label="HTML 파일 하나로 받기">{ICON_DL}</a>')
    page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>html,body{{margin:0;height:100%}}body{{display:flex;flex-direction:column;height:100dvh;background:#fff}}
.lecture-frame{{flex:1;width:100%;border:0;display:block}}</style>
{ANALYTICS}
</head>
<body>{nav.replace(DOWNLOAD_MARK, link).replace(THEME_MARK, "")}<iframe class="lecture-frame" src="view.html" title="{title}"></iframe></body>
</html>
"""
    out = PUBLIC / dest
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "download.html").write_text(original, encoding="utf-8")   # 받기용: 강의 원본 그대로
    (out / "view.html").write_text(unify_fonts(original, dest, lecture=True), encoding="utf-8")   # 사이트 화면용: 본문만 Pretendard(96%)
    print(f"  /{dest}/ ← {src.relative_to(HERE)} (download.html 원본 + view.html 글꼴만 Pretendard)")


def copy_page(src, dest, nav, top="", totop=False):
    """top: 요약 제목 아래에 끼울 블록(자료 줄 + 강의 목차). 사이트 화면에만 넣고 download.html 원본에는 넣지 않는다.
    totop: 강의 요약이면 오른쪽 아래 맨 위로 버튼을 넣는다(사이트 화면에만)."""
    original = (src / "index.html").read_text(encoding="utf-8")
    original, n_hidden = strip_hidden_links(original, dest)
    text, n_links = strip_local_links(original)
    if top:
        text = insert_after_title(text, top)
    link = (f'<a class="cn-ico cn-dl" href="download.html" download="{html.escape(download_name(original))}" '
            f'data-tip="HTML 파일 하나로 받기 (인터넷 없이 열림)" aria-label="HTML 파일 하나로 받기">{ICON_DL}</a>')
    nav = nav.replace(DOWNLOAD_MARK, link)
    text = unify_fonts(text, dest)
    text, nav = add_theme(text, nav, "prefers-color-scheme" in original)   # 끼운 목차 블록의 CSS가 아니라 원본 기준
    if totop:
        text = add_totop(text, "prefers-color-scheme" in original)
    text, n_body = re.subn(r"(<body[^>]*>)", lambda m: m.group(1) + nav + ANALYTICS, text, count=1)
    assert n_body == 1, f"<body> 없음: {src}"
    out = PUBLIC / dest
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(text, encoding="utf-8")
    (out / "download.html").write_text(original, encoding="utf-8")   # 사이트 메뉴·통계 없는 원본
    for name in FILES.get(dest, []):
        shutil.copy2(src / name, out / name)
    note = f" (사이트에 없는 링크 {n_links}개를 글자로)" if n_links else ""
    note += f" (공개 전 가이드 링크 {n_hidden}개를 글자로)" if n_hidden else ""
    print(f"  /{dest}/ ← {src.relative_to(HERE)}{note}")


def insert_after_title(text, block):
    """요약 페이지의 제목 머리(<h1>을 감싼 <header>) 바로 뒤에 넣는다. 머리가 없으면 </h1> 뒤."""
    m = re.search(r"<h1\b", text)
    assert m, "<h1> 없음"
    end = text.find("</header>", m.end())
    nxt = min([i for i in (text.find("<section", m.end()), text.find("<h2", m.end())) if i != -1], default=len(text))
    if end != -1 and end < nxt:
        # 머리 안쪽 끝(제목과 같은 폭의 감싸개 안)에 넣는다: <header><div class="wrap">…</div></header>이면 그 </div> 앞
        inner = text[m.end():end].rstrip()
        before = text[text.rfind("<header", 0, m.start()):m.start()]
        wrapped = before.count("<div") - before.count("</div>") > 0      # 제목이 머리 안의 <div> 감싸개 속에 있다
        at = m.end() + len(inner) - len("</div>") if wrapped and inner.endswith("</div>") else end
    else:
        at = text.find("</h1>", m.end()) + len("</h1>")
    light = "" if "prefers-color-scheme" in text else " lt-light"   # 다크 모드가 없는 요약은 블록도 밝게 둔다
    return text[:at] + f'\n<div class="lt-top{light}">{block}</div>\n' + text[at:]
