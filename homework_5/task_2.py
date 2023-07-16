'''
Задача №2:
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

def path_elem(text):
    way = '\\'.join(text.split('\\')[:-1])
    *_, name, expansion = text.replace('.', '\\').split('\\')
    result = (way, name, expansion)
    return result


print(path_elem("C:\ProgramFiles\Seminar\\task_08.py"))