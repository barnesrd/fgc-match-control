from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox
from PySide6.QtCore import Qt

class OptionDropdown(QWidget):
    def __init__(self, label: str, options: dict):
        super().__init__()
        layout = QHBoxLayout()
        
        layout.addWidget(QLabel(label), alignment=Qt.AlignmentFlag.AlignLeft)
        
        self._combo_box = QComboBox()
        option_list = options.keys()
        for key in option_list:
            self._combo_box.addItem(key, options[key])
        layout.addWidget(self._combo_box, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.setLayout(layout)