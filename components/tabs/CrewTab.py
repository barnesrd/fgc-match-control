from PySide6.QtWidgets import QWidget, QGridLayout, QLabel

from components.widgets import PlayerCell

class CrewTab(QWidget):
    def __init__(self, profile: dict, theme: dict):
        super().__init__()
        layout = QGridLayout()

        layout.addWidget(QLabel('TODO'))

        self.setLayout(layout)
        self.show()