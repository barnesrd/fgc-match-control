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
        self._timer: Timer|None
    
    @property
    def value(self) -> str:
        return self.text()
    
    def _timeout(self):
        if AppController().profile.submit_mode != SubmitMode.ON_EDIT:
            return
        if self._timer is not None:
            self._timer.cancel()
        self._timer = Timer(
            AppController().profile.debounce,
            self.on_submit,
            [self.value]
        )
        self._timer.start()
        