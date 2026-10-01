from PySide6.QtWidgets import QMenu


class Game(QMenu):
    def __init__(self):
        super().__init__('Game')
        self.addAction('P4AU')
