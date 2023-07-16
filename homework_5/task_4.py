'''
Задача №4:
 Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def fibonachi(number):
    fibonachi1, fibonachi2 = 0, 1
    for i in range(number):
        fibonachi1, fibonachi2 = fibonachi2, fibonachi1 + fibonachi2
        yield fibonachi1


print(*fibonachi(20))