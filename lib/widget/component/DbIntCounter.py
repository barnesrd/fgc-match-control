from PySide6.QtWidgets import QPushButton, QWidget, QGridLayout, QCheckBox
from PySide6.QtGui import QIntValidator

from .DbEntry import DbEntry

class DbIntCounter(QWidget):
    def __init__(
        self, 
        on_submit: callable,
        minimum: int = 0,
        maximum: int = 999,
        default: int = 0
    ):
        super().__init__()
        self._minimum = minimum
        self._maximum = max(minimum, maximum)
        if default < minimum or default > maximum:
            self._default = minimum
        else:
            self._default = default
        self.on_submit = on_submit
        
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        
        self._entry = DbEntry(on_submit)
        self.counterEntry.setValidator(QIntValidator(minimum, maximum))
        self._entry.setText(str(self.default))
        self._entry.setFixedWidth(30)
        layout.addWidget(self._entry, 0, 0)
        
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
    def minimum(self):
        return self._minimum
    
    @minimum.setter
    def minimum(self, minimum: int):
        self._minimum = minimum
        
    @property
    def maximum(self):
        return self._maximum
    
    @maximum.setter
    def maximum(self, maximum: int):
        self._maximum = maximum
        
    def increment(self) -> None:
        if int(self._entry.value) >= self._maximum:
            return
        self.counterEntry.setText(str(int(self._entry.value) + 1))

    def decrement(self) -> None:
        if int(self._entry.value) <= self._minimum:
            return
        self.counterEntry.setText(str(int(self._entry.value) - 1))