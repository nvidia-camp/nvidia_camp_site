"""Day16 oneday 요약 HTML 빌드.

구성안.md의 문장·표·코드와 실측(facts.json)을 template.html에 채워 index.html을 만든다.

실행: python3 build.py
"""
import difflib
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MD = (HERE / "구성안.md").read_text(encoding="utf-8")
F = json.loads((HERE / "facts.json").read_text(encoding="utf-8"))
T = (HERE / "template.html").read_text(encoding="utf-8")

NAVY, ACCENT, GREEN, ORANGE, MUTED, LINE = "#142849", "#4B74A6", "#2E6B45", "#C0703E", "#52667E", "#D8E4F2"
INKS = {"ocr": "#245C9C", "vlm": "#7A4F0E", "deploy": "#4A5870", "check": "#2E6B45"}


def contrast(hex_color):
    """흰 글자와의 대비. 구역 배지 색이 4.5:1 이상인지 확인한다."""
    def lin(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    lum = 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
    return 1.05 / (lum + 0.05)


for name, ink in INKS.items():
    assert contrast(ink) >= 4.5, (name, ink, contrast(ink))


def esc(s):
    return html.escape(str(s), quote=False)


def md_inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", s)


def zone(period):
    m = re.match(r"\d", str(period or ""))
    if not m:
        return "base"
    n = int(m.group())
    return "ocr" if n <= 3 else "vlm" if n <= 5 else "deploy" if n == 6 else "check"


def section(title):
    i = MD.index(title)
    j = MD.find("\n## ", i + 1)
    return MD[i: j if j > 0 else len(MD)]


def subsection(title):
    i = MD.index(title)
    j = MD.find("\n### ", i + 1)
    k = MD.find("\n## ", i + 1)
    ends = [x for x in (j, k) if x > 0]
    return MD[i: min(ends) if ends else len(MD)]


def table_rows(text, ncol):
    rows = []
    for line in text.split("\n"):
        if not line.startswith("| ") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip()[1:-1].split(" | ")]
        if len(cells) == ncol:
            rows.append(cells)
    return rows[1:]  # 머리글 제외


# ── 머리말 · ① 개념 · 약속 ──
lede = re.search(r"## 오늘을 한 문장으로\n\n> \*\*(.+?)\*\*", MD).group(1)
one = section("## 오늘을 한 문장으로")
ideas = re.findall(r"^\d\. (\*\*.+?\*\*.*)$", one[one.index("**꼭 알고 갈 개념"):one.index("**하루 내내")], re.M)
promises = re.findall(r"^\d\. (\*\*.+?\*\*.*)$", one[one.index("**하루 내내"):], re.M)
assert len(ideas) == 3 and len(promises) == 3, (ideas, promises)
ideas_html = "\n".join(f'    <div class="idea"><span class="n">{i}</span><p>{md_inline(t)}</p></div>' for i, t in enumerate(ideas, 1))
promises_html = "\n".join(f'    <div class="promise"><span class="n">{i}</span><p>{md_inline(t)}</p></div>' for i, t in enumerate(promises, 1))

# ── ③ 교시별 핵심: 개념 칸 "이름(뜻), A(뜻) vs B(뜻)" 풀기 ──
periods = table_rows(section("## 교시별 핵심"), 3)
assert len(periods) == 8, len(periods)


def split_top(s, sep=", "):
    out, depth, cur = [], 0, ""
    i = 0
    while i < len(s):
        ch = s[i]
        depth += ch == "("
        depth -= ch == ")"
        if depth == 0 and s.startswith(sep, i):
            out.append(cur)
            cur, i = "", i + len(sep)
            continue
        cur += ch
        i += 1
    return out + [cur]


def term_html(item):
    parts = []
    for p in split_top(item, " vs "):
        m = re.match(r"(.+?)\((.+)\)$", p.strip())
        name, d = (m.group(1), m.group(2)) if m else (p.strip(), "")
        parts.append(f'<b>{md_inline(name)}</b>' + (f'<span class="d">{md_inline(d)}</span>' if d else ""))
    return '<span class="term">' + '<span class="vs">vs</span>'.join(parts) + "</span>"


def term_names(cell):
    names = []
    for item in split_top(cell):
        for p in split_top(item, " vs "):
            names.append(re.sub(r"\(.*\)$", "", p.strip()))
    return names


