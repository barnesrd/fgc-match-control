from PySide6.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QLabel
import logging

from lib.widget.component import DbEntry, DbIntCounter, DbEntrySelect
from lib.classes import AppController
from data.globals import CONTROLLER, COUNTRIES


class ScorePlayer(QWidget):
    def __init__(self, label: str, on_submit: callable):
        logging.debug(f'Setting up scoreboard Player cell with label: "{label}"')
        super().__init__()

        self.on_submit = on_submit

        layout = QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        # Initial Label
        label_widget = QLabel(label)
        label_widget.setFixedWidth(
            self.fontMetrics().averageCharWidth() * len(label) + 8
        )
        layout.addWidget(label_widget)

        # Name Entry
        logging.debug('Creating name input box...')
        self._name = DbEntry(lambda data: self.update('name', data))
        self._name.setPlaceholderText('Name')
        layout.addWidget(self._name)

        # Character Entry
        logging.debug('Creating character input dropdown...')
        self._character = DbEntrySelect(
            lambda data: self.update('character', data)
        )
        self._character.setPlaceholderText('Character')
        layout.addWidget(self._character)
        logging.debug('Adding character input to character listeners...')
        CONTROLLER.add_character_listener(self._character)

        # Country Entry
        logging.debug('Creating country input dropdown...')
        self._country = DbEntrySelect(lambda data: self.update('country', data))
        self._country.setPlaceholderText('Country')
        logging.debug(f'Registering {len(COUNTRIES)} countries to country dropdown...')
        self._country.items = COUNTRIES
        layout.addWidget(self._country)

        # Score Entry
        logging.debug('Creating score entry...')
        self._score = DbIntCounter(
            lambda data: self.update('score', data), 0, 999
        )
        layout.addWidget(self._score)
        
        self.setLayout(layout)

        self._data = self.data
        logging.debug('Player cell successfully loaded!')

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
            'score': self._score.value,
        }

    def update(self, key: str, value: str | int):
        if self._data.get(key) is None:
            return
        self._data[key] = value
        self.on_submit(self._data)

    def clear(self):
        self._name.reset()
        self._character.reset()
        self._country.reset()
        self._score.reset()

    def reset_score(self):
        self._score.clear()
