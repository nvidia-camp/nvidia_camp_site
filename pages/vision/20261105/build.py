"""Day14 oneday 요약 HTML 빌드.

구성안(nvidia_camp/04_vision/20261105/Day14_개념가이드_00_하루개요.md)의 코드·표와 실측 그림 데이터(facts.json)를
template.html에 채워 index.html을 만듭니다.

실행: python3 build.py
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAMP = HERE.parents[3]   # nvidia_camp
MD = (CAMP / "04_vision/20261105/Day14_개념가이드_00_하루개요.md").read_text(encoding="utf-8")
F = json.loads((HERE / "facts.json").read_text(encoding="utf-8"))
T = (HERE / "template.html").read_text(encoding="utf-8")
CLS = F["classes"]


def md_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def zone(period):
    n = int(re.match(r"\d", period).group())
    return "prep" if n <= 3 else "learn" if n <= 5 else "explain"


# ── 핵심 코드: 구성안의 python 블록을 교시 블록별로 자른다 ──
code = re.search(r"### 핵심 코드\n\n```python\n(.*?)```", MD, re.S).group(1).rstrip("\n").split("\n")
segs, cur = [], []
for line in code:
    if line.startswith("# ── "):
        if cur:
            segs.append(cur)
        cur = []
        continue
    cur.append(line)
segs.append(cur)
segs = [[l for l in s] for s in segs]
for s in segs:  # 앞뒤 빈 줄 제거
    while s and not s[0].strip():
        s.pop(0)
    while s and not s[-1].strip():
        s.pop()

TOKEN = re.compile(r'(?P<s>"[^"]*"|\'[^\']*\')|(?P<k>\b(?:for|in|if|float)\b)|(?P<n>\b\d+(?:\.\d+)?\b)')


def hl(line):
    i = line.find("#")
    body, com = (line, "") if i < 0 else (line[:i], line[i:])
    out, pos = [], 0
    for m in TOKEN.finditer(body):
        out.append(html.escape(body[pos:m.start()], quote=False))
        out.append(f'<span class="{m.lastgroup}">{html.escape(m.group(), quote=False)}</span>')
        pos = m.end()
    out.append(html.escape(body[pos:], quote=False))
    if com:
        out.append(f'<span class="c">{html.escape(com, quote=False)}</span>')
    return "".join(out)


ANN = [
    ("8", "seed 고정", "무작위 시작값을 맨 앞에서 고정합니다. 그래야 다시 돌려도 같은 결과가 나옵니다."),
    ("1", "① 데이터 읽기", "폴더 이름이 곧 라벨 번호입니다. <code>class_to_idx</code>로 매핑을 눈으로 확인하고, 입력 규칙(32×32, 값 0~1)도 여기서 정합니다."),
    ("2", "② 모델 만들기", "얼리고 → 새 Head를 붙이고 → <code>eval()</code>. 얼리기는 <b>가중치</b>를, <code>eval()</code>은 <b>BN 기억값</b>을 고정하는 서로 다른 스위치입니다."),
    ("3·4", "③ 학습 ×8 → ④ best 복원", "열린 파라미터만 optimizer에 넘깁니다. 한 epoch = 지우기 → 오차 → gradient → 한 걸음. valid는 채점만 하고, valid loss가 가장 낮았던 가중치를 기억했다가 되돌립니다."),
    ("4·5", "⑤ 평가", "가장 큰 점수가 예측입니다. 클래스마다 같은 비중인 Macro F1과 confusion matrix(행=실제, 열=예측)로 <b>어디서</b> 틀렸는지 봅니다."),
    ("6", "⑥ 설명 · Grad-CAM", "target 클래스 점수를 마지막 Conv 특징 지도로 미분해 채널별 중요도를 구하고, 점수를 <b>올린</b> 곳(<code>relu</code>)만 남깁니다."),
    ("7·8", "⑦ 저장", "결과뿐 아니라 <b>어떻게 만들었는지</b>(lr·epoch·seed·test 미사용)까지 저장해야 다른 사람이 다시 만들 수 있습니다."),
]
assert len(segs) == len(ANN), (len(segs), len(ANN))
code_html = []
for s, (p, title, text) in zip(segs, ANN):
    z = zone(p)
    code_html.append(
        f'    <div class="cseg {z}"><pre><code>{chr(10).join(hl(l) for l in s)}</code></pre>'
        f'<div class="ann"><p class="t"><span class="period {z}">{p}교시</span>{title}</p><p>{text}</p></div></div>')

# ── 코드 속 파라미터: 위 코드 → 고친 코드 → 결과 (+ 꼭 기억할 7가지의 배울 점) ──
# 고친 코드의 <m>…</m>는 바뀐 부분 표시
# (교시, 이름, 위 코드, 고친 코드, (지표, 전, 후, 색) 또는 None, 결과 한 줄, 조건·출처, 배울 점 또는 None)
GROUPS = [
    ("숫자·옵션만 바꾸기", "줄은 그대로 두고 값만 고쳤습니다", [
        ("3", "보폭 lr", "AdamW(..., lr=0.01)", "AdamW(..., lr=<m>0.001</m>)",
         ("Accuracy", "1.0", "0.778", "after"), "8 epoch 안에 덜 배움. 반대로 0.1로 키우면 초반 valid loss가 11.7까지 튐(응용)", "기본 데이터", None),
        ("3", "epoch", "for epoch in range(8):", "for epoch in range(<m>1</m>):",
         ("Accuracy", "1.0", "0.556", "after"), "triangle을 하나도 찾지 못함", "기본 데이터", None),
        ("8", "seed", "torch.manual_seed(14)", "torch.manual_seed(<m>0</m>)  # 1·42·7도",
         ("Macro F1", "0.80", "0.51~0.58", "after"), "설정은 같은데 seed만 바꿔도 결과가 이만큼 흔들림", "응용 데이터 · 응용 실습 설정(lr 0.003)",
         "한 번의 결과로 결론 내리지 않는다. seed를 바꿔 여러 번 확인한다"),
        ("4", "class weight", "nn.CrossEntropyLoss()", "nn.CrossEntropyLoss(<m>weight=[0.3, 0.9, 1.8]</m>)",
         ("Macro F1", "0.804", "1.0", "good"), "triangle recall 0.5 → 1.0. 너무 세게(1/개수²) 주면 오히려 0.539", "응용 데이터 · 응용 실습 설정(lr 0.003)",
         "불균형 대응은 \"세게\"가 아니라 \"균형\". 적은 클래스를 살리되 과하게 밀지 않는다"),
        ("4", "평균 방식", 'f1_score(..., average="macro")', 'f1_score(..., average="<m>weighted</m>")',
         ("F1", "0.242", "0.416", "after"), "모든 이미지를 circle로 예측했는데 점수가 올라감. Accuracy도 0.571로 절반을 넘음", "손 예제 (circle 4 · square 2 · triangle 1)",
         "불균형한 데이터에서 Accuracy·weighted는 실패를 가린다. 클래스마다 같은 비중인 Macro F1을 본다"),
    ]),
    ("코드 한 줄 넣기·빼기", "줄을 추가하거나, 지우거나, 주석을 풀었습니다", [
        ("2", "사전학습 사용", "backbone = load_pretrained_backbone()", "backbone = <m>new_backbone()</m>  # 가중치 안 불러옴",
         ("Macro F1", "1.0", "0.167", "after"), "모든 이미지를 한 클래스로 예측", "기본 데이터",
         "전이학습의 가치. 특징을 못 뽑는 Backbone 위에서는 Head도 배울 수 없다"),
        ("1", "입력 규칙", "Compose([Resize((32, 32)), ToTensor()])", "Compose([Resize((32, 32)), ToTensor(),\n        <m>Normalize(ImageNet 평균, 표준편차)</m>])",
         ("Accuracy", "1.0", "0.933", "after"), "그런데 평균 확신도는 0.90 → 0.955로 오히려 올라감", "응용 데이터",
         "입력 규칙을 깨면 조용히, 자신 있게 틀린다. 사전학습 때의 입력 규칙을 그대로 지킨다"),
        ("2", "BN 모드", "backbone.eval()", "backbone.<m>train()</m>",
         ("Macro F1", "0.956", "0.790", "after"), "얼린 층의 BN 기억값이 학습 중에 바뀜", "응용 데이터 · Partial 학습",
         "requires_grad(가중치 고정)와 eval()(BN 기억값 고정)은 서로 다른 스위치다"),
        ("3", "Partial", "# backbone[4].requires_grad_(True)", "<m>backbone[4].requires_grad_(True)</m>  # 주석 해제",
         ("학습 파라미터", "771", "1,923", ""), "마지막 Conv 층(1,152개)까지 함께 학습", "데이터와 무관", None),
        ("6", "양의 반응만", "cam = (...).sum(dim=1).relu()", "cam = (...).sum(dim=1)  <m># relu 뺌</m>",
         None, "점수를 낮추는 영역(약 43%)까지 함께 칠해져, 어디가 근거인지 흐려짐", "응용 데이터", None),
    ]),
    ("순서만 바꾸기", "같은 줄들의 순서만 바꿨습니다 (흔한 실수)", [
        ("2", "동결 순서", "for p in backbone.parameters():\n    p.requires_grad = False\nmodel = nn.Sequential(backbone, head)",
         "model = nn.Sequential(backbone, head)\nfor p in <m>model</m>.parameters():\n    p.requires_grad = False",
         ("학습 파라미터", "771", "0", "after"), "새 Head까지 얼어서 아무것도 배우지 않음. 오류 메시지는 없음", "데이터와 무관",
         "순서 실수는 오류 없이 조용히 일어난다. 학습 파라미터 수를 꼭 출력해 확인한다"),
    ]),
    ("모델은 그대로, 고르고 읽는 방법만 바꾸기", "학습은 같고, 어떤 모델을 남길지나 무엇을 물을지만 바꿨습니다", [
        ("7", "best 복원", "model.load_state_dict(best_state)", "<m># 이 줄을 지움</m> → 마지막 epoch 그대로 사용",
         ("valid loss", "0.006", "0.277", "after"), "best 9 epoch 대신 다시 나빠진 16 epoch 모델이 남음", "응용 데이터 · lr 0.1, 16 epoch", None),
        ("6", "설명할 클래스", "score[0, target]  # target = 예측 square", "score[0, <m>0</m>]  # target = circle",
         ("target 점수", "+2.17", "−1.18", ""), "같은 square 이미지에 다른 질문을 한 셈. 열지도 모양도 바뀜", "응용 데이터", None),
    ]),
]


def code_mark(t):
    t = html.escape(t, quote=False).replace("&lt;m&gt;", "<mark>").replace("&lt;/m&gt;", "</mark>")
    return t


knob_html = []
n_key = 0
for gname, gdesc, rows in GROUPS:
    knob_html.append(f'      <p class="kgroup">{gname}<span>{gdesc}</span></p>')
    for p, name, old, new, delta, res, src, lesson in rows:
        z = zone(p)
        d = ""
        if delta:
            metric, a_, b_, cls = delta
            d = (f'<p class="delta"><span class="note">{metric}</span><span class="big">{a_}</span>'
                 f'<span class="arrow">→</span><span class="big {cls}">{b_}</span></p>')
        key = ""
        if lesson:
            n_key += 1
            key = f'<p class="lesson"><span class="keytag">꼭 기억</span>{html.escape(lesson)}</p>'
        knob_html.append(
            f'      <div class="krow{" key" if lesson else ""}"><p class="kname"><span class="period {z}">{p}교시</span>{name}</p>'
            f'<pre class="old">{code_mark(old)}</pre><span class="go">→</span><pre class="new">{code_mark(new)}</pre>'
            f'<div class="res">{d}<p>{html.escape(res)}</p><p class="src">{src}</p></div>{key}</div>')
assert n_key == 7, n_key

# ── 응용·심화가 더 요구하는 것 (구성안 표) ──
demand_html = []
for m in re.finditer(r"^\| (\d) (\S+) \| (.+?) \| (.+?) \|$", MD, re.M):
    p, label, app, deep = m.groups()
    z = zone(p)

    def cell(t, extra=""):
        main, _, why = t.partition(". ")
        why = f'<span class="why">{md_inline(why)}</span>' if why else ""
        return f'<div class="cell{extra}">{md_inline(main)}{why}</div>'
    demand_html.append(f'      <p class="rowlab"><span class="period {z}">{p}교시</span>{label}</p>{cell(app)}{cell(deep, " deep")}')
assert len(demand_html) == 8

# ── 그림 ──
def svg_counts():
    tr, va = F["counts"]["applied_train"], F["counts"]["applied_valid"]
    W, bw, gap, top, H = 300, 26, 10, 18, 120
    mx = max(tr)
    parts = [f'<svg viewBox="0 0 {W} {H + 34}" width="{W}" height="{H + 34}" role="img" aria-label="클래스별 이미지 수: train {tr}, valid {va}">']
    for i, name in enumerate(CLS):
        x = 20 + i * 95
        for j, (v, col) in enumerate(((tr[i], "#4B74A6"), (va[i], "#C9D9EE"))):
            h = v / mx * (H - top)
            xx = x + j * (bw + 4)
            parts.append(f'<rect x="{xx}" y="{H - h}" width="{bw}" height="{h}" rx="3" fill="{col}"/>')
            parts.append(f'<text x="{xx + bw / 2}" y="{H - h - 4}" font-size="11" text-anchor="middle" fill="#1C2B40" font-weight="700">{v}</text>')
        parts.append(f'<text x="{x + bw + 2}" y="{H + 16}" font-size="12" text-anchor="middle" fill="#222F44">{name}</text>')
    parts.append(f'<line x1="10" x2="{W - 10}" y1="{H}" y2="{H}" stroke="#D8E4F2"/>')
    parts.append(f'<rect x="20" y="{H + 24}" width="10" height="10" rx="2" fill="#4B74A6"/><text x="34" y="{H + 33}" font-size="11" fill="#52667E">train</text>'
                 f'<rect x="80" y="{H + 24}" width="10" height="10" rx="2" fill="#C9D9EE"/><text x="94" y="{H + 33}" font-size="11" fill="#52667E">valid</text>')
    parts.append("</svg>")
    return "".join(parts)


def fig_A():
    sm = "".join(
        f'<figure><div class="imgs">{"".join(f"<img class=px src={u} alt=\"{n} 예시\">" for u in F["samples"][n])}</div><figcaption>{n}</figcaption></figure>'
        for n in CLS)
    split = ('<div class="split">'
             '<p class="r"><span class="g"><i></i><i></i><i></i></span> 한 원본에서 만든 비슷한 이미지 묶음 = 그룹</p>'
             '<p class="r"><span class="g"><i></i><i></i></span><span class="arrow">|</span><span class="g"><i class="v"></i></span> <span class="bad">✕ 누수</span> 같은 묶음이 train·valid에 갈라짐 → valid 점수가 부풀려짐</p>'
             '<p class="r"><span class="g"><i></i><i></i><i></i></span><span class="arrow">|</span><span class="g"><i class="v"></i><i class="v"></i></span> <span class="ok">✓ 그룹 분할</span> 묶음째로 한쪽에만</p>'
             '<p class="cap">파랑 = train, 주황 = valid</p></div>')
    return (f'<div class="viz"><p class="viz-title">폴더 이름이 곧 라벨, 개수는 불균형 <span class="note">(응용 데이터)</span></p>'
            f'<div class="viz-row"><div class="samples">{sm}</div>{svg_counts()}</div></div>'
            f'<div class="viz"><p class="viz-title">누수를 막는 그룹 분할</p>{split}</div>')


def fig_B():
    layers = [("Conv1", 216), ("BN1", 16), ("Conv2", 1152), ("BN2", 32), ("Head", 771)]
    rows = [("Head-only", {"Head"}, F["trainable"]["head"]),
            ("Partial", {"Head", "Conv2"}, F["trainable"]["partial"]),
            ("Full", {"Conv1", "BN1", "Conv2", "BN2", "Head"}, F["trainable"]["full"])]
    W, rh = 560, 34
    out = [f'<svg viewBox="0 0 {W} {len(rows) * rh + 26}" width="100%" role="img" aria-label="전략별로 열리는 층과 학습 파라미터 수">']
    xs = [90, 152, 208, 290, 346]
    ws = [56, 50, 76, 50, 70]
    for (lab, _), x, w in zip(layers, xs, ws):
        out.append(f'<text x="{x + w / 2}" y="12" font-size="11" text-anchor="middle" fill="#52667E">{lab}</text>')
    out.append(f'<text x="{xs[3] + ws[3] + 8}" y="12" font-size="11" fill="#52667E" text-anchor="start"></text>')
    for r, (name, open_, n) in enumerate(rows):
        y = 18 + r * rh
        out.append(f'<text x="0" y="{y + 18}" font-size="12.5" font-weight="700" fill="#1C2B40">{name}</text>')
        for (lab, cnt), x, w in zip(layers, xs, ws):
            on = lab in open_
            fill = "#142849" if on else "#F0F6FD"
            stroke = "#142849" if on else "#C9D9EE"
            out.append(f'<rect x="{x}" y="{y + 4}" width="{w}" height="22" rx="5" fill="{fill}" stroke="{stroke}"/>')
            out.append(f'<text x="{x + w / 2}" y="{y + 19}" font-size="10.5" text-anchor="middle" fill="{"#fff" if on else "#52667E"}">{"열림" if on else "🔒"}</text>')
        out.append(f'<text x="{W - 4}" y="{y + 19}" font-size="13" font-weight="700" text-anchor="end" fill="#142849">{n:,}개</text>')
    out.append(f'<text x="{xs[0]}" y="{len(rows) * rh + 22}" font-size="10.5" fill="#52667E">층별 파라미터 수: Conv1 216 · BN1 16 · Conv2 1,152 · BN2 32 · Head 771</text>')
    out.append("</svg>")
    sw = ('<div class="switches">'
          '<div class="switch"><p class="sh"><span class="tg"></span><code>requires_grad = False</code></p><p><b>가중치</b>를 고정. 학습이 이 숫자를 바꾸지 못함</p></div>'
          '<div class="switch"><p class="sh"><span class="tg"></span><code>model.eval()</code></p><p><b>BN 기억값</b>(평균·분산)을 고정. 얼려도 <code>train()</code>이면 바뀜</p></div>'
          '</div><p class="cap" style="margin-top:6px">둘은 다른 스위치입니다. Partial에서 BN을 train 모드로 두면 Macro F1 0.956 → <b class="after">0.790</b> (응용 데이터)</p>')
    return (f'<div class="viz"><p class="viz-title">어디까지 열면 몇 개를 배우나 <span class="note">(학습 파라미터 수)</span></p>{"".join(out)}</div>'
            f'<div class="viz"><p class="viz-title">얼리는 스위치는 두 개</p>{sw}</div>')


def fig_C():
    cv = F["curves"]
    W, H, L, R, Tp, B = 560, 230, 40, 96, 26, 34
    ymax, n = 1.0, 16
    sx = lambda e: L + (e - 1) / (n - 1) * (W - L - R)
    sy = lambda v: Tp + (1 - v / ymax) * (H - Tp - B)
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="lr별 epoch에 따른 valid loss 곡선">',
           f'<defs><clipPath id="plot"><rect x="{L}" y="{Tp}" width="{W - L - R}" height="{H - Tp - B}"/></clipPath></defs>']
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        out.append(f'<line x1="{L}" x2="{W - R}" y1="{sy(v)}" y2="{sy(v)}" stroke="#E6EEF8"/>'
                   f'<text x="{L - 6}" y="{sy(v) + 4}" font-size="10" text-anchor="end" fill="#52667E">{v:g}</text>')
    for e in (1, 4, 8, 12, 16):
        out.append(f'<text x="{sx(e)}" y="{H - B + 16}" font-size="10" text-anchor="middle" fill="#52667E">{e}</text>')
    out.append(f'<text x="{(L + W - R) / 2}" y="{H - 2}" font-size="10.5" text-anchor="middle" fill="#52667E">epoch</text>')
    out.append(f'<text x="{L - 6}" y="{Tp - 12}" font-size="10.5" text-anchor="start" fill="#52667E">valid loss</text>')
    styles = {"0.001": ("#9DB3CF", "lr 0.001 · 느림"), "0.01": ("#4B74A6", "lr 0.01"), "0.1": ("#C98A5E", "lr 0.1 · 튐")}
    for lr, (col, lab) in styles.items():
        h = cv[lr]["hist"]
        pts = " ".join(f"{sx(i + 1):.1f},{sy(v):.1f}" for i, v in enumerate(h))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round" clip-path="url(#plot)"/>')
        out.append(f'<text x="{W - R + 6}" y="{sy(h[-1]) + 4}" font-size="11" fill="{col}" font-weight="700">{lab}</text>')
    h = cv["0.1"]["hist"]
    out.append(f'<text x="{sx(3) + 8}" y="{Tp - 12}" font-size="10.5" fill="#8A4B2A">↑ lr 0.1의 1·2 epoch는 {h[0]:.1f} · {h[1]:.1f}로 그래프 위로 벗어남</text>')
    be = cv["0.1"]["best_ep"]
    bx, by = sx(be), sy(h[be - 1])
    out.append(f'<line x1="{bx}" x2="{bx}" y1="{sy(0.46)}" y2="{by - 6}" stroke="#142849" stroke-width="1"/>'
               f'<circle cx="{bx}" cy="{by}" r="5" fill="#142849"/>'
               f'<text x="{bx}" y="{sy(0.5)}" font-size="11" font-weight="700" text-anchor="middle" fill="#142849">best · {be} epoch</text>')
    lx, ly = sx(16), sy(h[-1])
    out.append(f'<line x1="{lx}" x2="{lx}" y1="{sy(0.4)}" y2="{ly - 6}" stroke="#8A4B2A" stroke-width="1"/>'
               f'<circle cx="{lx}" cy="{ly}" r="5" fill="#fff" stroke="#8A4B2A" stroke-width="2"/>'
               f'<text x="{lx}" y="{sy(0.43)}" font-size="10.5" text-anchor="end" fill="#8A4B2A">마지막 · 16 epoch (다시 올라감)</text>')
    out.append("</svg>")
    return (f'<div class="viz"><p class="viz-title">lr은 보폭, epoch은 예산 <span class="note">(응용 데이터, Head-only, 16 epoch)</span></p>{"".join(out)}'
            '<p class="cap">작은 lr은 16 epoch 동안 느리게 내려가고, 큰 lr은 처음에 크게 튑니다. 마지막 epoch가 가장 좋은 epoch는 아니라서 valid loss가 가장 낮았던 순간(best)을 따로 저장합니다.</p></div>')


def fig_D():
    a, b = F["imbalance"]["none"], F["imbalance"]["weight"]
    W, H, L = 300, 150, 10
    out = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="class weight 적용 전후 클래스별 recall">']
    base = 110
    for i, name in enumerate(CLS):
        x = 20 + i * 95
        for j, (v, col) in enumerate(((a["recall"][i], "#C9D9EE"), (b["recall"][i], "#142849"))):
            hh = v * 85
            xx = x + j * 30
            out.append(f'<rect x="{xx}" y="{base - hh}" width="26" height="{hh}" rx="3" fill="{col}"/>'
                       f'<text x="{xx + 13}" y="{base - hh - 4}" font-size="10.5" text-anchor="middle" fill="#1C2B40" font-weight="700">{v:g}</text>')
        out.append(f'<text x="{x + 28}" y="{base + 16}" font-size="12" text-anchor="middle" fill="#222F44">{name}</text>'
                   f'<text x="{x + 28}" y="{base + 30}" font-size="10" text-anchor="middle" fill="#52667E">train {F["counts"]["applied_train"][i]}장</text>')
    out.append(f'<line x1="10" x2="{W - 10}" y1="{base}" y2="{base}" stroke="#D8E4F2"/></svg>')
    vs = ('<div class="vs">'
          f'<div><p class="vh">class weight <span class="note">= 배점</span></p><p>뽑는 횟수는 그대로, 적은 클래스 오답에 큰 벌점</p>'
          f'<p class="dots"><i class="c0"></i><i class="c0"></i><i class="c0"></i><i class="c0"></i><i class="c0"></i><i class="c0"></i><i class="c1"></i><i class="c1"></i><i class="c2 big"></i></p>'
          f'<p class="cap">weight = {b["weight"]} (1/개수, 평균 1)</p></div>'
          '<div><p class="vh">Sampler <span class="note">= 출제 빈도</span></p><p>벌점은 그대로, 적은 클래스를 더 자주 뽑음</p>'
          '<p class="dots"><i class="c0"></i><i class="c0"></i><i class="c0"></i><i class="c1"></i><i class="c1"></i><i class="c1"></i><i class="c2"></i><i class="c2"></i><i class="c2"></i></p>'
          '<p class="cap">둘을 함께 쓰면 보정이 두 번 들어갑니다</p></div></div>')
    return (f'<div class="viz"><p class="viz-title">class weight 전후 클래스별 recall <span class="note">(응용 데이터)</span></p>'
            f'<div class="viz-row">{"".join(out)}<div class="cap" style="max-width:12rem;align-self:center"><p><span style="display:inline-block;width:10px;height:10px;background:#C9D9EE;border-radius:2px"></span> 적용 전 · Macro F1 {a["f1"]}</p>'
            f'<p><span style="display:inline-block;width:10px;height:10px;background:#142849;border-radius:2px"></span> 적용 후 · Macro F1 {b["f1"]:g}</p>'
            f'<p style="margin-top:6px">가장 적은 triangle을 절반만 찾다가 모두 찾습니다.</p></div></div></div>'
            f'<div class="viz"><p class="viz-title">두 가지 대응은 다른 방식</p>{vs}</div>')


def fig_E():
    ac = F["all_circle"]
    true_dots = "".join(f'<i class="c{c}"></i>' for c in ac["y_true"])
    pred_dots = "".join('<i class="c0"></i>' for _ in ac["y_true"])
    bars = ""
    for lab, v, col in (("Accuracy", ac["acc"], "#C9D9EE"), ("Weighted F1", ac["weighted"], "#9DB3CF"), ("Macro F1", ac["macro"], "#142849")):
        bars += (f'<div style="display:grid;grid-template-columns:6.5rem 1fr 2.6rem;align-items:center;gap:6px;font-size:0.8125rem">'
                 f'<span>{lab}</span><span style="height:12px;border-radius:3px;background:{col};width:{v * 100:.0f}%"></span><b>{v}</b></div>')
    left = (f'<div style="flex:1;min-width:16rem"><p class="cap">실제 <span class="dots" style="display:inline-flex;vertical-align:middle">{true_dots}</span></p>'
            f'<p class="cap">예측 <span class="dots" style="display:inline-flex;vertical-align:middle">{pred_dots}</span> 전부 circle</p>'
            f'<div style="display:flex;flex-direction:column;gap:4px;margin-top:6px">{bars}</div>'
            '<p class="cap" style="margin-top:6px">circle F1은 0.727이지만 square·triangle은 0. Macro는 세 클래스를 같은 비중으로 평균해서 실패가 드러납니다.</p></div>')
    cm = F["imbalance"]["none"]["cm"]
    c, x0, y0 = 46, 62, 34
    svg = [f'<svg viewBox="0 0 {x0 + 3 * c + 10} {y0 + 3 * c + 8}" width="{x0 + 3 * c + 10}" role="img" aria-label="confusion matrix {cm}">']
    svg.append(f'<text x="{x0 + 1.5 * c}" y="10" font-size="11" text-anchor="middle" fill="#52667E">예측 →</text>')
    for j, n in enumerate(CLS):
        svg.append(f'<text x="{x0 + j * c + c / 2}" y="{y0 - 6}" font-size="10" text-anchor="middle" fill="#222F44">{n}</text>')
    for i, n in enumerate(CLS):
        svg.append(f'<text x="{x0 - 6}" y="{y0 + i * c + c / 2 + 4}" font-size="10" text-anchor="end" fill="#222F44">{n}</text>')
        for j in range(3):
            v = cm[i][j]
            diag = i == j
            fill = "#142849" if diag and v else ("#C98A5E" if v else "#F0F6FD")
            if diag and v:
                fill = "#4B74A6" if v < 30 else "#142849"
            svg.append(f'<rect x="{x0 + j * c + 1}" y="{y0 + i * c + 1}" width="{c - 2}" height="{c - 2}" rx="4" fill="{fill}"/>'
                       f'<text x="{x0 + j * c + c / 2}" y="{y0 + i * c + c / 2 + 5}" font-size="13" font-weight="700" text-anchor="middle" fill="{"#fff" if v else "#9DB3CF"}">{v}</text>')
    svg.append(f'<text x="2" y="{y0 + 3 * c + 4}" font-size="11" fill="#52667E">↑ 실제</text></svg>')
    right = (f'<div><div style="display:flex;gap:var(--space-3);align-items:flex-start">{"".join(svg)}'
             '<p class="cap" style="max-width:10rem">행 = 실제, 열 = 예측. 대각선이 정답입니다. triangle 30장 중 <b class="after">15장</b>을 circle로 착각했습니다.</p></div></div>')
    return (f'<div class="viz"><p class="viz-title">Accuracy는 속인다 · 전부 circle로 예측한 예제</p>{left}</div>'
            f'<div class="viz"><p class="viz-title">어디서 틀렸나 · confusion matrix <span class="note">(응용 데이터, class weight 적용 전)</span></p>{right}</div>')


def fig_F():
    g = F["gradcam"]
    figs = [f'<figure><img class="px" src="{g["orig"]}" alt="원본 {g["label"]} 이미지"><figcaption><b>원본</b>정답 {g["label"]}</figcaption></figure>']
    for c in g["cams"]:
        figs.append(f'<figure><img class="px" src="{c["png"]}" alt="target {c["target"]} Grad-CAM"><figcaption><b>target = {c["target"]}</b>'
                    f'점수 {c["score"]:+.2f} · 확률 {c["prob"]:.3f}</figcaption></figure>')
    scale = '<div class="scale-wrap"><div class="scale"><span>1</span><span class="bar"></span><span>0</span></div></div>'
    neg = g["cams"][1]["neg_share"]
    return (f'<div class="viz"><p class="viz-title">같은 이미지, target만 바꾼 Grad-CAM <span class="note">(응용 데이터)</span></p>'
            f'<div class="cams">{"".join(figs)}{scale}<div class="cap" style="max-width:15rem;align-self:center">'
            f'<p>두 열지도 모두 가장 밝은 곳이 1이 되도록 맞춘 값입니다. 그래서 확률 0.03인 circle도 밝게 보일 수 있습니다. <b>밝기 ≠ 점수</b>.</p>'
            f'<p style="margin-top:6px">circle 쪽은 점수를 <b>낮추는</b> 영역이 {neg * 100:.0f}%라서, <code>relu</code>로 지운 뒤 남은 일부만 보입니다.</p></div></div></div>')


FIGS = {"A": fig_A(), "B": fig_B(), "C": fig_C(), "D": fig_D(), "E": fig_E(), "F": fig_F()}

groups = []
for m in re.finditer(r"^### ([A-F])\. (.+?) — \"(.+?)\"\n(.*?)(?=\n### |\n---|\Z)", MD, re.S | re.M):
    L, title, q, body = m.groups()
    rows = []
    for line in body.strip().split("\n")[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        name, val, mean = cells[0], cells[1], cells[2]
        rows.append(f'<div class="prow"><p class="nm">{md_inline(name)}</p><p><span class="val">{md_inline(val)}</span><span class="mean">{md_inline(mean)}</span></p></div>')
    groups.append(f'    <div class="pgroup"><div class="gh"><span class="L">{L}</span><h3>{title}</h3><span class="q">{q}</span></div>'
                  f'{FIGS[L]}<div class="params">{"".join(rows)}</div></div>')
assert len(groups) == 6

# ── 파이프 그림 ──
pipe_img = "".join(f'<img class="px" src="{F["samples"][n][0]}" alt="{n}">' for n in CLS[:1])
feat = "".join(f'<i style="opacity:{0.25 + 0.75 * ((i * 7) % 11) / 10:.2f}"></i>' for i in range(16))

out = (T.replace("{{CODE}}", "\n".join(code_html))
        .replace("{{KNOBS}}", "\n".join(knob_html))
        .replace("{{DEMAND}}", "\n".join(demand_html))
        .replace("{{PGROUPS}}", "\n".join(groups))
        .replace("{{PIPE_IMG}}", pipe_img)
        .replace("{{FEAT_BAR}}", feat))
assert "{{" not in out, re.findall(r"\{\{\w+\}\}", out)
(HERE / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out) // 1024, "KB")
