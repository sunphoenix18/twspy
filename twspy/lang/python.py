import sys

from .overloading import overloaded

if sys.version_info[0] >= 3:
    cmp = lambda x, y: (x > y) - (x < y)
else:
    from __builtin__ import cmp


class classmethod(classmethod):
    def __getattr__(self, name):
        return getattr(self.__func__, name)
