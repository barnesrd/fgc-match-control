from PySide6.QtWidgets import QStatusBar, QLabel

from lib.classes import AppController


class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()

        self.message = QLabel('Message')
        self.addPermanentWidget(self.message)

        self.showMessage(
            f'FG Overlay Beta v.{AppController.version} written by Jolteo_', 5000
        )