steps = []
for p, q, concepts in periods:
    steps.append(f'    <div class="step"><p class="t"><span class="period {zone(p)}">{p}교시</span>{md_inline(q)}</p>'
                 f'<div class="terms">{"".join(term_html(c) for c in split_top(concepts))}</div></div>')

# ── ② 하루 지도 ──
TITLES = {"1": "OCR 흐름·문서 전처리", "2": "OCR 실행·Box·품질평가", "3": "정보 추출·JSON 구조화",
          "4": "VLM·이미지 질의응답", "5": "OCR·VLM 결합·평가·보안", "6": "TensorRT·<wbr>Jetson·<wbr>DeepStream",
          "7": "OCR·VLM 미니 앱 통합", "8": "최종 검증·평가·회고"}
Q = {p: q for p, q, _ in periods}
NAMES = {p: term_names(c) for p, _, c in periods}
ZONES = [("ocr", "OCR 경로", "이미지에서 글자와 값을 꺼낸다", "123"),
         ("vlm", "VLM 경로", "이미지에 묻고 답을 검증한다", "45"),
         ("deploy", "배포 설계", "현장 장치에서 돌린다", "6"),
         ("check", "통합·검증", "기록을 잇고 다시 실행한다", "78")]
day = ['  <div class="day">']
for k, (z, name, small, ps) in enumerate(ZONES):
    cards = "".join(
        f'<div class="pcard"><h3><span class="period {z}">{p}교시</span>{TITLES[p]}</h3><p class="q">{md_inline(Q[p])}</p>'
        f'<div class="tags">{"".join(f"<span>{md_inline(n)}</span>" for n in NAMES[p][:4])}</div></div>' for p in ps)
    day.append(f'    <div class="zone {z}"><p class="zone-name">{name}<small>{small}</small></p><div class="cards">{cards}</div></div>')
    if k < len(ZONES) - 1:
        day.append('    <span class="go">→</span>')
day.append("  </div>")

# ── ④ 흐름 띠 ──
flow = []
for m in re.finditer(r"^\| (준비|[①-⑧]) \| ([^|]+) \| ([^|]+) \| (\d|–) \|$", MD, re.M):
    n, what, how, p = (c.strip() for c in m.groups())
    badge = f'<span class="period {zone(p)}">{p}</span>' if p != "–" else '<span class="period base">준비</span>'
    label = esc(what) if n == "준비" else f"{n} {esc(what)}"
    flow.append(f'    <div><p class="h"><b>{label}</b>{badge}</p><p>{md_inline(how)}</p></div>')
assert len(flow) == 9, len(flow)

# ── ④ 핵심 코드: 머리줄로 블록 나누기 ──
code = re.search(r"### 핵심 코드\n\n```python\n(.*?)```", MD, re.S).group(1).rstrip("\n").split("\n")
segs, heads, cur = [], [None], []
for line in code:
    m = re.match(r"# ── \[(준비|\d)(?:교시)?\]", line)
    if m:
        segs.append(cur)
        heads.append(m.group(1))
        cur = []
        continue
    cur.append(line)
segs.append(cur)
for s in segs:
    while s and not s[0].strip():
        s.pop(0)
    while s and not s[-1].strip():
        s.pop()

TOKEN = re.compile(r'(?P<s>r?"[^"]*"|\'[^\']*\')|(?P<k>\b(?:import|from|for|in|if|else|and|is|not|None|True|False|with|as)\b)|(?P<n>\b\d+(?:\.\d+)?\b)')


def hl(line):
    # 문자열 안의 #은 주석이 아니다: 문자열 밖의 첫 #만 주석으로 본다
    in_s, q, cut = False, "", -1
    for i, ch in enumerate(line):
        if in_s:
            if ch == q:
                in_s = False
        elif ch in "\"'":
            in_s, q = True, ch
        elif ch == "#":
            cut = i
            break
    body, com = (line, "") if cut < 0 else (line[:cut], line[cut:])
    out, pos = [], 0
    for m in TOKEN.finditer(body):
        out += [esc(body[pos:m.start()]), f'<span class="{m.lastgroup}">{esc(m.group())}</span>']
        pos = m.end()
    out.append(esc(body[pos:]))
    if com:
        out.append(f'<span class="c">{esc(com)}</span>')
    return "".join(out)


