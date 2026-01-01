from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

def setVisualTheme(app: Qt) -> None:
    font: QFont = app.font()
    font.setStyleHint(QFont.System)
    app.setFont(font)