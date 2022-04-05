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
        try:
            config = toml.load(self.__path)
            return config
        except FileNotFoundError:
            self.init_config_file()
            config = toml.load(self.__path)
            return config

    def update(self, config: dict) -> None:
        with open(self.__path, 'w') as f:
            r = toml.dump(config, f)
            # print(r)

    def init_config_file(self):
        init_data = """suffix_list = ['*.*','*.mp4','*.avi','*.mkv']

[path]
# home - current user home
# cwd - current work directory
# custom - customize path, if choose, start_path is necessary
start_from = 'cwd'
# if wrong, it will start from home
start_path = '' """
        with open(self.__path, 'w') as f:
            f.write(init_data)