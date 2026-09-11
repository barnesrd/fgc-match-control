from PySide6.QtWidgets import QMainWindow
import qt_themes

from .metaclass import Singleton
from .Game import Game
from .Profile import Profile

class AppController(metaclass=Singleton):
    _name: str = 'Match Control'
    _version: str = '0.6'
    
    _valid_themes: set[str] = {
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
    
    _game: Game
    _profile: str = Profile()
    _theme: str
    
    _window: QMainWindow
    
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
            qt_themes.setTheme(theme)
            self._theme = theme
        else:
            print('Invalid theme! Falling back to default theme.')
            qt_themes.set_theme('blender')
            self._theme = 'blender'
            
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, filepath: str):
        self._game = Game(filepath)
        
    @property
    def profile(self):
        return self._profile
    
    @profile.setter
    def profile(self, filepath: str):
        self._profile = Profile(filepath)