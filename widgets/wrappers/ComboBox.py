from PySide6.QtWidgets import QComboBox


class ComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.f = lambda: None

    def setOnFocusOut(self, func: callable) -> None:
        self.f = func

    def focusOutEvent(self, e) -> None:
        self.f()
        super().focusOutEvent(e)
