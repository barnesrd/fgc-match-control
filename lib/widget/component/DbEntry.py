from PySide6.QtWidgets import QLineEdit, QCompleter
from threading import Timer

from lib.classes import AppController
from lib.classes.enum import SubmitMode

class DbEntry(QLineEdit):
    def __init__(
        self,
        on_submit: callable,
    ):
        super().__init__()
        self.on_submit = on_submit
        self._autocomplete_list: list[str]|None
        self._timer: Timer|None
    
    @property
    def value(self) -> str:
        return self.text()

    @property
    def autocomplete_list(self):
        return self._autocomplete_list

    @autocomplete_list.setter
    def autocomplete_list(self, l: items[str]):
        completer = QCompleter(items)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.setCompleter(completer)

    
    def _timeout(self):
        if AppController().profile.submit_mode != SubmitMode.ON_EDIT:
            return
        if self._timer is not None:
            self._timer.cancel()
        self._timer = Timer(
            AppController().profile.debounce / 2,
            self.on_submit,
            [self.value]
        )
        self._timer.start()
        
    def clear(self):
        self.setText('')