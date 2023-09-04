'''
Задача 6
На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
Напишите 3-7 тестов pytest для данного проекта. Исользуйте фикстуры.
'''

from task_01_basic import UserData, data_from_json
from task_01_basic_users import Project

import pytest
import json
import os

JSON_FILE = 'task04.json'
@pytest.fixture
def setup():
    data = {
           1: {101: 'John'},
           3: {102: 'Vasya'},
           6: {103: 'Petya'}
            }
    return data

def test_write_json():
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(setup, f)
    assert os.path.exists(JSON_FILE)

def test_load_json():
    JSON_FILE = 'task04.json'
    test_result = data_from_json(JSON_FILE)
    assert setup == test_result

def test_add_user():
    test_project = Project()
    test_project.load_json(JSON_FILE)
    test_dict = test_project.enter('Kolya', 104)
    assert setup == test_dict

#что пользователь не добавляется
def test_not_add_user():
    test_project = Project()
    test_project.load_json(JSON_FILE)
    test_dict = test_project.enter('John', 101)
    assert setup != test_dict


if __name__ == '__main__':
    pytest.main(['-vv'])
