# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = [1, 1]
    for i in range(2, m): # строим ряд Фибоначчи до m-го элемента
    	fib.append(fib[i-1]+fib[i-2])
    return fib[n-1:m]

# print(fibonacci(5, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(0, len(origin_list)):
    	for j in range(len(origin_list)-1, i, -1):
    		if origin_list[j-1] > origin_list[j]:
    			x = origin_list[j-1]
    			origin_list[j-1] = origin_list[j]
    			origin_list[j] = x
    return origin_list

# print([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
# print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, iter):
	output = []
	for item in iter:
		if func(item) == True:
			output.append(item)
	return output 

a = (1, 2, 3, 4, 5, 6)

print(my_filter(lambda x : x % 2 == 0, a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# предлагаю решить задачу по определению параллелограмма - это
# четырехугольник, стороны которого попарно параллельны

def pp_line(p1, p2): # общее уравнение прямой по двум точкам
	# на вход координаты двух точек в виде кортежей (p1 = (x1, y1))
	# на выход выдается кортеж коэффициентов (A, B, C) Ax + By + C = 0
	A = p1[1] - p2[1]
	B = p2[0] - p1[0]
	C = p1[0]*p2[1] - p2[0]*p1[1]
	return (A, B, C)

def ll_par(coef1, coef2):
	# на вход кортежи из коэффициентов общих уравнений двух прямых (A, B, C)
	# на выход - True если прямые параллельны, False - если нет.
	# нужно обработать исключения, связанные с нулевыми A, B 
	if (coef1[0] == 0 & coef2[0] == 0) | (coef1[1] == 0 & coef2[1] == 0):
		return True # случай параллельности координатным осям
	elif coef1[0] == 0 | coef1[1] == 0: # нулевой коэффициент в уравнении 1
		return ((coef1[0]/coef2[0]) == (coef1[1]/coef2[1]))

	elif coef2[0] == 0 | coef2[1] == 0: # нулевой коэффициент в уравнении 2
		return((coef2[0]/coef1[0]) == (coef2[1]/coef1[1]))

		# предусмотрели все возможные деления на ноль
	else: # обработка случая ненулевых коэффициентов
		return((coef2[0]/coef1[0]) == (coef2[1]/coef1[1])) 

def is_pgram(p_list):
	# на вход - координаты точек p1, p2, p3, p4 списком четырех кортежей
	# на выход - True, если стороны попарно параллельны
	# False - иначе
	p1p2 = pp_line(p_list[0], p_list[1])
	p2p3 = pp_line(p_list[1], p_list[2])
	p3p4 = pp_line(p_list[2], p_list[3])
	p4p1 = pp_line(p_list[3], p_list[0])
	p1p3 = pp_line(p_list[0], p_list[2])
	p2p4 = pp_line(p_list[1], p_list[3])

	# возможно всего две комбинации условий попарной параллельности
	# для отрезков прямых через четыре точки на плоскости:

	return ((ll_par(p1p2, p3p4) & ll_par(p2p3, p4p1)) | 
			(ll_par(p1p2, p3p4) & ll_par(p1p3, p2p4)))


# p_rectangular = [(0, 0), (0, 4), (6, 4), (6, 0)] # тест на прямоугольник
# p_parallel = [(1, -1), (5, 5), (9, 4), (5, -2)] # тест на обычный пар-мм
# p_not = [(1, -1), (5, 5), (9, 4), (5, 0)] # не параллелограмм

# print(p_rectangular)
# print('Is parallelogram: ', is_pgram(p_rectangular))
# print(p_parallel)
# print('Is parallelogram: ', is_pgram(p_parallel))
# print(p_not)
# print('Is parallelogram: ', is_pgram(p_not))

