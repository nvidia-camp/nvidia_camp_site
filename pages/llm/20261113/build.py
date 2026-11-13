"""Day20 LLM·Transformer: template.html + 실행 기록(capture/capture.json) → index.html

- 그림 1(시스템 지도)·그림 3(LLM 안)은 아래 코드가 SVG로 그린다. 좌표는 이 파일에 있다.
- 화면의 숫자는 강의 슬라이드 코드(p.29·34·62·74)를 실행한 capture.json 에서 읽고,
  expect()로 슬라이드 값(p.8·p.63 Weight, p.74)과 대조한다.
기록을 새로 만들 때: cd capture && uv run --project ~/envs/dl python capture.py
실행: python3 build.py
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAP = json.loads((HERE / "capture" / "capture.json").read_text(encoding="utf-8"))
E = html.escape


def expect(cond, msg):
    assert cond, msg


P29, P34, P62, P74 = (CAP[k] for k in ("p29", "p34", "p62", "p74"))
W = P62["weights"]
PR = P74["probs"]["1.0"]
expect([round(x, 2) for x in W[0]] == [1.0, 0.0, 0.0], "p.63 t1 row")
expect([round(x, 2) for x in W[1]] == [0.33, 0.67, 0.0], "p.63 t2 row")
expect([round(x, 2) for x in W[2]] == [0.25, 0.25, 0.5], "p.63 t3 row")
expect(all(abs(s - 1) < 1e-6 for s in P62["row_sums"]), "row sums")
expect([round(x, 3) for x in PR] == [0.665, 0.245, 0.09], "p.74 T=1")
expect(P34["shape"][0] == 2 and P34["attention_mask"][0].count(0) == P34["tokens"][0].count("[PAD]"), "p.34 mask")

SPECIAL = {"[CLS]", "[SEP]", "[PAD]"}


def f(x, d=2):
    s = f"{x:.{d}f}"
    return "0" if float(s) == 0 else s


# ── SVG 부품 ─────────────────────────────────────────────
def cls_paths(paths):
    return ("pp " + " ".join(f"p-{p}" for p in paths.split())) if paths else ""


def node(x, y, w, h, title, sub="", badge="", cls="", paths="", href=None, sub2=""):
    g = [f'<g class="nd {cls} {cls_paths(paths)}">',
         f'<rect class="n" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>',
         f'<text class="t" x="{x + 12}" y="{y + 26}">{E(title)}</text>']
    if sub:
        g.append(f'<text class="s" x="{x + 12}" y="{y + 46}">{E(sub)}</text>')
    if sub2:
        g.append(f'<text class="s" x="{x + 12}" y="{y + 64}">{E(sub2)}</text>')
    if badge:
        g.append(f'<text class="bd" x="{x + w - 10}" y="{y + 18}" text-anchor="end">{E(badge)}</text>')
    g.append("</g>")
    out = "".join(g)
    return f'<a href="{href}" class="lnk">{out}</a>' if href else out


def edge(pts, label="", lp=None, anchor="middle", paths="", dashed=False, both=False, cls=""):
    d = "M " + " L ".join(f"{x} {y}" for x, y in pts)
    marks = ' marker-end="url(#ar)"' + (' marker-start="url(#ar)"' if both else "")
    out = f'<g class="{cls_paths(paths)} {cls}"><path class="e{" d" if dashed else ""}" d="{d}"{marks}/>'
    if label:
        out += f'<text class="el" x="{lp[0]}" y="{lp[1]}" text-anchor="{anchor}">{E(label)}</text>'
    return out + "</g>"


def pin(x, y, n):
    return f'<g class="pin"><circle cx="{x}" cy="{y}" r="12"/><text x="{x}" y="{y + 4.5}" text-anchor="middle">{n}</text></g>'


def text(x, y, s, cls="s", anchor="start", extra=""):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}"{extra}>{E(s)}</text>'


def heat(x0, y0, cw, ch, labels=True):
    """Causal Mask를 적용한 3×3 Attention Weight (p.62 실행)"""
    out = []
    names = ["t1", "t2", "t3"]
    if labels:
        for j, n in enumerate(names):
            out.append(text(x0 + j * cw + cw / 2, y0 - 6, n, "hl", "middle"))
        for i, n in enumerate(names):
            out.append(text(x0 - 6, y0 + i * ch + ch / 2 + 4, n, "hl", "end"))
    for i in range(3):
        for j in range(3):
            v = W[i][j]
            x, y = x0 + j * cw, y0 + i * ch
            if P62["mask"][i][j]:
                out.append(f'<rect class="hm off" x="{x}" y="{y}" width="{cw}" height="{ch}"/>')
                out.append(text(x + cw / 2, y + ch / 2 + 4, "0", "hv off", "middle"))
            else:
                out.append(f'<rect class="hm" x="{x}" y="{y}" width="{cw}" height="{ch}" style="fill:color-mix(in srgb, var(--heat) {v * 85:.0f}%, var(--color-surface))"/>')
                out.append(text(x + cw / 2, y + ch / 2 + 4, f(v), "hv" + (" hi" if v >= .5 else ""), "middle"))
    return "".join(out)


def soft_bars(x, y, maxw, gap=26, endx=None):
    out = []
    for i, (lab, p) in enumerate(zip("ABC", PR)):
        yy = y + i * gap
        out.append(text(x, yy + 11, lab, "hl"))
        out.append(f'<rect class="track" x="{x + 16}" y="{yy}" width="{maxw}" height="13" rx="3"/>')
        out.append(f'<rect class="barf" x="{x + 16}" y="{yy}" width="{maxw * p:.1f}" height="13" rx="3"/>')
        out.append(text(endx, yy + 11, f(p, 3), "hl", "end"))
    return "".join(out)


DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
        '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" class="mk"/></marker>'
        '<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<rect width="7" height="7" class="hb"/><line x1="0" y1="0" x2="0" y2="7" class="hl2"/></pattern>'
        '</defs></svg>')


# ── 그림 1 · 시스템 지도 ─────────────────────────────────
def system_map():
    s = []
    s.append('<rect class="bnd" x="140" y="110" width="990" height="440" rx="16"/>')
    s.append(text(160, 134, "애플리케이션 · Backend", "bt"))
    # 선 (상자보다 먼저)
    s.append(edge([(120, 268), (170, 268)], "질문", (145, 260), paths="sum rag agt"))
    s.append(edge([(170, 292), (120, 292)], "응답", (145, 310), paths="sum rag agt"))
    s.append(edge([(300, 280), (350, 280)], "질문", (325, 272), paths="sum rag"))
    s.append(edge([(520, 280), (580, 280)], "Context", (550, 272), paths="sum rag"))
    s.append(edge([(660, 222), (660, 190), (270, 190), (270, 250)], "생성한 답", (470, 182), paths="sum rag agt"))
    s.append(edge([(215, 250), (215, 150), (920, 150), (920, 250)], "업무 요청", (560, 142), paths="agt", dashed=True))
    s.append(edge([(780, 264), (860, 264)], "행동 제안", (820, 256), paths="agt", dashed=True))
    s.append(edge([(860, 298), (780, 298)], "Tool 결과", (820, 316), paths="agt", dashed=True))
    s.append(edge([(980, 280), (1004, 280)], "", paths="agt", dashed=True))
    s.append('<text class="el pp p-agt" x="992" y="242" text-anchor="middle">실행 요청</text>')
    s.append(edge([(1066, 310), (1066, 390)], "허용될 때만", (1058, 356), anchor="end", paths="agt", dashed=True))
    s.append(edge([(1004, 420), (940, 420), (940, 310)], "실행 결과", (972, 438), paths="agt", dashed=True))
    s.append(edge([(235, 310), (235, 380)], "조회·수정", (227, 350), anchor="end", paths="rag", both=True))
    s.append(edge([(235, 440), (235, 466)], "", paths="rag", dashed=True))
    s.append('<text class="el pp p-rag" x="245" y="459" text-anchor="start">Chunk 저장</text>')
    s.append(edge([(310, 494), (380, 494)], "가까운 Chunk", (345, 486), paths="rag", dashed=True))
    s.append(edge([(405, 310), (405, 460)], "질문", (397, 400), anchor="end", paths="rag", dashed=True))
    s.append(edge([(465, 460), (465, 310)], "문서 발췌", (473, 400), anchor="start", paths="rag", dashed=True))
    # 상자
    s.append(node(16, 250, 104, 60, "사용자", "질문하는 사람", paths="sum rag agt"))
    s.append(node(170, 250, 130, 60, "FastAPI", "요청·응답", "11/10", "done", "sum rag agt"))
    s.append(node(350, 250, 170, 60, "Context 조립", "지시·대화·근거·질문", "그림 2", "c2", "sum rag", href="#cw"))
    s.append(node(170, 380, 150, 60, "PostgreSQL", "원본 지식", "11/11", "done", "rag"))
    s.append(node(160, 466, 150, 56, "벡터 인덱스", "11/18~19", "", "later", "rag"))
    s.append(node(380, 460, 170, 56, "Retriever", "가까운 문서 찾기", "11/20", "later", "rag"))
    s.append(node(860, 250, 120, 60, "Agent", "단계 진행", "이후", "later", "agt"))
    s.append(node(1004, 250, 120, 60, "권한 확인", "Backend · 승인", "", "later", "agt"))
    s.append(node(1004, 390, 120, 60, "Tool API", "업무 시스템", "이후", "later", "agt"))
    # 가운데 LLM: 테두리 고리로 '모델 · 외부 API'임을 따로 표시
    s.append('<rect class="hubring" x="572" y="214" width="216" height="132" rx="16"/>')
    s.append(node(580, 222, 200, 116, "LLM", "판단 · 문장 생성", "11/13 오늘", "now", "sum rag agt", href="#llm", sub2="다음 Token 반복 · 그림 3"))
    s.append(text(680, 366, "모델 · 외부 API로 호출", "hubl", "middle"))
    # 답이 틀어질 수 있는 곳 (p.80)
    s += [pin(520, 310, "1"), pin(550, 516, "2"), pin(780, 222, "3"), pin(380, 190, "4")]
    return (f'<svg class="dg map-svg" viewBox="0 100 1140 460" role="img" '
            f'aria-label="시스템 지도: 가운데 LLM을 중심으로 FastAPI, Context 조립, Retriever, PostgreSQL, 벡터 인덱스, Agent, 권한 확인, Tool API가 연결된 구조">{"".join(s)}</svg>')


# ── 그림 3 · LLM 안 (넓은 화면) ───────────────────────────
def llm_wide():
    s = []
    s.append('<rect class="bnd" x="14" y="20" width="1112" height="376" rx="16"/>')
    s.append(text(32, 48, "LLM", "bt"))
    s.append(text(32, 68, "모델 안에서 일어나는 계산", "s"))
    # 학습할 때만
    s.append('<rect class="note" x="810" y="36" width="306" height="96" rx="10"/>')
    s.append(text(824, 60, "학습할 때만", "t"))
    s.append(text(824, 82, "Logit과 정답 Token으로 Loss를 구하고", "s"))
    s.append(text(824, 102, "backward() · optimizer.step()으로", "s"))
    s.append(text(824, 122, "가중치를 고친다. 추론 때는 가중치 고정", "s"))
    s.append(edge([(875, 180), (875, 134)], "", dashed=True))
    # Block 묶음
    for k, off in enumerate((16, 8)):
        s.append(f'<rect class="stack" x="{400 + off}" y="{74 - off}" width="360" height="300" rx="12"/>')
    s.append('<rect class="blk" x="400" y="74" width="360" height="300" rx="12"/>')
    s.append(text(414, 98, "Transformer Block × N", "t"))
    s.append(text(748, 98, "4·5교시", "bd", "end"))
    s.append('<rect class="att" x="420" y="110" width="320" height="140" rx="8"/>')
    s.append(text(432, 134, "Self-Attention", "t"))
    for i, line in enumerate(["Q·K를 비교해 참고 비율", "미래 칸은 Mask로 0", "행마다 합이 1", "V를 그 비율로 섞음"]):
        s.append(text(432, 160 + i * 21, line, "s"))
    s.append(heat(612, 142, 38, 32))
    for y, h, label in [(258, 28, "+ Residual · LayerNorm"), (294, 34, "FFN · Token마다 따로 변환"), (336, 28, "+ Residual · LayerNorm")]:
        s.append(f'<rect class="sub" x="420" y="{y}" width="320" height="{h}" rx="6"/>')
        s.append(text(580, y + h / 2 + 5, label, "s", "middle"))
    s.append('<path class="res" d="M 740 118 L 752 118 L 752 272 L 744 272" marker-end="url(#ar)"/>')
    s.append('<path class="res" d="M 740 300 L 752 300 L 752 350 L 744 350" marker-end="url(#ar)"/>')
    # 상자와 선
    s.append(node(30, 180, 130, 80, "Token ID", "101 9489 …", "2교시"))
    s.append(node(200, 180, 140, 80, "Embedding", "ID마다 벡터 하나", "3교시"))
    s.append(node(810, 180, 130, 80, "LM Head", "어휘 전체 점수", "6교시"))
    s.append('<rect class="n2" x="990" y="150" width="130" height="150" rx="10"/>')
    s.append(text(1002, 174, "Softmax", "t"))
    s.append(soft_bars(1002, 190, 54, endx=1114))
    s.append(text(1002, 286, "→ A 선택", "hl"))
    s.append(edge([(160, 220), (200, 220)], "(T)", (180, 210)))
    s.append(edge([(340, 220), (400, 220)], "(T, D)", (370, 210)))
    s.append(edge([(760, 220), (810, 220)], "(T, D)", (785, 210)))
    s.append(edge([(940, 220), (990, 220)], "Logit", (965, 210)))
    s.append(edge([(1055, 300), (1055, 432), (95, 432), (95, 260)], "고른 Token을 문장 끝에 붙여 다시 입력 · EOS가 나올 때까지", (575, 424), cls="loop"))
    return (f'<svg class="dg wide" viewBox="0 0 1140 450" role="img" '
            f'aria-label="LLM 안: Token ID, Embedding, Transformer Block, LM Head, Softmax와 반복 고리">{"".join(s)}</svg>')


# ── 그림 3 · LLM 안 (좁은 화면) ───────────────────────────
def llm_narrow():
    s = []
    s.append('<rect class="bnd" x="10" y="20" width="318" height="958" rx="16"/>')
    s.append(text(24, 46, "LLM", "bt"))
    s.append(node(50, 66, 240, 64, "Token ID", "101 9489 …", "2교시"))
    s.append(edge([(170, 130), (170, 170)], "(T)", (180, 155), anchor="start"))
    s.append(node(50, 170, 240, 64, "Embedding", "ID마다 벡터 하나", "3교시"))
    s.append(edge([(170, 234), (170, 278)], "(T, D)", (180, 260), anchor="start"))
    for off in (12, 6):
        s.append(f'<rect class="stack" x="{30 + off}" y="{278 - off}" width="270" height="392" rx="12"/>')
    s.append('<rect class="blk" x="30" y="278" width="270" height="392" rx="12"/>')
    s.append(text(42, 302, "Transformer Block × N", "t"))
    s.append(text(290, 302, "4·5교시", "bd", "end"))
    s.append('<rect class="att" x="44" y="314" width="232" height="226" rx="8"/>')
    s.append(text(56, 338, "Self-Attention", "t"))
    s.append(text(56, 360, "Q·K를 비교해 참고 비율", "s"))
    s.append(text(56, 380, "미래 칸은 Mask로 0", "s"))
    s.append(heat(110, 408, 38, 32))
    s.append(text(56, 530, "행마다 합 1 · V를 그 비율로 섞음", "s"))
    for y, h, label in [(548, 28, "+ Residual · LayerNorm"), (584, 34, "FFN · Token마다 변환"), (626, 28, "+ Residual · LayerNorm")]:
        s.append(f'<rect class="sub" x="44" y="{y}" width="232" height="{h}" rx="6"/>')
        s.append(text(160, y + h / 2 + 5, label, "s", "middle"))
    s.append('<path class="res" d="M 276 322 L 288 322 L 288 562 L 280 562" marker-end="url(#ar)"/>')
    s.append('<path class="res" d="M 276 590 L 288 590 L 288 640 L 280 640" marker-end="url(#ar)"/>')
    s.append(edge([(170, 670), (170, 712)], "(T, D)", (180, 694), anchor="start"))
    s.append(node(50, 712, 240, 64, "LM Head", "어휘 전체 점수 (Logit)", "6교시"))
    s.append(edge([(170, 776), (170, 816)], "Logit", (180, 800), anchor="start"))
    s.append('<rect class="n2" x="50" y="816" width="240" height="146" rx="10"/>')
    s.append(text(62, 840, "Softmax", "t"))
    s.append(soft_bars(62, 856, 150, endx=282))
    s.append(text(62, 948, "→ A 선택", "hl"))
    s.append(edge([(290, 890), (340, 890), (340, 98), (290, 98)], "", cls="loop"))
    s.append(f'<text class="el" x="352" y="494" text-anchor="middle" transform="rotate(-90 352 494)">고른 Token을 붙여 다시 입력</text>')
    return (f'<svg class="dg narrow" viewBox="0 0 360 990" role="img" '
            f'aria-label="LLM 안: Token ID, Embedding, Transformer Block, LM Head, Softmax와 반복 고리">{"".join(s)}</svg>')


# ── HTML 조각 ─────────────────────────────────────────────
def chips(tokens, ids):
    return "".join(f'<span class="{"tk sp" if t in SPECIAL else "tk"}"><b>{E(t)}</b><i>{i}</i></span>' for t, i in zip(tokens, ids))


def pad_table():
    rows = []
    for n, (toks, ids, mask) in enumerate(zip(P34["tokens"], P34["input_ids"], P34["attention_mask"]), 1):
        tc = "".join(f'<td class="{"padc" if t == "[PAD]" else ("spc" if t in SPECIAL else "")}">{E(t)}</td>' for t in toks)
        mc = "".join(f'<td class="m{m}">{m}</td>' for m in mask)
        rows.append(f'<tr class="grp-top"><th scope="row">문장 {n}</th>{tc}</tr><tr><th scope="row">attention_mask</th>{mc}</tr>')
    return f'<div class="table-wrap"><table class="pad"><tbody>{"".join(rows)}</tbody></table></div>'


fill = {
    "DEFS": DEFS,
    "MAP": system_map(),
    "LLM_WIDE": llm_wide(),
    "LLM_NARROW": llm_narrow(),
    "P29_TEXT": E(P29["text"]),
    "P29_CHIPS": chips(P29["tokens"], P29["ids"]),
    "P29_CHARS": str(P29["chars"]),
    "P29_N": str(P29["n_tokens"]),
    "P34_TABLE": pad_table(),
    "ENV": f'PyTorch {CAP["env"]["torch"]} · Transformers {CAP["env"]["transformers"]}',
}

tpl = (HERE / "template.html").read_text(encoding="utf-8")
missing = sorted(set(re.findall(r"\{\{(\w+)\}\}", tpl)) - fill.keys())
expect(not missing, f"채울 값 없음: {missing}")
out = re.sub(r"\{\{(\w+)\}\}", lambda m: fill[m.group(1)], tpl)
(HERE / "index.html").write_text(out, encoding="utf-8")
print(f"index.html {len(out):,} bytes")
