'''
Доработаем задачи 5-6. Создайте класс-фабрику.
    ○ Класс принимает тип животного (название одного из созданных классов)
    и параметры для этого типа.
    ○ Внутри класса создайте экземпляр на основе переданного типа и
    верните его из класса-фабрики.
'''


class Animal:

    def __init__(self, name: str, age: int = None, skill: dict = {}, specificity: list = []):
        self.__name = name
        self.__age = age
        self.__skill = skill
        self.__specificity = specificity
        self.__type = self.__class__.__name__


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


    def get_type(self):
        return self.__type


    def get_full_info(self):
        return self.get_name(), self.get_age(), self.get_type(), self.__skill


class Cat(Animal):

    def __init__(self, name: str, age: int, skill={'meow': "Meow-meow-meow"}, specificity=['head', 'paws', 'tail']):
        super().__init__(name, age, skill, specificity)


class Dog(Animal):

    def __init__(self, name: str, age: int, skill={'bark': "Woof woof"}, specificity=['head', 'paws', 'tail']):
        super().__init__(name, age, skill, specificity)


class AnimalFactory:

    def _get_type(self, animal_type: str):
        types = {"dog": Dog, "cat": Cat}
        return types[animal_type.lower()]


    def create_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_type(animal_type)
        return new_animal(*args, **kwargs)


    def __init__(self, animal_type: str, *args, **kwargs):
        self.obj = self.create_animal(animal_type, args, kwargs)


    def get_animal(self):
        return self.obj


if __name__ == '__main__':
    factory = AnimalFactory("dog", "Barsik", 10)
    print(factory.get_animal().get_info())
    print(factory.get_animal().get_full_info())
