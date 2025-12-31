from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

from components.widgets.Entry import Entry

class CommCell(QWidget):
    def __init__(self, label: str, commentators: dict):
        super().__init__()
        self.commentators = commentators

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        layout.addWidget(QLabel(label), 0, 0)

        # Name
        self.name = Entry('Name', commentators.keys())
        self.name.setOnFocusOut(self.autofillComms)
        layout.addWidget(self.name, 0, 1)

        # Plug / Handle
        self.plug = Entry('Plug/Handle')
        layout.addWidget(self.plug, 0, 2)

        self.setLayout(layout)

    def clear(self) -> None:
        self.name.setText('')
        self.plug.setText('')

    def setTextContents(self, name: str, plug: str) -> None:
        self.name.setText(name)
        self.plug.setText(plug)

    def reload(self, commentators: dict) -> None:
        self.commentators = commentators
        self.name.loadAutocomplete(commentators.keys())

    def autofillComms(self):
        commentator = self.commentators.get(self.name.text())
        if commentator is None:
            return
        self.plug.setText(commentator.get('hndl', ''))