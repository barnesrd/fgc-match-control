from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

from components.widgets.Entry import Entry

class CommCell(QWidget):
    def __init__(self, label: str):
        super().__init__()

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        layout.addWidget(QLabel(label), 0, 0)

        # Name
        self.name = Entry('Name')
        layout.addWidget(self.name, 0, 1)

        # Plug / Handle
        self.plug = Entry('Plug/Handle')
        layout.addWidget(self.plug, 0, 2)

        self.setLayout(layout)