from PySide6.QtWidgets import QWidget, QGridLayout

from components.widgets import LabelEdit

class CrewTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        layout.addWidget(LabelEdit("Team 1"))

        self.setLayout(layout)
        self.show()