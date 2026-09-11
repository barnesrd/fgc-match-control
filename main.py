import sys
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app: QApplication = QApplication([])
    
    sys.exit(app.exec())