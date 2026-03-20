from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QCheckBox

from widgets.components.Entry import Entry
from widgets.components.ComboBox import ComboBox

class CommCell(QWidget):
    def __init__(self, label: str, commentators: dict, navigators: dict, submitFunc: callable, editSubmitToggle: QCheckBox):
        super().__init__()
        self.commentators = commentators
        self.navigators = navigators
        self.submitFunc = submitFunc
        self.editSubmitToggle = editSubmitToggle

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        layout.addWidget(QLabel(label), 0, 0)

        # Name
        self.name = Entry('Name', commentators.keys(), 25)
        self.name.setOnFocusOut(self.autofillComms)
        layout.addWidget(self.name, 0, 1)

        # Plug / Handle
        self.plug = Entry('Plug/Handle', [], 25)
        self.plug.setOnFocusOut(self.trySubmit)
        layout.addWidget(self.plug, 0, 2)

        self.nav = ComboBox()
        self.nav.setToolTip('Sets the navigator graphic to be used on the commentator overlay')
        self.nav.setOnFocusOut(self.trySubmit)
        self.configureNav(navigators)
        layout.addWidget(self.nav, 0, 3)

        self.setLayout(layout)

    def clear(self) -> None:
        self.name.setText('')
        self.plug.setText('')

    def getName(self) -> str:
        return self.name.text()

    def getPlug(self) -> str:
        return self.plug.text()
    
    def getNavCode(self) -> str:
        return self.navigators.get(self.nav.currentText(), '')

    def configureNav(self, navigators: dict):
        if len(navigators) == 0:
            self.nav.hide()
            return
        self.nav.addItems(sorted(navigators.keys()))
        self.nav.show()

    def setTextContents(self, name: str, plug: str) -> None:
        self.name.setText(name)
        self.plug.setText(plug)

    def reload(self, commentators: dict, navigators: list[str]) -> None:
        self.commentators = commentators
        self.name.loadAutocomplete(commentators.keys())
        self.nav.clear()
        self.configureNav(navigators)

    def trySubmit(self):
        if self.editSubmitToggle.isChecked():
            self.submitFunc()

    def autofillComms(self):
        commentator = self.commentators.get(self.name.text())
        if commentator is not None:
            self.plug.setText(commentator.get('hndl', ''))
            if self.nav.findText(commentator.get('nav', '')) != -1:
                self.nav.setCurrentText(commentator.get('nav'))
        self.trySubmit()
