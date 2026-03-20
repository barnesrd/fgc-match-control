from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QCheckBox

from widgets.components.Entry import Entry
from widgets.components.ComboBox import ComboBox


class MatchCell(QWidget):
    def __init__(
        self,
        matchTitles: list[str],
        backgrounds: list[str],
        submitFunc: callable,
        editSaveToggle: QCheckBox,
    ):
        super().__init__()
        self.matchTitles = matchTitles
        self.backgrounds = backgrounds
        self.submitFunc = submitFunc
        self.editSaveToggle = editSaveToggle

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        self.title = Entry('Match Title', matchTitles, 20)
        self.title.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.title, 0, 0)

        layout.addWidget(QLabel('Background Image:'), 0, 1)

        self.backgroundSelect = ComboBox()
        self.backgroundSelect.addItems(backgrounds)
        self.backgroundSelect.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.backgroundSelect, 0, 2)

        self.setLayout(layout)

    def trySubmit(self) -> None:
        if self.editSaveToggle.isChecked():
            self.submitFunc()

    def reload(self, matchTitles: list[str], backgrounds: list[str]) -> None:
        self.matchTitles = matchTitles
        self.backgrounds = backgrounds
        self.title.loadAutocomplete(matchTitles)
        self.backgroundSelect.clear()
        self.backgroundSelect.addItems(backgrounds)

    def clear(self):
        self.title.setText('')
        self.backgroundSelect.setCurrentIndex(0)
