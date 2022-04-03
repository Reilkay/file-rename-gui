import toml


class Config:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.__path = './config.toml'

    def get(self) -> dict:
        config = toml.load(self.__path)
        return config

    def update(self, config: dict) -> None:
        with open(self.__path, 'w') as f:
            r = toml.dump(config, f)
            # print(r)