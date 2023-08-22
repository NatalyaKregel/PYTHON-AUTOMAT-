#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from math import gcd                #функция gcd, вычисляет наибольший общий делитель двух чисел
from fractions import Fraction
import math

def parse_num(s):
    index = s.find('/')
    a = int(s[:index])
    b = int(s[index + 1:])
    return a, b


num1 = input("Введите первую дробь в формате 'a/b': ")
num2 = input("Введите вторую дробь в формате 'a/b': ")

#numerator - числитель
#denominator - знаменатель

numerator1, denominator1 = parse_num(num1)
numerator2, denominator2 = parse_num(num2)
print(f"Произведение дробей {num1}*{num2} = {numerator1 * numerator2}/{denominator1 * denominator2}")

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)
print(f"Через fraction = {fraction1 * fraction2}")

if denominator1 == denominator2:
    print(f"Сумма дробей {num1}+{num2} = {numerator1 + numerator2}/{denominator1}")
    print(f"Через fraction = {fraction1 + fraction2}")
else:
    cd = int(denominator1 * denominator2 / gcd(denominator1, denominator2))
    rn = int(cd / denominator1 * numerator1 + cd / denominator2 * numerator2)
    g2 = gcd(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print(f"Сумма дробей {num1}+{num2} = {n}/{d}")
    print(f"Через fraction = {fraction1 + fraction2}")
    