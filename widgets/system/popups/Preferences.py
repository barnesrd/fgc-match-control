from PySide6.QtWidgets import QDialog, QLabel, QHBoxLayout

class Preferences(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Preferences')
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.addWidget(QLabel('Hello World'))
        self.setLayout(layout)
