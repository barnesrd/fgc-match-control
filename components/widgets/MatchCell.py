from PySide6.QtWidgets import QWidget, QGridLayout, QComboBox

from components.widgets.Entry import Entry

class MatchCell(QWidget):
    def __init__(self, validMatches: list[str]):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        self.title = Entry('Match Title')
        layout.addWidget(self.title, 0, 0)

        self.background = QComboBox()
        self.background.addItems(validMatches)
        layout.addWidget(self.background, 0, 1)

        self.setLayout(layout)

