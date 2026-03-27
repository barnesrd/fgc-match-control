from util.fileOps import open_file
from dataclasses import dataclass
from json import load


@dataclass
class GameTheme:
    name: str
    characters: dict[str:str]
    backgrounds: dict[str:str]
    navs: dict[str:str]

    def __init__(
        self,
        name: str,
        characters: dict[str:str],
        backgrounds: dict[str:str],
        navs: dict[str:str],
    ):
        self.name = name
        self.characters = characters
        self.backgrounds = backgrounds
        self.navs = navs

    @classmethod
    def fromJSON(cls, jsonpath: str):
        data: dict

        with open_file(jsonpath, mode='r') as f:
            data = load(f)

        return cls(
            data.get('name'),
            data.get('characters'),
            data.get('backgrounds'),
            data.get('navs'),
        )
