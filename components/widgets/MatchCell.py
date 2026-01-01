from PySide6.QtWidgets import QWidget, QGridLayout, QComboBox, QLabel

from components.widgets.Entry import Entry

class MatchCell(QWidget):
    def __init__(self, matchTitles: list[str], backgrounds: list[str]):
        super().__init__()
        self.matchTitles = matchTitles
        self.backgrounds = backgrounds

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        self.title = Entry('Match Title', matchTitles, 20)
        layout.addWidget(self.title, 0, 0)

        layout.addWidget(QLabel('Background Image:'), 0, 1)

        self.backgroundSelect = QComboBox()
        self.backgroundSelect.addItems(backgrounds)
        layout.addWidget(self.backgroundSelect, 0, 2)

        self.setLayout(layout)

    def reload(self, matchTitles: list[str], backgrounds: list[str]) -> None:
        self.matchTitles = matchTitles
        self.backgrounds = backgrounds
        self.title.loadAutocomplete(matchTitles)
        self.backgroundSelect.clear()
        self.backgroundSelect.addItems(backgrounds)

    def clear(self):
        self.title.setText('')
        self.backgroundSelect.setCurrentIndex(0)