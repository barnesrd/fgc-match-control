from PySide6.QtWidgets import QWidget, QTextEdit, QLabel, QGridLayout

class LabelEdit(QWidget):
    def __init__(self, text: str):
        super().__init__()
        layout = QGridLayout()
        layout.addWidget(
            QLabel(text),
            0, 0
        )
        layout.addWidget(
            QTextEdit(),
            0, 1
        )
        self.setLayout(layout)
        self.show()