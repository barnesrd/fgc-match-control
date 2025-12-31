from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

from components.widgets.Entry import Entry

class PlayerCell(QWidget):
    def __init__(self, label: str):
        super().__init__()
        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.addWidget(
            QLabel(label),
            0, 0
        )
        # Name Entry
        self.name = Entry('Name')
        layout.addWidget(self.name, 0, 1)

        # Character Entry
        self.character = Entry('Character')
        layout.addWidget(self.character, 0, 2)

        # Country Entry
        self.country = Entry('Country')
        layout.addWidget(self.country, 0, 3)


        self.setLayout(layout)
        self.show()