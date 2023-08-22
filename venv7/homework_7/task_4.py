'''
ЗАДАЧА №4:
Напишите функцию группового переименования файлов. Она должна:
* -- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* -- принимать параметр количество цифр в порядковом номере.
* -- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* -- принимать параметр расширение конечного файла.
* -- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''


from pathlib import Path

__all__ = [
    'group_rename_files',
]


def group_rename_files(directory: Path, name_for_files: str, amount_digit: int, old_file_extension: str,
                       new_file_extension: str, range_of_letters: list[int]) -> None:
    for i, file in enumerate(directory.glob(f'*.{old_file_extension}'), start=1):
        file_name_, _ = file.name.split('.')
        start = min(range_of_letters[0], len(file_name_))
        stop = min(range_of_letters[1], len(file_name_))
        file_name = file_name_[start:stop]
        new_file_name = f'{file_name}{name_for_files}{i:0{amount_digit}}.{new_file_extension}'

        file.rename(file.parent / new_file_name)

    if __name__ == '__main__':
        group_rename_files(Path('files'), name_for_files='_test_', amount_digit=3, old_file_extension='bin',
                           new_file_extension='txt', range_of_letters=[2, 6])