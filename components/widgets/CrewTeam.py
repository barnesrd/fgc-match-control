from PySide6.QtWidgets import QWidget, QFrame, QGridLayout, QVBoxLayout
from PySide6.QtCore import Qt

from components.widgets.Entry import Entry
from components.widgets.CrewPlayer import CrewPlayer
from components.widgets.HorizLine import HorizLine

class CrewTeam(QWidget):
    def __init__(self, profile: dict, theme: dict):
        super().__init__()
        
        layout = QVBoxLayout()

        self.teamName = Entry('Team Name')
        layout.addWidget(self.teamName)

        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.StyledPanel)
        frame.setFrameShadow(QFrame.Shadow.Plain)
        frame.setLineWidth(3)

        layout.addWidget(frame)

        playerLayout = QGridLayout(frame)
        playerLayout.setSpacing(0)
        playerLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.players = [
            CrewPlayer()
        ]

        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())
        playerLayout.addWidget(CrewPlayer())

        self.setLayout(layout)
        
    def addPlayer(self):
        pass

