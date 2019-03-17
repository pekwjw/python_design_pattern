# -*- coding:utf-8 -*-

# method1
def singleton(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class cls(object):
    def __init__(self):
        pass

# method2
class singleton_new(object):
    _instance = None
    def __init__(self):
        self.number = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance

    def Number(self):
        self.number += 1
        return self.number

def main():
    c1 = cls()
    c2 = cls()
    assert id(c1) == id(c2)

    single1 = singleton_new()
    single2 = singleton_new()

    print id(single1) == id(single2)
    print single1.Number()
    print single2.Number()

if __name__ == "__main__":
    main()
