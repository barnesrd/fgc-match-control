from PySide6.QtWidgets import QStatusBar, QLabel

from data.appdata import version

class StatusBar(QStatusBar):
    def __init__(self, theme: str, profile: str):
        super().__init__()

        settingLabel = QLabel(f'Theme: {theme} | Profile: {profile}')
        self.addPermanentWidget(settingLabel)

        self.showMessage(f'FG Overlay Beta v.{version} written by Jolteo_', 5000)
