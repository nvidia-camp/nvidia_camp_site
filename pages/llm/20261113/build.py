"""Day20 LLM·Transformer 하루 통합 뷰: template.html + 실행 기록(capture/capture.json) → index.html

- 화면의 숫자는 강의 슬라이드 코드(p.29·34·43·45·54·62·74)를 실행한 capture.json 에서 읽는다.
- 아래 expect()로 강의 슬라이드의 값(p.8·p.63 Weight, p.74 등)과 대조한다.
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


P29, P34, P43, P45, P54, P62, P74 = (CAP[k] for k in ("p29", "p34", "p43", "p45", "p54", "p62", "p74"))
W = P62["weights"]
expect([round(x, 2) for x in W[0]] == [1.0, 0.0, 0.0], "p.63 t1 row")
expect([round(x, 2) for x in W[1]] == [0.33, 0.67, 0.0], "p.63 t2 row")
expect([round(x, 2) for x in W[2]] == [0.25, 0.25, 0.5], "p.63 t3 row")
expect(all(abs(s - 1) < 1e-6 for s in P62["row_sums"]), "row sums")
expect([round(x, 2) for x in P62["out"][2]] == [0.75, 0.75], "p.8 value sum")
expect([round(x, 3) for x in P74["probs"]["1.0"]] == [0.665, 0.245, 0.09], "p.74 T=1")
expect(round(P43["ab"], 4) == 0.9701 and P43["ac"] == -1.0, "p.43 cosine")
expect(P45["shape"] == [3, 384], "p.45 shape")
expect(P54["x"] == P54["y"] == [2, 5, 8], "p.54 shape")
expect(P34["shape"][0] == 2 and P34["attention_mask"][0].count(0) == P34["tokens"][0].count("[PAD]"), "p.34 mask")

SPECIAL = {"[CLS]", "[SEP]", "[PAD]"}


def f(x, d=2):
    s = f"{x:.{d}f}"
    return "0" if float(s) == 0 and d <= 2 else s


def chips(tokens, ids):
    out = []
    for t, i in zip(tokens, ids):
        cls = "tk sp" if t in SPECIAL else "tk"
        out.append(f'<span class="{cls}"><b>{E(t)}</b><i>{i}</i></span>')
    return "".join(out)


def matrix(rows, cap, heat=False, masked=None, cols=("t1", "t2", "t3"), rlabels=("t1", "t2", "t3"), d=2, extra="", mask_text="−∞"):
    head = "".join(f"<th scope='col'>{c}</th>" for c in cols)
    body = []
    for r, row in enumerate(rows):
        cells = []
        for c, v in enumerate(row):
            if masked and masked[r][c]:
                cells.append(f'<td class="off">{mask_text}</td>')
            elif heat:
                cells.append(f'<td class="heat{" hi" if v >= 0.5 else ""}" style="--w:{v:.3f}">{f(v, d)}</td>')
            else:
                cells.append(f"<td>{f(v, d)}</td>")
        body.append(f"<tr><th scope='row'>{rlabels[r]}</th>{''.join(cells)}</tr>")
    return (f'<figure class="mx{extra}"><figcaption>{cap}</figcaption><table><thead><tr><th></th>{head}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></figure>')


def bars(values, labels, d=3, scale=None):
    scale = scale or max(values)
    rows = []
    for lab, v in zip(labels, values):
        rows.append(f'<div class="bar"><span>{lab}</span><i style="--p:{max(v, 0) / scale * 100:.1f}%"></i><b>{f(v, d)}</b></div>')
    return "".join(rows)


def pad_table():
    rows = []
    for n, (toks, ids, mask) in enumerate(zip(P34["tokens"], P34["input_ids"], P34["attention_mask"]), 1):
        tcells = "".join(f'<td class="{"padc" if t == "[PAD]" else ("spc" if t in SPECIAL else "")}">{E(t)}</td>' for t in toks)
        icells = "".join(f'<td class="{"padc" if t == "[PAD]" else ""}">{i}</td>' for t, i in zip(toks, ids))
        mcells = "".join(f'<td class="m{m}">{m}</td>' for m in mask)
        rows.append(f'<tr class="grp-top"><th scope="row">문장 {n} Token</th>{tcells}</tr>'
                    f'<tr><th scope="row">input_ids</th>{icells}</tr>'
                    f'<tr><th scope="row">attention_mask</th>{mcells}</tr>')
    return f'<div class="table-wrap"><table class="pad"><tbody>{"".join(rows)}</tbody></table></div>'


def padmask_grid():
    toks = P34["tokens"][0]
    mask = P34["attention_mask"][0]
    real = [t for t, m in zip(toks, mask) if m]
    head = "".join(f"<th scope='col'>{E(t)}</th>" for t in toks)
    body = ""
    for q in real:
        body += f"<tr><th scope='row'>{E(q)}</th>" + "".join('<td class="on"></td>' if m else '<td class="off">✕</td>' for m in mask) + "</tr>"
    return f'<div class="table-wrap"><table class="vis wide"><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def sim_table():
    labs = ["문장 1", "문장 2", "문장 3"]
    return matrix(P45["similarity"], "model.similarity 결과", heat=True, cols=labs, rlabels=labs, extra=" sim")


def temp_rows():
    out = []
    for t in ["0.5", "1.0", "2.0"]:
        out.append(f'<div class="trow"><span class="tlab">T = {t}</span><div class="tbars">{bars(P74["probs"][t], ["A", "B", "C"], scale=1)}</div></div>')
    return "".join(out)


s3 = W[2]
V = P62["q"]
VSUM = (f'<span class="term"><b>{f(s3[0])}</b> × [{f(V[0][0], 0)}, {f(V[0][1], 0)}]</span><i>+</i>'
        f'<span class="term"><b>{f(s3[1])}</b> × [{f(V[1][0], 0)}, {f(V[1][1], 0)}]</span><i>+</i>'
        f'<span class="term"><b>{f(s3[2])}</b> × [{f(V[2][0], 0)}, {f(V[2][1], 0)}]</span><i>=</i>'
        f'<span class="term sum">[{f(P62["out"][2][0])}, {f(P62["out"][2][1])}]</span>')

fill = {
    "P29_TEXT": E(P29["text"]),
    "P29_CHIPS": chips(P29["tokens"], P29["ids"]),
    "P29_CHARS": str(P29["chars"]),
    "P29_N": str(P29["n_tokens"]),
    "P29_VOCAB": f'{P29["vocab_size"]:,}',
    "FLOW_TOKENS": " ".join(E(t) for t in P29["tokens"][:6]) + " …",
    "FLOW_IDS": " ".join(str(i) for i in P29["ids"][:5]) + " …",
    "P34_SHAPE": f'({P34["shape"][0]}, {P34["shape"][1]})',
    "P34_TABLE": pad_table(),
    "PADMASK": padmask_grid(),
    "P43_AB": f'{P43["ab"]:.4f}',
    "P43_AC": f'{P43["ac"]:.0f}',
    "P45_SHAPE": f'({P45["shape"][0]}, {P45["shape"][1]})',
    "P45_SIM": sim_table(),
    "P45_TEXTS": "".join(f"<li>{E(t)}</li>" for t in P45["texts"]),
    "P45_12": f(P45["similarity"][0][1], 2),
    "P45_13": f(P45["similarity"][0][2], 2),
    "SCORES": matrix(P62["scores"], "① Score = QKᵀ / √2"),
    "MASKED": matrix(P62["scores"], "② Mask: 미래 위치 −∞", masked=P62["mask"]),
    "WEIGHTS": matrix(W, "③ Softmax → Weight", heat=True, masked=P62["mask"], mask_text="0"),
    "OUTV": matrix(P62["out"], "④ Weight × V", cols=("x", "y")),
    "NOMASK": matrix(P62["weights_nomask"], "Mask 없이 Softmax", heat=True),
    "WITHMASK": matrix(W, "Weight · Causal Mask 적용", heat=True, masked=P62["mask"], mask_text="0"),
    "VSUM": VSUM,
    "LOGIT_BARS": bars(P74["logits"], ["A", "B", "C"], d=1, scale=2),
    "PROB_BARS": bars(P74["probs"]["1.0"], ["A", "B", "C"], scale=1),
    "P1": f(P74["probs"]["1.0"][0], 3),
    "T05": f(P74["probs"]["0.5"][0], 3),
    "T20": f(P74["probs"]["2.0"][0], 3),
    "TEMP_ROWS": temp_rows(),
    "ENV": f'PyTorch {CAP["env"]["torch"]} · Transformers {CAP["env"]["transformers"]} · sentence-transformers {CAP["env"]["sentence_transformers"]}',
}

tpl = (HERE / "template.html").read_text(encoding="utf-8")
missing = sorted(set(re.findall(r"\{\{(\w+)\}\}", tpl)) - fill.keys())
expect(not missing, f"채울 값 없음: {missing}")
out = re.sub(r"\{\{(\w+)\}\}", lambda m: fill[m.group(1)], tpl)
(HERE / "index.html").write_text(out, encoding="utf-8")
print(f"index.html {len(out):,} bytes")