ANN = {
    None: ("import", "OpenCV는 이미지 처리, pytesseract는 OCR, jiwer는 CER, transformers는 VLM을 맡습니다. 데이터는 scikit-image에 들어 있습니다."),
    "준비": ("데이터", "왼쪽이 어두운 스캔 페이지를 불러오고, 청구서 7줄을 그린 뒤 <b>일부러 비스듬히 찍은 사진</b>으로 바꿉니다. 그린 글자 <code>lines</code>가 곧 정답입니다."),
    "1": ("① 전처리", "스캔 페이지는 <b>주변 31×31 블록마다 기준</b>을 잡아 흑백으로 나눕니다. 사진은 네 모서리를 정면 네 모서리로 옮겨 펴고, 원본은 그대로 둔 채 보정본을 저장합니다."),
    "2": ("② OCR", "<code>image_to_string</code>은 글자 전체, <code>image_to_data</code>는 단어마다 <b>Text·Box·Confidence</b> 표를 줍니다. 낮은 점수는 지우지 않고 검토 목록으로 두고, 정답과 비교해 CER을 잽니다."),
    "3": ("③ 구조화", "<code>TOTAL:</code> 줄에서 괄호 안 숫자만 꺼내 <b>원문(raw)과 숫자 값(value)</b>을 함께 남기고, 그 단어의 점수·위치를 근거로 붙입니다. 품목 합이 합계와 다르면 검토 이유를 기록합니다."),
    "4": ("④ VLM 질문", "이미지와 질문을 <b>한 메시지</b>로 묶어 묻습니다. <code>do_sample=False</code>면 같은 입력에 같은 답, <code>return_full_text=False</code>면 새 답만 받습니다."),
    "5": ("⑤ 결합", "VLM 답이 <b>OCR 원문과 같을 때만 채택</b>합니다. 다르면 None(보류)으로 두고 사람이 확인합니다. 보류는 정답으로 세지 않습니다."),
    "6": ("⑥ 배포 설계", "장비가 필요해 실행하지 않고 공식 명령만 남깁니다. PyTorch → ONNX로 내보내고, <b>실제로 돌릴 장치에서</b> TensorRT Engine을 Build합니다."),
    "7": ("⑦ 통합 기록", "CER·합계(원문·값·점수·위치)·검토 이유·VLM 답·최종 값을 <b>한 JSON</b>으로 남깁니다. <code>ensure_ascii=False</code>면 원문 글자가 그대로 저장됩니다."),
}
assert len(segs) == len(heads) == 9, (len(segs), heads)
code_html = []
for s, p in zip(segs, heads):
    z = zone(p) if p not in (None, "준비") else "base"
    title, text = ANN[p]
    badge = (f'<span class="period {z}">{p}교시</span>' if p not in (None, "준비")
             else f'<span class="period base">{"준비" if p else "import"}</span>')
    code_html.append(f'    <div class="cseg {z}"><pre><code>{chr(10).join(hl(l) for l in s)}</code></pre>'
                     f'<div class="ann"><p class="t">{badge}{title}</p><p>{text}</p></div></div>')

# ── 꼭 알고 갈 함수 ──
funcs = table_rows(subsection("### 꼭 알고 갈 함수"), 5)
assert len(funcs) == 8, len(funcs)
funcs_html = []
for p, fn, when, how, check in funcs:
    funcs_html.append(
        f'      <div class="fcard"><p class="fn"><span class="period {zone(p)}">{p}교시</span>{md_inline(fn)}</p>'
        f'<dl><dt>용도</dt><dd>{md_inline(when)}</dd><dt>사용법</dt><dd>{md_inline(how)}</dd>'
        f'<dt>확인할 점</dt><dd>{md_inline(check)}</dd></dl></div>')

# ── 그림 ──
P, PS, W = F["page"], F["persp"], F["words"]


def fmt(v):
    """0.0082 → 0.008, 1.0 → 1.0 (소수점 아래 한 자리는 남긴다)"""
    if not isinstance(v, float):
        return str(v)
    s = f"{v:.3f}".rstrip("0")
    return s + "0" if s.endswith(".") else s


def trio(items, title, cap):
    figs = "".join(f'<figure><img src="{src}" alt="{esc(alt)}"><figcaption><b>{lab}</b> {res}</figcaption></figure>'
                   for src, alt, lab, res in items)
    return f'<div class="viz"><p class="viz-title">{title}</p><div class="trio">{figs}</div><p class="cap">{cap}</p></div>'


