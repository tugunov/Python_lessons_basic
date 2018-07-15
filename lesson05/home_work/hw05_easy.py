# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir():
    import os
    for n in '0123456789':
        dir_path = os.path.join(os.getcwd(), 'dir_' + n)
        try:
            os.mkdir(dir_path)
            print('Директория dir_{} создана.'.format(n))
        except FileExistsError:
            print('Директория {} уже существует.'.format(dir_path))

def del_dir():
    import os
    for n in '0123456789':
        dir_path = os.path.join(os.getcwd(), 'dir_' + n)
        try:
            os.rmdir(dir_path)
            print('Директория dir_{} удалена.'.format(n))
        except PermissionError:
            print('Директория на удаление не пустая.')


make_dir()

# del_dir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
