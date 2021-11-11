# Lesson_1

# Задание 1:
name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
password = int(input("Введите пароль: "))
print(f"Добрый день, {name} {surname}. Вы ввели правильный пароль. Добро пожаловать!")


# Задание 2:
seconds = int(input("Введите время в секундах: "))
print(f"Время в формате чч:мм:сс: {seconds // 3600}:{(seconds / 60) % 60:.0f}:{seconds % 60}")


# Задание 3:
n = int(input("Введите целое положительное число: "))
print(f"{n}{2 * n}{3 * n}")


# Задание 4:
n = int(input("Введите целое положительное число: "))
max_digit = 0
while n != 0:
    end = n % 10
    if end > max_digit:
        max_digit = end
    n = n // 10
print(max_digit)


# Задание 5:
proceeds = int(input("Ваша выручка в рублях: "))
costs = int(input("Ваши издержки в рублях: "))
ratio = proceeds - costs
if ratio > 0:
    print(f"Ваша прибыль составляет {ratio} рублей.")
    print(f"Рентабельность выручки: {ratio * 100 / proceeds: .2f}  %.")
elif ratio < 0:
    print(f"Ваш убыток составляет {ratio} рублей")
else:
    print("Ваша прибыль равна 0.")
employees = int(input("Число сотрудников: "))
print(f"Прибыль в расчете на 1 сотрудника: {ratio / employees: .2f} рублей.")


# Задание 6:
a = int(input("Сколько километров Вы сегодня пробежали? Ваш ответ: "))
b = 6
day = 1
while a <= b:
    a = a + (a * 10) / 100
    day += 1
print(f"На {day} день Ваш результат будет не менее 6 км.")
