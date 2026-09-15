from PySide6.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QLabel

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
        self._name = DbEntry(lambda data: self.update('name', data))
        self._name.setPlaceholderText('Name')
        layout.addWidget(self._name, 0, 1)
        
        # Character Entry
        self._character = DbEntry(lambda data: self.update('character', data))
        self._character.setPlaceholderText('Character')
        layout.addWidget(self._character, 0, 2)
        
        # Country Entry
        self._country = DbEntry(lambda data: self.update('country', data))
        self._country.setPlaceholderText('Country')
        layout.addWidget(self._country, 0, 3)
        
        # Score Entry
        self._score = DbIntCounter(lambda data: self.update('score', data), 0, 999)
        layout.addWidget(self._score, 0, 4)

        self.setLayout(layout)

        self._data = self.data
        
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: dict):
        self._name.setText(data.get('name', ''))
        self._country.setText(data.get('country', ''))
        self._score.setText(data.get('score', self._score.default))

    @data.getter
    def data(self):
        return {
            'name': self._name.value,
            'character': self._character.value,
            'country': self._country.value,
            'score': self._score.value
        }

    def update(self, key: str, value: str|int):
        if self._data.get(key) is None:
            return
        self._data[key] = value
        self.on_submit(self._data)
    
    def clear(self):
        self._name.clear()
        self._character.clear()
        self._country.clear()
        self._score.clear()

    def reset_score(self):
        self._score.clear()