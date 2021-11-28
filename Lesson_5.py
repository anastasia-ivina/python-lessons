# Задание 1, 2.
with open("text.txt", "w+", encoding="utf-8") as first_file:
    text = print('Для выхода нажмите Enter.')
    while True:
        text = input('Enter some text: ')
        first_file.write(f"{text}\n")
        if not text:
            break
    first_file.seek(0)
    print(first_file.read(), end='')
    first_file.seek(0)
    content = first_file.readlines()
    num_lines = len([line for line in content if line.split()])
    num_words = {line: len(word.split()) for line, word in zip(range(1, num_lines + 1), content)}
    print("Количество строк:", num_lines)
    print("Количество слов в каждой строке:", num_words)


# Задание 3.
with open("text_3.txt", "r+", encoding="utf-8") as file_3:
    lines = file_3.readlines()
    new_list = [el.split() for el in lines]
    surn_list = [new_list[ind][0] for ind in range(len(new_list)) if float(new_list[ind][1]) < 20000.0]
    print(f"Сотрудники с з/п менее 20 тыс.руб: {surn_list}")
    sal_list = [float(new_list[ind][1]) for ind in range(len(new_list))]
    from functools import reduce
    def new_func(el_1, el_2):
        return el_1 + el_2
    print(f"Средняя величина дохода сотрудников: {reduce(new_func, sal_list) / len(sal_list)} тыс.руб.")


# Задание 4.
from translate import Translator
file_translate = Translator(from_lang="english", to_lang="russian")
with open("text_4.txt", "r", encoding="utf-8") as file_4:
    lines = []
    for line in file_4:
        lines.append(file_translate.translate(line))
    print(lines)
with open("text_4_1.txt", "w+", encoding="utf-8") as file_4_1:
   for el in lines:
       file_4_1.write(f"{el}\n")


# Задание 5.
with open("number.txt", "w+", encoding="utf-8") as number_file:
    from random import randrange
    from functools import reduce
    my_list = []
    for n in range(10):
        my_list.append(randrange(4, 40, 4))
    print(my_list)
    def new_funct(el_1, el_2):
        return el_1 + el_2
    print(f"Сумма всех чисел: {reduce(new_funct, my_list)}.")
    number_file.write(f"Сумма всех чисел: {reduce(new_funct, my_list)}.\n")
    my_list = map(str, my_list)
    list_el = [el for el in my_list]
    n = ' '.join(list_el)
    number_file.write(f"Набор чисел: {n}")


# Задание 6.
with open("text_6.txt", "r", encoding="utf-8") as file_6:
    lines = file_6.readlines()
    new_list = [el.split() for el in lines]
    lesson_list = [new_list[ind][0] for ind in range(len(new_list))]
    hours_list = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            a = [new_list[i][j] for j in range(len(new_list[i])) if new_list[i][j].endswith(')')]
        hours_list.extend([a])

    for i in range(len(hours_list)):
        for j in range(len(hours_list[i])):
            b = [(hours_list[i][j]).replace('(пр)', '') for j in range(len(hours_list[i]))]
        c.extend([b])

    for i in range(len(c)):
        for j in range(len(c[i])):
            b = [(c[i][j]).replace('(л)', '') for j in range(len(c[i]))]
        d.extend([b])

    for i in range(len(d)):
        for j in range(len(d[i])):
            b = [int((d[i][j]).replace('(лаб)', '')) for j in range(len(d[i]))]
        e.extend([b])

    for i in range(len(e)):
        f.append(sum(e[i]))

    sched_dict = {lesson: hours for lesson, hours in zip(lesson_list, f)}
    print(sched_dict)

# Задание 7.
with open("text_7.txt", "r", encoding="utf-8") as file_7:
    from translate import Translator
    from functools import reduce
    file_translate = Translator(from_lang="english", to_lang="russian")
    firms = file_7.readlines()
    firms_list = [el.split() for el in firms]
    profit_list = [firms_list[ind][2:] for ind in range(len(firms_list))]
    name_list = [file_translate.translate(firms_list[ind][0]) for ind in range(len(firms_list))]
    div_list = [(int(profit_list[ind][0]) - int(profit_list[ind][1])) for ind in range(len(profit_list))]
    aver_profit = [el for el in div_list if el > 0]
    def new_funct(el_1, el_2):
        return el_1 + el_2
    final_list = [{firm: income for firm, income in zip(name_list, div_list)},{file_translate.translate('average_profit'): (reduce(new_funct, aver_profit) / 4) }]
    print(final_list)
import json
with open("my_file.json", "w") as write_f:
    json.dump(final_list, write_f)