fig_threshold = trio(
    [(P["img_gray"], "스캔 페이지 원본", "원본 Gray", f'CER {fmt(P["gray_cer"])}'),
     (P["img_otsu"], "Otsu 이진화", f'Otsu (기준 {P["otsu_t"]:g})', f'CER <span class="after">{fmt(P["otsu_cer"])}</span>'),
     (P["img_adaptive"], "Adaptive 이진화", "Adaptive (31, 11)", f'CER <span class="good">{fmt(P["adaptive_cer"])}</span>')],
    '이진화 방법 <span class="note">(내장 스캔 페이지 · PSM 6)</span>',
    "Otsu는 페이지 전체에 기준 하나를 써서 어두운 왼쪽 글자가 검게 묻힙니다. Adaptive는 주변마다 기준을 따로 잡아 글자를 살립니다.")

fig_persp = trio(
    [(PS["img_photo"], "비스듬한 청구서 사진", "비스듬한 사진", f'CER {fmt(PS["photo"]["cer"])}'),
     (PS["img_warped"], "정면 보정", "정면 보정", f'CER <span class="good">{fmt(PS["warped"]["cer"])}</span> · 필드 {PS["warped"]["fields"]}/3'),
     (PS["img_wrong"], "시작점을 잘못 잡은 보정", "시작점이 오른쪽 위", f'CER <span class="after">{fmt(PS["wrong"]["cer"])}</span> · 필드 {PS["wrong"]["fields"]}/3')],
    '네 모서리 순서 <span class="note">(코드로 그린 청구서)</span>',
    f'이 정도 기울기는 Tesseract가 보정 없이도 읽습니다. 하지만 시작점을 잘못 잡으면 문서가 90도 돌아가 찌그러집니다. '
    f'두 점만 맞바꾸면 사각형이 꼬여 화면의 {round((1 - PS["swap_visible"]) * 100)}%가 검게 나옵니다(CER {fmt(PS["swap_cer"])}).')


def bars(rows, key, label, default):
    mx = max(r["cer"] for r in rows)
    out = ""
    for r in rows:
        w = r["cer"] / mx * 100
        is_def = r[key] == default
        col = NAVY if is_def else (ORANGE if r["cer"] > 0.1 else ACCENT)
        out += (f'<div style="display:grid;grid-template-columns:5.6rem 1fr 3rem;gap:6px;align-items:center;font-size:0.75rem">'
                f'<span style="{"font-weight:700;color:var(--color-heading)" if is_def else ""}">{label} {r[key]}{" (코드)" if is_def else ""}</span>'
                f'<span style="display:block;height:11px;width:{w:.1f}%;background:{col};border-radius:2px"></span>'
                f'<b style="text-align:right">{fmt(r["cer"])}</b></div>')
    return f'<div style="display:flex;flex-direction:column;gap:3px">{out}</div>'


fig_blockc = (f'<div class="viz"><p class="viz-title">blockSize와 C에 따른 CER <span class="note">(내장 스캔 페이지 · 낮을수록 좋음)</span></p>'
              f'{bars(F["block"], "bs", "blockSize", 31)}{bars(F["C"], "C", "C", 11)}'
              f'<p class="cap">blockSize는 3 이상 홀수만 됩니다(30을 넣으면 실행 오류). C는 30에서 가장 좋았습니다. 알맞은 값은 문서마다 다르니 CER로 고릅니다.</p></div>')


