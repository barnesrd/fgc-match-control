import sys
from PySide6.QtWidgets import QApplication
import logging

from display import MainWindow
from data.globals import CONTROLLER
from lib.classes import Game
from lib.util.logger_util import setup_logger

if __name__ == '__main__':
    app: QApplication = QApplication([])

    setup_logger(False)
    logging.info('Logger has been successfully configured')
    logging.debug('Debug mode has been enabled')

    CONTROLLER.game = {
        'game_id': 'p4au',
        'name': 'persona 4 arena',
        'characters': {'hel': 'hl'},
    }
    CONTROLLER.profile = {'name': 'default'}

    main = MainWindow()

    CONTROLLER._window = main

    sys.exit(app.exec())
