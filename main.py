import sys
from PySide6.QtWidgets import QApplication

from display import MainWindow
from lib.classes import AppController

if __name__ == '__main__':
    app: QApplication = QApplication([])
    
    main = MainWindow()
    AppController()._window = main

    sys.exit(app.exec())