def fig_conf():
    ws = sorted(W, key=lambda w: w["conf"])
    Wc, Hc, L, R, Tp, B = 560, 170, 30, 10, 12, 26
    n = len(ws)
    bw = (Wc - L - R) / n
    sy = lambda v: Tp + (1 - v / 100) * (Hc - Tp - B)
    out = [f'<svg viewBox="0 0 {Wc} {Hc}" width="100%" role="img" aria-label="단어별 confidence">']
    for v in (0, 50, 90, 100):
        dash = ' stroke-dasharray="4 3"' if v in (50, 90) else ""
        col = ORANGE if v == 50 else (NAVY if v == 90 else "#E6EEF8")
        out.append(f'<line x1="{L}" x2="{Wc - R}" y1="{sy(v):.1f}" y2="{sy(v):.1f}" stroke="{col}"{dash}/>'
                   f'<text x="{L - 4}" y="{sy(v) + 3.5:.1f}" font-size="10" text-anchor="end" fill="{MUTED}">{v}</text>')
    for i, w in enumerate(ws):
        col = ORANGE if not w["correct"] else "#9DB3CF"
        x = L + i * bw + 1.5
        out.append(f'<rect x="{x:.1f}" y="{sy(w["conf"]):.1f}" width="{bw - 3:.1f}" height="{sy(0) - sy(w["conf"]):.1f}" rx="1.5" fill="{col}"/>')
    bad = ws[0]
    out.append(f'<text x="{L + bw + 6:.1f}" y="{sy(bad["conf"]) + 12:.1f}" font-size="10.5" font-weight="700" fill="{ORANGE}">← 오답 {esc(bad["text"])} {bad["conf"]:g}점</text>')
    out.append(f'<text x="{Wc - R - 2}" y="{sy(50) - 4:.1f}" font-size="10" text-anchor="end" fill="{ORANGE}">기준 50: 검토 0개</text>'
               f'<text x="{Wc - R - 2}" y="{sy(90) + 12:.1f}" font-size="10" text-anchor="end" fill="{NAVY}">기준 90: 검토 1개</text>'
               f'<text x="{(L + Wc - R) / 2}" y="{Hc - 6}" font-size="10" text-anchor="middle" fill="{MUTED}">단어 {n}개 (점수 낮은 순)</text></svg>')
    lo = min(w["conf"] for w in W if w["correct"])
    return (f'<div class="viz"><p class="viz-title">단어별 confidence <span class="note">(정면 보정한 청구서)</span></p>{"".join(out)}'
            f'<p class="cap">유일한 오답은 숫자 0을 글자 O로 읽은 <code>DOCO3</code>입니다. 맞는 단어 {n - 1}개는 모두 {lo:g}점 이상. 기준은 오답의 점수 분포를 보고 정합니다.</p></div>')


def fig_vlm():
    rows = '<div class="r hd"><span>질문</span><span>VLM 답</span><span>OCR 원문</span><span>대조</span></div>'
    for v in F["vlm"]:
        ocr_v = f"<code>{esc(v['ocr'])}</code>" if v["ocr"] else '<span class="absent">문서에 없음</span>'
        verdict = '<span class="ok">채택</span>' if v["adopted"] else '<span class="hold">보류</span>'
        rows += f'<div class="r"><span>{v["label"]}</span><code>{esc(v["answer"])}</code>{ocr_v}{verdict}</div>'
    return (f'<div class="viz"><p class="viz-title">실제 VLM에 물어본 결과 <span class="note">({esc(F["env"]["model"].split("/")[-1])} · do_sample=False)</span></p>'
            f'<div class="qa">{rows}</div>'
            f'<p class="cap">문서에 없는 값도 자연스럽게 지어냅니다. "없으면 null이라고 답해"를 붙여도 세금은 <code>{esc(F["vlm_null"])}</code>. '
            f'"JSON으로 답해"에도 <code>{esc(F["vlm_json"]["reply"])}</code>만 답해 형식을 지키지 않았습니다. 그래서 답을 OCR 원문과 대조합니다.</p></div>')


def fig_units():
    head = '<div class="r hd"><span>사진</span><span>CER</span><span>필드</span><span>놓친 필드</span></div>'
    rows = ""
    for r in F["lowres"]:
        miss = "공급자" if r["missing"] == ["supplier"] else ("없음" if not r["missing"] else ", ".join(r["missing"]))
        cls = "hold" if r["missing"] else "ok"
        rows += (f'<div class="r"><span>{r["scale"]:g}배 ({r["size"][0]}×{r["size"][1]})</span><span>{fmt(r["cer"])}</span>'
                 f'<span class="{cls}">{r["fields"]}/3</span><span>{miss}</span></div>')
    r4 = F["lowres"][1]
    rows += (f'<div class="r"><span>0.4배 → 2배 확대</span><span>{fmt(r4["x2_cer"])}</span><span class="ok">{r4["x2_fields"]}/3</span><span>없음</span></div>')
    return (f'<div class="viz"><p class="viz-title">CER과 필드 정답은 다른 것을 잰다 <span class="note">(청구서를 줄인 저해상도 사진)</span></p>'
            f'<div class="qa units">{head}{rows}</div>'
            f'<p class="cap">0.4배에서 OCR이 <code>{esc(r4["supplier_line"])}</code>처럼 줄 앞에 글자 하나를 붙여 <code>^SUPPLIER:</code> 규칙과 안 맞았습니다. '
            f'CER은 6.6%뿐인데 필드 하나를 통째로 놓쳤습니다.</p></div>')


