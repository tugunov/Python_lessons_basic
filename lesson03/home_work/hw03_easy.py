# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_len(str_in): 
# так как нельзя использовать встроенные функции, то пишем свою len()
	l = 0
	for i in str_in:
		l += 1
	return l

# вообще говоря, функции явного преобразования типа - тоже встроенные
# но как обойтись без них - непонятно
def my_round(number, ndigits):
    snum = str(number)
    ppos = snum.find('.')
    sres = ''
    
    if int(snum[ppos+ndigits+1]) in (0, 1, 2, 3, 4): # без range
        # округление в меньшую сторону
        sres = snum[:ppos+ndigits+1] # просто обрезаем все, что справа
    else: # округление в большую сторону
        # прибавляем единицу к дробной части
        r_part = str(int(snum[ppos+1:ppos+ndigits+1]) + 1)

        if my_len(r_part) == ndigits:
            sres = snum[:ppos+1] + r_part
        else:
            sres = snum[:ppos-1] + str(int(snum[ppos-1])+1) + '.' + r_part[1:]
    
    # здесь у sres нужно обрезать незначащие нули 
    # (возможно, и всю дробную часть)
    cnt = 0
    for i in sres[::-1]:
        if i != '0':
            break
        else:
            cnt += 1
    sres = sres[:my_len(sres)-cnt]
    
    if sres[-1] == '.':
        sres = sres[:my_len(sres)-1]


    return sres

print(my_round(2.1234567, 3))
print(my_round(2.1999967, 4))
print(my_round(2.9999967, 4))
print(my_round(2.999996745, 7))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

# Функция принимает на вход номер билета
# На выход выдает строковое сообщение:
# Счастливый/Несчастливый/Сообщение о превышении длины номера билета	

    tkt_str = str(ticket_number)
    if len(tkt_str) > 6:
    	return 'Номер билета должен быть не длиннее шести знаков!' 
    # Если номер не превышает шести символов - дополним его до формата
    tkt_str = '0'*(6-len(tkt_str)) + tkt_str
    left_part = 0
    right_part = 0

    for i in range(0, 3): # суммируем цифры левой и правой части
        left_part += int(tkt_str[i])
        right_part += int(tkt_str[i+3])
    if left_part == right_part:
    	return 'Счастливый билет!'
    else:
    	return 'Несчастливый билет.'


# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
# print(lucky_ticket(43675144))
