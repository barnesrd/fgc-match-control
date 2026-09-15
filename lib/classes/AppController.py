from PySide6.QtWidgets import QMainWindow, QLineEdit, QComboBox
import qt_themes

from .metaclass import Singleton
from .Game import Game
from .Profile import Profile
from lib.widget.component import DbEntry, DbSelect

class AppController(metaclass=Singleton):
    _name: str = 'Match Control'
    _version: str = '0.6'
    
    valid_themes: set[str] = {
        'blender',
        'atom_one',
        'catppuccin_frappe',
        'catppuccin_latte',
        'catppuccin_macchiato',
        'catppuccin_mocha',
        'dracula',
        'github_dark',
        'github_light',
        'modern_dark',
        'modern_light',
        'monokai',
        'nord',
        'one_dark_two',
    }
    
    _game_list: list[Game]
    _selected_game: Game
    _profile: str = Profile()
    _theme: str
    
    _window: QMainWindow
    _character_listeners: set[QLineEdit|QComboBox] = {}
    _nav_listeners: set[QComboBox] = {}
    
    @property
    def name(self):
        return self._name
    
    @property
    def version(self):
        return self._version
    
    @property
    def theme(self):
        return self._theme
    
    @theme.setter
    def theme(self, theme: str):
        if theme in self._valid_themes:
            self._theme = theme
        else:
            print('Invalid theme! Falling back to default theme.')
            self._theme = 'blender'
        qt_themes.set_theme(self._theme)

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game: Game):
        self._selected_game = game
        for listener in self._character_listeners:
            if isinstance(listener, QLineEdit):
                listener.clear()

        
    @property
    def profile(self):
        return self._profile
    
    @profile.setter
    def profile(self, filepath: str):
        self._profile = Profile(filepath)

    def add_character_listener(self, listener: QLineEdit):
        self._character_listeners.add(listener)
    
    def remove_character_listener(self, listener: QLineEdit):
        self._character_listeners.discard(listener)