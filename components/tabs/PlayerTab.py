from PySide6.QtWidgets import QWidget, QGridLayout
from components.widgets import LabelEdit

class PlayerTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(
            LabelEdit('Player 1:'),
            0, 0
        )
        
        self.setLayout(layout)