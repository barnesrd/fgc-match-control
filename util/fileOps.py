from os import getcwd, path
from contextlib import closing
from json import load

from data.fallbacks import config, profile, theme

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