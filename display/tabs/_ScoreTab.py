from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QCheckBox,
    QHBoxLayout,
)
from time import time
from threading import Timer
import logging

from lib.widget.cell import ScorePlayer, ScoreComm, ScoreMatch
from lib.widget.component import HorizLine
from data.globals import CONTROLLER
from lib.classes.enum import SubmitMode


class ScoreTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.verticalSizeConstraint()

        # Player Entry
        layout.addWidget(QLabel('<b><i>Player Data</i></b>'), 0, 0, 1, 2)

        player_buttons = QHBoxLayout()

        player_clear = QPushButton('Clear')
        player_clear.clicked.connect(self.clear_players)
        player_buttons.addWidget(player_clear)

        player_swap = QPushButton('Swap')
        player_swap.clicked.connect(self.swap_players)
        player_buttons.addWidget(player_swap)

        score_reset = QPushButton('Reset Score')
        score_reset.clicked.connect(self.reset_score)
        player_buttons.addWidget(score_reset)

        layout.addLayout(player_buttons, 0, 2, 1, 2)

        self.p1 = ScorePlayer(
            'Player 1:',
            lambda data: self.update_bulk(
                {
                    'p1name': data['name'],
                    'p1char': data['character'],
                    'p1ctry': data['country'],
                    'p1scor': data['score'],
                }
            ),
        )

        self.p2 = ScorePlayer(
            'Player 2:',
            lambda data: self.update_bulk(
                {
                    'p2name': data['name'],
                    'p2char': data['character'],
                    'p2ctry': data['country'],
                    'p2scor': data['score'],
                }
            ),
        )

        layout.addWidget(self.p1, 1, 0, 1, 4)
        layout.addWidget(self.p2, 2, 0, 1, 4)

        # Separator
        layout.addWidget(HorizLine(), 3, 0, 1, 4)

        # Commentator Entry
        layout.addWidget(QLabel('<b><i>Commentator Data</i></b>'), 4, 0, 1, 2)

        comm_clear = QPushButton('Clear')
        comm_clear.clicked.connect(self.clear_commentators)
        layout.addWidget(comm_clear, 4, 2)

        comm_swap = QPushButton('Swap')
        comm_swap.clicked.connect(self.swap_commentators)
        layout.addWidget(comm_swap, 4, 3)

        self.c1 = ScoreComm(
            'Comm 1:',
            lambda data: self.update_bulk(
                {
                    'c1name': data['name'],
                    'c1plug': data['plug'],
                    'c1nav': data['nav'],
                }
            ),
        )

        self.c2 = ScoreComm(
            'Comm 2:',
            lambda data: self.update_bulk(
                {
                    'c2name': data['name'],
                    'c2plug': data['plug'],
                    'c2nav': data['nav'],
                }
            ),
        )

        layout.addWidget(self.c1, 5, 0, 1, 4)
        layout.addWidget(self.c2, 6, 0, 1, 4)

        # Separator
        layout.addWidget(HorizLine(), 7, 0, 1, 4)

        # Match Data Entry
        layout.addWidget(QLabel('<b><i>Match Data</i></b>'), 8, 0, 1, 2)

        self.match = ScoreMatch(
            lambda data: self.update_bulk(
                {'title': data['title'], 'background': data['background']}
            )
        )
        layout.addWidget(self.match, 9, 2, 1, 2)

        matchClear = QPushButton('Clear')
        matchClear.clicked.connect(self.match.clear)
        layout.addWidget(matchClear, 8, 3, 1, 1)

        # Separator
        layout.addWidget(HorizLine(), 10, 0, 1, 4)

        # Final Buttons

        clear = QPushButton('Clear')
        clear.clicked.connect(self.clear)
        layout.addWidget(clear, 11, 2, 1, 1)

        submit = QPushButton('Submit')
        submit.clicked.connect(self.submit)
        layout.addWidget(submit, 11, 3, 1, 1)

        self.setLayout(layout)

        self._timer: Timer | None = None

        p1_data = self.p1.data
        p2_data = self.p2.data
        c1_data = self.c1.data
        c2_data = self.c2.data
        m_data = self.match.data

        self._data = {
            'p1name': p1_data['name'],
            'p1char': p1_data['character'],
            'p1ctry': p1_data['country'],
            'p1scor': p1_data['score'],
            'p2name': p2_data['name'],
            'p2char': p2_data['character'],
            'p2ctry': p2_data['country'],
            'p2scor': p2_data['score'],
            'c1name': c1_data['name'],
            'c1plug': c1_data['plug'],
            'c1nav': c1_data['nav'],
            'c2name': c2_data['name'],
            'c2plug': c2_data['plug'],
            'c2nav': c2_data['nav'],
            'title': m_data['title'],
            'background': m_data['background'],
        }

    def start_timeout(self):
        if CONTROLLER.profile.submit_mode != SubmitMode.ON_EDIT:
            return
        if self._timer is not None:
            self._timer.cancel()
        self._timer = Timer(CONTROLLER.profile.debounce / 2, self.submit)
        self._timer.start()

    def update_bulk(self, data: dict):
        self._data = self._data | data
        self.start_timeout()

    def submit(self):
        logging.debug(f'Data submitted from Score tab: {self._data}')

    def clear_commentators(self):
        self.c1.clear()
        self.c2.clear()

    def swap_commentators(self):
        temp = self.c1.data
        self.c1.data = self.c2.data
        self.c2.data = temp

    def clear_players(self):
        self.p1.clear()
        self.p2.clear()

    def swap_players(self):
        temp = self.p1.data
        self.p1.data = self.p2.data
        self.p2.data = temp

    def reset_score(self):
        self.p1.reset_score()
        self.p2.reset_score()

    def clear(self):
        self.clear_commentators()
        self.clear_players()
        self.match.clear()
