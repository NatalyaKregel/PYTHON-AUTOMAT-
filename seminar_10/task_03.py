'''
Напишите класс для хранения информации о человеке:
    ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы:
    birthday для увеличения возраста на год,
    full_name для вывода полного ФИО и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст
'''


class Person:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.name = first_name.capitalize()
        self.surname = last_name.capitalize()
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        print(f"{self.surname} {self.name}")

    def get_age(self) -> float:
        return self.__age


if __name__ == '__main__':
    p1 = Person("MikE", "JeKson", 30)
    p1.full_name()
    print(f'{p1.get_age() = }')
    p1.birthday()
    print(f'{p1.get_age() = }')