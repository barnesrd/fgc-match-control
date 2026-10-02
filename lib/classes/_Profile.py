from dataclasses import dataclass
import qt_themes
from PySide6.QtWidgets import QCompleter
import logging

from .enum import SubmitMode

c_mode_map = {'popup_completion': QCompleter.CompletionMode.PopupCompletion}

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


class Profile:
    _required = {'name': str}
    _optional = {
        'submit_mode': int,
        'debounce': float,
        'theme': str,
        'complete_mode': str,
    }
    _default = {
        'name': 'Invalid Profile',
        'submit_mode': 1,
        'debounce': 0.7,
        'theme': 'blender',
        'complete_mode': 'popup_completion',
    }

    def __init__(self, data: dict):
        if not Profile.validate(data):
            self._digest_dict(Profile._default)
            return
        self._digest_dict(data)

    @classmethod
    def validate(cls, data: dict) -> bool:
        for key in Profile._required.keys():
            if not key in data or not isinstance(
                data[key], Profile._required[key]
            ):
                logging.error(
                    f'Profile validation error: Missing required key or invalid type - {key} with value {data.get(key)}. '
                    f'Expected type {Profile._required[key].__name__}, got type {type(data.get(key)).__name__}'
                )
                return False
        for key in Profile._optional.keys():
            if key in data and not isinstance(
                data.get(key), Profile._optional[key]
            ):
                logging.warning(
                    f'Profile validation error: Optional key present with invalid type - {key} with value {data.get(key)}. '
                    f'Expected type {Profile._optional[key].__name__}, got type {type(data.get(key)).__name__}'
                )
                return False
        return True

    def _digest_dict(self, data: dict):
        for key in Profile._required.keys():
            setattr(self, key, data.get(key, Profile._default[key]))
        for key in Profile._optional.keys():
            data[key] = data.get(key, Profile._default[key])
            match key:
                case 'complete_mode':
                    setattr(
                        self,
                        key,
                        c_mode_map.get(data[key], Profile._default[key]),
                    )
                case 'submit_mode':
                    setattr(
                        self,
                        key,
                        SubmitMode(data[key])
                        if data[key] in SubmitMode
                        else SubmitMode(Profile._default[key]),
                    )
                case _:
                    setattr(self, key, data.get(key, Profile._default[key]))

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, theme: str):
        self._theme = theme
        if theme not in valid_themes:
            logging.error(f'Invalid theme provided: {theme}. Reverting to default theme: {Profile._default['theme']}')
            self._theme = Profile._default['theme']
        qt_themes.set_theme(self._theme)
