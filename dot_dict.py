# coding=utf-8
from collections import defaultdict


class DotDict(object):
    u""" словарь с точками
    """
    def __init__(self):
        self.__val = defaultdict(lambda: DotDict())

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __setitem__(self, key, value):
        if self.__val is None:
            self.__val = {}
        self.__val[key] = value

    def __getitem__(self, key):
        return self.__val[key]

    def get_value(self, key, default_value=None):
        u""" возвращает значение ключа, если есть или default значение """
        val = self._DotDict__val[key]
        return val if not isinstance(val, DotDict) else default_value
