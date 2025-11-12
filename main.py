import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    font = app.font()
    font.setStyleHint(QFont.System)
    app.setFont(font)

    sys.exit(app.exec())