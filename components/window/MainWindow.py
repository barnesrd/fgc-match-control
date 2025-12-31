from PySide6.QtWidgets import QMainWindow, QTabWidget
from components.tabs import PlayerTab, CrewTab

from components.widgets import Menubar
from data.fallbacks import profile

class MainWindow(QMainWindow):
    def __init__(self, profile: dict, theme: dict, config: dict):
        super().__init__()
        self.show()

        self.setMenuBar(Menubar())

        gameProfile = profile.get(config.get('activeTheme'), profile['p4au'])

        tabber = QTabWidget()
        tabber.setTabPosition(QTabWidget.North)

        tabber.addTab(
            PlayerTab(gameProfile, theme),
            "Scoreboard"
        )
        tabber.addTab(
            CrewTab(gameProfile, theme),
            "Crew Battle"
        )
        
        self.setCentralWidget(tabber)