from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

class ConfirmDialog(QDialog):
    def __init__(self, prompt: str):
        super().__init__()
        
        layout = QVBoxLayout()

        label = QLabel(prompt)
        label.setMargin(10)

        layout.addWidget(label)
        
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Yes |
            QDialogButtonBox.StandardButton.No
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        layout.addWidget(buttons)
        self.setLayout(layout)
        self.accept()
