'''
Задача №2:
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
'''

string_user = "Напишите преобразование в одну строку"
res_dict = {key: ord(key) for key in string_user}
res = {}
for key in string_user:
    res[key] = ord(key)

print(res_dict)
print(res)