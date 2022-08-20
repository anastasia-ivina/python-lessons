# Задача 2.
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
import cProfile
import timeit


def eratosthenes(num):
    sieve = list(range(5000))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1[num-1]

# print(eratosthenes(7))
eratosthenes(12)
# python -m timeit -n 100 -s "import Lesson_4_task_2" "Lesson_4_task_2.eratosthenes(10)"
# 100 loops, best of 5: 1.69 msec per loop
# "Lesson_4_task_2.eratosthenes(100)"
# 100 loops, best of 5: 1.65 msec per loop
# "Lesson_4_task_2.eratosthenes(500)"
# 100 loops, best of 5: 1.52 msec per loop


def isitPrime(n):
    l = [2]
    for i in range(3, 5001, 2):

        if (i > 10) and (i % 10 == 5):
            continue
        for j in l:
            if j > int((i ** 0.5) + 1):
                l.append(i)
                break
            if (i % j == 0):
                break
        else:
            l.append(i)
    return l[n-1]

#print(isitPrime(14))
isitPrime(4)

# python -m timeit -n 100 -s "import Lesson_4_task_2" "Lesson_4_task_2.isitPrime(10)"
# 100 loops, best of 5: 8.67 msec per loop
# "Lesson_4_task_2.isitPrime(100)"
# 100 loops, best of 5: 8.82 msec per loop
# "Lesson_4_task_2.isitPrime(500)"
# 100 loops, best of 5: 8.82 msec per loop


# cProfile.run('eratosthenes(12)')
# 674 function calls in 0.002 seconds
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.001    0.001    0.002    0.002 Lesson_4_task_2.py:13(eratosthenes)
#         1    0.000    0.000    0.000    0.000 Lesson_4_task_2.py:20(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       669    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('isitPrime(40)')
# 672 function calls in 0.010 seconds
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.010    0.010    0.010    0.010 Lesson_4_task_2.py:33(isitPrime)
#         1    0.001    0.001    0.010    0.010 {built-in method builtins.exec}
#       668    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ВЫВОД: алгоритм на основе решета Эратосфена работает несколько быстрее,
# сложность алгоритмов приблизительно одинаковая.

