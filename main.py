import sys
from PySide6.QtWidgets import QApplication

from util.theming import setVisualTheme
from util.fileOps import getConfig, getProfile, getGame, createFileStructure
from widgets.window import MainWindow
from data.globals import appdata

if __name__ == '__main__':
    app: QApplication = QApplication([])

    app.setApplicationName(appdata.name)
    app.setApplicationVersion(appdata.version)

    createFileStructure()

    config = getConfig()
    profile = getProfile()
    game = getGame()

    setVisualTheme(app, config.get('activeTheme'))

    main = MainWindow(profile, game, config)

    appdata.mainWindow = main
    console.log(appdata.mainWindow)

    sys.exit(app.exec())
