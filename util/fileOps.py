from os import getcwd, path, makedirs
from pathlib import Path
from contextlib import closing, contextmanager
from json import load, dump
from typing import Generator, TextIO

from data.fallbacks import config, profile, game


@contextmanager
def open_file(filepath: str, **kwargs) -> Generator[TextIO, None, None]:
    f = open(filepath, **kwargs)
    try:
        yield f
    except FileNotFoundError:
        print(f'Path {filepath} does not exist!')
    finally:
        f.close()


def create_file(filepath: str, content: str, replace: bool = True) -> None:
    if not replace and path.exists(filepath):
        return
    dirpath = path.dirname(filepath)
    if dirpath == '':
        raise ValueError(f'Provided filepath {filepath} is invalid!')
    makedirs(dirpath, exist_ok=replace)
    with open_file(filepath, mode='w') as f:
        f.write(content)


def createFileStructure() -> None:
    Path('./profiles').mkdir(parents=True, exist_ok=True)
    if not path.exists('./profiles/default.json'):
        with closing(
            open(path.join(getcwd(), 'profiles/default.json'), 'w')
        ) as f:
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
    with closing(
        open(path.join(getcwd(), './json/scoreOverlay.json'), 'w')
    ) as f:
        dump(data, f, indent=4)


def getConfig() -> dict:
    with open_file(path.join(getcwd(), 'config.json'), mode='r') as f:
        return load(f)


def getProfile() -> dict:
    with open_file(
        path.join(getcwd(), f'profiles/{config.get("activeProfile")}.json'),
        mode='r',
    ) as f:
        return load(f)


def getGame() -> dict:
    with open_file(
        path.join(getcwd(), f'games/{config.get("activeGame")}.json'), mode='r'
    ) as f:
        return load(f)
