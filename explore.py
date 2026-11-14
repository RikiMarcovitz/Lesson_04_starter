import json
from pathlib import Path
import selection_core

events = json.loads(Path("data/events.json").read_text(encoding="utf-8"))
event = next(e for e in events if e["id"] == "evt_100")

try:
    result = selection_core.submit_selection(event, "cli_100", ["med_9"], ["add_to_album"])
    print("התקבל:", result)
except selection_core.SelectionError as exc:
    print("נדחה עם קוד:", exc.code)

print("בחירות באירוע:", event["selections"])