from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QCheckBox

from widgets.components.Entry import Entry
from data.countries import countries
from widgets.components.IntCounter import IntCounter


class PlayerCell(QWidget):
    def __init__(
        self,
        label: str,
        players: dict,
        characters: dict,
        submitFunc: callable,
        editSubmitToggle: QCheckBox,
    ):
        super().__init__()
        self.players = players
        self.characters = characters
        self.submitFunc = submitFunc
        self.editSubmitToggle = editSubmitToggle

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.addWidget(QLabel(label), 0, 0)

        # Name Entry
        self.name = Entry('Name', self.players.keys(), 25)
        self.name.setOnFocusOut(self.autofillPlayer)
        self.name.setToolTip("Player's name")
        layout.addWidget(self.name, 0, 1)

        # Character Entry
        self.character = Entry('Character', self.characters.keys(), 2)
        self.character.setToolTip("Player's character")
        self.character.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.character, 0, 2)

        # Country Entry
        self.country = Entry('Country', countries.keys(), 2)
        self.country.setToolTip("Player's country")
        self.country.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.country, 0, 3)

        self.counter = IntCounter(0, 99, 0, submitFunc, editSubmitToggle)
        self.counter.setToolTip("Player's score (Affects scoreboard)")
        layout.addWidget(self.counter, 0, 4)

        self.setLayout(layout)
        self.show()

    def getName(self) -> str:
        return self.name.text()

    def getCharacterCode(self) -> str:
        return self.characters.get(self.character.text(), '')

    def getCountryCode(self) -> str:
        return countries.get(self.country.text(), '')

    def getScore(self) -> int:
        return int(self.counter.counter.text())

    def reload(self, players: dict, characters: dict):
        self.players = players
        self.characters = characters
        self.name.loadAutocomplete(self.players.keys())
        self.character.loadAutocomplete(self.characters.keys())

    def setTextContents(self, name: str, character: str, country: str) -> None:
        self.name.setText(name)
        self.character.setText(character)
        self.country.setText(country)

    def trySubmit(self):
        if self.editSubmitToggle.isChecked():
            self.submitFunc()

    def autofillPlayer(self):
        player = self.players.get(self.name.text())
        if player is not None:
            self.character.setText(player.get('char', ''))
            self.country.setText(player.get('ctry', ''))
        self.trySubmit()

    def clear(self):
        self.name.setText('')
        self.character.setText('')
        self.country.setText('')
        self.counter.reset()
