from PySide6.QtWidgets import QMenu, QWidget
from display.popups import Preferences


class File(QMenu):
    def __init__(self):
        super().__init__('File')
        self.addAction('Overlay Location')
        self.addAction('Preferences', self.preferencesAction)
        self.addAction('Settings')

    def preferencesAction(self) -> None:
        self.p = Preferences()
        self.p.show()
