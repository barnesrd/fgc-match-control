from PySide6.QtWidgets import QFrame


class HorizLine(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)
