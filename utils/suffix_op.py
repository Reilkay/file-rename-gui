import re
from typing import Pattern


class SuffixOperation:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass

    def pre_operate(self, suffix: str) -> str:
        pattern = re.compile(r'\.([a-zA-Z0-9]+|\*)$')
        pattern1 = re.compile(r'\*\.([a-zA-Z0-9]+|\*)$')
        pattern2 = re.compile(r'[a-zA-Z0-9]+|\*$')
        resu = ''
        if pattern.fullmatch(suffix):
            resu = suffix
        elif pattern1.fullmatch(suffix):
            resu = pattern.search(suffix).group()
        elif pattern2.fullmatch(suffix):
            resu = '.' + suffix
        return resu

    def get_regular_expression(self, suffix: str) -> Pattern:
        suffix = self.pre_operate(suffix)
        # 忽略大小写
        pattern = re.compile(suffix + '$', re.IGNORECASE)
        return pattern