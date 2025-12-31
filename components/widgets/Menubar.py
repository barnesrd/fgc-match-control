from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QToolBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class Menubar(QMenuBar):
    def __init__(self):
        super().__init__()

        fileMenu = QMenu('File')
        fileMenu.addAction('Overlay Location')
        self.addMenu(fileMenu)

        profileMenu = QMenu('Profile')
        profileMenu.addAction('New Profile')
        profileMenu.addAction('Load Profile')
        profileMenu.addAction('Remove Profile')
        self.addMenu(profileMenu)

        themeMenu = QMenu('Theme')
        themeMenu.addAction('P4AU')
        self.addMenu(themeMenu)

        aboutMenu = QMenu('About')
        aboutMenu.addAction('Github Repository')
        aboutMenu.addAction('License')
        self.addMenu(aboutMenu)

        helpMenu = QMenu('Help')
        helpMenu.addAction('How to Use Overlays')
        self.addMenu(helpMenu)

        self.setNativeMenuBar(True)
       