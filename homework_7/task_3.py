'''Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''
from os import chdir
from pathlib import Path


def sort_file(path: Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)

    if groups is None:
        groups = {
            Path('video'): ['avi','mkdir'],
            Path('image'): ['jpg','png'],
            Path('text'): ['txt','doc'],
        }

    reverse_groups = {}

    for target_dir, extension_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for extension in extension_list:
            reverse_groups[f'.{extension}'] = target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups.keys():
            file.replace(reverse_groups[file.suffix] / file.name)
            

if __name__ == '__main__':
    sort_file(Path('C:/Пользователи/new_dir/'))                 