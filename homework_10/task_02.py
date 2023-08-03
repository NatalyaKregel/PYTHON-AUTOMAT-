'''
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки
'''

class Animal:

    def __init__(self, name: str, age: int = None, skill: dict = {}, specificity: list = []):
        self.__name = name
        self.__age = age
        self.__skill = skill
        self.__specificity = specificity

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

    def make_ability(self, ability: str) -> None:
        if ability.lower() in self.__skill.keys():
            print(f"{self.get_name()}: {self.__skill[ability.lower()]}")
        else:
            print("Unknown command!")

    def add_skill(self, skill_name: str, skill: str):
        if skill in self.__skill.keys():
            print("I can do it already!")
        else:
            self.__skill[skill_name] = skill

    def all_skills(self):
        print(self.__skill)


class Cat(Animal):
    _type = 'Cat'

    def __init__(self, name: str, age: int, skill={'meow': "Meow-meow-meow"}, specificity=['head', 'paws', 'tail']):
        super().__init__(name, age, skill, specificity)


class Dog(Animal):
    _type = 'Dog'

    def __init__(self, name: str, age: int, skill={'bark': "Woof woof"}, specificity=['head', 'paws', 'tail']):
        super().__init__(name, age, skill, specificity)


if __name__ == '__main__':
    a1 = Cat('Murka', 3)
    a2 = Dog('Barsik', 5)

    a1.make_ability('meow')
    a1.make_ability('any')
    print(a1.get_name(), a1.get_age())
    print(*a1.get_info())
    a1.add_skill("running", "started running")
    a1.all_skills()
    a1.make_ability('running')

    a2.make_ability('bark')
    print(a2.get_name(), a2.get_age())
    print(*a2.get_info())