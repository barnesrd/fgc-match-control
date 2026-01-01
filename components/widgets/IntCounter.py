from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget, QGridLayout
from PySide6.QtGui import QIntValidator

class IntCounter(QWidget):
    def __init__(self, minimum: int = 0, maximum: int = 999, default: int = 0):
        super().__init__()
        self.default = default
        self.minimum = minimum
        self.maximum = maximum
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.counter = QLineEdit()
        self.counter.setValidator(QIntValidator(minimum, maximum))
        self.counter.setText(str(default))
        self.counter.setFixedWidth(30)
        layout.addWidget(self.counter, 0, 0)

        minus = QPushButton('-')
        minus.clicked.connect(self.decrement)
        minus.setFixedWidth(15)
        layout.addWidget(minus, 0, 1)

        plus = QPushButton('+')
        plus.clicked.connect(self.increment)
        plus.setFixedWidth(15)
        layout.addWidget(plus, 0, 2)

        self.setFixedWidth(60)
        self.setLayout(layout)

    def reset(self) -> None:
        self.counter.setText(str(self.default))

    def adjustCount(self):
        num = int(self.counter.text())
        if num < self.minimum:
            self.counter.setText(str(self.minimum))
            return
        if num > self.maximum:
            self.counter.setText(str(self.maximum))
            return

    def increment(self) -> None:
        if int(self.counter.text()) >= self.maximum:
            return
        self.counter.setText(str(int(self.counter.text())+1))

    def decrement(self) -> None:
        if int(self.counter.text()) <= self.minimum:
            return
        self.counter.setText(str(int(self.counter.text())-1))