from PySide6.QtWidgets import QMainWindow, QTabWidget

from lib.widget.component import MenuBar, StatusBar
from .tabs import ScoreTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMenuBar(MenuBar())

        self.setStatusBar(StatusBar())

        tabber = QTabWidget()
        tabber.setTabPosition(QTabWidget.North)

        tabber.addTab(ScoreTab(), 'General')

        self.setCentralWidget(tabber)

        self.show()