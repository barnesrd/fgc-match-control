import argparse

from lib.classes.metaclass import Singleton

class FlagParser(argparse.ArgumentParser, metaclass=Singleton):
    def __init__(self):
        super().__init__(
            prog='python main.py',
            description='''
                            FGC Match Control
                        ''',
            fromfile_prefix_chars='?',
        )

        self.add_argument(
            '-c', '--config', type=str, help='The filepath to load config data from'
        )

        self.add_argument(
            '-d',
            '--debug',
            action='store_true',
            help='Runs the program in debug mode',
        )
        
        self.add_argument(
            '-lp',
            '--logpath',
            type=str,
            help='The directory to save log files to'
        )
        
        self.add_argument(
            '-lt',
            '--logtag',
            type=str,
            default='',
            help='Adds a custom tag to the start of log files for organization'
        )
        
        self.add_argument(
            '--console',
            action='store_true',
            help='Launches a console window to view logs'
        )

        self.args = vars(self.parse_args())
