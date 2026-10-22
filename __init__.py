import re
from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo

def gen_find(note, field, regex):
    for id in mw.col.find_notes(f"note:{note}"):
        for m in regex.finditer(mw.col.get_note(id)[field]):
            yield m.group(0)

def main():
    KANJI = re.compile(r'[\u4e00-\u9faf\u3400-\u4dbf]')
    seen = set(gen_find("Vocabulary", "Front", KANJI))
    known = set(gen_find("Kanji", "Front", KANJI))
    missing = seen - known
    if missing:
        showInfo(f"Missing the following kanji\n\n{" ".join(seen - known)}")
    else:
        showInfo("No missing kanji found!")
    
action = QAction("Find missing kanji", mw)
action.triggered.connect(main)
mw.form.menuTools.addAction(action)
