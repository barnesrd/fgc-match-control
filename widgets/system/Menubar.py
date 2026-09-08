from PySide6.QtWidgets import QMenuBar, QMenu

from .toolbar import About, File, Game, Help, Profile


class Menubar(QMenuBar):
    def __init__(self, config: dict):
        super().__init__()
        self.config = config

        self.addMenu(File())

        self.addMenu(Profile())

        self.addMenu(Game())

        self.addMenu(About())

        self.addMenu(Help())

        self.setNativeMenuBar(True)