GROUP_FIGS = {"숫자·옵션만 바꾸기": [fig_blockc, fig_conf()], "코드 한 줄 넣기·바꾸기": [fig_threshold, fig_vlm()],
              "순서만 바꾸기": [fig_persp], "모델은 그대로, 판정하고 세는 방법만 바꾸기": [fig_units()]}

# ── 코드 속 파라미터 ──
LR, VL = F["lowres"], {v["label"]: v for v in F["vlm"]}
blk = {r["bs"]: r["cer"] for r in F["block"]}
cc = {r["C"]: r["cer"] for r in F["C"]}
DELTA = {  # 파라미터 → (지표, 전, 후, 색). 숫자는 모두 facts.json 실측
    "blockSize": ("CER", fmt(blk[31]), fmt(blk[3]), "after"),
    "C": ("CER", fmt(cc[11]), fmt(cc[0]), "after"),
    "PSM": ("CER", fmt(F["psm"]["6"]["cer"]), fmt(F["psm"]["7"]["cer"]), "after"),
    "confidence 기준": ("검토 목록", str(F["review"]["50"]), str(F["review"]["90"]), "good"),
    "max_new_tokens": ("답", VL["합계"]["answer"], F["vlm_tokens3"], "after"),
    "이진화 방법": ("CER", fmt(P["adaptive_cer"]), fmt(P["otsu_cer"]), "after"),
    "확대": ("CER", fmt(LR[1]["cer"]), fmt(LR[1]["x2_cer"]), "good"),
    "좌표 되돌리기": ("왼쪽 위 점", "({}, {})".format(*F["box_back"]["warped"]), "({:g}, {:g})".format(*F["box_back"]["back"]), ""),
    "정규표현식": ("고른 금액", F["total"]["raw"], F["first_number"], "after"),
    "질문": ("답", f'합계 {VL["합계"]["answer"]}', f'세금 {VL["세금"]["answer"]}', "after"),
    "모서리 순서": ("CER", fmt(PS["warped"]["cer"]), fmt(PS["wrong"]["cer"]), "after"),
    "대조": ("할인액", "보류", VL["할인액"]["answer"], "after"),
    "평가 단위": ("0.4배 사진", f'CER {fmt(LR[1]["cer"])}', f'필드 {LR[1]["fields"]}/3', "after"),
    "합계 검증": ("검토 이유", F["misread_reason"], "없음", "after"),
}


def old_new(old, new):
    """md 칸이 코드 하나면 차이를 노랗게 표시한 pre로, 설명이 섞였으면 글 상자로."""
    m_old = re.fullmatch(r"`([^`]+)`", old)
    m_new = re.fullmatch(r"`([^`]+)`(?:\s+#.*)?", new) if new.count("`") == 2 else None
    if m_old and m_new:
        a = m_old.group(1)
        b_full = new[1:new.rindex("`")]
        code, _, com = b_full.partition("  # ")
        ta, tb = re.findall(r"\w+|\s+|[^\w\s]", a), re.findall(r"\w+|\s+|[^\w\s]", code)
        out = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
            seg = esc("".join(tb[j1:j2]))
            out.append(seg if op == "equal" else (f"<mark>{seg}</mark>" if seg.strip() else seg))
        new_html = "".join(out) + (f"  {esc('# ' + com)}" if com else "")
        return f'<pre class="old">{esc(a)}</pre>', f'<pre class="new">{new_html}</pre>'
    return f'<p class="prose old">{md_inline(old)}</p>', f'<p class="prose new">{md_inline(new)}</p>'


