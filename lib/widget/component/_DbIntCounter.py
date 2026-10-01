from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QGridLayout,
    QCheckBox,
    QHBoxLayout,
)
from PySide6.QtGui import QIntValidator

from ._DbEntry import DbEntry


class DbIntCounter(QWidget):
    def __init__(
        self,
        on_submit: callable,
        minimum: int = 0,
        maximum: int = 999,
        default: int = 0,
    ):
        super().__init__()
        self._minimum = minimum
        self._maximum = max(minimum, maximum)
        if default < minimum or default > maximum:
            self._default = minimum
        else:
            self._default = default
        self.on_submit = on_submit

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        minus = QPushButton('-')
        minus.clicked.connect(self.decrement)
        minus.setFixedWidth(self.fontMetrics().averageCharWidth() + 14)
        layout.addWidget(minus)

        self._entry = DbEntry(on_submit)
        self._entry.setValidator(QIntValidator(minimum, maximum))
        self._entry.setText(str(self.default))
        layout.addWidget(self._entry)

        self._adjust_entry_width()

        plus = QPushButton('+')
        plus.clicked.connect(self.increment)
        plus.setFixedWidth(self.fontMetrics().averageCharWidth() + 14)
        layout.addWidget(plus)

        self.setFixedWidth(minus.width() + self._entry.width() + plus.width())
        self.setLayout(layout)

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, minimum: int):
        self._minimum = minimum
        self._adjust_entry_width()

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: int):
        self._maximum = maximum
        self._adjust_entry_width()

    def _adjust_entry_width(self):
        max_len = max(len(str(self.minimum)), len(str(self.maximum)))
        self._entry.setFixedWidth(
            max_len * self.fontMetrics().averageCharWidth() + 14
        )

    def increment(self) -> None:
        if int(self._entry.value) >= self._maximum:
            return
        self._entry.setText(str(int(self._entry.value) + 1))

    def decrement(self) -> None:
        if int(self._entry.value) <= self._minimum:
            return
        self._entry.setText(str(int(self._entry.value) - 1))

    @property
    def default(self):
        return self._default

    @property
    def value(self) -> int:
        return int(self._entry.value)

    def reset(self):
        self._entry.setText(str(self._default))
