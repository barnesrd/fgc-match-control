from PySide6.QtWidgets import QLineEdit, QCompleter
from PySide6.QtCore import Qt
from threading import Timer

from lib.classes import AppController
from lib.classes.enum import SubmitMode
from data.globals import CONTROLLER


class DbEntry(QLineEdit):
    _min_view_characters = 10
    _width_padding = 8

    def __init__(
        self,
        on_submit: callable,
    ):
        super().__init__()
        self.on_submit = on_submit
        self._autocomplete_list: list[str] | None
        self._timer: Timer | None = None
        self.setMinimumWidth(
            max(len(self.placeholderText()), self._min_view_characters)
            * self.fontMetrics().averageCharWidth()
        )
        self.textChanged.connect(self._timeout)

    @property
    def value(self) -> str:
        return self.text()

    @property
    def autocomplete_list(self):
        return self._autocomplete_list

    @autocomplete_list.setter
    def autocomplete_list(self, items: list[str]):
        completer = QCompleter(items)
        completer.setCompletionMode(AppController().profile.complete_mode)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        min_characters = max(
            len(self.placeholderText()), self._min_view_characters
        )
        if len(items) > 0:
            min_characters = max(len(max(item_list, key=len)), min_characters)
        self.setMinimumWidth(
            min_characters * self.fontMetrics().averageCharWidth()
            + self._width_padding
        )
        self.setCompleter(completer)

    def _timeout(self):
        if CONTROLLER.profile.submit_mode != SubmitMode.ON_EDIT:
            return
        if self._timer is not None:
            self._timer.cancel()
        self._timer = Timer(
            CONTROLLER.profile.debounce / 2, self.on_submit, [self.value]
        )
        self._timer.start()

    def reset(self):
        self.setText('')
