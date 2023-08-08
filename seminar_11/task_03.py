'''
Задача 3:
Добавьте к задачам 1 и 2 строки документации для классов.
'''


class Archive:
    """Save old value"""
    _instance = None

    def __init__(self, num: int, val: str):
        """Add new num and val"""
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        """Created new class with lists for nums and vals."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.number = []
            cls._instance.value = []
        else:
            cls._instance.number.append(cls._instance.num)
            cls._instance.value.append(cls._instance.val)
        return cls._instance


if __name__ == '__main__':
    s = Archive(123, 'sdf')
    print(s.number, s.value)

    s = Archive(5887, 'Hello')
    print(s.number, s.value)
    s = Archive(8952, 'Hi')
    print(s.number, s.value)
    help(Archive)