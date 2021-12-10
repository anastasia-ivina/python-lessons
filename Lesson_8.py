#__________________________Задание 1__________________________

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def first_method(cls, date):
        d = list(map(int, date.replace('-', ' ').split()))
        return cls(d)

    @staticmethod
    def is_valid(obj):
        return f"Неверные данные!" if  obj.date[0] > 31 or 0 >= obj.date[0] or 0 >= obj.date[1] or obj.date[1] > 12\
                                       or obj.date[2] > 4999 else f"{obj.date[0]:02.0f}.{obj.date[1]:02.0f}.{obj.date[2]:02.0f}"


f_1 = Date.first_method(input("Введите произвольную дату в формате «день-месяц-год» (напр., 11-12-2012): "))
print(f_1.date)
print(Date.is_valid(f_1))
f_2 = Date(input("Введите произвольную дату в формате «день-месяц-год» (напр., 11-12-2012): "))
print(f_2.date)
print((f_2.first_method(f_2.date)).date)
print(Date.is_valid(f_2.first_method(f_2.date)))


#__________________________Задание 2__________________________

class My_error(Exception):
    def __init__(self, text):
        self.date = text
def my_fun(arg_1, arg_2):
    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        if arg_2 == 0:
            raise My_error("Делитель равен нулю!")

    except (ValueError, My_error) as err:
        print(err)
        print("Программа завершена.")

    else:
        division = arg_1 / arg_2
        return print(f"Результат деления: {round(division, 2)}.")

my_fun((input('Введите делимое: ')), (input('Введите делитель: ')))


#__________________________Задание 3__________________________

print("Для выхода из программы введите:  stop")
new_list = []
while True:
    try:
        element = input("Введите любое целое число: ").lower()
        if element == "stop":
            print(new_list)
            break
        elif element.startswith('-') and element.replace('-', '').isdigit() == True:
            new_list.append(int(element))
            print(new_list)
            continue
        elif element.isdigit() == False:
                raise My_error("Введите целое число!")

    except (My_error) as error:
        print(error)

    else:
        new_list.append(int(element))
        print(new_list)


#__________________________Задание 7__________________________

class Complex_num:
    def __init__(self, com_num_1, com_num_2):
        self.number_1 = com_num_1
        self.number_2 = com_num_2

    def __add__(self, other):

        return f"Сумма комплексных чисел: {(self.number_1 + other.number_1)}+{(self.number_2 + other.number_2)}j." \
            if (self.number_2 + other.number_2) >= 0 \
            else f"Сумма комплексных чисел: {(self.number_1 + other.number_1)}{(self.number_2 + other.number_2)}j."

    def __mul__(self, other):

        return f"Произведение комплексных чисел: {self.number_1 * other.number_1 - self.number_2 * other.number_2}+" \
               f"{self.number_1 * other.number_2 + self.number_2 * other.number_1}j" \
            if self.number_1 * other.number_2 + self.number_2 * other.number_1 >= 0 \
             else f"Произведение комплексных чисел: {self.number_1 * other.number_1 - self.number_2 * other.number_2}" \
               f"{self.number_1 * other.number_2 + self.number_2 * other.number_1}j"

num_1 = Complex_num(int(input("Введите целое число: ")), int(input("Введите целое число: ")))
num_2 = Complex_num(int(input("Введите целое число: ")), int(input("Введите целое число: ")))

print(num_1 + num_2)
print(num_1 * num_2)

#__________________________Задания 4,5,6__________________________
class Warehouse:
    def model_(self, *printers):
        model_ = {self.equipment: self.amount}
        return model_

    @staticmethod
    def accept_issue_eqip():
        return models


class OfficeEquipment:
    def __init__(self, eq, pr_n, am):
        self.equipment = eq
        self.product_name = pr_n
        self.amount = int(am)
        self.specifications = {"Тип оргтехники": eq, "Наименование": pr_n, "Количество товара": int(am)}

    def __str__(self):
        return f"{self.specifications}"


class Printer(OfficeEquipment):
    def __init__(self, eq, pr_n, am, c_p):
        super().__init__(eq, pr_n, am)
        self.color_print = c_p
        self.specifications = {"Тип оргтехники": eq, "Наименование": pr_n, "Количество товара": int(am),
                               "Цвет печати": c_p}


