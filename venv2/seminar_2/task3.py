#Задание №3
#✔ Напишите программу, которая получает целое число и возвращает
#его двоичное, восьмеричное строковое представление.
#✔ Функции bin и oct используйте для проверки своего
#результата, а не для решения.
#Дополнительно:
#✔ Попробуйте избежать дублирования кода
#в преобразованиях к разным системам счисления
#✔ Избегайте магических чисел
#✔ Добавьте аннотацию типов где это возможно

BINARY_SYSTEM = 2
OCTAL_SYSTEM = 8

number: int = int(input('\nВведите число: '))

def system_selection() -> int:
    system: int = 0
    while system != BINARY_SYSTEM and system != OCTAL_SYSTEM:
        system = int(input('\nВыберите систему счисления\n'
                           '\n2 - двоичная система счисления' 
                           '\n8 - восьмеричная система счисления'))
    return system

def transfer_to_the_system(number: int, system: int) -> str:
    result: str = ''

    while number != 0:
        mod: str = str(number % system)
        result = mod + result
        number //= system
    return result

selection: int = system_selection()
transfer: str = transfer_to_the_system(number, selection)

print(f'\nРезультат: {transfer}')

print(f'\nЧисло в двоичной системе счисления: {bin(number)[2:]}') #2: обрезает первые 2 цифры

print(f'\nЧисло в восьмеричной системе счисления: {oct(number)[2:]}')