ksec = subsection("### 코드 속 파라미터")
knob_html, n_key, n_rows = [], 0, 0
for gm in re.finditer(r"^\*\*(.+?)\*\* — (.+?)\n\n(\|.*?)(?=\n\n|\Z)", ksec, re.S | re.M):
    gname, gdesc, table = gm.groups()
    knob_html.append(f'      <p class="kgroup">{esc(gname)}<span>{esc(gdesc)}</span></p>')
    for p, name, old, new, res, cond, lesson in table_rows(table, 7):
        metric, a_, b_, cls = DELTA[name]
        # md 결과 문장과 실측 숫자가 같은지 확인
        for v in (a_, b_):
            if re.fullmatch(r"[\d.]+", v):
                assert v in res or v.rstrip("0") in res, (name, v, res)
        o, nw = old_new(old, new)
        d = (f'<p class="delta"><span class="note">{esc(metric)}</span><span class="big">{esc(a_)}</span>'
             f'<span class="arrow">→</span><span class="big {cls}">{esc(b_)}</span></p>')
        key = ""
        if lesson:
            n_key += 1
            key = f'<p class="lesson"><span class="keytag">꼭 기억</span>{md_inline(lesson)}</p>'
        knob_html.append(
            f'      <div class="krow{" key" if lesson else ""}"><p class="kname"><span class="period {zone(p)}">{esc(p)}교시</span>{esc(name)}</p>'
            f'{o}<span class="go">→</span>{nw}<div class="res">{d}<p>{md_inline(res)}</p><p class="src">{md_inline(cond)}</p></div>{key}</div>')
        n_rows += 1
    figs = GROUP_FIGS[gname]
    span = ' style="grid-column:1 / -1"' if len(figs) == 1 else ""
    knob_html.append(f'      <div class="figs">' + "".join(f.replace('<div class="viz">', f'<div class="viz"{span}>', 1) for f in figs) + "</div>")
assert n_rows == 14 and n_key == 7, (n_rows, n_key)

# ── ① 한 장 그림 ──
def ocr_overlay():
    Wi, Hi = 700, 480
    body = ""
    for w in W:
        x, y, bw_, bh = w["box"]
        if w["text"] == F["total"]["raw"]:
            body += f'<rect x="{x - 3}" y="{y - 3}" width="{bw_ + 6}" height="{bh + 6}" fill="none" stroke="{GREEN}" stroke-width="4"/>'
        elif not w["correct"]:
            body += f'<rect x="{x - 2}" y="{y - 2}" width="{bw_ + 4}" height="{bh + 4}" fill="none" stroke="{ORANGE}" stroke-width="3"/>'
        else:
            body += f'<rect x="{x}" y="{y}" width="{bw_}" height="{bh}" fill="none" stroke="{ACCENT}" stroke-width="1.6" opacity="0.8"/>'
    return (f'<svg viewBox="0 0 {Wi} {Hi}" width="100%" role="img" aria-label="단어 Box를 그린 보정본">'
            f'<image href="{PS["img_warped"]}" x="0" y="0" width="{Wi}" height="{Hi}"/>{body}</svg>')


tot = F["total"]
adopted = sum(v["adopted"] for v in F["vlm"])
record = "\n".join([
    f'"raw": "{tot["raw"]}"',
    f'"value": {int(tot["raw"])}',
    f'"conf": {tot["conf"]:g}',
    f'"box": {tot["box"]}',
    f'"vlm": "{VL["합계"]["answer"]}"',
    f'"final": {int(tot["raw"])}'])
