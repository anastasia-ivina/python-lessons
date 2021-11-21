# Задание 1.
def my_fun(arg_1, arg_2):
    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        division = arg_1 / arg_2
    except (ValueError, ZeroDivisionError) as err:
        print(err)
    else:
        division = arg_1 / arg_2
        return division
print(f"Результат деления: {my_fun((input('Введите делимое: ')), (input('Введите делитель: ')))}")


# Задание 2.
print((lambda **kwargs: kwargs)(имя=(input("Имя: ")), фамилия=(input("Фамилия: ")), год_рождения=(input(("Год рождения: "))),
               город_проживания=(input("Город проживания: ")), email=(input("Email: ")), телефон=(input("Номер телефона: "))))

# Задание 3.
def my_func(arg_1, arg_2, arg_3):
    global div
    my_list = [arg_1, arg_2, arg_3]
    min_ = min(my_list)
    div = sum(my_list) - min_
    return div
my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')))
print(f"Сумма двух наибольших: {div}")

# Задание 4.
def my__func(x, y):
    global exp
    exp = abs(x) ** (-y)
    return exp
my__func(float(input('Введите действительное положительное число x: ')), int(input('Введите целое число y: ')))
print(f"Число х в степени (-у): {exp}.")
def my__func(x, y):
    global exp
    exp = 1 / abs(x)
    for i in range(1, y):
        exp *= (1 / abs(x))
        i += 1
    return exp
my__func(float(input('Введите действительное положительное число x: ')), int(input('Введите целое число y: ')))
print(f"Число х в степени (-у): {exp}.")


# Задание 6, 7.
def int_func():
    string = (input("Введите слова из латинских букв, разделенные пробелами: ")).lower()
    return string
print(int_func().capitalize())
print(int_func().title())


# Задание 5.
print('Для выхода нажмите "q".')
def new_func(*args):
    global int_func
    my_list = list(map(int, *args))
    print(f"Сумма: {sum(my_list)}.")
    def int_func(*args):
        new_list = list(*args)
        try:
            for el in (new_list):
                if el == "q":
                    new_list.remove("q")
                    my_list.extend(map(int, new_list))
                    print(f"Сумма: {sum(my_list)}.")
                    exit()
            new_list = list(map(int, *args))
            my_list.extend(new_list)
        except ValueError as err:
            print(f"Сумма: {sum(my_list)}.")
            print(err)
        return print(f"Сумма: {sum(my_list)}.")
    return int_func

new_func((input('Введите числа, разделенные пробелами: ')).split())
while True:
    int_func((input('Введите числа, разделенные пробелами: ')).split())
    continue

