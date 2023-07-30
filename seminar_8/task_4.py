'''Задание №4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора. Получившиеся записи сохраните в json файл, 
где каждая строка csv файла представлена как отдельный json словарь. 
Имя исходного и конечного файлов передавайте как аргументы функции.
'''

import json
import csv
from pathlib import Path

def csv_to_json(csv_file, json_file):
    with (open(csv_file, 'r', encoding='utf-8') as csv_f,
         open(json_file, 'r', encoding='utf-8', newline="") as json_f):
        file = list(csv.reader(csv_f, dialect='excel'))
    
    lst = []
    for i, line in enumerate(file):
        if i == 0:
           headers_name, headers_id, headers_level = file[0]
        else:
            level, id_cod, name = line        
            lst.append({headers_id: id.zfill(10), headers_name: name.title, headers_level: level, 'hash': hash(name+id_cod)})
            json.dump(lst, json_f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    csv_to_json('test_bd.csv', 'test_bd.json')