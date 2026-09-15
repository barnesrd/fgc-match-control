from PySide6.QtWidgets import QComboBox

from lib.classes import AppController
from lib.classes.enum import SubmitMode

class DbSelect(QComboBox):
    def __init__(
        self,
        on_submit: callable
    ):
        super().__init__()
        self.on_submit = on_submit
    
    @property
    def value(self) -> str:
        return self.currentText()

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
        self.setCurrentIndex(-1)