from PySide6.QtWidgets import QMainWindow, QLineEdit, QComboBox
import qt_themes
import logging

from .metaclass import Singleton
from ._Game import Game
from ._Profile import Profile


class AppController(metaclass=Singleton):
    _name: str = 'Match Control'
    _version: str = '0.6'

    _game_list: list[Game]
    _selected_game: Game
    _selected_profile: Profile
    _theme: str

    _window: QMainWindow

    _player_listeners: set = set()
    _comm_listeners: set = set()
    _character_listeners: set = set()
    _nav_listeners: set = set()

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def game(self):
        return self._selected_game

    @game.setter
    def game(self, data: dict):
        logging.info('Game setter in AppController called')
        self._selected_game = Game(data)
        logging.info(
            f'Game set to ID: {self._selected_game.game_id} | Name: {self._selected_game.name}'
        )
        for listener in self._character_listeners:
            if isinstance(listener, QLineEdit):
                listener.clear()
                listener.autocomplete_list = (
                    self._selected_game.get_character_names()
                )
                listener.setDisabled(
                    len(self._selected_game.get_character_names()) == 0
                )
            elif isinstance(listener, QComboBox):
                listener.setCurrentIndex(-1)
                listener.items = self._selected_game.characters
                listener.setDisabled(
                    len(self._selected_game.get_character_names()) == 0
                )
            else:
                raise Exception(
                    f'Unaccounted character listener type: {type(listener)}'
                )

    @property
    def profile(self) -> Profile:
        return self._selected_profile

    @profile.setter
    def profile(self, data: dict):
        logging.info('Profile setter in AppController called')
        self._selected_profile = Profile(data)
        logging.info(f'Profile set to Name: {self._selected_profile.name}')

    def add_character_listener(self, listener):
        self._character_listeners.add(listener)

    def remove_character_listener(self, listener):
        self._character_listeners.discard(listener)
