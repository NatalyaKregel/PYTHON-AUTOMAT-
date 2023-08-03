'''
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
    ○ шестизначный идентификационный номер
    ○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
'''


class Person:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.name = first_name.capitalize()
        self.surname = last_name.capitalize()
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self) -> None:
        print(f"{self.surname} {self.name}")

    def get_age(self) -> float:
        return self.__age


class Employee(Person):

    def __init__(self, name: str, last_name: str, age: int, id: int):
        super().__init__(name, last_name, age)
        self.__id = id
        self.__level = None

    def set_level(self):
        sum_digits = [int(i) for i in str(self.__id)]
        self.__level = sum(sum_digits) % 7

    def get_level(self) -> int:
        return self.__level

    def get_id(self) -> int:
        return self.__id


if __name__ == '__main__':
    e1 = Employee("Mike", "Jekson", 25, 123406)
    print(e1.full_name(), e1.get_age(), e1.get_id(), e1.set_level(), e1.get_level())