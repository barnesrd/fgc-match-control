from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

from components.widgets.Entry import Entry
from data.countries import countries

class PlayerCell(QWidget):
    def __init__(self, label: str, players: dict, characters: dict):
        super().__init__()
        self.players = players
        self.characters = characters

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.addWidget(
            QLabel(label),
            0, 0
        )

        # Name Entry
        self.name = Entry('Name', self.players.keys())
        self.name.setOnFocusOut(self.autofillPlayer)
        layout.addWidget(self.name, 0, 1)

        # Character Entry
        self.character = Entry('Character', self.characters.keys(), 2)
        layout.addWidget(self.character, 0, 2)

        # Country Entry
        self.country = Entry('Country', countries.keys(), 2)
        layout.addWidget(self.country, 0, 3)

        self.setLayout(layout)
        self.show()

    def reload(self, players: dict, characters: dict):
        self.players = players
        self.characters = characters
        self.name.loadAutocomplete(self.players.keys())
        self.character.loadAutocomplete(self.characters.keys())

    def setTextContents(self, name: str, character: str, country: str) -> None:
        self.name.setText(name)
        self.character.setText(character)
        self.country.setText(country)

    def autofillPlayer(self):
        player = self.players.get(self.name.text())
        if player is None:
            return
        self.character.setText(player.get('char', ''))
        self.country.setText(player.get('ctry', ''))

    def clear(self):
        self.name.setText('')
        self.character.setText('')
        self.country.setText('')