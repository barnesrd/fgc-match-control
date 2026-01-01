from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from components.widgets import PlayerCell, CrewTeam

class CrewTab(QWidget):
    def __init__(self, profile: dict, theme: dict):
        super().__init__()
        layout = QHBoxLayout()
        layout.setSpacing(0)

        layout.addWidget(CrewTeam(profile, theme))

        buttonLayout = QVBoxLayout()

        plus = QPushButton('+')
        plus.setFixedWidth(15)
        plus.setToolTip('Add a player to both teams')
        buttonLayout.addWidget(plus)

        minus = QPushButton('-')
        minus.setFixedWidth(15)
        minus.setToolTip('Remove a player from both teams')
        buttonLayout.addWidget(minus)

        buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(buttonLayout)
        
        layout.addWidget(CrewTeam(profile, theme))

        self.setLayout(layout)
        self.show()