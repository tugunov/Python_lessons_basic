# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
# # -- СПОСОБ 1 --
# import re
# pattern1 = '([a-z]+)[A-Z]+'
# pattern2 = '[a-z]+$'
# found = re.findall(pattern1, line) + re.findall(pattern2, line)
# print(found)

# # -- СПОСОБ 2 --
# newline = ''
# sequences = []
# lower = list(map(chr, range(ord('a'), ord('z')+1)))

# print(lower)
# for i in line:
# 	if i in lower:
# 		newline += i
# 	else:
# 		if newline != '':
# 			sequences.append(newline)
# 		newline = ''

# if newline != '': #строка символов после последнего символа в верхнем регистре
# 	sequences.append(newline)

# print(sequences)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

line3 = 'mtASDFGHkFHddkfhgAFIt'

# # -- СПОСОБ 1 --
# import re
# pattern = '[a-z]{2,2}([A-Z]+)[A-Z]{2,2}'
# found = re.findall(pattern, line)
# print(found)

# # -- СПОСОБ 2 --
# symbols = []
# lo = list(map(chr, range(ord('a'), ord('z')+1)))
# up = list(map(chr, range(ord('A'), ord('Z')+1)))
# loline = ''
# upline = ''

# for i in line3:
# 	if i in lo:
# 		if len(loline)==2:
# 			# print(loline, upline)
# 			if len(upline)>=4:
# 				symbols.append(upline[:len(upline)-2])
# 				upline = ''
# 			loline = ''
			
# 		loline += i
# 		# print(loline)
# 	elif i in up:
#               # что-то еще
# 		upline += i
# 		print(upline)
	
# print(symbols)
def find_symbols(line):
    # на вход функция получает строку для поиска
    # на выход выдается список найденных соответственно условию подстрок
    symbols = []
    lo = list(map(chr, range(ord('a'), ord('z')+1)))
    up = list(map(chr, range(ord('A'), ord('Z')+1)))

    for i, el in enumerate(line):
        try:
            if (el in up) & (line[i+1] in lo) & (line[i+2] in lo):
                j = i + 3
                sequence = ''
                while(line[j] in up):
                    sequence += line[j]
                    j += 1
                if len(sequence)>=3:
                    symbols.append(sequence[:len(sequence)-2])
        except IndexError:
            return(symbols)

print(find_symbols(line_2))

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import os
import re

name = 'number'
newpath = os.path.join(name) # создаем файл в той же папке, где лежит код
f = open(newpath, 'w', encoding='UTF-8')
for i in range(0, 2500):
    f.write(str(random.randint(0, 10)))
f.close()

f = open(newpath, 'r', encoding='UTF-8')
pattern = '1{2,2500}|2{2,2500}|3{2,2500}|4{2,2500}|5{2,2500}|6{2,2500}|'\
'7{2,2500}|8{2,2500}|9{2,2500}|0{2,2500}'
found = re.findall(pattern, f.readline()) # все последовательности одинаковых цифр длиной 2 и более
f.close()

max_len = 0 # находим наибольшую длину последовательности
for el in found:
    if len(el)>max_len:
        max_len = len(el)
# самых длинных последовательностей может быть несколько
# соберем из них множество и преобразуем его в строку
result = ''
for item in (set(list(filter(lambda x: len(x)==max_len, found)))):
    result += item + ' '

print('Максимальная последовательность одинаковых цифр: {}'.format(result))