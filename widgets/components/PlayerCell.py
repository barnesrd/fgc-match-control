from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QCheckBox

from widgets.wrappers import Entry, IntCounter


class PlayerCell(QWidget):
    def __init__(
        self,
        label: str,
        submitFunc: callable,
        editSubmitToggle: QCheckBox,
    ):
        super().__init__()

        self.submitFunc = submitFunc
        self.editSubmitToggle = editSubmitToggle

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        # Initial Label
        layout.addWidget(QLabel(label), 0, 0)

        # Name Entry
        self.name_entry = Entry('Name', [], 25)
        # self.name_entry.setOnFocusOut(self.autofillPlayer)
        self.name_entry.setToolTip("Player's name")
        layout.addWidget(self.name_entry, 0, 1)

        # Character Entry
        self.character_entry = Entry('Character', [], 2)
        self.character_entry.setToolTip("Player's character")
        self.character_entry.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.character_entry, 0, 2)

        # Country Entry
        self.country_entry = Entry('Country', [], 2)
        self.country_entry.setToolTip("Player's country")
        self.country_entry.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.country_entry, 0, 3)

        self.score_counter = IntCounter(0, 99, 0, submitFunc, editSubmitToggle)
        self.score_counter.setToolTip("Player's score (Affects scoreboard)")
        layout.addWidget(self.score_counter, 0, 4)

        self.setLayout(layout)
        self.show()

    @property
    def name(self) -> str:
        return self.name_entry.text()

    @property
    def character(self) -> str:
        return self.character_entry.text()

    @property
    def country(self) -> str:
        return self.country_entry.text()

    @property
    def score(self) -> int:
        return self.score_counter.count

    def getScore(self) -> int:
        return int(self.score_counter.counter.text())

    def setTextContents(self, name: str, character: str, country: str) -> None:
        self.name_entry.setText(name)
        self.character_entry.setText(character)
        self.country_entry.setText(country)

    def trySubmit(self):
        if self.editSubmitToggle.isChecked():
            self.submitFunc()

    def clear(self):
        self.name_entry.setText('')
        self.character_entry.setText('')
        self.country_entry.setText('')
        self.score_counter.reset()


"""
    def autofillPlayer(self):
        player = self.players.get(self.name_entry.text())
        if player is not None:
            self.character_entry.setText(player.get('char', ''))
            self.country_entry.setText(player.get('ctry', ''))
        self.trySubmit()
"""
