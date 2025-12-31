from PySide6.QtWidgets import QWidget, QGridLayout

from components.widgets import PlayerCell

class CrewTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        layout.addWidget(PlayerCell("Team 1"))

        self.setLayout(layout)
        self.show()