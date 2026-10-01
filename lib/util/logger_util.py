from rich.logging import RichHandler
from rich.console import Console
from pathlib import Path
import logging


def setup_logger(debug: bool, logpath: str | None = None):
    file_log_format = '%(asctime)s | %(levelname)-8s | %(filename)-21s:%(lineno)-3s:%(funcName)-16s | %(message)s'
    console_log_format = '%(message)s'

    rh = RichHandler()
    rh.setFormatter(logging.Formatter(console_log_format))

    logger = logging.getLogger('rich')

    logging.root = logger

    config = {
        'level': logging.INFO if not debug else logging.DEBUG,
        'handlers': [rh],
    }

    if logpath is not None:
        if Path().parent.exists():
            config['format'] = logging.Formatter(file_log_format)
            fh = logging.FileHandler(logpath)
            fh.setFormatter(logging.Formatter(file_log_format))
            config['handlers'].append(fh)
        else:
            logging.warning(
                'A logpath was provided to the logger, but the path does not exist. Logs will not be saved!'
            )

    logging.basicConfig(**config)
