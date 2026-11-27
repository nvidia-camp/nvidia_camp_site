"""Build Day30 site pages from the two supplied instructor documents."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
MATERIALS = HERE.parents[3] / "05_LLM_RAG" / "20261127"


def read(name):
    return (HERE / name).read_text(encoding="utf-8")


def replace_once(text, before, after):
    if text.count(before) != 1:
        raise ValueError(f"Expected one occurrence of {before[:100]}")
    return text.replace(before, after, 1)


def tabs(spec):
    links = [("./" if spec else "../", "요구사항 명세서 v1.1"),
             ("basic/" if spec else "./", "Basic 완주 안내 v2")]
    anchors = []
    for index, (url, label) in enumerate(links):
        active = ' aria-current="page"' if index == (0 if spec else 1) else ""
        anchors.append(f'<a data-site href="{url}"{active}>{label}</a>')
    return '<div class="day30-tabs" role="navigation" aria-label="Day30 프로젝트 자료">' + "".join(anchors) + "</div>"


def heading_and_extras(match):
    eyebrow, title, subtitle, extras = match.groups()
    title = re.sub(r"<br\s*/?>", " ", title)
    subtitle = re.sub(r"<br\s*/?>", " ", subtitle)
    return (
        '<header class="day30-heading">'
        f'{eyebrow}{title}{subtitle}</header>',
        extras.strip(),
    )


def build_spec(text):
    header = re.search(r'<header class="hero">(\s*<div class="eyebrow">.*?</div>)(\s*<h1>.*?</h1>)(\s*<p class="hero-lead">.*?</p>)(.*?)</header>', text, re.S)
    topbar = re.search(r'<div class="topbar">.*?</button></div></div>', text, re.S)
    toc = re.search(r'<nav class="toc"[^>]*>(.*?)</nav>', text, re.S)
    if not header or not topbar or not toc:
        raise ValueError("Missing SRS header, controls, or table of contents")
    banner, extras = heading_and_extras(header)
    links, _, requirement_search = toc[1].partition('<div class="toc-tools">')
    if not requirement_search:
        raise ValueError("Missing SRS requirement search")
    links = re.sub(r"^<header>.*?</header>", "", links)
    text = replace_once(text, topbar[0], "")
    text = replace_once(text, header[0], banner + tabs(spec=True) +
                        '<nav class="toc" aria-label="요구사항명세서 목차">' + links + '</nav>')
    text = replace_once(text, toc[0], "")
    text = replace_once(text, '<main class="content">', '<main class="content">' +
                        '<div class="spec-intro">' + topbar[0] + extras + '</div>')
    search_point = '<div class="requirement-toolbar">'
    text = replace_once(text, search_point, '<div class="toc-tools">' + requirement_search + search_point)
    for section, label in (
        ("sec01", "프로젝트 목표와 환경"),
        ("sec06", "RAG·Agent·API 구현 계약"),
        ("sec10", "검증·제출·기준 자료"),
    ):
        marker = f'<section class="doc-section" id="{section}">'
        text = replace_once(text, marker, f'<h2 class="doc-part">{label}</h2>' + marker)
    text, observers = re.subn(r"  const links=\$\$\('\.toc>a\[href\^=\"#\"\]'\);.*?(?=\n\}\)\(\);)", "", text, flags=re.S)
    if observers != 1:
        raise ValueError("Expected one original SRS scroll observer")
    # Keep the original Copy controls available in the standalone document.
    return text.replace('aria-label="코드 복사">Copy</button><pre>',
                        'aria-label="코드 복사">Copy</button><pre data-copy>')


def build_guide(text):
    header = re.search(r'<header>(\s*<div class="eyebrow">.*?</div>)(\s*<h1>.*?</h1>)(\s*<p class="lead">.*?</p>)(.*?)</header>', text, re.S)
    if not header:
        raise ValueError("Missing Basic guide header")
    banner, extras = heading_and_extras(header)
    text = replace_once(text, header[0], banner + tabs(spec=False))
    text = replace_once(text, "<main>", "<main>" + extras)
    text = replace_once(text, '<nav aria-label="목차">', '<nav class="toc" aria-label="목차">')
    return re.sub(r"<style>.*?</style>",
                  lambda m: re.sub(r"\bnav\b", "nav.toc", m[0]), text, flags=re.S)


def render(spec, pattern, target):
    (source,) = MATERIALS.glob(pattern)
    text = source.read_text(encoding="utf-8")
    text = build_spec(text) if spec else build_guide(text)
    styles = [read("document.css"), read("spec.css")] if spec else [read("guide.css"), read("document.css"), read("progress.css")]
    if spec:
        styles.append("@media screen {\n" + read("spec-light.css") + "\n}")
    scripts = [read("document.js")]
    if not spec:
        scripts.append(read("progress.js"))
    page_class = "spec-page" if spec else "guide-page"
    text = replace_once(text, "<body>", f'<body class="day30-page {page_class}">')
    text = replace_once(text, "</head>", "<style>\n" + "\n".join(styles) + "</style></head>")
    text = replace_once(text, "</body>", "<script>\n" + "\n".join(scripts) + "</script></body>")
    (HERE / target).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    render(True, "*v1.1.html", "index.html")
    render(False, "*v2.html", "basic/index.html")
