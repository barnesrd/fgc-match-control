from PySide6.QtWidgets import QMenu


class About(QMenu):
    def __init__(self):
        super().__init__('About')
        self.addAction('Github Repository')
        self.addAction('License')
