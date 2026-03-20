from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from util.fileOps import config
import qt_themes
from data.appdata import validVisualThemes

def setVisualTheme(app: Qt, theme: str) -> None:
    font: QFont = app.font()
    font.setStyleHint(QFont.System)
    app.setFont(font)
    if theme in validVisualThemes:
        qt_themes.set_theme(theme)
    else:
        print('Invalid theme! Falling back to blender theme.')
        qt_themes.set_theme('blender')