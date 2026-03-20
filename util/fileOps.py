from os import getcwd, path, mkdir
from pathlib import Path
from contextlib import closing
from json import load, dump

from data.fallbacks import config, profile, game

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
    try: 
        with closing(open(path.join(getcwd(), 'config.json'), 'r')) as f:
            return load(f)
    except:
        print('Config loaded wrong, falling back')
        return config

def getProfile() -> dict:
    try:
        with closing(open(path.join(getcwd(), f'profiles/{config.get('activeProfile')}.json'), 'r')) as f:
            print(getConfig().get('activeProfile'))
            return load(f)
    except:
        print('Profile loaded wrong, falling back')
        # Fallback profile
        return profile

def getGame() -> dict:
    try:
        with closing(open(path.join(getcwd(), f'games/{config.get('activeGame')}.json'), 'r')) as f:
            print(getConfig().get('activeGame'))
            return load(f)
    except:
        print('Game loaded wrong, falling back')
        # Fallback game
        return game
