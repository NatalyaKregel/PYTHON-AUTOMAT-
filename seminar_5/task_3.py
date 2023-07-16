'''
Задача №3:
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
'''

string_user = "Напишите преобразование в одну строку"
res_dict = {key: ord(key) for key in string_user}
print(res_dict.items())
my_iter = iter(res_dict.items())
for i in range(5):
    print(next(my_iter))