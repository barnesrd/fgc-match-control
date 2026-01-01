from PySide6.QtWidgets import QWidget, QGridLayout, QLabel

from components.widgets import PlayerCell, IntCounter

class CrewTab(QWidget):
    def __init__(self, profile: dict, theme: dict):
        super().__init__()
        layout = QGridLayout()

        layout.addWidget(IntCounter(0, 2))

        self.setLayout(layout)
        self.show()