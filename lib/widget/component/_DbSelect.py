from PySide6.QtWidgets import QComboBox

from threading import Timer
from lib.classes import AppController
from lib.classes.enum import SubmitMode
from data.globals import CONTROLLER


class DbSelect(QComboBox):
    def __init__(self, on_submit: callable):
        super().__init__()
        self.on_submit = on_submit
        self._timer: Timer | None = None

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

    @property
    def value(self) -> str:
        return self.currentData() or ''

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
        self.setCurrentIndex(-1)
