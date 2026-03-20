from PySide6.QtWidgets import QMenuBar, QMenu


class Menubar(QMenuBar):
    def __init__(self, config: dict):
        super().__init__()
        self.config = config

        self.fileMenu = QMenu('File')
        self.fileMenu.addAction('Overlay Location')
        self.fileMenu.addAction('Preferences')
        self.fileMenu.addAction('Settings')
        self.addMenu(self.fileMenu)

        self.profileMenu = QMenu('Profile')
        self.profileMenu.addAction('New Profile')
        self.profileMenu.addAction('Load Profile')
        self.profileMenu.addAction('Remove Profile')
        self.addMenu(self.profileMenu)

        self.gameMenu = QMenu('Game')
        self.gameMenu.addAction('P4AU')
        self.addMenu(self.gameMenu)

        self.aboutMenu = QMenu('About')
        self.aboutMenu.addAction('Github Repository')
        self.aboutMenu.addAction('License')
        self.addMenu(self.aboutMenu)

        self.helpMenu = QMenu('Help')
        self.helpMenu.addAction('How to Use Overlays')
        self.helpMenu.addAction('How to Save Info')
        self.helpMenu.addAction('Making Themes')
        self.addMenu(self.helpMenu)

        self.setNativeMenuBar(True)
