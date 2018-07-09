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
	for item in iter:
		if func(item) == True:
			output.append(item)
	return output

# a = (1, 2, 3, 4, 5, 6)

# f_obj = filter(lambda x : x % 2 == 0, a)
# num_list = list(f_obj)
# print(num_list)
# print(my_filter(lambda x : x % 2 == 0, a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# предлагаю решить задачу по признаку параллелограма: если диагонали
# четырехугольника при пересечении делятся пополам - это параллелограм

def pp_line(p1, p2): # уравнение линии по двум точкам
	# на вход координаты двух точек в виде кортежей (p1 = (x1, y1))
	# на выход выдается кортеж коэффициентов (A, B, C) Ax + By + C = 0
	A = p1[1] - p2[1]
	B = p2[0] - p1[0]
	C = p1[0]*p2[1] - p2[0]*p1[1]
	return (A, B, C)
	

def line_x(coef1, coef2): # координаты пересечения двух прямых по коэффициентам
	# на вход кортежи из коэффициентов двух прямых (A, B, C)
	# на выходе точка пересечения (если она есть)
	import numpy as np
	# решение СЛАУ с помощью библиотеки numpy
	a = np.array([[coef1[0], coef1[1]], [coef2[0], coef2[1]]])
	b = np.array([(-1)*coef1[2], (-1)*coef2[2]])

	x = np.linalg.solve(a, b)
	# return x[0], x[1]
	return x

def pp_mid(p1, p2): 
	# возвращает координаты середины отрезка по координатам концов отрезка
	return (p1[0] + p2[0])/2, (p1[1] + p2[1])/2
	

def is_pgram(p_list):
	pass

p1 = (0, 0)
p2 = (0, 4)
p3 = (6, 4)
p4 = (6, 0)
eq1 = pp_line(p1, p4)
eq2 = pp_line(p2, p3)
print(eq1)
print(eq2)
print(line_x(eq1, eq2))
print(pp_mid(p1, p3))
print(pp_mid(p2, p4))

# p_list = [(1, 1), (1, 5), (6, 5), (6, 1)]
# print(l_intersect(pp_line(p_list[0], p_list[2]),
# 	pp_line(p_list[1], p_list[3])))



