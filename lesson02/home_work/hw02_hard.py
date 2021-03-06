# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

print('==Задание-1==')
print('Вычислить значение линейной функции, заданной строкой вида y = kx + b, при заданном значении х')
equation = 'y = -12x + 11111140.2121'
x = 2.5

print(equation)
# уравнение представляет собой строку вида y = kx + b. 
# Получим k и b в численном виде

# нужно проверить, есть ли в строке свободный член b

# сохраним позиции разделителей для поиска подстрок, 
# содержащих коэффициенты. В кортеже
position = (equation.find('='), equation.find('x'))

# в подстроках удаляются все пробелы после чего производится 
# преобразование в вещественный тип
k = float(equation[position[0]+1:position[1]].replace(' ', ''))
b = float(equation[position[1]+1:].replace(' ', '')) # знак числа b при таком преобразовании сохраняется правильно

y = k*x + b
print('y = {}'.format(y))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

print('==Задание-2==')
print('Дата задана в виде строки формата dd.mm.yyyy. Проверить, корректно ли введена дата')

days_in_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) # кортеж с количеством дней в каждом месяце
year_limit = range(1, 9999+1) # диапазон для года по условию задачи
month_limit = range(1, 12+1) # диапазон для календарного месяца

status = ''
while (status != 'q'):
    date = input('Введите число в формате dd.mm.yyyy: ')
    if (len(date) == 10) & (date[2] == '.') & (date[5] == '.'): # проверка шаблона: длина и позиции точек
        if int(date[6:]) in year_limit: # проверка конвертации и значения года
            if int(date[3:5]) in month_limit: # проверка конвертации и значения месяца
                if int(date[0:2]) in range(1, days_in_month[int(date[3:5])-1]+1): # проверка дня в связи с месяцем
                    print('Дата введена корректно!') # успешная ветка
                else:
                    print('Некорректный ввод номера дня.')
            else:
                print('Некорректный ввод номера месяца.')
        else:
            print('Некорректный ввод года')
    else:
        print('Некорректная длина полей или расстановка точек')

    status = input('Повторить ввод (y) или завершить работу (q)? (y/q):')



# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

print('==Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)==')
print('Вывести по номеру комнаты номер этажа и порядковый номер слева на этаже')

# башню можно представить в виде квадратов, поставленных друг на друга.
# Номер квадрата соответствует его собственной высоте в этажах и его ширине в комнатах.

sq = 1 # инициализируем номер квадрата
room_max = 0 # максимальный номер комнаты в квадрате
N = 2000000000 # порядковый номер комнаты для поиска

while room_max <= 2000000000: # поищем, в каком квадрате находится комната
    room_max = room_max + sq**2 # число комнат: 1**2 + 2**2 + 3**2 + ...
    if room_max > N: 
        # комната с указанным номером находится в sq-ом квадрате 
        # c максимальным номером комнаты room_max
        print('Номер квадрата: {}'.format(sq))
        print('Номер максимальной комнаты в квадрате: {}'.format(room_max))

        floor = 0
        # верхний этаж квадрата: 1 + 2 + 3 + ... sq раз
        for i in range(1, sq+1): 
            floor = floor + i
        print('Номер верхнего этажа квадрата: {}'.format(floor))

        # вычисляем сдвиг по этажам и по комнатам будет остатком и целым 
        # от деления номера комнаты на номер квадрата соответственно
        floor = floor - ((room_max - N) // sq) # номер этажа комнаты
        room_num = sq - ((room_max - N) % sq) # номер комнаты слева

        print ('Этаж: {} Номер комнаты слева: {}'.format(floor, room_num))
    sq += 1
