'''
Задание №1
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
Обрабатывайте не числовые данные как исключения.
'''

def get(text: str = None) -> int:
    while True:
        data = input(text)
        try:
            num = float(data)
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
    return num


if __name__ == '__main__':
    number = get('Введите число: ')
    print(number)

