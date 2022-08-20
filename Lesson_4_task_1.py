# Задача 1.
# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
import cProfile
import timeit


def recursive_counter(number, even=0, odd=0):

    if number <= 0:
        return even, odd

    reduced_number, last_digit = divmod(number, 10)
    if last_digit % 2 == 0:
        return recursive_counter(reduced_number, even+1, odd)
    else:
        return recursive_counter(reduced_number, even, odd+1)

N = 123456789
even, odd = recursive_counter(N)
#print(f'В числе {N} есть {even} чётных цифр и {odd} нечётных.')

# python -m timeit -n 100 -s "import Lesson_4_task_1" "Lesson_4_task_1.recursive_counter(123456789)"
# 100 loops, best of 5: 7.13 usec per loop



def recursion(num):
    a = 0
    str1 = ''
    str2 = ''
    while num != 0:
        a = num % 10
        num = num // 10
        if (a % 2) == 0:
            str1 += str(a)
        else:
            str2 += str(a)
    return f'Количество четных цифр во введенном числе: {len(str1)}.\n' \
           f'Количество нечетных цифр во введенном числе: {len(str2)}.'

number = 654775376465
recursion(number)
# print(recursion(654775376465))

# python -m timeit -n 100 -s "import Lesson_4_task_1" "Lesson_4_task_1.recursion(654775376465)"
# 100 loops, best of 5: 5.89 usec per loop

# cProfile.run('recursive_counter(N)')
# 22 function calls (13 primitive calls) in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:8(recursive_counter)
#         9    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('recursion(number)')
# 6 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 Lesson_4_task_1.py:28(recursion)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ВЫВОД: функция recursion работает быстрее, алгоритм менее сложный.
