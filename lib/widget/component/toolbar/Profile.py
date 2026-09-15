from PySide6.QtWidgets import QMenu


class Profile(QMenu):
    def __init__(self):
        super().__init__('Profile')
        self.addAction('New Profile')
        self.addAction('Load Profile')
        self.addAction('Remove Profile')