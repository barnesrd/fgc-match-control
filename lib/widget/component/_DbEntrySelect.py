from PySide6.QtWidgets import QCompleter
from PySide6.QtCore import Qt

from data.globals import CONTROLLER
from ._DbSelect import DbSelect


class DbEntrySelect(DbSelect):
    _width_padding = 36
    _min_view_characters = 10

    def __init__(self, on_submit: callable):
        super().__init__(on_submit)
        self.setEditable(True)
        self._items = []
        self.setMinimumWidth(
            max(len(self.placeholderText()), self._min_view_characters)
            * self.fontMetrics().averageCharWidth()
            + self._width_padding
        )

    def reset(self):
        self.lineEdit().clear()
        self.setCurrentIndex(-1)

    def setPlaceholderText(self, text: str):
        self.lineEdit().setPlaceholderText(text)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items: dict):
        self._items = items
        self.clear()
        item_list = items.keys()
        for key in item_list:
            self.addItem(key, items[key])
        completer = QCompleter(item_list)
        completer.setCompletionMode(CONTROLLER.profile.complete_mode)
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
        self.reset()

    @items.deleter
    def items(self):
        self._items = {}
        self.clear()
        self.setCompleter(None)
        min_characters = max(
            len(self.placeholderText()), self._min_view_characters
        )
        self.setMinimumWidth(
            min_characters * self.fontMetrics().averageCharWidth()
            + self._width_padding
        )
        self.reset()
