from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QCheckBox, QToolTip

from components.widgets import PlayerCell, CommCell, MatchCell, HorizLine

class PlayerTab(QWidget):
    def __init__(self, profile: dict, theme: dict):
        super().__init__()

        layout = QGridLayout()

        # Player Entry
        layout.addWidget(QLabel('<b><i>Player Data</i></b>'), 0, 0, 1, 2)

        playerClear = QPushButton('Clear Players')
        playerClear.clicked.connect(self.clearPlayers)
        layout.addWidget(playerClear, 0, 2)

        playerSwap = QPushButton('Swap')
        playerSwap.clicked.connect(self.swapPlayers)
        layout.addWidget(playerSwap, 0, 3)

        self.p1 = PlayerCell('Player 1:', profile.get('players', {}), theme.get('characters', {}))
        self.p2 = PlayerCell('Player 2:', profile.get('players', {}), theme.get('characters', {}))

        layout.addWidget(self.p1, 1, 0, 1, 4)
        layout.addWidget(self.p2, 2, 0, 1, 4)

        # Separator
        layout.addWidget(HorizLine(), 3, 0, 1, 4)

        # Commentator Entry
        layout.addWidget(QLabel('<b><i>Commentator Data</i></b>'), 4, 0, 1, 2)

        commClear = QPushButton('Clear Commentators')
        commClear.clicked.connect(self.clearComms)
        layout.addWidget(commClear, 4, 2)

        commSwap = QPushButton('Swap')
        commSwap.clicked.connect(self.swapCommentators)
        layout.addWidget(commSwap, 4, 3)

        self.c1 = CommCell('Comm 1:', profile.get('commentators', {}))
        self.c2 = CommCell('Comm 2:', profile.get('commentators', {}))

        layout.addWidget(self.c1, 5, 0, 1, 4)
        layout.addWidget(self.c2, 6, 0, 1, 4)

        # Separator
        layout.addWidget(HorizLine(), 7, 0, 1, 4)

        # Match Data Entry
        layout.addWidget(QLabel('<b><i>Match Data</i></b>'), 8, 0, 1, 2)

        self.m = MatchCell(profile.get('matchTitles'), [])
        layout.addWidget(self.m, 9, 0, 1, 2)

        # Buttons
        self.editSaveToggle = QCheckBox('Save on edit')
        self.editSaveToggle.setToolTip('Edit occurs when exiting focus of the selected textbox.')
        layout.addWidget(self.editSaveToggle, 10, 0)

        self.clearToggle = QCheckBox('Reset overlay on Clear')
        self.clearToggle.setToolTip('Resets data to blank for overlays when pressing the "Clear" button')
        layout.addWidget(self.clearToggle, 10, 1)

        clear = QPushButton('Clear')
        clear.clicked.connect(self.clearAllData)
        layout.addWidget(clear, 10, 2)

        submit = QPushButton('Submit')
        layout.addWidget(submit, 10, 3)

        self.setLayout(layout)

    def swapPlayers(self):
        tempName = self.p1.name.text()
        tempCharacter = self.p1.character.text()
        tempCountry = self.p1.country.text()

        self.p1.setTextContents(
            self.p2.name.text(),
            self.p2.character.text(),
            self.p2.country.text()
        )
        self.p2.setTextContents(
            tempName,
            tempCharacter,
            tempCountry
        )

    def swapCommentators(self):
        tempName = self.c1.name.text()
        tempPlug = self.c1.plug.text()

        self.c1.setTextContents(
            self.c2.name.text(),
            self.c2.plug.text()
        )
        self.c2.setTextContents(
            tempName,
            tempPlug
        )

    def clearPlayers(self) -> None:
        self.p1.clear()
        self.p2.clear()

    def clearComms(self) -> None:
        self.c1.clear()
        self.c2.clear()
    
    def clearMatch(self) -> None:
        self.m.clear()

    def clearAllData(self) -> None:
        self.clearPlayers()
        self.clearComms()
        self.clearMatch()
        