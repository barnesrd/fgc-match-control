from PySide6.QtWidgets import QMainWindow, QTabWidget
from components.tabs import PlayerTab, CrewTab

class MainWindow(QMainWindow):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.show()

        tabber = QTabWidget()
        tabber.setTabPosition(QTabWidget.North)

        tabber.addTab(PlayerTab(), "Scoreboard")
        tabber.addTab(CrewTab(), "Crew Battle")
        
        self.setCentralWidget(tabber)

    def pressIntercept(self, key):
        print(key)