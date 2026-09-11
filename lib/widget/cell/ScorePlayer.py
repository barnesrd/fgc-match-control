from PySide6.QtWidgets import QWidget, QHBoxLayout

from lib.widget.component import DbEntry, DbIntCounter

class ScorePlayer(QWidget):
    def __init__(
        self,
        label: str,
        on_submit: callable
    ):
        super().__init__()
        
        self.on_submit = on_submit
        
        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        # Initial Label
        layout.addWidget(QLabel(label), 0, 0)
        
        # Name Entry
        self._name = DbEntry(self.submit)
        self._name.setPlaceholderText('Name')
        layout.addWidget(self._name, 0, 1)
        
        # Character Entry
        self._character = DbEntry(self.submit)
        self._character.setPlaceholderText('Character')
        layout.addWidget(self._character, 0, 2)
        
        # Country Entry
        self._country = DbEntry(self.submit)
        self._country.setPlaceholderText('Country')
        layout.addWidget(self._country, 0, 3)
        
        # Score Entry
        self._score = DbIntCounter(self.submit, 0, 99)
        layout.addWidget(self._score, 0, 4)
        
    def submit(self):
        pass