# Задание 1.
from sys import argv
name, work_hours, wage_rate, prize = argv
argv = list(map(int, argv[1:]))
salary = (argv[0] * argv[1]) + argv[2]
print(f"Выработка в часах: {work_hours}.")
print(f"Ставка в час: {wage_rate}.")
print(f"Премия: {prize}.")
print(f"Заработная плата: {salary}.")

# Задание 2.
my_list = [22, 78, 76, 1, 123, 654, 98, 12, 11, 10, 43]
new_list = [my_list[el] for el in range(len(my_list)) if my_list[el] > my_list[el - 1]]
print(new_list)

# Задание 3.
list_1 = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]
print(list_1)

# Задание 4.
numbers = [1, 1, 1, 2, 33, 44, 5, 6, 6, 12, 34, 55, 55, 68]
new_numbers = [n for n in numbers if numbers.count(n) == 1]
print(new_numbers)

# Задание 5.
from functools import reduce
list_3 = [x for x in range(100, 1001, 2)]
print(list_3)
def new_func(el_1, el_2):
    return el_1 * el_2
print(f"Произведение всех элементов списка: {reduce(new_func, list_3)}")

#  Задание 6.
from itertools import count
for i in count(4):
    if i < 21:
        print(i)
    else:
        break

from itertools import cycle
n = 0
for el in cycle(['cat', 'dog', 12, 4.6, ('cow', 'rose')]):
    if n > 20:
        break
    else:
        print(el)
        n += 1

# Задание 7.
def factorial():
    res = 1
    for i in {1, 2, 3, 4, 5, 6}:
        res *= i
        yield res
for el in factorial():
    print(el)