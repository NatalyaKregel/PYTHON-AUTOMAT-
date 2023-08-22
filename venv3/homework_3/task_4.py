'''
Задача 4.
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''

from itertools import permutations

def get_perm(items:dict) -> list:
    list_permutations = list()
    for n in range(len(items) + 1):
        list_permutations += list(permutations(items.items(), n))
    return list_permutations


def get_load_options(list_permutations: list) -> set:
    result = set()
    for perm in list_permutations:
        step_res = []
        weight = 0
        for item in perm:
            if weight + item[1] <= capacity:
                weight += item[1]
                step_res.append(item[0])
            else:
                break        
        if weight > 0:
            step_res.sort()
            tuple_res = tuple(step_res)
            weight = round(weight, 1)
            result.add((tuple_res, weight))
    return result


def sort_options(options: set) -> list:
    return sorted(options, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    items = {'сок': 1, 'хлеб': 1, 'овощи': 2, 'бутерброды': 3, 'рыба': 3, 'фрукты': 3, 'грибы': 4, 'шашлык': 4}
    capacity = float(input("Введите грузоподъемность рюкзака: "))

    options = sort_options(get_load_options(get_perm(items)))
    for option in options:
        print(f'Вариант загрузки рюкзака: {option[0]}, общий вес: {option[1]: .1f}')
    