
@dataclass
class Game:
    id: str = 'Unrecognized Game'
    name: str = 'Name Unspecified'
    characters: dict = {}
    navigators: dict|None = None
    
    def get_character_names(self) -> list[str]:
        return self.characters.keys()
