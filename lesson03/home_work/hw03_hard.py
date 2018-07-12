# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def make_part(lst, left, right):
	# на вход принимает номера диапазона нахождения слагаемой дроби в списке lst
	# возвращает кортеж из числителя и знаменателя сложной дроби
	part = []
	for i in range(left, right):
		
		if lst[i].find('/') != -1:
			part.append(int(lst[i].split('/')[0]))
			part.append(int(lst[i].split('/')[1]))
		else:
			part.append(int(lst[i]))

	if len(part) == 1:
		numerator = part[0]
		denominator = 1
	elif len(part) == 2:
		numerator = part[0]
		denominator = part[1]
	else:
		numerator = (part[0]/abs(part[0]))*(abs(part[0])*part[2] + part[1])
		denominator = part[2]
	
	return (numerator, denominator)

def sum_dec (string):
	# на вход - строка с выражением сложения или вычитания дробей
	# на выход - строка с упрощенным результатом
	s = string.split(' ')
	i = 0
	oper = 0
	for item in s:
		if (item == '+') | (item == '-'):
			oper = i
		i += 1

	if s[oper] == '+':
		znak = 1
	elif s[oper] == '-':
		znak = -1

	left = make_part(s, 0, oper)
	right = make_part(s, oper+1, len(s))

	num = int(left[0]*right[1] + znak*(left[1]*right[0]))
	den = int(left[1]*right[1])

	if abs(num) > den:
		a = int((abs(num) // den) * (abs(num)/num))
		b = abs(num) % den
		c = den

		return 'Результат: {} {}/{}'.format(str(a), str(b), str(c))
	else:
		return 'Результат: {}/{}'.format(str(num), str(den))

s1 = '5/6 + 4/7'
print(s1)
print(sum_dec(s1))
s2 = '-2/3 - -2'
print(s2)
print(sum_dec(s2))



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

p_workers = os.path.join('data','workers')
p_hours = os.path.join('data','hours_of')

f_w = open(p_workers, 'r', encoding='UTF-8')
f_h = open(p_hours, 'r', encoding='UTF-8')

w_string = f_w.readlines() #читаем данные  в списки
h_string = f_h.readlines()

f_w.close()
f_h.close()

w_table = [] # для хранения и работы с таблицами данных
h_table = []
res_table = []

for line in w_string: # преобразовываем списки в двумерные списки-таблицы
	s = line.replace('\n', '')
	s = s.split(' ')
	s = list(filter(lambda x: x!='', s))
	w_table.append(s)

for line in h_string:
	s = line.replace('\n', '')
	s = s.split(' ')
	s = list(filter(lambda x: x!='', s))
	h_table.append(s)

w_table.pop(0) # удаляем заголовки в таблицах
h_table.pop(0)

print(w_table)
print(h_table)

for line in w_table:
	name = line[0]
	surname = line[1]
	salary = float(line[2])
	norm_hours = int(line[4])
	for h_line in h_table:
		if (h_line[0] == name) & (h_line[1] == surname):
			fact_hours = int(h_line[2])

	if fact_hours <= norm_hours:
		salary = salary * (fact_hours/norm_hours)
	else:
		salary = salary * (1 + (fact_hours - norm_hours) / norm_hours)

	res_table.append([name, surname, str(round(salary, 2))])

	# print('{} {} {}'.format(name, surname, round(salary, 2)))

# красивый вывод на печать данных о фактической зарплате
name_max = 0
surname_max = 0
salary_max = 0

for line in res_table:
	if len(line[0])>name_max:
		name_max = len(line[0])
	if len(line[1])>surname_max:
		surname_max = len(line[1])
	if len(line[2])>salary_max:
		salary_max = len(line[2])

for line in res_table:
	print('{}{} {}{} {}'.format(line[0], ' '*(name_max - len(line[0])),
		line[1], ' '*(surname_max - len(line[1])), line[2]))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

path = os.path.join('data','fruits.txt')
f = open(path, 'r', encoding='UTF-8')
fruits = f.readlines() # список фруктов с символами перевода строки
f.close()

fruits = list(filter(lambda x: x != '\n', fruits)) # без символов перевода строки

# сначала создаем пустые файлы только для существующих начальных букв из списка
for letter in list(map(chr, range(ord('А'), ord('Я')+1))): 
	for fruit in fruits:
		if letter in fruit[0]:
			name = 'fruits_' + letter
			newpath = os.path.join('data', name)
			f = open(newpath, 'w', encoding='UTF-8')
			f.close()

for fruit in fruits: # теперь записываем фрукты в файлы
	name = 'fruits_' + fruit[0]
	path = os.path.join('data', name)
	f = open(path, 'a', encoding='UTF-8') # открытие на дозапись
	f.write(fruit) # дозапись фрукта в файл
	f.close()



