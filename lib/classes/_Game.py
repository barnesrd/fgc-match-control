import logging


class Game:
    _required = {
        'game_id': str,
        'name': str,
        'characters': dict,
    }
    _optional = {'navigators': dict}
    _default = {
        'game_id': 'defoinv',
        'name': 'Default Game (Or Invalid)',
        'characters': {},
        'navigators': {},
    }

    def __init__(self, data: dict):
        if not Game.validate(data):
            self._digest_dict(Game._default)
            return
        self._digest_dict(data)

    @classmethod
    def validate(cls, data: dict) -> bool:
        for key in Game._required.keys():
            if not key in data or not isinstance(
                data[key], Game._required[key]
            ):
                logging.error(
                    f'Game validation error: Missing required key or invalid type - "{key}" with value "{data.get(key)}". '
                    f'Expected type {Game._required[key].__name__}, got type {type(data.get(key)).__name__}'
                )
                return False
        for key in Game._optional.keys():
            if key in data and not isinstance(
                data.get(key), Game._optional[key]
            ):
                logging.warning(
                    f'Game validation error: Optional key present with invalid type - "{key}" with value "{data.get(key)}". '
                    f'Expected type {Game._optional[key].__name__}, got type {type(data.get(key)).__name__}'
                )
                return False
        return True

    def _digest_dict(self, data: dict):
        for key in Game._required.keys():
            logging.debug(f'Required Game attribute "{key}" being set to "{data.get(key, Game._default[key])}".')
            setattr(self, key, data.get(key, Game._default[key]))
        for key in Game._optional.keys():
            logging.debug(f'Optional Game attribute "{key}" being set to "{data.get(key, Game._default[key])}".')
            setattr(self, key, data.get(key, Game._default[key]))
