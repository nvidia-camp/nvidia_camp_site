"""구성안.md의 핵심 코드로 Day16 노트북을 만든다.

같은 셀로 두 파일을 쓴다.
- Day16_핵심코드.ipynb: 이 폴더에서 Jupyter(커널 "Python (dl)")로 연다
- 두 번째 인자 경로: Colab 업로드용 (kernelspec python3 + colab 메타데이터)

사용: python3 build_nb.py [colab용 출력 경로]
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
plan = (HERE / "구성안.md").read_text(encoding="utf-8")
block = plan.split("### 핵심 코드", 1)[1].split("```python", 1)[1].split("```", 1)[0]
parts = re.split(r"^# ── \[(.+?)\].*$", block, flags=re.M)
imports = parts[0].strip("\n")
names = {"준비": "prep", "1교시": "p1", "2교시": "p2", "3교시": "p3",
         "4교시": "p4", "5교시": "p5", "6교시": "p6", "7교시": "p7"}
src = {names[parts[i]]: parts[i + 1].strip("\n") for i in range(1, len(parts), 2)}
assert list(src) == list(names.values()), list(src)
cells = []


def md(text):
    cells.append({"cell_type": "markdown", "metadata": {},
                  "source": text.strip("\n").splitlines(keepends=True)})


def code(text):
    cells.append({"cell_type": "code", "execution_count": None, "metadata": {},
                  "outputs": [], "source": text.strip("\n").splitlines(keepends=True)})


md("""
# Day16 · OCR·VLM 문서 AI 핵심 코드

2026-11-09 · Vision·멀티모달 AI 응용 4/4

문서 이미지에서 값을 꺼낼 때 **그 값의 근거(원문·위치·점수)를 함께 남기고, 근거가 없는 값은 사람이 보도록 남기는** 흐름을 1교시부터 7교시까지 한 번에 따라갑니다.

**실행 방법**
- Colab: 메뉴 `런타임 → 모두 실행`. 처음 한 번 Tesseract 설치에 1분쯤 걸립니다.
- 내 컴퓨터 Jupyter: Tesseract 엔진을 먼저 설치하고(macOS `brew install tesseract`), 커널을 `Python (dl)`로 고른 뒤 `모두 실행`. 0번 설치 셀은 Colab에서만 동작하고 여기서는 건너뜁니다.

**데이터는 따로 받지 않습니다.**
- `skimage.data.page()`: scikit-image에 들어 있는 실제 스캔 페이지. 왼쪽이 어두워 조명이 고르지 않습니다 → 1교시 이진화
- 코드로 그린 청구서: `cv2.putText`로 7줄을 그립니다. 그린 글자가 곧 정답이라 CER과 필드 정답을 바로 잴 수 있습니다

**모두 실제로 실행합니다.** OCR은 Tesseract, VLM은 작은 공개 모델 SmolVLM-256M(약 0.5GB, 4교시에서 처음 한 번 내려받음, 로그인 불필요)입니다. 6교시 TensorRT만 장비가 필요해 공식 명령을 주석으로 둡니다. Colab은 `런타임 → 런타임 유형 변경 → GPU`면 VLM이 더 빠르지만 CPU로도 됩니다.
""")

md("## 0. 설치 (Colab에서만)\nTesseract OCR 엔진과 Python 연결 라이브러리를 설치합니다. OpenCV·scikit-image·pandas·transformers는 Colab에 이미 있습니다. 내 컴퓨터에서는 아무것도 하지 않습니다.")
code("""
import sys

if "google.colab" in sys.modules:
    !apt-get -qq install -y tesseract-ocr > /dev/null
    !pip -q install pytesseract jiwer
""")

md("## import")
code(imports)

md("## 이미지 보기 준비\nColab에는 `cv2_imshow`가 있습니다. 내 컴퓨터 Jupyter에는 없어서 같은 이름의 함수를 만듭니다. 이 셀은 화면에 보여 주는 용도라 핵심 코드에는 없습니다.")
code("""
try:
    from google.colab.patches import cv2_imshow   # Colab
except ImportError:
    from IPython.display import Image, display

    def cv2_imshow(img):                          # 내 컴퓨터 Jupyter
        ok, png = cv2.imencode(ext=".png", img=img)
        display(Image(data=png.tobytes()))
""")

md("""
## 준비 · 데이터
내장 스캔 페이지를 불러오고, 청구서를 그린 뒤 **일부러 비스듬히 찍은 사진**처럼 바꿉니다. 1교시에서 이 사진을 다시 정면으로 되돌립니다.
""")
code(src["prep"] + """

