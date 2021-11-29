# _________________________Задание 1._________________________

import time
import turtle
from time import sleep

class TrafficLight:
    __color_1 = 'красный'
    __color_2 = 'желтый'
    __color_3 = 'зеленый'

    def running(self):
        i = 0
        for i in range(3):
            i += 1
            circle = turtle.Turtle()
            circle.shape("circle")
            circle.pensize(2)
            circle.speed(20)
            circle.circle(50)
            print(f"Загорелся \033[31m {self.__color_1} \033[0m сигнал сфетофора.")
            circle.pencolor("red")
            circle.fillcolor("red")
            circle.begin_fill()
            circle.circle(50)
            circle.end_fill()
            time.sleep(7.0)
            print(f"Загорелся \033[33m {self.__color_2} \033[0m сигнал сфетофора.")
            circle.pencolor("yellow")
            circle.fillcolor("yellow")
            circle.begin_fill()
            circle.circle(50)
            circle.end_fill()
            time.sleep(2.0)
            print(f"Загорелся \033[32m {self.__color_3} \033[0m сигнал сфетофора.")
            circle.pencolor("green")
            circle.fillcolor("green")
            circle.begin_fill()
            circle.circle(50)
            circle.end_fill()
            time.sleep(3.0)

lamp = TrafficLight()
print(lamp.running())


# _________________________Задание 2._________________________

class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w
    def mass(self, mass_1sqm, thick):
        print(f"Масса асфальта, необходимая для покрытия дороги: {(self._length * self._width * mass_1sqm * thick) / 1000} т.")

r = Road(200, 5500)
r.mass(10, 5)

# _________________________Задание 3._________________________

class Worker:
    def __init__(self, n, surn, pos, wage, bonus):
        self.name = n
        self.surname = surn
        self.position = pos
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, n, surn, pos, wage, bonus):
        super().__init__(n, surn, pos, wage, bonus)

    def get_full_name(self):
        print(f"Имя и фамилия сотрудника: {self.name} {self.surname}.")
        print(f"Должность сотрудника: {self.position}.")

    def get_total_income(self):
        print(f"Доход сотрудника (с учетом премии): {self._income.get('wage') + self._income.get('bonus')} руб.")

p = Position("Анастасия", "Ивина", "врач", 460000, 50000)
print(p.name)
print(p.surname)
print(p.position)
print(p._income)
p.get_full_name()
p.get_total_income()

# _________________________Задание 4._________________________

import random
class Car:
    def __init__(self, n, c, s):
        self.color = c
        self.name = n
        self.is_police = False
        self.speed = s
    def go(self):
        print(f"{self.name} поехал!")
    def stop(self):
        print(f"{self.name} остановился!")
    def turn(self):
        turn_list = ["налево", "направо"]
        print(f"{self.name} повернул {random.choice(turn_list)}!")
    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}: {self.speed} км/ч.")
class TownCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s)
    def show_speed(self):
        if self.speed <= 60:
            print(f"Текущая скорость автомобиля {self.name}: {self.speed} км/ч.")
        else:
            print(f"Машина превысила скорость!")
class WorkCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s)
    def show_speed(self):
        if self.speed <= 40:
            print(f"Текущая скорость автомобиля {self.name}: {self.speed} км/ч.")
        else:
            print("Машина превысила скорость!")
class SportCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s)
class PoliceCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s)
        self.is_police = True
    def show_speed(self):
        print(f"Текущая скорость полицейского автомобиля {self.name}: {self.speed} км/ч.")

car_1 = Car("BMW", "синий", 90)
print(car_1.name)
car_1.go()
print(car_1.color)

car_2 = TownCar("Lexus", "белый", 45)
print(car_2.color)
car_2.show_speed()

car_3 = WorkCar("CAT", "желтый", 39)
print(car_3.is_police)
car_3.turn()
car_3.show_speed()

car_4 = SportCar("Ferrari", "красный", 100)
car_4.show_speed()
car_4.stop()

car_5 = PoliceCar("Ford", "белый", 80)
print(car_1.name)
car_5.show_speed()
print(car_5.is_police)


# _________________________Задание 5._________________________

class Stationery:
    title = "Let's do some drawing!"
    def draw(self):
       print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой!")

class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом!")

class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером!")

st_1 = Stationery()
print(st_1.title)
st_1.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
