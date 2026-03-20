from PySide6.QtWidgets import QMainWindow, QTabWidget
from widgets.tabs import PlayerTab, CrewTab

from widgets.system import Menubar, StatusBar
from data.fallbacks import profile

class MainWindow(QMainWindow):
    def __init__(self, profile: dict, game: dict, config: dict):
        super().__init__()
        self.show()

        self.setMenuBar(Menubar(config))

        gameProfile = profile.get(config.get('activeGame'), profile['p4au'])

        self.setStatusBar(StatusBar(config.get('activeGame'), config.get('activeProfile')))

        tabber = QTabWidget()
        tabber.setTabPosition(QTabWidget.North)

        tabber.addTab(
            PlayerTab(gameProfile, game, self.statusBar()),
            "Scoreboard"
        )
        tabber.addTab(
            CrewTab(gameProfile, game),
            "Crew Battle"
        )
        
        self.setCentralWidget(tabber)