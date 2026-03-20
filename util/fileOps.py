from os import getcwd, path
from pathlib import Path
from contextlib import closing, contextmanager
from json import load, dump
from typing import Generator, TextIO

from data.fallbacks import config, profile, game

@contextmanager
def open_file(filepath: str, mode: str) -> Generator[TextIO]:
    f = open(filepath, mode)
    try:
        yield f
    except FileNotFoundError:
        print(f'Path {filepath} does not exist!')
    finally:
        f.close()

def createFileStructure() -> None:
    Path('./profiles').mkdir(parents=True, exist_ok=True)
    if not path.exists('./profiles/default.json'):
        with closing(open(path.join(getcwd(), 'profiles/default.json'), 'w')) as f:
            dump(profile, f, indent=4)
    Path('./games').mkdir(parents=True, exist_ok=True)
    if not path.exists('./games/p4au.json'):
        with closing(open(path.join(getcwd(), 'games/p4au.json'), 'w')) as f:
            dump(game, f, indent=4)
    if not path.exists('./config.json'):
        with closing(open(path.join(getcwd(), 'config.json'), 'w')) as f:
            dump(config, f, indent=4)

def exportScoreJson(data: dict) -> None:
    Path('./json').mkdir(parents=True, exist_ok=True)
    with closing(open(path.join(getcwd(), './json/scoreOverlay.json'), "w")) as f:
        dump(data, f, indent=4)

def getConfig() -> dict:
    with open_file(path.join(getcwd(), 'config.json'), 'r') as f:
        return load(f)

def getProfile() -> dict:
    with open_file(path.join(getcwd(), f'profiles/{config.get('activeProfile')}.json'), 'r') as f:
        return load(f)

def getGame() -> dict:
    with open_file(path.join(getcwd(), f'games/{config.get('activeGame')}.json'), 'r') as f:
        return load(f)
