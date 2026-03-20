import sys
from PySide6.QtWidgets import QApplication

from util.theming import setVisualTheme
from util.fileOps import getConfig, getProfile, getGame, createFileStructure
from widgets.window import MainWindow
from data.appdata import name, version

if __name__ == '__main__':
    app: QApplication = QApplication([])

    app.setApplicationName(name)
    app.setApplicationVersion(version)

    createFileStructure()

    config = getConfig()
    profile = getProfile()
    game = getGame()
    
    setVisualTheme(app, config.get('activeTheme'))

    main = MainWindow(profile, game, config)

    sys.exit(app.exec())