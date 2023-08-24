'''
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''

import csv
from functools import reduce
from pathlib import Path

class Validate:
    """Проверяет полное имя на первую заглавную букву и наличие только букв"""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство {self.param_name} невозможно удалить')

    def validate(self, value):                                          
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть текстовым')
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = Validate()
    second_name = Validate()
    surname = Validate()
    _lessons = None

    def __init__(self, name: str, second_name: str, surname: str, lessons: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.lessons = lessons

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, lessons: Path):
        if self.lessons is not None:
            raise AttributeError(f'Список предметов уже определен')
        self._lessons = {"lessons": {}}
        with open(lessons, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons["lessons"][row[0]] = {"estimates": [],
                                                    "tests": [],
                                                    "middle_estimate_test": None}
        self._lessons["middle_estimate"] = None


    def new_estimate(self, name_of_lesson: str, number: int, type_est: str = "lesson"):
        if type_est == "lesson":
            if number < 2 or number > 5:
                raise ValueError("Рейтинг вне допустимого диапазона (2-5)")
            self.lessons["lesson"][name_of_lesson]["estimates"].append(number)
            self.lessons["middle_estimate"] = self.middle_estimate(self.lessons)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise ValueError("Рейтинг вне допустимого диапазона (0-100)")
            self.lessons["lessons"][name_of_lesson]["tests"].append(number)
            self.lessons["lessons"][name_of_lesson]["middle_estimate_test"] = \
                reduce(lambda x, y: x + y, self.lessons["lessons"][name_of_lesson]["tests"]) / \
                len(self.lessons["lessons"][name_of_lesson]["tests"])


    @staticmethod
    def middle_estimate(lessons: dict):
        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["estimates"]) for name in lessons["lessons"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)


    def __repr__(self):
        result = f'''Student: full_name="{self.name} {self.second_name} {self.surname}",
middle_estimate={self.lessons["middle_estimate"]}\n'''
        for key, value in self.lessons["lesson"].items():
            result += f'{key}={value["middle_estimate_test"]}\n'
        return result


if __name__ == '__main__':
    s1 = Student("Nikolay", "Alekseevich", "Eremeev", Path('lessons.csv'))
    print(s1)
    s1.new_estimate("русский язык", 4)
    s1.new_estimate("математика", 5)
    s1.new_estimate("физика", 5)
    s1.new_estimate("биология", 5)
    s1.new_estimate("химия", 3)
    print(s1)
    s1.new_estimate("русский язык", 3)
    s1.new_estimate("математика", 4)
    s1.new_estimate("физика", 5)
    s1.new_estimate("биология", 4)
    s1.new_estimate("химия", 2)
    print(s1)
    s1.new_estimate("русский язык", 66, "test")
    s1.new_estimate("математика", 80, "test")
    s1.new_estimate("физика", 90, "test")
    s1.new_estimate("биология", 80, "test")
    s1.new_estimate("химия", 50, "test")
    print(s1)
    s1.new_estimate("русский язык", 75, "test")
    s1.new_estimate("математика", 90, "test")
    s1.new_estimate("физика", 95, "test")
    s1.new_estimate("биология", 90, "test")
    s1.new_estimate("химия", 70, "test")
    print(s1)