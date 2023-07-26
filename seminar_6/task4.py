# - Создайте модуль с функцией внутри.
# - Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# - Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# - 'Зимой и летом одним цветом',  ['ель', 'ёлка', 'сосна']
  
def game_02(riddle:str, answers:list, attempt=3):
    print(f'загадка: {riddle}\n ')
    for i in range(1, attempt + 1):
        var = input(f'Попытка {i}. Введите ответ: ')
        if var in answers:
            print('Правильно! ')
            return i
    return 0

if __name__ == '__main__':
    print(game_02('Зимой и летом одним цветом',  ['ель', 'ёлка', 'сосна']))
'''   

def guess(text:str, answers:list[str], count=3) -> int:
    for i in range(count):
        game_answer = input(f' {text}: ').lower()
        if game_answer in answers:
            print('Правильно! ')
            return i+1
    return 0

if __name__ == '__main__':
    print(guess('Зимой и летом одним цветом',  ['ель', 'ёлка', 'сосна'], 3))
      

'''