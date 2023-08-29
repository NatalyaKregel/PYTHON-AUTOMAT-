'''
Задание №3
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
'''

class BaseException(Exception):
    pass


class LevelException(BaseException):
    print('Level')


class AccesException(BaseException):
    print('Access')