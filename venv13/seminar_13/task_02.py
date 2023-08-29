'''
Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и значение по умолчанию.
При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
'''

def get_dict(user_dict, key_dict, val_d=None):
    try:
        res = user_dict[key_dict]
        return res
    except KeyError as k:
        return f'Нет такого ключа, дефолтное значение {val_d}'


user = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
if __name__ == '__main__':
    print(get_dict(user, 5))