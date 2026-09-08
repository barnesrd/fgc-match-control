from PySide6.QtWidgets import QComboBox

from classes import SubmitMode


class ComboBox(QComboBox):
    def __init__(
        self, onSubmit: callable, submitMode: SubmitMode = SubmitMode.ON_EDIT
    ):
        super().__init__()
        self.currentIndexChanged.connect(self._submit)
        self._onSubmit = onSubmit
        self.submitMode = submitMode

    @property
    def value(self) -> str:
        return self.currentText

    def _submit(self) -> None:
        if self._submitMode != SubmitMode.ON_EDIT:
            return
        self._onSubmit()
