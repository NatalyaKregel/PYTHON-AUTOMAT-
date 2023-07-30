'''
Задание №5
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое 
в виде одноимённых pickle файлов.
'''

import json
import os
import pickle
from pathlib import Path

def json_pickle(file_folder):
    for i in os.listdir(file_folder):
        if i.endswith(".json"):
            with (open(i.replace(".json", ".pickle"), "wb") as f_pickle,
                  open(i) as f_json):               
                pickle.dump(f_json.read(), f_pickle)


if__name__ == '__main__':
    json_pickle(Path.cwd("C:/Пользователи/new_dir/"))