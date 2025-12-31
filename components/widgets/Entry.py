from PySide6.QtWidgets import QLineEdit, QToolTip

from util.data_ops import getEntryWidth

class Entry(QLineEdit):
    def __init__(self, placeholder: str = "", maxLength: int = 20):
        super().__init__()

        self.setPlaceholderText(placeholder)
        self.setMaxLength(maxLength)
        self.setMinimumWidth(getEntryWidth(maxLength, self))
