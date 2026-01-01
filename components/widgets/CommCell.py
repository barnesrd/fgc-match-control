from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QComboBox

from components.widgets.Entry import Entry

class CommCell(QWidget):
    def __init__(self, label: str, commentators: dict, navigators: list[str]):
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

        self.nav = QComboBox()
        self.nav.setToolTip('Sets the navigator graphic to be used on the commentator overlay')
        self.configureNav(navigators)
        layout.addWidget(self.nav, 0, 3)

        self.setLayout(layout)

    def clear(self) -> None:
        self.name.setText('')
        self.plug.setText('')

    def configureNav(self, navigators: list[str]):
        if len(navigators) == 0:
            self.nav.hide()
            return
        self.nav.addItems(sorted(navigators))
        self.nav.show()

    def setTextContents(self, name: str, plug: str) -> None:
        self.name.setText(name)
        self.plug.setText(plug)

    def reload(self, commentators: dict, navigators: list[str]) -> None:
        self.commentators = commentators
        self.name.loadAutocomplete(commentators.keys())
        self.nav.clear()
        self.configureNav(navigators)

    def autofillComms(self):
        commentator = self.commentators.get(self.name.text())
        if commentator is None:
            return
        self.plug.setText(commentator.get('hndl', ''))