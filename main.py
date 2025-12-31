import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from util.theming import set_theme
from components.window import MainWindow

if __name__ == '__main__':
    app: QApplication = QApplication([])

    set_theme(app)

    main = MainWindow(800, 600)

    sys.exit(app.exec())