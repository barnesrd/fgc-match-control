from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from data.globals import CONTROLLER
from lib.widget.component.form import OptionDropdown

class Preferences(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preferences")
        layout = QHBoxLayout()
        
        self.option1 = OptionDropdown('Option 1', {'a': 1, 'b': 2})
        layout.addWidget(self.option1)
        
        self.setLayout(layout)
        