# Задача 1.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import deque
N = int(input("Количество предприятий: "))
companies = {}

for i in range(N):
    companies[input(f'Название {i+1}-го предприятия предприятия: ')] = float(input(f'Прибыль за 4 квартала '
                                                                                   f'{i+1}-го предприятия: '))
print(companies)
t = list(companies.values())
mean_profit = sum(t) / N
upper_mean = deque()
lower_mean = deque()
for k, v in companies.items():
    if v > mean_profit:
        upper_mean.append(k)
    elif v < mean_profit:
        lower_mean.append(k)


print(f'Средняя прибыль для всех компаний составила: {round(mean_profit, 2)}')
print(f'Прибыль выше среднего у {len(upper_mean)} компаний: ')
for name in upper_mean:
    print(name)
print(f'Прибыль ниже среднего у {len(lower_mean)} компаний: ')
for name in lower_mean:
    print(name)
