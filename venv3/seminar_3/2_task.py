# ------------------------------------------- 2 -----------------------------
# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте
# если возможно в один из вариантов ниже:
#     целое положительное число
#     вещественное положительное или отрицательное число
#     строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
#     строку в верхнем регистре в остальных случаях

data = input('Введите данные: ')

if data.isdecimal():
    result = int(data)
elif data.replace('.', '', 1).isdecimal():
    result = float(data)
elif data[0] == "-" and data.replace('-', '', 1).replace('.', '', 1).isdecimal():
    result = float(data)
elif data != data.lower():
    result = data.lower()
else:
    result = data.upper()

print(f'{result = }')

