from PySide6.QtWidgets import QWidget, QHBoxLayout

from widgets.components.Entry import Entry
from widgets.components.IntCounter import IntCounter
from widgets.components.ComboBox import ComboBox

class CrewPlayer(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setSpacing(1)
        layout.setContentsMargins(0,0,0,0)

        self.name = Entry("Name")
        layout.addWidget(self.name)

        self.character = Entry("Character")
        layout.addWidget(self.character)

        self.lives = IntCounter(0, 2, 2)
        self.lives.setToolTip('Number of lives for this player')
        self.lives.counter.setFixedWidth(15)
        self.lives.setFixedWidth(45)
        layout.addWidget(self.lives)

        self.setLayout(layout)
        