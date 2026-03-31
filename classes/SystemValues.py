from classes.metaclasses import Singleton


class SystemValues(metaclass=Singleton):
    _name: str = 'FG Overlay Control'
    _version: str = '0.5'

    _validVisualThemes: set[str] = {
        'blender',
        'atom_one',
        'catppuccin_frappe',
        'catppuccin_latte',
        'catppuccin_macchiato',
        'catppuccin_mocha',
        'dracula',
        'github_dark',
        'github_light',
        'modern_dark',
        'modern_light',
        'monokai',
        'nord',
        'one_dark_two',
    }

    _profile: dict
    _gameTheme: dict

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def validVisualThemes(self):
        return self._validVisualThemes
