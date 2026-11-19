"""강의 트리(tree.md) 읽기와 '강의 목차 한눈에 보기' 블록."""
import html
import re

from .config import web


# ── 강의 트리 (교재 구성) ──────────────────────────────────────────────
TREE_LINE = re.compile(r"^([│ ]*)([├└]─ )?(.*)$")
PDF_PAGE = re.compile(r"\s*\((PDF p\.[^)]*)\)\s*$")
LAB = re.compile(r"^실습\s*\d|일일\s*프로젝트")


def read_tree(path):
    """tree.md의 첫 ```text 블록 → (교재 제목 또는 None, [묶음 {t, c}])"""
    m = re.search(r"```text\n(.*?)```", path.read_text(encoding="utf-8"), re.S)
    assert m, f"```text 블록 없음: {path}"
    roots, stack = [], []
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        prefix, conn, label = TREE_LINE.match(line).groups()
        depth = len(prefix) // 3 + 1 if conn else 0
        node = {"t": label.strip(), "c": []}
        while stack and stack[-1][0] >= depth:
            stack.pop()
        (stack[-1][1]["c"] if stack else roots).append(node)
        stack.append((depth, node))
    if len(roots) == 1 and roots[0]["c"]:      # 맨 위 한 줄이 교재 제목인 형식 (Day21)
        return roots[0]["t"], roots[0]["c"]
    return None, roots


def tree_leaves(n):
    return 1 if not n["c"] else sum(tree_leaves(c) for c in n["c"])


def tree_item(n):
    """카드 안 한 줄: 화면 제목(+ PDF 쪽). 가운데 묶음이 있으면 작은 소제목 아래로 넣는다."""
    t = n["t"]
    pg = PDF_PAGE.search(t)
    if pg:
        t = t[:pg.start()]
    if n["c"]:
        return f'<li class="lt-sg"><span>{html.escape(t)}</span><ul>{"".join(tree_item(c) for c in n["c"])}</ul></li>'
    page = f'<em>{html.escape(pg.group(1).replace("PDF ", ""))}</em>' if pg else ""
    return f'<li{" class=lt-lab" if LAB.search(t) else ""}><span>{wbr(t)}</span>{page}</li>'


def wbr(t):
    """가운뎃점(·)으로 이은 긴 영어 낱말이 좁은 카드에서 글자 중간에 끊기지 않게, · 뒤에서 줄을 바꿀 수 있게 한다."""
    return html.escape(t).replace("·", "·<wbr>")


def tree_flat(n):
    return [n] if not n["c"] else [x for c in n["c"] for x in tree_flat(c)]


# '강의 목차 한눈에 보기' 블록의 스타일. 요약 페이지에도 그대로 끼워 넣을 수 있게 .lt 안에서만 쓰고 색도 따로 둔다.
TREE_CSS = "<style>\n" + web("tree.css") + "</style>"


def day_top(d):
    """요약 페이지 제목 아래 블록: 강의 목차 한눈에 보기 (자료 링크는 상단 메뉴에 둔다)"""
    return TREE_CSS + (tree_block(d["tree"], css=False) if d["tree"] else "")


def pull_labs(nodes):
    """실습 화면을 어느 깊이에 있든 뽑아낸다 → (실습들, 나머지). 실습만 있던 가운데 묶음은 지운다."""
    labs, keep = [], []
    for c in nodes:
        if c["c"]:
            sub_labs, sub_keep = pull_labs(c["c"])
            labs += sub_labs
            if sub_keep:
                keep.append({"t": c["t"], "c": sub_keep})
        elif LAB.search(c["t"]):
            labs.append(c)
        else:
            keep.append(c)
    return labs, keep


def lab_row(c):
    t = c["t"]
    pg = PDF_PAGE.search(t)
    if pg:
        t = t[:pg.start()]
    page = f'<em>{html.escape(pg.group(1).replace("PDF ", ""))}</em>' if pg else ""
    # 카드 머리에 교시 번호가 이미 있으므로, 실습 띠에서는 '실습 01 · ' 같은 앞 번호를 빼고 설명만 남긴다.
    label = re.sub(r"^실습\s*(?:\d+\s*[·.]\s*)?", "", t)
    return f'<p class="lt-lab-row"><b>실습</b><span>{wbr(label)}</span>{page}</p>'


def tree_block(path, open_=False, css=True):
    """'강의 목차 한눈에 보기'(강사님 강의 자료 기준): 누르면 교시 카드 판이 펼쳐진다.
    교시마다 카드 하나에 원문 화면 제목을 모두 적고, 실습은 카드 맨 아래 띠로 둔다."""
    _, groups = read_tree(path)
    intro = [g for g in groups if g["t"].partition(" · ")[0] == "도입" and tree_leaves(g) <= 3]
    cards = []
    for g in groups:
        if g in intro:
            continue
        head, _, rest = g["t"].partition(" · ")
        labs, body = pull_labs(g["c"])
        name = (rest or head).strip().lower()
        body = [c for c in body if c["c"] or c["t"].strip().lower() != name]   # 교시 이름과 같은 화면(교시 표지)은 뺀다
        lab = "".join(lab_row(c) for c in labs)
        cards.append(f'<article class="lt-cd"><header><span class="lt-n">{html.escape(head) if rest else ""}</span>'
                     f'<span class="lt-c">화면 {tree_leaves(g)}</span><h3>{html.escape(rest or head)}</h3></header>'
                     f'<ol>{"".join(tree_item(c) for c in body)}</ol>{lab}</article>')
    strip = ""
    if intro:
        items = " · ".join(html.escape(n["t"]) for g in intro for n in tree_flat(g))
        strip = f'<p class="lt-intro"><b>도입</b><span>{items}</span></p>'
    total = sum(tree_leaves(g) for g in groups)
    return f"""{TREE_CSS if css else ""}<section class="lt" id="lecture-tree" aria-label="강의 목차">
<details class="lt-box"{" open" if open_ else ""}>
<summary><span class="lt-t"><b>강의 목차 한눈에 보기</b><small>강사님 강의 자료 기준 · {len(cards)}개 묶음 · 화면 {total}개</small></span>
<span class="lt-btn"><span class="o">펼치기</span><span class="c">접기</span></span></summary>
<div class="lt-body">{strip}<div class="lt-board">{"".join(cards)}</div>
<p class="lt-note">강의 자료의 화면 제목을 원문 그대로 옮겼습니다. 실습은 각 교시 카드 맨 아래에 모았습니다.</p></div>
</details></section>"""
