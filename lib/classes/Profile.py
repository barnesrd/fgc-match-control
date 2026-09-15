from dataclasses import dataclass
import qt_themes
from PySide6.QtWidgets import QCompleter

from .enum import SubmitMode
from . import AppController

@dataclass
class Profile:
    name: str
    submit_mode: SubmitMode = SubmitMode.ON_EDIT
    debounce: float = 0.5
    theme: str = 'blender'
    complete_mode: QCompleter.CompletionMode = QCompleter.CompletionMode.PopupCompletion

    def set_theme(self, theme: str):
        if theme in AppController.valid_themes:
            self.theme = theme
        else:
            print(f'Invalid theme provided: ${theme} | Reverting back to default')
            self.theme = 'blender'
        qt_themes.set_theme(theme)

