# - Улучшить задачу 2
# - Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# - Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# - Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint
from sys import argv


def guess_game(start=0, stop=10, attempts=3):
    guess = randint(start, stop)
    for i in range(1, attempts + 1):
            n = int(input(f'Попытка номер {i}, отгадайте число: '))
            if n > guess:
               turn = "Меньше"
            elif n < guess:
               turn = "Больше"
            else:
                 print ("Победа")
                 return True
            print(turn)
    else:
         return False


if __name__ == '__main__':
    _, *param = argv

    print(guess_game(*(int(i) for i in param))) 
