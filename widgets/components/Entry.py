from PySide6.QtWidgets import QLineEdit, QCompleter
from PySide6.QtCore import Qt

from util.qtHelpers import getEntryWidth


class Entry(QLineEdit):
    def __init__(
        self, placeholder: str = '', autocomplete: list[str] = [], maxLength: int = 20
    ):
        super().__init__()
        self.onFocusOut = lambda: None
        self.initialMaxLength = maxLength

        self.loadAutocomplete(autocomplete)

        self.setPlaceholderText(placeholder)

    # Adjusts minimum width and returns the maximum amount of characters set for this entry
    def adjustMinWidth(self, autocomplete: list[str]) -> int:
        if len(autocomplete) == 0:
            maxChars = self.initialMaxLength
        else:
            maxChars = max(len(max(autocomplete, key=len)), self.initialMaxLength)
        (self.setMaxLength(maxChars),)
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

    def setOnFocusOut(self, f: callable) -> None:
        self.onFocusOut = f

    def focusOutEvent(self, e) -> None:
        self.onFocusOut()
        super().focusOutEvent(e)
