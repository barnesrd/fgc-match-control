from PySide6.QtWidgets import QMenu


class Help(QMenu):
    def __init__(self):
        super().__init__('Help')
        self.addAction('How to Use Overlays')
        self.addAction('How to Save Info')
        self.addAction('Making Themes')