'''
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п. У каждого класса должны быть как общие свойства, 
например имя, так и специфичные для класса. Для каждого класса создайте метод, 
выводящий информацию специфичную для данного класса.
'''
class Animal:

    def __init__(self, name: str, age: int = None):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        self.__age = age

    def get_info(self) -> tuple:
        return self.get_name(), self.get_age()


class Cat(Animal):
    _type = 'Cat'

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__skill = {'meow': "Meow-meow-meow"}
        self.__specificity = ['head', 'paws', 'tail']

    def make_ability(self, ability: str) -> None:
        if ability.lower() in self.__skill.keys():
            print(f"{self.get_name()} says: {self.__skill[ability.lower()]}")
        else:
            print("Unknown command!")


class Dog(Animal):
    _type = 'Dog'

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__skill = {'bark': "Woof woof"}
        self.__specificity = ['head', 'paws', 'tail']

    def make_ability(self, ability: str) -> None:
        if ability.lower() in self.__skill.keys():
            print(f"{self.get_name()} says: {self.__skill[ability.lower()]}")
        else:
            print("Unknown command!")


if __name__ == '__main__':
    a1 = Cat('Murka', 3)
    a2 = Dog('Barsik', 5)

    a1.make_ability('meow')
    a1.make_ability('any')
    print(a1.get_name(), a1.get_age())
    print(*a1.get_info())

    a2.make_ability('bark')
    print(a2.get_name(), a2.get_age())
    print(*a2.get_info())