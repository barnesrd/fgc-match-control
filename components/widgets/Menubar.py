from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QToolBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class Menubar(QMenuBar):
    def __init__(self, window: QMainWindow):
        super().__init__()

        self.setNativeMenuBar(True)
       