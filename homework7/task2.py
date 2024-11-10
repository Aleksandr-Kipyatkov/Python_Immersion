# 2. Напишите функцию группового переименования файлов. Она должна:

# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


__all__ = ['file_group_rename']

from pathlib import Path


def file_group_rename(file_name: str = '', 
                      num_of_dig: int = 1, 
                      orig_ext: str = '', 
                      new_ext: str = None, 
                      range_of_symb: tuple[int, int] = (3, 6)):
    """
    :param file_name: желаемое конечное имя файлов
    :param num_of_dig: количество цифр в порядковом номере
    :param orig_ext: расширение исходного файла
    :param new_ext: расширение конечного файла. Если не передано, то оригинальное расширение
    :param range_of_symb: диапазон сохраняемого оригинального имени
    :return: new file name
    """
    
    count = 0
    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj.is_file():
            name, ext = obj.stem, obj.suffix[1:]
            if ext == orig_ext:
                if new_ext is None:
                    new_ext = orig_ext
                count += 1
                new_name = name[range_of_symb[0]:range_of_symb[1]] + file_name + f'{count:0>{num_of_dig}}.' + new_ext
                obj.rename(new_name)
                print(f'{obj} renamed to {new_name}')


if __name__ == '__main__':
    file_group_rename('exersize', 2, 'py', 'pyt')

