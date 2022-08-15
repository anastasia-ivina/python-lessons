# Задача 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

list_ = [random.randint(1, 20) for i in range(11)]
print(list_)
max_ = list_[0]
min_ = list_[1]
for ele in list_:
    if ele > max_:
        max_ = ele
    elif ele < min_:
        min_ = ele
list_[list_.index(max_)] = min_
list_[list_.index(min_)] = max_
print(f'Максимальный элемент: {max_}.   Минимальный элемент: {min_}.\n{list_}')


