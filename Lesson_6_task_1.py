# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев
# в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.


# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

import sys

def inversion(num):
    s = ''
    while num != 0:
        s += str(num % 10)
        num = num // 10
    return s
b = inversion(int(input('Введите натуральное число: ')))
print(b)

# type = <class 'str'>, size = 53, object = 4321




number = input('Введите натуральное число: ')
l = [number]
lst = []
for i in range(len(number)):
    lst.append(number[-1])
    n = number.rstrip(number[-1])
    number = n
str_ = ''.join(lst)
print(str_)
l.extend([lst, str_])

# type = <class 'list'>, size = 120, object = ['1234', ['4', '3', '2', '1'], '4321']
# 	 type = <class 'str'>, size = 53, object = 1234
# 	 type = <class 'list'>, size = 88, object = ['4', '3', '2', '1']
# 		 type = <class 'str'>, size = 50, object = 4
# 		 type = <class 'str'>, size = 50, object = 3
# 		 type = <class 'str'>, size = 50, object = 2
# 		 type = <class 'str'>, size = 50, object = 1
# 	 type = <class 'str'>, size = 53, object = 4321



num = input('Введите натуральное число: ')
ls = list(num)
ls.reverse()
ss = ''.join(ls)
print(ss)
l_1 = [num, ls, ss]

# type = <class 'list'>, size = 80, object = ['1234', ['4', '3', '2', '1'], '4321']
# 	 type = <class 'str'>, size = 53, object = 1234
# 	 type = <class 'list'>, size = 88, object = ['4', '3', '2', '1']
# 		 type = <class 'str'>, size = 50, object = 4
# 		 type = <class 'str'>, size = 50, object = 3
# 		 type = <class 'str'>, size = 50, object = 2
# 		 type = <class 'str'>, size = 50, object = 1
# 	 type = <class 'str'>, size = 53, object = 4321



# Версия и разрядность ОС и интерпретатора Python:
# 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] win32


def size(x, level=0):
    print('\t'*level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                size(xx, level+1)
        elif not isinstance(x, str):
            for xx in x:
                size(xx, level+1)

size(l)
size(b)
size(l_1)

# ВЫВОД: лучший код первый, так как используется меньше всего памяти.
