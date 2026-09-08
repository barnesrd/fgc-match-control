from PySide6.QtWidgets import QLineEdit, QCompleter
from PySide6.QtCore import Qt
from threading import Timer
from classes import SubmitMode

from util.qtHelpers import getEntryWidth
from data.globals import appdata


class DebouncedEntry(QLineEdit):
    def __init__(
        self,
        onSubmit: callable,
        placeholder: str = '',
        autocomplete: list[str] = [],
        maxLength: int = 20,
        debounce: float = 0.5
    ):
        super().__init__()
        self._initialMaxLength = maxLength

        self.loadAutocomplete(autocomplete)

        self.setPlaceholderText(placeholder)

        self._onSubmit = onSubmit
        self._timer: Timer | None = None
        if debounce <= 0:
            raise ValueError('Entry debounce cannot be 0 or less!')
        self._debounce = debounce
        self.textChanged.connect(self._startTimeout)

    def _startTimeout(self) -> None:
        if self.SubmitMode != SubmitMode.ON_EDIT:
            return
        if self._timer is not None:
            self._timer.cancel()
        self._timer = Timer(self._debounce, self._onSubmit, [self.text()])
        self._timer.start()

    @property
    def value(self) -> string:
        return self.text()

    @property
    def debounce(self) -> float:
        return self._debounce

    @debounce.setter
    def debounce(self, debounce: int) -> None:
        self._debounce = debounce
        self._timer = Timer(self._debounce, self._onSubmit, [self.text()])

    @property
    def onSubmit(self) -> callable:
        return self._onSubmit

    @onSubmit.setter
    def onSubmit(self, onSubmit: callable) -> None:
        self._onSubmit = onSubmit
        self._timer = Timer(self._debounce, self._onSubmit, [self.text()])

    # Adjusts minimum width and returns the maximum amount of characters set for this entry
    def adjustMinWidth(self, autocomplete: list[str]) -> int:
        if len(autocomplete) == 0:
            maxChars = self._initialMaxLength
        else:
            maxChars = max(
                len(max(autocomplete, key=len)), self._initialMaxLength
            )
        self.setMaxLength(maxChars)
        self.setMinimumWidth(getEntryWidth(maxChars, self))
        return maxChars

    # Loads autocomplete data and adjusts entry size accordingly
    def loadAutocomplete(self, autocomplete: list[str]) -> None:
        completer = QCompleter(autocomplete)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.setCompleter(completer)
        self.adjustMinWidth(autocomplete)
