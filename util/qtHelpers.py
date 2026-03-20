from PySide6.QtWidgets import QLineEdit


def getEntryWidth(characters: int, entry: QLineEdit) -> int:
    fm = entry.fontMetrics()
    return characters * fm.averageCharWidth()
