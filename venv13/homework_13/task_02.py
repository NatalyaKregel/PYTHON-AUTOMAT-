'''
Задание
Решить задачи, которые не успели решить на семинаре. Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''

from student_exeptions import StudentNameError, InvalidSubjectError, InvalidGradeError, InvalidTestError
from typing import List, Any, Iterable
import csv
import os

# Дескриптор для ФИО
class NameDescriptor:
    def __set_name__(self, owner: Any, name: str) -> None:
        self.assigned_attribute: str = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        return instance.dict[self.assigned_attribute]

    def __set__(self, instance: Any, value: str) -> Any:
        name: str = value.replace(" ", "")

        if name and name.isalpha() and value.istitle() and value.istitle():
            instance.__dict__[self.assigned_attribute] = value
        else:
            raise StudentNameError(f'{err_name}:{value}')

# Основной класс ПРЕДМЕТ
class StudentSubject:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.grade_scores: List[int] = []
        self.test_scores: List[int] = []

    def add_grade_score(self, scores: int) -> None:
        if 2 <= scores <= 5:
            self.grade_scores.append(scores)
        else:
            raise InvalidGradeError(err_grade)

    def add_test_score(self, result: int) -> None:
        if 0 <= result <= 100:
            self.test_scores.append(result)
        else:
            raise InvalidTestError(err_test)

# Основной класс ПРОФИЛЬ
class StudentProfile:
    subjects_list: NameDescriptor = NameDescriptor()

    def __init__(self, csv_file: str) -> None:
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f'{err_file}: {csv_file}')

        self.student_subjects: List[StudentSubject] = self.load_subjects_from_csv('subjects.csv')

    def load_subjects_from_csv(self, csv_file: str) -> List[StudentSubject]:
        student_subjects: List[StudentSubject] = []

        with open('subjects.csv', newline='', encoding='utf-8') as file:
            reader: Iterable = csv.reader(file)

            for row in reader:
                subject_title: str = row[0]
                student_subjects.append(StudentSubject(subject_title))

        return student_subjects

    def get_subject(self, subject_name: str) -> StudentSubject:
        for student_subject in self.student_subjects:
            if student_subject.name == subject_name:
                return student_subject
        raise InvalidSubjectError(f'{err_object}: {subject_name}')

    def add_grade(self, subject_name: str, grade: int) -> None:
        student_subject: StudentSubject = self.get_subject(subject_name)
        student_subject.add_grade_score(grade)

    def add_test_result(self, subject_name: str, result: int) -> None:
        student_subject: StudentSubject = self.get_subject(subject_name)
        student_subject.add_test_score(result)

    def calculate_average_grade(self, subject_name: str) -> float:
        student_subject: StudentSubject = self.get_subject(subject_name)

        if student_subject.grade_scores:
            return sum(student_subject.grade_scores) / len(student_subject.grade_scores)

        return 0.0

    def calculate_average_grade_all_subjects(self) -> float:
        student_grades: List[int] = [grade for subject in self.student_subjects for grade in subject.grade_scores]

        if student_grades:
            return sum(student_grades) / len(student_grades)

        return 0.0

    def calculate_average_test_result(self, subject_name: str) -> float:
        student_subject: StudentSubject = self.get_subject(subject_name)

        if student_subject.test_scores:
            return sum(student_subject.test_scores) / len(student_subject.test_scores)

        return 0.0

    def calculate_average_test_all_subjects(self) -> float:
        student_test: List[int] = [test for subject in self.student_subjects for test in subject.test_scores]

        if student_test:
            return sum(student_test) / len(student_test)

        return 0.0


if __name__ == "__main__":
    try:
        err_name = StudentNameError('ФИО должно начинаться с заглавной буквы и содержать только буквы!')
        err_grade = InvalidGradeError('Оценка по предмету должна находиться в диапазоне от 2 до 5!')
        err_test = InvalidTestError('Оценка по тесту должна находиться в диапазоне от 0 до 100!')
        err_object = InvalidSubjectError(f'Предмет отсутствует в списке!')
        err_file = FileNotFoundError(f'Файл не найден!')


        student: StudentProfile = StudentProfile("subjects.csv")
        student.subjects_list:str = "Петрова Ольга Петровна"

        #оценки по предметам:
        student.add_grade("Физика", 3)
        student.add_grade("Физика", 5)
        student.add_grade("Математика", 4)
        student.add_grade("Математика", 5)
        student.add_grade("Информатика", 2)
        student.add_grade("Информатика", 3)

        print("\nДНЕВНИК:\n\033[32mСредний балл по Физике: \033[0m",
              round(student.calculate_average_grade("Физика"), 2))
        print("\033[32mСредний балл по Математике: \033[0m",
              round(student.calculate_average_grade("Математика"), 2))
        print("\033[32mСредний балл по Информатике: \033[0m",
              round(student.calculate_average_grade("Информатика"), 2))
        print("\033[32mОБЩИЙ СРЕДНИЙ БАЛЛ ПО ВСЕМ ПРЕДМЕТАМ: \033[0m",
              round(student.calculate_average_grade_all_subjects(), 2))
        print(" -------------------------------------- ")

        #оценки по тестам:
        student.add_test_result("Химия", 63)
        student.add_test_result("Химия", 86)
        student.add_test_result("Биология", 96)
        student.add_test_result("Биология", 100)
        print("\033[32mСредний результат тестов по Химии: \033[0m",
              round(student.calculate_average_test_result("Химия"), 2))
        print("\033[32mСредний результат тестов по Биологии: \033[0m",
              round(student.calculate_average_test_result("Биология"), 2))
        print("\033[32mОБЩИЙ СРЕДНИЙ БАЛЛ ПО ТЕСТАМ: \033[0m",
              round(student.calculate_average_test_all_subjects(), 2))
    except (
            StudentNameError, InvalidSubjectError, InvalidGradeError,
            InvalidTestError, FileNotFoundError) as e:
        print(f"\n\033[31mОшибка: {e}\033[0m")
    finally:
        print('ФАЙЛ ЗАКРЫТ')

