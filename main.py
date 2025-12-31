import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from util.theming import setVisualTheme
from util.fileOps import getConfig, getProfile, getTheme
from components.window import MainWindow

if __name__ == '__main__':
    app: QApplication = QApplication([])

    setVisualTheme(app)

    config = getConfig()
    profile = getProfile()
    theme = getTheme()

    main = MainWindow(profile, theme, config)

    sys.exit(app.exec())