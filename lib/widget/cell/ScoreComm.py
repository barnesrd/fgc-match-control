from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QCheckBox

from lib.widget.component import DbEntry, DbSelect

class ScoreComm(QWidget):
    def __init__(
        self,
        label: str,
        on_submit: callable
    ):
        super().__init__()

        self.on_submit = on_submit

        layout = QGridLayout()
        layout.setContentsMargins(2, 2, 2, 2)

        layout.addWidget(QLabel(label), 0, 0)

        # Name
        self._name = DbEntry(lambda data: self.update('name', data))
        self._name.setPlaceholderText('Name')
        layout.addWidget(self._name, 0, 1)

        self._plug = DbEntry(lambda data: self.update('plug', data))
        self._plug.setPlaceholderText('Handle')
        layout.addWidget(self._plug, 0, 2)

        self._nav = DbSelect(lambda data: self._update('nav', data))
        self._nav.setPlaceholderText('Nav')
        layout.addWidget(self._nav, 0, 3)

        self.setLayout(layout)

        self._data = self.data
        print(self._data)

    def update(self, key: str, value: str|int):
        if self._data.get(key) is None:
            return
        self._data[key] = value
        self.on_submit(self._data)

    def clear(self):
        self._name.clear()
        self._plug.clear()
        self._nav.clear()
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: dict):
        self._name.setText(data.get('name', ''))
        self._plug.setText(data.get('plug', ''))

    @data.getter
    def data(self):
        return {
            'name': self._name.value,
            'plug': self._plug.value,
            'nav': self._nav.value
        }