cv2_imshow(page)      # 왼쪽이 어두운 스캔 페이지
cv2_imshow(photo)     # 비스듬한 청구서 사진
""")

md("""
## 1교시 · 전처리
- **이진화:** 글자(검정)와 배경(흰색)을 나눕니다. Adaptive Threshold는 주변 31×31 블록마다 기준을 따로 잡아서, 조명이 고르지 않은 페이지에서도 글자를 살립니다.
- **원근 보정:** 사진 속 문서의 네 모서리(`corners`)를 정면 네 모서리(`front`)로 옮깁니다. 두 목록의 **순서가 같아야** 합니다.
""")
code(src["p1"] + """

cv2_imshow(binary)
cv2_imshow(warped)
""")

md("""
## 2교시 · OCR
`image_to_data`는 단어마다 **Text·Box(left, top, width, height)·Confidence**를 줍니다. confidence는 정답 확률이 아니라 **검토 순서**입니다. 낮은 점수는 지우지 않고 검토 목록으로 남깁니다.

CER = (치환 + 삭제 + 삽입) ÷ 정답 글자 수
""")
code(src["p2"] + """

print(text)
print("CER:", round(score, 4))
print("검토 목록(conf < 50):", len(review), "개")
words[["text", "conf", "left", "top", "width", "height"]]
""")

md("""
## 3교시 · 구조화
라벨(`TOTAL:`) 줄에서 값을 찾고, **원문(raw)·정규화값(value)·점수·위치**를 함께 남깁니다. 품목 금액의 합이 합계와 다르면 검토 이유를 기록합니다.
""")
code(src["p3"] + """

print(total)
print("검토 이유:", reasons)
""")

md("""
## 4교시 · VLM 질문
이미지와 질문을 **하나의 메시지**에 넣어 VLM에 묻습니다. 호출 코드는 강의 PDF p.54, Hugging Face 공식 문서와 같습니다. `do_sample=False`면 같은 입력에 같은 답이 나옵니다. (수업 실습의 기본 경로는 강사가 써 둔 제공 응답입니다.)
""")
code(src["p4"] + """

print(answer)
""")

md("""
## 5교시 · 결합과 평가
VLM의 답이 OCR이 읽은 원문과 같을 때만 채택합니다. 다르면 `None`(보류)으로 두고 사람이 확인합니다. **보류는 정답으로 세지 않습니다.**
""")
code(src["p5"] + """

print("VLM 답:", answer, "| OCR 원문:", total["raw"], "| 최종 값:", final)
""")

md("## 6교시 · 배포 설계\n장비 없이 순서와 조건만 기록합니다. Engine Build는 실제로 돌릴 장치(Jetson·GPU)에서 합니다.")
code(src["p6"])

md("## 7교시 · 통합 기록\n한 문서의 처리 결과를 하나의 JSON으로 남깁니다. 8교시에는 이 노트북을 다시 실행해 같은 결과가 나오는지 대조합니다.")
code(src["p7"] + """

print(open("doc03.json", encoding="utf-8").read())
""")

md("""
---
## 직접 바꿔 보기
한 번에 **한 곳만** 바꾸고 CER이나 필드가 어떻게 달라지는지 봅니다.

