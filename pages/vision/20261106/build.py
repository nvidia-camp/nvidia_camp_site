"""Day15 oneday 요약 HTML 빌드.

구성안.md의 코드·표와 실측 데이터(facts.json)를 template.html에 채워 index.html을 만든다.

실행: python3 build.py
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MD = (HERE / "구성안.md").read_text(encoding="utf-8")
F = json.loads((HERE / "facts.json").read_text(encoding="utf-8"))
T = (HERE / "template.html").read_text(encoding="utf-8")

NAVY, ACCENT, GREEN, ORANGE, MUTED, LINE = "#142849", "#4B74A6", "#2E6B45", "#C0703E", "#52667E", "#D8E4F2"
OBJ_COL = {1: "#4B74A6", 2: "#D9A44E", 3: "#9C8BD0", 0: "#C9D2DE"}  # 추적: square · circle · triangle · 정답과 안 겹침


def esc(s):
    return html.escape(str(s), quote=False)


def md_inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", s)


def zone(period):
    m = re.match(r"\d", period or "")
    if not m:
        return "base"
    n = int(m.group())
    return "prep" if n <= 3 else "learn" if n <= 5 else "explain" if n <= 7 else "final"


def section(title):
    i = MD.index(title)
    j = MD.find("\n## ", i + 1)
    return MD[i: j if j > 0 else len(MD)]


# ── 머리말 한 문장 ──
lede = re.search(r"## 오늘을 한 문장으로\n\n> \*\*(.+?)\*\*", MD).group(1)

# ── ③ 교시별 핵심 ──
steps = []
for m in re.finditer(r"^\| (\d) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", section("## 교시별 핵심"), re.M):
    p, q, concepts, b1, b2, b3 = (c.strip() for c in m.groups())
    z = zone(p)
    steps.append(
        f'    <div class="step"><div class="what"><p class="t"><span class="period {z}">{p}교시</span>{md_inline(q)}</p>'
        f'<p class="c">{md_inline(concepts).replace(", ", " · ")}</p></div>'
        f'<div class="stairs"><div class="s1"><span class="lv l1">기본</span><span>{md_inline(b1)}</span></div><span class="to">→</span>'
        f'<div class="s2"><span class="lv l2">응용</span><span>{md_inline(b2)}</span></div><span class="to">→</span>'
        f'<div class="s3"><span class="lv l3">심화</span><span>{md_inline(b3)}</span></div></div></div>')
assert len(steps) == 8, len(steps)

# ── ④ 흐름 띠 ──
flow = []
for m in re.finditer(r"^\| ([①-⑧]) \| ([^|]+) \| ([^|]+) \| (\d) \|$", MD, re.M):
    n, what, how, p = (c.strip() for c in m.groups())
    flow.append(f'    <div><p class="h"><b>{n} {esc(what)}</b><span class="period {zone(p)}">{p}</span></p><p>{md_inline(how)}</p></div>')
assert len(flow) == 8, len(flow)

# ── ④ 핵심 코드: 교시 블록별로 자르고, 3교시에 dataset.yaml을 붙인다 ──
code = re.search(r"### 핵심 코드\n\n```python\n(.*?)```", MD, re.S).group(1).rstrip("\n").split("\n")
yml = re.search(r"3교시의 dataset.yaml:\n\n```yaml\n(.*?)```", MD, re.S).group(1).rstrip("\n").split("\n")
segs, heads, cur = [], [None], []
for line in code:
    if line.startswith("# ── "):
        segs.append(cur)
        heads.append(re.match(r"# ── \[(\d)교시\]", line).group(1))
        cur = []
        continue
    cur.append(line)
segs.append(cur)
for s in segs:
    while s and not s[0].strip():
        s.pop(0)
    while s and not s[-1].strip():
        s.pop()

TOKEN = re.compile(r'(?P<s>"[^"]*"|\'[^\']*\')|(?P<k>\b(?:import|from|for|in|if|and|is|not|None|True|False)\b)|(?P<n>\b\d+(?:\.\d+)?\b)')


def hl(line):
    i = line.find("#")
    body, com = (line, "") if i < 0 else (line[:i], line[i:])
    out, pos = [], 0
    for m in TOKEN.finditer(body):
        out += [esc(body[pos:m.start()]), f'<span class="{m.lastgroup}">{esc(m.group())}</span>']
        pos = m.end()
    out.append(esc(body[pos:]))
    if com:
        out.append(f'<span class="c">{esc(com)}</span>')
    return "".join(out)


def hl_yaml(line):
    i = line.find("#")
    body, com = (line, "") if i < 0 else (line[:i], line[i:])
    body = re.sub(r"^(\s*)([\w]+):", lambda m: f'{m.group(1)}<span class="y">{esc(m.group(2))}</span>:', esc(body))
    return body + (f'<span class="c">{esc(com)}</span>' if com else "")


docs = {}
for m in re.finditer(r"^\| ([\d·]+) \| (.+) \| ([^|]+) \|$", MD[MD.index("**공식 문서 대조**"):MD.index("### 코드 속 파라미터")], re.M):
    for p in m.group(1).split("·"):
        docs.setdefault(p, []).append(m.group(3).strip())
N = F["funnel"]["n_candidates"]
ANN = {
    None: ("준비", "OpenCV는 그리기, <code>torchvision.ops</code>는 박스 계산, <code>ultralytics</code>는 YOLO 학습·추론·추적을 맡습니다."),
    "1": ("① 좌표", "같은 박스를 픽셀 xyxy(모서리)에서 cxcywh(중심·크기)로 바꾸고, <b>x는 폭 W로, y는 높이 H로</b> 나눠 0~1로 만듭니다. OpenCV 색은 BGR 순서입니다."),
    "2": ("② 채점 기준", "<code>box_iou</code>는 예측 × 정답 겹침 표를 만듭니다. 0.5 이상이고 클래스가 같으면, 점수 높은 예측부터 <b>정답 하나에 하나씩만</b> TP로 연결합니다."),
    "3": ("③ 라벨·데이터", "라벨 한 줄 = 객체 하나(<code>class cx cy w h</code>). dataset.yaml이 경로와 클래스 이름을 모델에 연결합니다. 객체가 없는 이미지는 빈 파일입니다."),
    "4": ("④ 학습", "<code>.yaml</code>은 구조만 만들어 처음부터 학습하고, <code>.pt</code>는 학습된 가중치까지 불러옵니다. 학습이 끝나면 best.pt·last.pt가 남습니다."),
    "5": ("⑤ 검증", "학습 직후 <code>model</code>은 best.pt입니다. 인자 없이 <code>val()</code>을 부르면 학습한 데이터 설정 그대로 val을 채점합니다."),
    "6": ("⑥ 추론", f"안에서 후보 {N}개 → conf로 거름 → NMS로 중복 제거 → Results. 탐지가 0개인 이미지도 결과에 남습니다."),
    "7": ("⑦ 추적", "Tracker가 프레임 사이 같은 객체에 Track ID를 붙입니다. ID가 아직 없는 프레임이 있으니 <code>is_track</code>을 먼저 확인합니다."),
}
assert len(segs) == len(heads) == 8, (len(segs), heads)
code_html = []
for s, p in zip(segs, heads):
    z = zone(p)
    lines = [hl(l) for l in s if "(아래 YAML)" not in l]
    if p == "3":
        lines += ["", '<span class="c"># dataset.yaml</span>'] + [hl_yaml(l) for l in yml]
    title, text = ANN[p]
    badge = f'<span class="period {z}">{p}교시</span>' if p else '<span class="period base">import</span>'
    src = f'<p class="doc">문서: {esc(" · ".join(docs[p]))}</p>' if p in docs else ""
    code_html.append(f'    <div class="cseg {z}"><pre><code>{chr(10).join(lines)}</code></pre>'
                     f'<div class="ann"><p class="t">{badge}{title}</p><p>{text}</p>{src}</div></div>')

# ── ④ 코드 속 파라미터: 위 코드 → 고친 코드 → 결과 ──
cs = {r["conf"]: r for r in F["conf_sweep"]}
ns = {r["iou"]: r for r in F["nms_sweep"]}
V, E95, TR, WH, SP = F["val"], F["eval95"], F["track"], F["wh_swap"], F["split"]
c25, c50, c90, n50 = cs[0.25], cs[0.5], cs[0.9], ns[0.5]
first_nz = next(e for e, v in zip(F["curve"]["epoch"], F["curve"]["map50"]) if v > 0)
f2 = lambda v: f"{v:.2f}"
f3 = lambda v: f"{v:.3f}"
GROUPS = [
    ("숫자·옵션만 바꾸기", "줄은 그대로 두고 값만 고쳤습니다", [
        ("6", "conf", 'model.predict("images/val", conf=0.25)', 'model.predict("images/val", conf=<m>0.5</m>)',
         ("Precision", f2(c25["P"]), f2(c50["P"]), "good"),
         f'남는 박스 {c25["boxes"]} → {c50["boxes"]}, Recall {c25["R"]:g} 그대로. 0.9까지 올리면 Recall {c90["R"]:g}({c90["tp"] + c90["fn"]}개 중 {c90["fn"]}개 놓침)',
         "응용 val 12장 · 평가 IoU 0.5 · 깔때기의 첫 거름망",
         "올리면 거짓 탐지는 줄고 놓침은 늘어난다. Precision과 Recall을 함께 본다"),
        ("6", "NMS IoU", 'model.predict("images/val", conf=0.25)', 'model.predict("images/val", conf=0.25,\n              <m>iou=0.5</m>)  # 기본 0.7',
         ("FP", str(c25["fp"]), str(n50["fp"]), "good"),
         f'남는 박스 {c25["boxes"]} → {n50["boxes"]}. conf 0.25에서 남은 FP {c25["fp"]}개가 전부 같은 객체의 중복이었음. 0.95로 올리면 {ns[0.95]["boxes"]}개',
         "응용 val 12장 · 깔때기의 두 번째 거름망",
         "NMS IoU는 예측끼리의 겹침이다. 정답과 비교하는 평가 IoU와 이름만 같고 하는 일이 다르다"),
        ("2·5", "평가 IoU", "matched = iou >= 0.5", "matched = iou >= <m>0.95</m>",
         ("TP", str(c25["tp"]), str(E95["tp"]), ""),
         f'같은 예측 {E95["boxes"]}개인데 거의 다 FP가 됨. 같은 모델의 mAP50 {f3(V["best"]["map50"])}, mAP50-95 {f3(V["best"]["map"])}',
         "응용 val 12장 · conf 0.25",
         "기준이 엄격할수록 위치가 정확해야 TP다. mAP50-95가 낮으면 \"찾긴 하지만 박스가 덜 맞다\""),
        ("4", "epochs", 'model.train(data="dataset.yaml", epochs=60, imgsz=160)', 'model.train(data="dataset.yaml", epochs=<m>1</m>, imgsz=160)',
         ("mAP50", f3(V["best"]["map50"]), f'{F["epoch1"]["map50"]:g}', "after"),
         f"60 epoch 학습에서도 {first_nz - 1} epoch까지는 0이었음", "응용 데이터 · 처음부터 학습",
         "1 epoch이 돌아간 것은 \"연결 성공\"이지 \"탐지 성공\"이 아니다"),
        ("7", "persist", 'model.track("demo.avi",\n            tracker="bytetrack.yaml",\n            stream=True)',
         'model.track("demo2.avi",  # 다음 영상\n            tracker="bytetrack.yaml",\n            stream=True, <m>persist=True</m>)',
         ("가장 큰 ID", str(max(TR["ids_fresh"])), str(max(TR["ids_second_persist"])), "after"),
         f'새 영상인데 앞 영상의 ID({"·".join(map(str, sorted(set(TR["ids_first"]) & set(TR["ids_second_persist"]))))})를 이어 씀. 새 YOLO 객체로 시작하면 첫 실행과 같은 ID',
         "같은 모델 객체로 demo 영상을 다음 영상처럼 한 번 더",
         "Track ID는 모델에 저장된 값이 아니라 실행 중 상태다. persist는 같은 영상 안에서만 쓴다"),
    ]),
    ("순서만 바꾸기", "같은 값을 다른 자리에 넣었습니다 (흔한 실수)", [
        ("1", "W·H 순서", "labels = cxcywh / torch.tensor([160, 128, 160, 128])", "labels = cxcywh / torch.tensor([<m>128, 160</m>, <m>128, 160</m>])",
         ("IoU", "1.0", " · ".join(f2(v) for v in WH["iou"]), "after"),
         "라벨을 다시 픽셀로 되돌려 원래 박스와 비교. 오른쪽 박스는 이미지 밖으로 나감", "손 예제(정답 박스 3개)",
         "x는 W로, y는 H로 나눈다. 저장한 라벨은 다시 그려서 확인한다"),
    ]),
    ("학습 코드는 그대로, 나누고 고르는 방법만 바꾸기", "데이터를 나누는 단위나 남길 checkpoint만 바꿨습니다", [
        ("3", "분할 단위", 'split = "train" if group_id in train_groups else "val"', '# 이미지를 번갈아 배정\nsplit = "train" if <m>i % 2 == 0</m> else "val"',
         ("split을 넘나드는 그룹", str(SP["cross_group"]), str(SP["cross_image"]), "after"),
         f'{len(SP["groups"])}개 그룹 전부가 train과 val에 걸침', f'응용 데이터 {sum(len(g[1]) for g in SP["groups"])}장({len(SP["groups"])}그룹)',
         "같은 장면·연속 프레임이 양쪽에 섞이면 점수가 부풀려진다. 그룹 단위로 나눈다"),
        ("5", "checkpoint", "metrics = model.val()  # 학습 뒤 model = best.pt", 'model = YOLO(\n    "runs/detect/train/weights/<m>last.pt</m>")\nmetrics = model.val()',
         ("mAP50-95", f3(V["best"]["map"]), f3(V["last"]["map"]), "after"),
         f'mAP50은 오히려 {f3(V["best"]["map50"])} → {f3(V["last"]["map50"])}. best({F["best_epoch"]} epoch)는 mAP50-95가 가장 높은 epoch', f'응용 val · last = {F["last_epoch"]} epoch', None),
    ]),
]
assert (c25["P"], c50["P"], c90["R"], n50["fp"], E95["tp"]) == (0.698, 0.857, 0.4, 0, 1)


def code_mark(t):
    return esc(t).replace("&lt;m&gt;", "<mark>").replace("&lt;/m&gt;", "</mark>")


knob_html, n_key = [], 0
for gname, gdesc, rows in GROUPS:
    knob_html.append(f'      <p class="kgroup">{gname}<span>{gdesc}</span></p>')
    for p, name, old, new, delta, res, src, lesson in rows:
        metric, a_, b_, cls = delta
        d = (f'<p class="delta"><span class="note">{metric}</span><span class="big">{a_}</span>'
             f'<span class="arrow">→</span><span class="big {cls}">{b_}</span></p>')
        key = ""
        if lesson:
            n_key += 1
            key = f'<p class="lesson"><span class="keytag">꼭 기억</span>{esc(lesson)}</p>'
        knob_html.append(
            f'      <div class="krow{" key" if lesson else ""}"><p class="kname"><span class="period {zone(p)}">{p}교시</span>{name}</p>'
            f'<pre class="old">{code_mark(old)}</pre><span class="go">→</span><pre class="new">{code_mark(new)}</pre>'
            f'<div class="res">{d}<p>{esc(res)}</p><p class="src">{esc(src)}</p></div>{key}</div>')
assert n_key == 7, n_key

# ── 응용·심화가 더 요구하는 것 ──
demand = []
for m in re.finditer(r"^\| (\d) (\S+) \| ([^|]+) \| ([^|]+) \|$", MD, re.M):
    p, label, app, deep = (c.strip() for c in m.groups())

    def cell(t, extra=""):
        main, _, why = t.partition(". ")
        why = f'<span class="why">{md_inline(why)}</span>' if why else ""
        return f'<div class="cell{extra}">{md_inline(main)}{why}</div>'
    demand.append(f'      <p class="rowlab"><span class="period {zone(p)}">{p}교시</span>{label}</p>{cell(app)}{cell(deep, " deep")}')
assert len(demand) == 8


# ── 그림 도우미: 실제 이미지 위에 이미지 좌표로 덧그린 SVG ──
def img_svg(src, W, H, body, label, width=None, pad=0):
    w = f' width="{width}"' if width else ""
    return (f'<svg viewBox="{-pad} {-pad} {W + 2 * pad} {H + 2 * pad}"{w} role="img" aria-label="{esc(label)}">'
            f'<image href="{src}" x="0" y="0" width="{W}" height="{H}" style="image-rendering:pixelated"/>{body}</svg>')


def rect(b, color, sw=1.4, dash=None, opacity=1):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{b[0]:.1f}" y="{b[1]:.1f}" width="{b[2] - b[0]:.1f}" height="{b[3] - b[1]:.1f}" fill="none" '
            f'stroke="{color}" stroke-width="{sw}"{d} opacity="{opacity}"/>')


def tag(x, y, text, color, size=7):
    w = len(text) * size * 0.56 + 4
    return (f'<rect x="{x:.1f}" y="{y - size - 1:.1f}" width="{w:.1f}" height="{size + 3}" rx="1.5" fill="{color}"/>'
            f'<text x="{x + 2:.1f}" y="{y:.1f}" font-size="{size}" font-weight="700" fill="#fff">{esc(text)}</text>')


# ── ① 깔때기 ──
FU = F["funnel"]
W0, H0 = FU["W"], FU["H"]
grid_figs = []
for (gw, gh), s in zip(FU["grids"], (8, 16, 32)):
    dots = []
    for x, y, st, sc in FU["anchors"]:
        if st != s:
            continue
        r = 0.7 + 3.2 * sc if s == 8 else 1.0 + 3.6 * sc
        col = NAVY if sc > 0.25 else "#FFFFFF"
        op = 0.95 if sc > 0.25 else 0.75
        dots.append(f'<circle cx="{x}" cy="{y}" r="{r:.2f}" fill="{col}" stroke="{NAVY}" stroke-width="{0.35 if sc <= 0.25 else 0}" opacity="{op}"/>')
    lines = "".join(f'<line x1="{i * s}" x2="{i * s}" y1="0" y2="{H0}" stroke="#fff" stroke-width="0.4" opacity="0.6"/>' for i in range(1, gw)) + \
        "".join(f'<line x1="0" x2="{W0}" y1="{j * s}" y2="{j * s}" stroke="#fff" stroke-width="0.4" opacity="0.6"/>' for j in range(1, gh))
    body = f'<rect width="{W0}" height="{H0}" fill="#fff" opacity="0.45"/>{lines}{"".join(dots)}'
    grid_figs.append(f'<figure>{img_svg(FU["image"], W0, H0, body, f"격자 {gw}×{gh}의 후보 점")}'
                     f'<figcaption><b>{gw}×{gh}</b>칸 {s}px · 후보 {gw * gh}개</figcaption></figure>')

conf_body = "".join(rect(b[:4], NAVY, 1.1, opacity=0.85) for b in FU["after_conf"])
def place_tags(boxes, text_of, color_of, size):
    placed, out = [], ""
    for b in sorted(boxes, key=lambda b: -b[4]):
        t = text_of(b)
        w = len(t) * size * 0.56 + 4
        x, y = b[0], b[1] - 1.5
        if any(abs(x - px) < max(w, pw) and abs(y - py) < size + 3 for px, py, pw in placed):
            y = b[3] + size + 1.5
        placed.append((x, y, w))
        out += tag(x, y, t, color_of(b), size)
    return out


nms_body = "".join(rect(b[:4], NAVY, 1.4) for b in FU["after_nms"]) + place_tags(FU["after_nms"], lambda b: f'{F["names"][b[5]]} {b[4]:.2f}', lambda b: NAVY, 6.2)
gt_body = "".join(rect(g[:4], "#1C2B40", 1.0, "3 2") for g in FU["gt"])
score_body = gt_body + "".join(rect(b[:4], GREEN if b[6] else ORANGE, 1.6) for b in sorted(FU["after_nms"], key=lambda b: b[6])) + \
    "".join(tag(b[0], b[3] + 8, f"FP · conf {b[4]:.2f}", ORANGE, 6.5) for b in FU["after_nms"] if not b[6])
n_tp = sum(b[6] for b in FU["after_nms"])
n_fp = len(FU["after_nms"]) - n_tp
PAD = 9
funnel = f'''    <div class="funnel">
      <div class="fstep model"><p class="fh"><b>Backbone·Neck·Head</b><span class="tag">한 번 보고 격자마다 예측</span></p>
        <div class="grids">{"".join(grid_figs)}</div>
        <p class="fh"><span class="count">{N}<small>개 후보</small></span><span class="what">칸마다 박스 4개 + 클래스 점수 3개. 점이 클수록 점수가 높다(<span class="legend-dot" style="background:{NAVY}"></span>0.25 초과)</span></p></div>
      <span class="arrow">→</span>
      <div class="fstep filter"><p class="fh"><b>conf로 거르기</b><span class="knob">conf=0.25</span></p>
        {img_svg(FU["image"], W0, H0, conf_body, "conf 0.25 초과 후보 박스", pad=PAD)}
        <p class="fh"><span class="count">{len(FU["after_conf"])}<small>개</small></span><span class="what">점수 낮은 후보를 버림. 같은 객체에 박스가 여러 개 겹쳐 있다</span></p></div>
      <span class="arrow">→</span>
      <div class="fstep filter"><p class="fh"><b>NMS로 중복 지우기</b><span class="knob">iou=0.7</span></p>
        {img_svg(FU["image"], W0, H0, nms_body, "NMS 뒤 남은 박스", pad=PAD)}
        <p class="fh"><span class="count">{len(FU["after_nms"])}<small>개 = Results</small></span><span class="what">겹친 박스 중 점수가 가장 높은 것만 남김</span></p></div>
      <span class="arrow">→</span>
      <div class="fstep score"><p class="fh"><b>정답과 비교해 채점</b><span class="knob">평가 IoU ≥ 0.5</span></p>
        {img_svg(FU["image"], W0, H0, score_body, "정답 박스와 비교한 TP·FP", pad=PAD)}
        <p class="fh"><span class="count">TP {n_tp} · FP {n_fp}</span><span class="what">점선 = 정답 {len(FU["gt"])}개, <b class="good">초록 = TP</b>, <b class="after">주황 = FP</b>. NMS 기본값 0.7에서 남은 중복 1개가 FP가 됐다</span></p></div>
    </div>
    <p class="cap" style="margin-top:8px">응용 val 이미지 1장(정답 3개)을 공식 추론 경로 그대로 실행한 결과입니다. 입력 160×128 → 격자 20×16 + 10×8 + 5×4 = {N}칸.</p>'''


# ── ⑤ 파라미터 지도 그림 ──
def fig_A():
    sw = F["wh_swap"]
    W, H = sw["W"], sw["H"]
    body = ""
    for g, bk, v in zip(sw["gt"], sw["back"], sw["iou"]):
        body += rect(g[:4], NAVY, 1.6) + rect(bk, ORANGE, 1.4, "3 2")
        body += tag(min(bk[0], W - 30) if bk[0] < W else W - 30, bk[3] + 8, f"IoU {v:.2f}", ORANGE, 6.5)
    svg = img_svg(sw["image"], W, H, body, "정답 박스와 W·H를 뒤바꿔 되돌린 박스", width="100%", pad=14)
    lab = " ".join(f"{v:.6f}" for v in sw["label_right"])
    return (f'<div class="viz"><p class="viz-title">W·H를 뒤바꿔 정규화하면 박스가 어긋난다 <span class="note">(손 예제, 160×128)</span></p>'
            f'<div class="viz-row"><div style="flex:1 1 15rem">{svg}</div><div class="cap" style="flex:1 1 12rem;align-self:center">'
            f'<p><span class="legend-dot" style="background:{NAVY}"></span>실선 = 원래 정답 박스</p>'
            f'<p><span class="legend-dot" style="background:{ORANGE}"></span>점선 = <code>[128, 160, …]</code>로 나눈 라벨을 다시 픽셀로 되돌린 박스</p>'
            f'<p style="margin-top:6px">폭 160과 높이 128이 바뀌어 위치와 크기가 함께 틀어집니다. 오른쪽 박스는 이미지 밖으로 나갑니다.</p>'
            f'<p style="margin-top:8px">맞는 라벨 한 줄</p><p class="labelline">0 {lab}<span>class cx cy w h</span></p></div></div></div>')


def fig_B():
    fx, sw = F["fixture"], F["wh_swap"]
    W, H = sw["W"], sw["H"]
    body = "".join(rect(g[:4], "#1C2B40", 1.0, "3 2") for g in sw["gt"])
    marks = "①②③④"
    for i, p in enumerate(fx["pred"]):
        col = GREEN if p[7] else ORANGE
        body += rect(p[:4], col, 1.5)
        tx, ty = (p[2] + 2, p[1] + 8 + (9 if i == 1 else 0)) if p[2] < W - 12 else (p[0] - 10, p[1] + 8)
        body += f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="8.5" font-weight="700" fill="{col}">{marks[i]}</text>'
    svg = img_svg(sw["image"], W, H, body, "예측 4개와 정답 3개의 매칭", width="100%", pad=6)
    rows = ""
    why = ["", "같은 정답을 이미 ①이 차지 → 중복", "", "겹치는 정답 없음 → 배경"]
    for i, p in enumerate(fx["pred"]):
        col = GREEN if p[7] else ORANGE
        rows += (f'<p style="display:grid;grid-template-columns:1.2rem 3.2rem 4.6rem 1fr;gap:4px;align-items:baseline">'
                 f'<b style="color:{col}">{marks[i]}</b><span>{p[4]:.2f}</span><span>IoU {p[6]:.2f}</span>'
                 f'<span><b style="color:{col}">{"TP" if p[7] else "FP"}</b> {why[i]}</span></p>')
    table = (f'<div class="cap" style="font-size:0.75rem;display:flex;flex-direction:column;gap:2px">'
             f'<p style="display:grid;grid-template-columns:1.2rem 3.2rem 4.6rem 1fr;gap:4px;font-weight:700"><span></span><span>conf</span><span>최대 IoU</span><span>판정</span></p>{rows}'
             f'<p style="margin-top:4px">TP {fx["tp"]} · FP {fx["fp"]} · FN {fx["fn"]} → Precision {fx["tp"] / (fx["tp"] + fx["fp"]):.2f}, Recall {fx["tp"] / (fx["tp"] + fx["fn"]):.2f}</p></div>')
    # mAP vs 평가 IoU 기준
    vals = F["val"]["map_by_iou"]
    ths = [0.5 + 0.05 * i for i in range(10)]
    Wc, Hc, L, R, Tp, B = 580, 190, 34, 16, 16, 30
    sx = lambda t: L + (t - 0.5) / 0.45 * (Wc - L - R)
    sy = lambda v: Tp + (1 - v) * (Hc - Tp - B)
    out = [f'<svg viewBox="0 0 {Wc} {Hc}" width="100%" role="img" aria-label="평가 IoU 기준별 mAP">']
    for v in (0, 0.5, 1.0):
        out.append(f'<line x1="{L}" x2="{Wc - R}" y1="{sy(v)}" y2="{sy(v)}" stroke="#E6EEF8"/><text x="{L - 5}" y="{sy(v) + 3.5}" font-size="10" text-anchor="end" fill="{MUTED}">{v:g}</text>')
    for t in (0.5, 0.6, 0.7, 0.8, 0.9, 0.95):
        out.append(f'<text x="{sx(t)}" y="{Hc - B + 14}" font-size="10" text-anchor="middle" fill="{MUTED}">{t:g}</text>')
    out.append(f'<text x="{(L + Wc - R) / 2}" y="{Hc - 3}" font-size="10" text-anchor="middle" fill="{MUTED}">평가 IoU 기준</text>')
    mean = sum(vals) / len(vals)
    out.append(f'<line x1="{L}" x2="{Wc - R}" y1="{sy(mean)}" y2="{sy(mean)}" stroke="{ORANGE}" stroke-dasharray="4 3"/>'
               f'<text x="{L + 6}" y="{sy(mean) + 15}" font-size="10.5" font-weight="700" fill="{ORANGE}">mAP50-95 = 10개 기준의 평균 {mean:.3f}</text>')
    pts = " ".join(f"{sx(t):.1f},{sy(v):.1f}" for t, v in zip(ths, vals))
    out.append(f'<polyline points="{pts}" fill="none" stroke="{NAVY}" stroke-width="2.2"/>')
    out += [f'<circle cx="{sx(t):.1f}" cy="{sy(v):.1f}" r="3" fill="{NAVY}"/>' for t, v in zip(ths, vals)]
    out.append(f'<text x="{sx(0.5) + 4}" y="{sy(vals[0]) - 7}" font-size="10.5" font-weight="700" fill="{NAVY}">mAP50 {vals[0]:.3f}</text></svg>')
    return (f'<div class="viz"><p class="viz-title">1:1 매칭 · 예측 4개와 정답 3개 <span class="note">(손 예제, 평가 IoU 0.5)</span></p>'
            f'<div class="viz-row"><div style="flex:1 1 13rem">{svg}</div><div style="flex:1.3 1 15rem;align-self:center">{table}</div></div></div>'
            f'<div class="viz"><p class="viz-title">기준을 엄격하게 하면 mAP가 떨어진다 <span class="note">(실측 모델, 응용 val)</span></p>{"".join(out)}'
            f'<p class="cap">0.7까지는 거의 그대로인데 0.85부터 급히 떨어집니다. 객체는 찾지만 박스 위치가 아주 정확하지는 않다는 뜻입니다.</p></div>')


def fig_C():
    sp = F["split"]

    def strip(key, label, verdict, good):
        cells = ""
        for _, gs, im in sp["groups"]:
            s = gs if key == "group" else im
            cells += ('<span style="display:inline-flex;gap:1px;padding:2px;border:1px dashed #9DB3CF;border-radius:4px">' +
                      "".join(f'<i style="width:9px;height:12px;border-radius:2px;display:inline-block;background:{ACCENT if v == "train" else "#E3A877"}"></i>' for v in s) + "</span>")
        return (f'<p style="font-size:0.8125rem;font-weight:700;margin-top:6px">{label} <span class="{"good" if good else "after"}" style="font-weight:700">{verdict}</span></p>'
                f'<div style="display:flex;flex-wrap:wrap;gap:3px">{cells}</div>')
    neg = F["negative"]
    split = (strip("image", "이미지 번갈아", f'✕ {sp["cross_image"]}개 그룹이 train·val에 걸침', False) +
             strip("group", "그룹 단위", f'✓ 걸치는 그룹 {sp["cross_group"]}개', True) +
             f'<p class="cap" style="margin-top:6px">점선 상자 = 같은 장면에서 나온 이미지 2장(그룹). <span class="legend-dot" style="background:{ACCENT};border-radius:2px"></span>train <span class="legend-dot" style="background:#E3A877;border-radius:2px"></span>val</p>')
    negfig = (f'<div style="display:flex;gap:var(--space-3);align-items:center">'
              f'<img src="{neg["image"]}" alt="객체 없는 이미지" style="width:7rem;image-rendering:pixelated;border-radius:6px;border:1px solid {LINE}">'
              f'<div class="cap"><p><b>객체 없는 이미지</b>도 학습 데이터입니다.</p><p>라벨 파일은 있고 내용은 비어 있음({neg["label_bytes"]} byte) = "객체 0개"라는 기록. 파일이 아예 없는 누락과 다릅니다.</p>'
              f'<p>응용 데이터: train {neg["counts"].get("train", 0)}장 · val {neg["counts"].get("val", 0)}장 · test {neg["counts"].get("test", 0)}장</p></div></div>')
    return (f'<div class="viz"><p class="viz-title">누수를 막는 그룹 분할 <span class="note">(응용 데이터 train+val {sum(len(g[1]) for g in sp["groups"])}장, {len(sp["groups"])}그룹)</span></p>{split}</div>'
            f'<div class="viz"><p class="viz-title">빈 라벨 = 정상 기록</p>{negfig}</div>')


def fig_D():
    c = F["curve"]
    ep, m50, m = c["epoch"], c["map50"], c["map"]
    n = len(ep)
    W, H, L, R, Tp, B = 580, 210, 34, 70, 22, 30
    sx = lambda e: L + (e - 1) / (n - 1) * (W - L - R)
    sy = lambda v: Tp + (1 - v) * (H - Tp - B)
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="epoch별 mAP50과 mAP50-95">']
    out.append(f'<rect x="{sx(1)}" y="{Tp}" width="{sx(first_nz - 0.5) - sx(1)}" height="{H - Tp - B}" fill="#FDF6EF"/>'
               f'<text x="{(sx(1) + sx(first_nz - 0.5)) / 2}" y="{Tp + 14}" font-size="10.5" text-anchor="middle" fill="{ORANGE}" font-weight="700">1~{first_nz - 1} epoch: mAP 0</text>')
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        out.append(f'<line x1="{L}" x2="{W - R}" y1="{sy(v)}" y2="{sy(v)}" stroke="#E6EEF8"/><text x="{L - 5}" y="{sy(v) + 3.5}" font-size="10" text-anchor="end" fill="{MUTED}">{v:g}</text>')
    for e in (1, 10, 20, 30, 40, 50, 60):
        out.append(f'<text x="{sx(e)}" y="{H - B + 14}" font-size="10" text-anchor="middle" fill="{MUTED}">{e}</text>')
    out.append(f'<text x="{(L + W - R) / 2}" y="{H - 3}" font-size="10" text-anchor="middle" fill="{MUTED}">epoch (val 채점)</text>')
    for vals, col, lab in ((m50, "#9DB3CF", "mAP50"), (m, NAVY, "mAP50-95")):
        pts = " ".join(f"{sx(e):.1f},{sy(v):.1f}" for e, v in zip(ep, vals))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.2" stroke-linejoin="round"/>'
                   f'<text x="{W - R + 6}" y="{sy(vals[-1]) + 4}" font-size="11" font-weight="700" fill="{col}">{lab}</text>')
    be = F["best_epoch"]
    bx, by = sx(be), sy(m[be - 1])
    lx, ly = sx(n), sy(m[-1])
    out.append(f'<line x1="{bx}" x2="{bx}" y1="{by + 6}" y2="{sy(0.3)}" stroke="{NAVY}"/><circle cx="{bx}" cy="{by}" r="4.5" fill="{NAVY}"/>'
               f'<text x="{bx}" y="{sy(0.3) + 13}" font-size="10.5" font-weight="700" text-anchor="middle" fill="{NAVY}">best.pt · {be} epoch</text>'
               f'<line x1="{lx}" x2="{lx}" y1="{ly + 6}" y2="{sy(0.12)}" stroke="{ORANGE}"/><circle cx="{lx}" cy="{ly}" r="4.5" fill="#fff" stroke="{ORANGE}" stroke-width="2"/>'
               f'<text x="{lx}" y="{sy(0.12) + 13}" font-size="10.5" text-anchor="end" fill="{ORANGE}">last.pt · {n} epoch</text></svg>')
    return (f'<div class="viz"><p class="viz-title">60 epoch 동안의 val 지표 <span class="note">(실측 모델, 응용 데이터)</span></p>{"".join(out)}'
            f'<p class="cap">처음 {first_nz - 1} epoch은 박스를 하나도 맞히지 못했습니다. <code>epochs=1</code>로 따로 학습해도 mAP는 0입니다. best.pt는 mAP50-95가 가장 높았던 {be} epoch이고, 마지막 epoch과 다릅니다.</p></div>')


def fig_E():
    cs_ = F["conf_sweep"]
    W, H, L, R, Tp, B = 580, 200, 34, 70, 16, 30
    sx = lambda c: L + (c - 0.05) / 0.9 * (W - L - R)
    sy = lambda v: Tp + (1 - v) * (H - Tp - B)
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="conf에 따른 Precision과 Recall">']
    for v in (0, 0.5, 1.0):
        out.append(f'<line x1="{L}" x2="{W - R}" y1="{sy(v)}" y2="{sy(v)}" stroke="#E6EEF8"/><text x="{L - 5}" y="{sy(v) + 3.5}" font-size="10" text-anchor="end" fill="{MUTED}">{v:g}</text>')
    for c in (0.05, 0.25, 0.5, 0.75, 0.95):
        out.append(f'<text x="{sx(c)}" y="{H - B + 14}" font-size="10" text-anchor="middle" fill="{MUTED}">{c:g}</text>')
    out.append(f'<text x="{(L + W - R) / 2}" y="{H - 3}" font-size="10" text-anchor="middle" fill="{MUTED}">conf</text>')
    out.append(f'<line x1="{sx(0.25)}" x2="{sx(0.25)}" y1="{Tp}" y2="{H - B}" stroke="{MUTED}" stroke-dasharray="3 3"/>'
               f'<text x="{sx(0.25) + 4}" y="{H - B - 6}" font-size="10" fill="{MUTED}">기본 0.25</text>')
    for key, col, lab in (("P", NAVY, "Precision"), ("R", ORANGE, "Recall")):
        pts = " ".join(f"{sx(r['conf']):.1f},{sy(r[key]):.1f}" for r in cs_)
        out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.2"/>'
                   f'<text x="{W - R + 6}" y="{sy(cs_[-1][key]) + (4 if key == "P" else 4)}" font-size="11" font-weight="700" fill="{col}">{lab}</text>')
    out.append("</svg>")
    ns_ = F["nms_sweep"]
    mx = max(r["boxes"] for r in ns_)
    bars = ""
    for r in ns_:
        tw, fw = r["tp"] / mx * 100, r["fp"] / mx * 100
        bold = "font-weight:700;color:var(--color-heading)" if r["iou"] == 0.7 else ""
        bars += (f'<div style="display:grid;grid-template-columns:5.2rem 1fr 2.2rem;gap:6px;align-items:center;font-size:0.75rem">'
                 f'<span style="{bold}">iou {r["iou"]:g}{" 기본" if r["iou"] == 0.7 else ""}</span>'
                 f'<span style="display:flex;height:11px"><i style="width:{tw:.1f}%;background:{NAVY};border-radius:2px 0 0 2px"></i><i style="width:{fw:.1f}%;background:{ORANGE};border-radius:0 2px 2px 0"></i></span>'
                 f'<b>{r["boxes"]}</b></div>')
    bars = (f'<div style="display:flex;flex-direction:column;gap:3px">{bars}</div>'
            f'<p class="cap" style="margin-top:4px"><span class="legend-dot" style="background:{NAVY};border-radius:2px"></span>TP <span class="legend-dot" style="background:{ORANGE};border-radius:2px"></span>FP(중복). 낮출수록 겹친 중복을 더 지웁니다. 0.5 이하에서 FP 0.</p>')
    return (f'<div class="viz"><p class="viz-title">첫 거름망 conf · 올리면 Precision↑ Recall↓ <span class="note">(응용 val 12장)</span></p>{"".join(out)}</div>'
            f'<div class="viz"><p class="viz-title">두 번째 거름망 NMS IoU · 남는 박스 수 <span class="note">(conf 0.25)</span></p>{bars}</div>')


def fig_F():
    tr = F["track"]
    nf = tr["frames"]
    by_id = {}
    for f, tid, obj in tr["rows"]:
        by_id.setdefault(tid, {})[f] = obj
    ids = sorted(by_id)
    W, rh, L, Tp = 580, 15, 46, 16
    H = Tp + len(ids) * rh + 24
    cw = (W - L - 6) / nf
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="프레임별 Track ID">']
    for f in (0, 10, 20, nf - 1):
        out.append(f'<text x="{L + f * cw + cw / 2:.1f}" y="{Tp - 4}" font-size="9.5" text-anchor="middle" fill="{MUTED}">{f}</text>')
    for r, tid in enumerate(ids):
        y = Tp + r * rh
        out.append(f'<text x="{L - 6}" y="{y + 10}" font-size="10" text-anchor="end" fill="#1C2B40" font-weight="700">ID {tid}</text>')
        for f, obj in by_id[tid].items():
            out.append(f'<rect x="{L + f * cw + 0.5:.1f}" y="{y + 1}" width="{cw - 1:.1f}" height="{rh - 3}" rx="1.5" fill="{OBJ_COL[obj]}"/>')
    lx = L
    for obj, name in [(1, tr["obj_class"]["1"]), (2, tr["obj_class"]["2"]), (3, tr["obj_class"]["3"]), (0, "정답과 안 겹침")]:
        out.append(f'<rect x="{lx}" y="{H - 13}" width="10" height="10" rx="2" fill="{OBJ_COL[obj]}"/><text x="{lx + 14}" y="{H - 4}" font-size="10" fill="{MUTED}">{name}</text>')
        lx += 22 + len(name) * 7.5
    out.append(f'<text x="{W - 4}" y="{H - 4}" font-size="10" text-anchor="end" fill="{MUTED}">frame →</text></svg>')
    chips = lambda xs, col: "".join(f'<span style="display:inline-block;min-width:1.6rem;text-align:center;font-size:0.6875rem;padding:0 3px;border-radius:4px;background:{col};color:#fff;margin:1px">{x}</span>' for x in xs)
    persist = (f'<div class="cap" style="display:flex;flex-direction:column;gap:4px">'
               f'<p><b>새 YOLO 객체로 다음 영상</b> {chips(tr["ids_fresh"], ACCENT)}</p>'
               f'<p><b>같은 객체 + <code>persist=True</code></b> {chips(tr["ids_second_persist"], ORANGE)}</p>'
               f'<p>같은 영상을 다음 영상처럼 넣은 실험입니다. persist를 잘못 쓰면 앞 영상의 상태를 이어받아 ID가 이어 붙고 커집니다.</p></div>')
    return (f'<div class="viz"><p class="viz-title">실제 객체 {tr["objects"]}개 → Track ID {len(ids)}개 <span class="note">(demo 영상 {nf}프레임, ByteTrack)</span></p>{"".join(out)}'
            f'<p class="cap">한 객체가 여러 ID로 쪼개지고(fragmentation), 겹친 중복 박스에도 ID가 붙습니다. ID 개수는 객체 수가 아닙니다. 추적 품질은 탐지 품질에 묶입니다.</p></div>'
            f'<div class="viz"><p class="viz-title">Track ID는 실행 중 상태</p>{persist}</div>')


FIGS = {"A": fig_A(), "B": fig_B(), "C": fig_C(), "D": fig_D(), "E": fig_E(), "F": fig_F()}
groups = []
for m in re.finditer(r"^### ([A-F])\. (.+?) — \"(.+?)\"\n(.*?)(?=\n### |\n---|\Z)", MD, re.S | re.M):
    L_, title, q, body = m.groups()
    rows = []
    for line in body.strip().split("\n")[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(f'<div class="prow"><p class="nm">{md_inline(cells[0])}</p><p><span class="val">{md_inline(cells[1])}</span>'
                    f'<span class="mean">{md_inline(cells[2])}</span></p></div>')
    groups.append(f'    <div class="pgroup"><div class="gh"><span class="L">{L_}</span><h3>{title}</h3><span class="q">{q}</span></div>'
                  f'{FIGS[L_]}<div class="params">{"".join(rows)}</div></div>')
assert len(groups) == 6, len(groups)

env = F["env"]
out = T
for k, v in {"LEDE": md_inline(lede), "FUNNEL": funnel, "N_CAND": str(N), "STEPS": "\n".join(steps), "FLOW": "\n".join(flow),
             "CODE": "\n".join(code_html), "KNOBS": "\n".join(knob_html), "DEMAND": "\n".join(demand),
             "PGROUPS": "\n".join(groups), "ULTRA": env["ultralytics"], "TORCH": env["torch"], "OPENCV": env["opencv"]}.items():
    out = out.replace("{{" + k + "}}", v)
assert "{{" not in out, re.findall(r"\{\{\w+\}\}", out)
(HERE / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out) // 1024, "KB")