class Scanner(OfficeEquipment):
    def __init__(self, eq, pr_n, am, s_d):
        super().__init__(eq, pr_n, am)
        self.submiss_doc = s_d
        self.specifications = {"Тип оргтехники": eq, "Наименование": pr_n, "Количество товара": int(am),
                               "Подача документов": s_d}


class Xerox(OfficeEquipment):
    def __init__(self, eq, pr_n, am, sp):
        super().__init__(eq, pr_n, am)
        self.speed = int(sp)
        self.specifications = {"Тип оргтехники": eq, "Наименование": pr_n, "Количество товара": int(am),
                               "Скорость печати (стр/мин)": int(sp)}


p = Printer("принтер", "НР", 6, "цветная")
s = Scanner("сканер", "Canon", 12, "автоматическая")
x = Xerox("ксерокс", "Xerox", 14, 33)

models = {}
models.update(Warehouse.model_(p))
models.update(Warehouse.model_(s))
models.update(Warehouse.model_(x))

w = Warehouse()

while True:
    # меню операций
    print('\nВведите тип операции:\n<1> Принять на склад.\n<2> Выдать со склада.\n<Enter> Выход.')
    action = input('> ')

    if action in ['1', '2']:  # если выбрана операция

        # формируем список оргтехники

        s = ''
        for i, (key, value) in enumerate(models.items()):
            s += f'\n<{i}> {key} ({value} шт.)'

        # меню оргтехники
        while True:
            print(f'\nВведите модель оргтехники и кол-во:{s}')
            # выбираем модель
            try:
                model = int(input('модель > '))
                if model in range(len(models)):
                    # вводим кол-во
                    n = int(input('кол-во > '))
                    if (n <= 0):
                        raise ValueError
                else:
                    raise ValueError

            except ValueError:
                print(f'Некорректный ввод. Введите число от <0> до <{len(models)}>.')
                continue
            else:
                # совершаем операцию
                print('\nОперация:')
                if (action == '1'):  # принимаем технику на склад
                    if model == 0:
                        Warehouse.accept_issue_eqip()['принтер'] = Warehouse.accept_issue_eqip()['принтер'] + n
                        print(f"{Warehouse.accept_issue_eqip()}")
                    elif model == 1:
                        Warehouse.accept_issue_eqip()['сканер'] = Warehouse.accept_issue_eqip()['сканер'] + n
                        print(f"{Warehouse.accept_issue_eqip()}")
                    elif model == 2:
                        Warehouse.accept_issue_eqip()['ксерокс'] = Warehouse.accept_issue_eqip()['ксерокс'] - n
                        print(f"{Warehouse.accept_issue_eqip()}")

                elif (action == '2'):  # выдаём технику со склада
                    if model == 0 and n < Warehouse.accept_issue_eqip()['принтер']:
                        Warehouse.accept_issue_eqip()['принтер'] = Warehouse.accept_issue_eqip()['принтер'] - n
                        print(f"{Warehouse.accept_issue_eqip()}")
                    elif model == 1 and n < Warehouse.accept_issue_eqip()['сканер']:
                        Warehouse.accept_eqip()['сканер'] = Warehouse.accept_issue_eqip()['сканер'] - n
                        print(f"{Warehouse.accept_issue_eqip()}")
                    elif model == 2 and n < Warehouse.accept_issue_eqip()['ксерокс']:
                        Warehouse.accept_issue_eqip()['ксерокс'] = Warehouse.accept_issue_eqip()['ксерокс'] - n
                        print(f"{Warehouse.accept_issue_eqip()}")
                    #
                    #
                    if (n > Warehouse.accept_issue_eqip()['принтер'] or \
                            n > Warehouse.accept_issue_eqip()['сканер'] or \
                            n > Warehouse.accept_issue_eqip()['ксерокс']):  # если запрошено больше, чем есть

                        print(f'Внимание: На складе недостаточно товара!')
                        print(f"{Warehouse.accept_issue_eqip()}")
                        break

                break

            if (input('\nPress <Enter> to continue or any key to exit...') != ''):
                break
    elif action == '':  # если выбран выход - завершаем работу
        break
    else:
        print('Некорректный ввод. Для выбора введите <1> или <2>.')