from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout, QCheckBox
from PySide6.QtGui import QIntValidator

from widgets.wrappers.Entry import Entry


class IntCounter(QWidget):
    def __init__(
        self,
        minimum: int = 0,
        maximum: int = 999,
        default: int = 0,
        submitFunc: callable = None,
        editSaveToggle: QCheckBox = None,
    ):
        super().__init__()
        self.default = default
        self.minimum = minimum
        self.maximum = maximum
        self.submitFunc = submitFunc if submitFunc is not None else lambda: None
        self.editSaveToggle = editSaveToggle

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.counter_entry = Entry()
        self.counter_entry.setValidator(QIntValidator(minimum, maximum))
        self.counter_entry.setText(str(default))
        self.counter_entry.setFixedWidth(30)
        self.counter_entry.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.counter_entry, 0, 0)

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
    def count(self) -> int:
        return int(self.counter_entry.text())

    def reset(self) -> None:
        self.counter_entry.setText(str(self.default))

    def adjustCount(self):
        num = int(self.counter_entry.text())
        if num < self.minimum:
            self.counter_entry.setText(str(self.minimum))
            return
        if num > self.maximum:
            self.counter_entry.setText(str(self.maximum))
            return

    def trySubmit(self) -> None:
        if self.editSaveToggle is None:
            return
        if self.editSaveToggle.isChecked():
            self.submitFunc()

    def increment(self) -> None:
        if int(self.counter_entry.text()) >= self.maximum:
            return
        self.counter_entry.setText(str(int(self.counter_entry.text()) + 1))
        self.trySubmit()

    def decrement(self) -> None:
        if int(self.counter_entry.text()) <= self.minimum:
            return
        self.counter_entry.setText(str(int(self.counter_entry.text()) - 1))
        self.trySubmit()
