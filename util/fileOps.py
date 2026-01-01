from os import getcwd, path, mkdir
from pathlib import Path
from contextlib import closing
from json import load, dump

from data.fallbacks import config, profile, theme

def createFileStructure() -> None:
    Path('./profiles').mkdir(parents=True, exist_ok=True)
    if not path.exists('./profiles/default.json'):
        with closing(open(path.join(getcwd(), './profiles/default.json'), 'w')) as f:
            dump(profile, f, indent=4)
    Path('./themes').mkdir(parents=True, exist_ok=True)
    if not path.exists('./themes/p4au.json'):
        with closing(open(path.join(getcwd(), './themes/p4au.json'), 'w')) as f:
            dump(theme, f, indent=4)

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

def getTheme() -> dict:
    try:
        with closing(open(path.join(getcwd(), f'themes/{config.get('activeTheme')}.json'), 'r')) as f:
            print(getConfig().get('activeTheme'))
            return load(f)
    except:
        print('Theme loaded wrong, falling back')
        # Fallback theme
        return theme