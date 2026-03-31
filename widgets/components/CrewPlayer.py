from PySide6.QtWidgets import QWidget, QHBoxLayout

from widgets.wrappers import Entry, IntCounter


class CrewPlayer(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setSpacing(1)
        layout.setContentsMargins(0, 0, 0, 0)

        self.name_entry = Entry('Name')
        layout.addWidget(self.name_entry)

        self.character_entry = Entry('Character')
        layout.addWidget(self.character_entry)

        self.lives_entry = IntCounter(0, 2, 2)
        self.lives_entry.setToolTip('Number of lives for this player')
        self.lives_entry.counter_entry.setFixedWidth(15)
        self.lives_entry.setFixedWidth(45)
        layout.addWidget(self.lives_entry)

        self.setLayout(layout)

    @property
    def name(self) -> str:
        return self.name_entry.text()

    @property
    def character(self) -> str:
        return self.character_entry.text()

    @property
    def lives(self) -> int:
        return self.lives_entry.count
