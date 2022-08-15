# Задача 7.
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random

array = [random.randint(1, 30) for i in range(20)]
print(array)
lst = list(set(array))
if array.count(lst[0]) > 1:
    print(f'Два наименьших элемента списка: {lst[0]}, {lst[0]}.')
else:
    print(f'Два наименьших элемента списка: {lst[0]}, {lst[1]}.')

