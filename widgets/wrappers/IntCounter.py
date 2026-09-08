from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout, QCheckBox
from PySide6.QtGui import QIntValidator

from .Entry import Entry
from .DebouncedEntry import DebouncedEntry
from classes import SubmitMode


class IntCounter(QWidget):
    def __init__(
        self,
        onSubmit: callable,
        minimum: int = 0,
        maximum: int = 999,
        default: int = 0,
        submitMode: SubmitMode = SubmitMode.ON_EDIT,
    ):
        super().__init__()
        self.default = default
        self.minimum = minimum
        self.maximum = maximum
        self.onSubmit = onSubmit
        self._submitMode = submitMode

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.counterEntry = DebouncedEntry(submitFunc)
        self.counterEntry.setValidator(QIntValidator(minimum, maximum))
        self.counterEntry.setText(str(default))
        self.counterEntry.setFixedWidth(30)
        layout.addWidget(self.counterEntry, 0, 0)

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

    @property
    def value(self) -> int:
        return int(self.counterEntry.text())

    @property
    def submitMode(self) -> SubmitMode:
        return self._submitMode
    
    @submitMode.setter
    def submitMode(self, value: SubmitMode) -> SubmitMode:
        self._submitMode = value

    def reset(self) -> None:
        self.counterEntry.setText(str(self.default))

    def adjustCount(self):
        num = int(self.counterEntry.text())
        if num < self.minimum:
            self.counterEntry.setText(str(self.minimum))
            return
        if num > self.maximum:
            self.counterEntry.setText(str(self.maximum))
            return

    def increment(self) -> None:
        if int(self.counterEntry.value) >= self.maximum:
            return
        self.counterEntry.setText(str(int(self.counterEntry.text()) + 1))
        self.trySubmit()

    def decrement(self) -> None:
        if int(self.counterEntry.text()) <= self.minimum:
            return
        self.counterEntry.setText(str(int(self.counterEntry.text()) - 1))
        self.trySubmit()
