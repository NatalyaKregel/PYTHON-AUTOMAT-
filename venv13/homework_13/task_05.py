'''
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4) вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из
множества пользователей. добавление пользователя. Если уровень пользователя меньше,
чем ваш уровень, вызывайте исключение уровня доступа.
'''

from task04 import UserData, data_from_json
from task06 import MyLevelEx, MyAccessEx
from typing import Any


class Project:
    def __init__(self) -> None:
        self._current_user: None = None
        self._users: set = set()

    def load_json(self, path: str) -> None:
        self._users: set[UserData] = data_from_json(path)

    def sign_in(self, name: str, user_id: int) -> UserData:
        test_user: UserData = UserData(name, user_id, 0)

        if test_user not in self._users:
            raise MyAccessEx(user_id, name)

        for item in self._users:
            if item == test_user:
                self._current_user: Any = item
                return self._current_user

    def add_user(self, name: str, user_id: int, level: int) -> UserData:
        if level < self._current_user.level:
            raise MyLevelEx(name, level, self._current_user.level)

        new_user: UserData = UserData(name, user_id, level)
        self._users.add(new_user)

        return new_user


if __name__ == '__main__':

    try:
        project_1 = Project()
        project_1.load_json('task04.json')
        print(f'Успешный вход: {project_1.sign_in("Natalya", 14)}')

        test_user_1 = project_1.add_user('test_user', 15, 6)
        print(f'\nДобавлен пользователь: {test_user_1}')
        print(f'Успешный вход: {project_1.sign_in("test_user", 15)}')

        print(project_1.add_user('test_user_1', 34, 6))

    except(MyLevelEx, MyAccessEx) as e:
        print(f'\n\033[31mОшибка: {e}\033[0m')