hero = f'''    <div class="hero">
      <div class="hbox src" style="grid-column:1"><p class="hh"><b>문서 이미지 + 질문</b></p>
        <img src="{PS["img_photo"]}" alt="비스듬히 찍은 청구서 사진" style="border-radius:6px;background:#fff">
        <p class="what">코드로 그린 청구서를 비스듬히 찍은 사진</p></div>
      <span class="arrow span" style="grid-column:2">→</span>
      <div class="hbox ocr" style="grid-column:3;grid-row:1"><p class="hh"><b>OCR용 전처리</b><span class="tag">1교시</span></p>
        <img src="{PS["img_warped"]}" alt="정면 보정본" style="border-radius:6px;background:#fff">
        <p class="what">네 모서리로 정면 보정 (스캔은 Adaptive 이진화)</p></div>
      <span class="arrow" style="grid-column:4;grid-row:1">→</span>
      <div class="hbox ocr" style="grid-column:5;grid-row:1"><p class="hh"><b>OCR</b><span class="tag">2교시</span></p>
        {ocr_overlay()}
        <p class="what">단어마다 Text·Box·Confidence. <b style="color:{ORANGE}">주황</b> = 오답 <code>DOCO3</code></p></div>
      <span class="arrow" style="grid-column:6;grid-row:1">→</span>
      <div class="hbox ocr" style="grid-column:7;grid-row:1"><p class="hh"><b>값 + 근거</b><span class="tag">3교시</span></p>
        <p class="val">{tot["raw"]}</p>
        <p class="kv">raw <code>"{tot["raw"]}"</code><br>value <code>{int(tot["raw"])}</code><br>conf <code>{tot["conf"]:g}</code><br>box <code>{", ".join(map(str, tot["box"]))}</code></p></div>
      <div class="hbox vlm" style="grid-column:3;grid-row:2"><p class="hh"><b>원본 + 질문</b><span class="tag">4교시</span></p>
        <p class="qbubble">What is the total amount?</p><p class="what">이미지와 질문을 한 메시지로</p></div>
      <span class="arrow" style="grid-column:4;grid-row:2">→</span>
      <div class="hbox vlm" style="grid-column:5;grid-row:2"><p class="hh"><b>VLM</b><span class="tag">SmolVLM-256M</span></p>
        <p class="what">Vision Encoder → Projector → LLM<br>이미지와 질문을 함께 보고 답을 만든다</p></div>
      <span class="arrow" style="grid-column:6;grid-row:2">→</span>
      <div class="hbox vlm" style="grid-column:7;grid-row:2"><p class="hh"><b>답 후보</b></p>
        <p class="val">{esc(VL["합계"]["answer"])}</p><p class="what">문서에 없는 세금을 물으면 <code>{esc(VL["세금"]["answer"])}</code>을 지어냄</p></div>
      <span class="arrow span" style="grid-column:8">→</span>
      <div class="hbox check" style="grid-column:9"><p class="hh"><b>대조</b><span class="tag">5교시</span></p>
        <div class="verdict"><p>OCR 원문 = VLM 답 → <b class="good">채택</b></p><p>다르거나 원문에 없음 → <b class="after">보류</b>, 사람 확인</p></div>
        <p class="what">실측: 질문 {len(F["vlm"])}개 중 채택 {adopted} · 보류 {len(F["vlm"]) - adopted}</p></div>
      <span class="arrow span" style="grid-column:10">→</span>
      <div class="hbox out" style="grid-column:11"><p class="hh"><b>근거와 함께 기록</b><span class="tag" style="color:var(--ink-check)">7교시</span></p>
        <pre class="json">{esc(record)}</pre><p class="what">핵심만 줄인 모습. 전체는 7교시 코드의 <code>record</code></p></div>
    </div>
    <p class="cap" style="margin-top:8px">강의 PDF p.3의 구조를 따랐습니다. 사진·Box·숫자는 모두 핵심 코드를 실제로 실행한 결과입니다(Tesseract {F["env"]["tesseract"]}, {esc(F["env"]["model"])}).</p>'''

env = F["env"]
footer = (f'  <p>NVIDIA AI 코어 엔지니어 2기 · Day16 Vision·멀티모달 AI 응용 4/4 · 강의 PDF <code>Day16_20261109.pdf</code>(101쪽). '
          f'코드 문법: OpenCV Image Thresholding·Geometric Transformations, pytesseract, jiwer, Hugging Face Transformers(image-text-to-text), PyTorch ONNX, TensorRT trtexec.</p>\n'
          f'  <p>그림과 숫자는 핵심 코드와 같은 데이터(scikit-image 내장 스캔 페이지, 코드로 그린 청구서)로 직접 실행한 결과입니다. '
          f'Tesseract {env["tesseract"]}, OpenCV {env["opencv"]}, scikit-image {env["skimage"]}, transformers {env["transformers"]}, torch {env["torch"]}, VLM {esc(env["model"])}(do_sample=False). '
          f'스캔 페이지의 CER은 손으로 옮긴 정답 7줄 기준입니다.</p>\n'
          f'  <p>수업 실습의 기본 경로는 강사가 미리 써 둔 VLM 응답이라 실습 결과와 VLM 답이 다를 수 있습니다. TensorRT·Jetson·DeepStream은 실행하지 않은 설계입니다. 합성 영어 문서라 실제 한국어 문서·손글씨 성능을 뜻하지 않습니다.</p>')

out = T
for k, v in {"LEDE": md_inline(lede), "HERO": hero, "IDEAS": ideas_html, "PROMISES": promises_html,
             "DAY": "\n".join(day), "STEPS": "\n".join(steps), "FLOW": "\n".join(flow), "CODE": "\n".join(code_html),
             "FUNCS": "\n".join(funcs_html), "KNOBS": "\n".join(knob_html), "N_KEY": str(n_key), "FOOTER": footer}.items():
    out = out.replace("{{" + k + "}}", v)
assert "{{" not in out, re.findall(r"\{\{\w+\}\}", out)
(HERE / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out) // 1024, "KB")
