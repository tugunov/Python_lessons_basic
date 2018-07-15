# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys

def make_dir():
    # функция требует импорта модуля os
    for n in '0123456789':
        dir_path = os.path.join(os.getcwd(), 'dir_' + n)
        try:
            os.mkdir(dir_path)
            print('Директория dir_{} создана.'.format(n))
        except FileExistsError:
            print('Директория {} уже существует.'.format(dir_path))

def del_dir():
    # функция требует импорта модуля os
    for n in '0123456789':
        dir_path = os.path.join(os.getcwd(), 'dir_' + n)
        try:
            os.rmdir(dir_path)
            print('Директория dir_{} удалена.'.format(n))
        except PermissionError:
            print('Директория на удаление не пустая.')


# make_dir()

# del_dir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    # функция требует импорта модулей os и sys
    print('Список папок в текущей директории:')
    for el in os.listdir('.'):
        list_item = os.path.join(os.getcwd(), el)
        if os.path.isdir(list_item):
            print(el)

# make_dir()
# list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    # функция требует импорта модуля os
    scriptpath = os.path.join(os.getcwd(), sys.argv[0])
    copypath = os.path.join(os.getcwd(), sys.argv[0].replace('.py', '_copy.py'))
    scriptf = open(scriptpath, 'r', encoding='UTF-8')
    copyf = open(copypath, 'w', encoding='UTF-8')

    for line in scriptf.readlines():
        copyf.write(line)
    
    scriptf.close()
    copyf.close()

# copy_file()
