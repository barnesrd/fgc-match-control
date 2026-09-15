from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QCheckBox

from lib.widget.component import DbEntry, DbSelect


class ScoreMatch(QWidget):
    def __init__(
        self,
        on_submit: callable,
    ):
        super().__init__()
        self.on_submit = on_submit

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        self._title = DbEntry(lambda data: self.update('title', data))
        self._title.setPlaceholderText('Match Title')
        layout.addWidget(self._title, 0, 0)

        self._background = DbSelect(lambda data: self.update('background', data))
        self._background.setPlaceholderText('Background')
        layout.addWidget(self._background, 0, 1)

        self._data = {
            'title': self._title.value,
            'background': self._background.value
        }

        self.setLayout(layout)

    def update(self, key: str, value: str|int):
        if self._data.get(key) is None:
            return
        self._data[key] = value
        self.on_submit(self._data)

    def clear(self):
        self._title.clear()
        self._background.clear()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: dict):
        self._title.setText(data.get('title', ''))