#!/usr/bin/python
# -*- coding: utf-8 -*-


class Single(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        pass


def single(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls()

        return _instance[cls]
    return wrapper


def single_python3(cls):
    _instance = None

    def wrapper(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            _instance = cls()

        return _instance

    return wrapper


@single
class Single_1(object):
    def __init__(self):
        pass


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()

        return self._instance[self._cls]


@Singleton
class SingleClass(object):
    def __init__(self):
        pass


class SingletonInstance(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(SingletonInstance, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(SingletonInstance, self).__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(object):
    __metaclass__ = SingletonInstance

    def __init__(self):
        print('Creating Spam')


if __name__ == "__main__":
    single1 = Single()
    single2 = Single()

    id1 = id(single1)
    id2 = id(single2)
    print(id1, id2)
    print(id1 == id2)

    single_1 = Single_1()
    single_2 = Single_1()

    id_1 = id(single_1)
    id_2 = id(single_2)

    print(id_1, id_2)

    print(id(SingleClass()) == id(SingleClass()))

    a = Spam()
    b = Spam()
    print(id(a) == id(b))
    print(a is b)



