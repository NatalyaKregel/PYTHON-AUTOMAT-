#Напишите программу, которая вычисляет площадь
#круга и длину окружности по введённому диаметру.
#✔ Диаметр не превышает 1000 у.е.
#✔ Точность вычислений должна составлять
#не менее 42 знаков после запятой.


from decimal import Decimal, getcontext
from math import pi

getcontext().prec = 42
num_pi = Decimal(pi)

diametr: Decimal = 0
while diametr not in range(1,1001):
    diametr = Decimal(input('Введите диаметр от 1 до 1000:\n'))

area: Decimal = (num_pi * diametr ** 2 / 4)
length: Decimal = (num_pi * diametr)

print(f'площадь  = {area}')
print(f'длина = {length}')