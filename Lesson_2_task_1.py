# Задача 1.
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

print("Введите два числа и знак операции между ними.\n"
      "Знаки операций: '+', '-', '*', '/'\n"
      "Для выхода из программы в знаке операции наберите '0'.")
while True:
    a = float(input('Первое число: '))
    b = float(input('Второе число: '))
    sign = input('Знак операции: ')
    if sign != '0':
         if sign == '+' or '-' or '*' or '/':
              if b == 0 and sign == '/':
                   print("Нельзя делить на ноль.")
                   continue
              else:
                  if sign == '+':
                      print(f"{a + b}")
                  elif sign == '-':
                      print(f"{a - b}")
                  elif sign == '*':
                      print(f"{a * b}")
                  elif sign == '/':
                      print(f"{a / b}")
         else:
             print("Неверный знак. Введите данные еще раз.")
             continue
    else:
        break

