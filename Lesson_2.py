# Задание 1:
new_list = [22.5, 'coffee', 987, True, None, [3, 5]]
for el in new_list:
    print(type(el))


# Задание 2:
data = input('Введите произвольный набор чисел/символов/букв, не разделяя их: ')
my_list = list(data)
if (len(my_list)) % 2 == 0:
    change = [my_list[1::2]] + [my_list[0::2]]
    length_ch = len(my_list[1::2] + my_list[0::2])
    new_len = int(length_ch / 2)
    transposed = []
    for i in range(new_len):
        transposed_row = []
        for row in change:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(sum(transposed, []))
elif (len(my_list)) % 2 != 0:
    change = [my_list[1::2]] + [my_list[0::2]]
    length_ch = len(my_list[1::2] + my_list[0::2])
    new_len = int(length_ch / 2)
    transposed = []
    for i in range(new_len):
        transposed_row = []
        for row in change:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(f"{sum(transposed, []) + [my_list[-1]]}")



# Задание 3:
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
season_dict = {12: "зима", 1: "зима", 2: "зима",
               3: "весна", 4: "весна", 5: "весна",
               6: "лето", 7: "лето", 8: "лето",
               9: "осень", 10: "осень", 11: "осень"}
for key, value in (season_dict.items()):
    if month == key:
        print(f"Введенный Вами месяц относится к времени года: {value}.")
month_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
season_list = ["зима", "весна", "лето", "осень"]
for el in month_list:
    el = month
    if el == 12 or 0 < el <= 2:
         print(f"Введенный Вами месяц относится к времени года: {season_list[0]}.")
         break
    elif 2 < el < 6:
         print(f"Введенный Вами месяц относится к времени года: {season_list[1]}.")
         break
    elif 6 <= el <= 8:
         print(f"Введенный Вами месяц относится к времени года: {season_list[2]}.")
         break
    elif 8 < el <= 11:
         print(f"Введенный Вами месяц относится к времени года: {season_list[3]}.")
         break



# Задание 4:
str = input("Введите строку из нескольких слов, разделяя их пробелами: ")
str_list = str.split()
for ind, el in enumerate(str_list, 1):
    print(f"{ind}) {el[:10]}")



# Задание 5:
new_list = [9, 8, 7, 6, 6, 5, 5, 4]
print(f"Заданный рейтинг: {new_list}")
while len(new_list) <= 14:
    number = int(input("Введите новый элемент рейтинга (любое положительное натуральное число): "))
    for el in new_list:
        el = int(number)
        if el > new_list[0]:
            new_list.insert(0, number)
            print(new_list)
            break
        elif el < new_list[-1]:
            new_list.append(el)
            print(new_list)
            break
        elif not (el in new_list) and (el + 1) > el > (el - 1):
            new_list.insert((new_list.index(el + 1) + new_list.count(el + 1)), number)
            print(new_list)
            break
        elif not (el in new_list) and (el + 1) > el > (el - 1):
            new_list.insert((new_list.index(el - 1) - 1), number)
            print(new_list)
        elif el == number:
            new_list.insert((new_list.index(el) + new_list.count(el)), number)
            print(new_list)
            break
print(f"Получившийся рейтинг: {new_list}")