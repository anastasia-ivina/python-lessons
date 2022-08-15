# Задача 8.
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
M = 5
N = 4
a = []
for i in range(N):
    b = []
    summa = 0
    print(f'{i}-я строка: ')
    for j in range(M - 1):
        n = int(input())
        summa += n
        b.append(n)
    b.append(summa)
    a.append(b)

for line in a:
    for item in line:
       print(f'{item:>4}', end='')
    print()
