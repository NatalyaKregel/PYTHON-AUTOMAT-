'''
Задача 1.
Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
'''

def switch_action():
    action = input("Введите действие:\n"
                   "1 - добавить друга и его вещи;\n"
                   "2 - показать словарь;\n"
                   "3 - выход.\n")
    return action


def add_friend(friends_dict=dict()):
    friend, *things = input("Введите имя друга и его вещи через пробел: ").split()
    if friend not in friends_dict.keys():
        friends_dict[friend] = tuple(things)
    return friends_dict


action = switch_action()
while action != "3":
    if action == "1":
        friends_dict = add_friend()
    elif action == "2":
        print(friends_dict)
    elif action != 3:
        print("Введите корректное действие: ")
    action = switch_action()