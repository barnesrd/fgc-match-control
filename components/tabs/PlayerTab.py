from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QCheckBox

from components.widgets import PlayerCell, CommCell, MatchCell, HorizLine

class PlayerTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        # Player Entry
        layout.addWidget(QLabel('<b><i>Player Data</i></b>'), 0, 0, 1, 2)

        p1 = PlayerCell('Player 1:')
        p2 = PlayerCell('Player 2:')

        layout.addWidget(p1, 1, 0, 1, 4)
        layout.addWidget(p2, 2, 0, 1, 4)

        # Separator
        layout.addWidget(HorizLine(), 3, 0, 1, 4)

        # Commentator Entry
        layout.addWidget(QLabel('<b><i>Commentator Data</i></b>'), 4, 0, 1, 2)

        c1 = CommCell('Comm 1:')
        c2 = CommCell('Comm 2:')

        layout.addWidget(c1, 5, 0, 1, 4)
        layout.addWidget(c2, 6, 0, 1, 4)

        # Separator
        layout.addWidget(HorizLine(), 7, 0, 1, 4)

        # Match Data Entry
        layout.addWidget(QLabel('<b><i>Match Data</i></b>'), 8, 0, 1, 2)

        m = MatchCell(['Grand Finals', 'Top 8'])
        layout.addWidget(m, 9, 0, 1, 4)

        # Buttons
        clearToggle = QCheckBox('Reset overlay on Clear')
        layout.addWidget(clearToggle, 10, 1)

        clear = QPushButton('Clear')
        layout.addWidget(clear, 10, 2)

        submit = QPushButton('Submit')
        layout.addWidget(submit, 10, 3)

        self.setLayout(layout)