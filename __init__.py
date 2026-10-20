from aqt import mw
from aqt.qt import QAction
from aqt.utils import showInfo

def main():
    showInfo("Hello, Anki!")
    

action = QAction("Find missing kanji", mw)
action.triggered.connect(main)
mw.form.menuTools.addAction(action)
