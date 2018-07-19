# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копирование файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - переход в указанную директорию")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    print(file_path)

    try:
        if file_name.find('.') != -1: # если файл с расширением
            copy_path = file_name.replace('.', '_copy.')
        else:
            copy_path = file_name + '_copy'
        # копирование без shutil    
        scriptf = open(file_path, 'r', encoding='UTF-8')
        copyf = open(copy_path, 'w', encoding='UTF-8')

        for line in scriptf.readlines():
            copyf.write(line)
        
        scriptf.close()
        copyf.close()
        print('Файл успешно скопирован.')
    except Exception:
        print('Копия файла {} не может быть создана'.format(file_name))


def remove_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    print(file_path)

    if input('Удалить файл {} ? (y/n)'.format(file_name)) == 'y':
        try:
            os.remove(file_path)
            print('Файл успешно удален.')
        except FileNotFoundError:
            print('Файла {} не существует'.format(file_name))
    else:
        return

def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return

    if os.path.isabs(dir_name): # если путь абсолютный - просто его используем
        dir_path = dir_name
    else:
        print('Текущий ', os.getcwd()) # иначе составляем абс. путь для перехода
        dir_path = os.path.join(os.getcwd(), dir_name)
        print('Целевой ', dir_path)

    try:
        os.chdir(dir_path)
        print('Осуществлен переход в {}'.format(dir_path))
    except Exception:
        print('Невозможно перейти в указанную директорию, текущая ', os.getcwd())
   

def list_dir():
    dir_path = os.path.join(os.getcwd())
    print(os.path.abspath(dir_path))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": list_dir

}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