### ① 이진화: Otsu vs Adaptive
Otsu는 페이지 전체에 기준 하나를 씁니다. 스캔 페이지의 정답 글자는 손으로 옮겨 적었습니다.
""")
code('''
page_lines = [
    "Region-based segmentation",
    "Let us first determine markers of the coins and the",
    "background. These markers are pixels that we can label",
    "unambiguously as either object or background. Here,",
    "the markers are found at the two extreme parts of the",
    "histogram of grey values:",
    ">>> markers = np.zeros_like(coins)",
]                                            # 스캔 페이지의 글자 = 정답
PAGE_TEXT = "\\n".join(page_lines)

def page_cer(image):
    page_read = pytesseract.image_to_string(image=image, config="--psm 6")
    page_truth = " ".join(PAGE_TEXT.split())     # 줄바꿈·공백을 한 칸으로
    page_score = jiwer.cer(reference=page_truth, hypothesis=" ".join(page_read.split()))
    return round(page_score, 3)

t, otsu = cv2.threshold(
    src=page,
    thresh=0,                        # Otsu가 기준을 직접 고르므로 0
    maxval=255,
    type=cv2.THRESH_BINARY + cv2.THRESH_OTSU,
)
print("Gray 그대로     :", page_cer(page))
print("Otsu (기준", t, "):", page_cer(otsu))
print("Adaptive 31, 11 :", page_cer(binary))
cv2_imshow(otsu)
''')

md("### ② Adaptive의 blockSize와 C\n값을 바꿔 가며 CER을 봅니다. blockSize는 3 이상 **홀수**여야 합니다(짝수를 넣으면 오류).")
code('''
for block_size, C in [(31, 11), (3, 11), (101, 11), (31, 0), (31, 30), (31, 60)]:
    b = cv2.adaptiveThreshold(
        src=page,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY,
        blockSize=block_size,
        C=C,
    )
    print("blockSize", block_size, "C", C, "→ CER", page_cer(b))
''')

md("### ③ 모서리 순서를 바꾸면\n같은 네 점인데 **시작점을 오른쪽 위로** 잡았습니다. 문서가 90도 돌아가 찌그러집니다. 잘못 끼어든 글자 때문에 CER이 1을 넘을 수 있습니다.")
code('''
wrong = np.float32([[690, 10], [720, 470], [20, 450], [60, 40]])   # 시작점이 오른쪽 위
M_wrong = cv2.getPerspectiveTransform(src=wrong, dst=front)
bad = cv2.warpPerspective(src=photo, M=M_wrong, dsize=(700, 480))
bad_text = pytesseract.image_to_string(image=bad, config="--psm 6")
bad_score = jiwer.cer(reference=truth, hypothesis=" ".join(bad_text.split()))
print("CER:", round(bad_score, 3))
cv2_imshow(bad)
''')

md("### ④ PSM: 페이지 구조 가정\nPSM 6은 글 블록, 7은 **한 줄**, 8은 **한 단어**로 가정합니다. 전체 페이지를 한 줄로 가정하면 어떻게 될까요?")
code('''
for psm in [6, 7, 8]:
    psm_text = pytesseract.image_to_string(image=warped, config=f"--psm {psm}")
    print("PSM", psm, "→", repr(psm_text.strip()[:60]))
''')

md("### ⑤ confidence 분포\n점수가 낮은 단어부터 봅니다. 틀린 단어(`DOCO3`, 숫자 0을 글자 O로 읽음)는 몇 점일까요? 기준 50이면 걸릴까요?")
code('''
words.sort_values("conf")[["text", "conf"]].head(5)
''')

md("""
---
## VLM에 다른 질문 던져 보기
4교시에서 불러온 모델(`pipe`)에 질문만 바꿔 묻습니다. 작은 모델이라 답이 엉성할 수 있습니다. **그래서 근거 대조가 필요하다**는 것을 직접 확인하는 칸입니다.
""")
code('''
def ask(question, max_new_tokens=128):
    messages = [
        {"role": "user", "content": [
            {"type": "image", "path": "invoice.png"},
            {"type": "text", "text": question},
        ]},
    ]
    out = pipe(
        text=messages,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        return_full_text=False,
    )
    return out[0]["generated_text"].strip()

print("공급자 →", ask("What is the supplier name?"))
print("날짜   →", ask("What is the issue date?"))
''')

md("""
### 문서에 없는 값을 물으면?
청구서에는 세금·할인·전화번호가 없습니다. "모르면 null이라고 답해"를 붙이면 지켜질까요?
""")
code('''
print("세금        →", ask("What is the tax amount?"))
print("할인액      →", ask("What is the discount amount?"))
print("전화번호    →", ask("What is the supplier phone number?"))
print("세금(null)  →", ask("What is the tax amount? If it is not written, answer null."))
''')

md("""
### 답이 잘리면? 형식을 지킬까?
`max_new_tokens`를 3으로 줄여 보고, JSON으로 답하라고 해 봅니다. `json.loads`가 성공하는 것과 요청한 key(answer·evidence)가 온 것은 다릅니다.
""")
code('''
print("토큰 3개 →", ask("What is the total amount?", max_new_tokens=3))

reply = ask("Return JSON with keys answer and evidence. What is the total?")
print("JSON 요청 →", reply)
try:
    parsed = json.loads(s=reply)          # "33000"만 오면 숫자로 읽혀서 성공한다
except json.JSONDecodeError:
    parsed = None
print("answer·evidence key가 있나:", isinstance(parsed, dict) and "evidence" in parsed)
''')

local_cells = [dict(cell, id=f"cell-{n:02d}") for n, cell in enumerate(cells)]
local = {"nbformat": 4, "nbformat_minor": 5, "cells": local_cells, "metadata": {
    "kernelspec": {"name": "dl", "display_name": "Python (dl)", "language": "python"},
    "language_info": {"name": "python"}}}
out = HERE / "Day16_핵심코드.ipynb"
out.write_text(json.dumps(local, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("cells", len(cells), "->", out.name)

if len(sys.argv) > 1:      # Colab용: Drive 원본의 메타데이터를 유지한다
    colab = {"nbformat": 4, "nbformat_minor": 0, "cells": cells, "metadata": {
        "colab": {"provenance": [], "authorship_tag": "ABX9TyOUYaKCbRrejgN/pB+XVL5A"},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}}}
    Path(sys.argv[1]).write_text(json.dumps(colab, ensure_ascii=False, indent=1),
                                 encoding="utf-8")
    print("colab ->", sys.argv[1])
