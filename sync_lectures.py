# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""학습 자료 시트(업무 계정)의 '일자별 자료' 탭을 읽어 lectures.json을 만든다. 시트는 읽기만 한다.

사용: uv run sync_lectures.py   (site 폴더에서)

- 시트 ID와 탭 이름은 nvidia-lecture-sheet 스킬의 로컬 설정(config.json)에서 읽는다.
  공개 저장소에 시트 ID를 남기지 않기 위해서다.
- 읽는 열: Day, 일자, 교과목, PDF 링크(헤더 이름으로 찾음). 교시별 학습 내용은 저장하지 않는다.
- gws-work(업무 계정) 인증이 필요하다. 그래서 Vercel이 아니라 내 컴퓨터에서 실행하고 결과를 커밋한다.
"""
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "lectures.json"

data_dir = subprocess.run(["my-skills", "data-path", "nvidia-lecture-sheet"],
                          capture_output=True, text=True, check=True).stdout.strip()
config = json.loads((Path(data_dir) / "config.json").read_text(encoding="utf-8"))
sheet_id = config["spreadsheet_id"]
tab = config.get("daily_sheet_title", "일자별 자료")

params = json.dumps({"spreadsheetId": sheet_id, "range": f"{tab}!A1:Z300"})
result = subprocess.run(["gws-work", "sheets", "spreadsheets", "values", "get", "--params", params],
                        capture_output=True, text=True, check=True)
values = json.loads(result.stdout)["values"]

header = [h.strip() for h in values[0]]
col = {name: header.index(name) for name in ("Day", "일자", "교과목", "PDF 링크")}


def cell(row, name):
    i = col[name]
    return row[i].strip() if i < len(row) else ""


lectures = []
for row in values[1:]:
    day = cell(row, "Day")
    if not day:
        continue
    link = cell(row, "PDF 링크")
    lectures.append({
        "day": day,
        "date": cell(row, "일자")[:10],          # '2026-11-02 (월)' → '2026-11-02'
        "subject": cell(row, "교과목"),
        "link": link if link.startswith("http") else None,
    })

OUT.write_text(json.dumps(lectures, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
n_link = sum(1 for x in lectures if x["link"])
print(f"lectures.json: {len(lectures)}개 회차, 강의 자료 링크 {n_link}개 ({lectures[0]['date']} ~ {lectures[-1]['date']})")
