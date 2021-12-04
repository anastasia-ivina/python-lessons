#_____________________________Задание 1______________________________
from itertools import zip_longest
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return ('\n'.join(map(str, self.matrix))).replace('[', '').replace(']', '').replace(',', ' ')

    def __add__(self, other):
        self.matrix = [[el + el_ for el, el_ in zip_longest(row[0:3], row[3:], fillvalue=0)] for row in [x + y for x, y in zip_longest(self.matrix, other.matrix, fillvalue=0)]]
        return Matrix(self.matrix)

m_1 = Matrix([[56, 44, 23], [87, 12, 34], [17, 57, 70]])
m_2 = Matrix([[25, 6, 39], [57, 66, 31], [43, 8, 11]])
print(m_1)
print(m_2)
print(m_1 + m_2)

#_____________________________Задание 2______________________________
from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def consump_tiss(self):
        pass

class Coat(Clothes):

    def consump_tiss(self, s):
        self.size = s
        self.consump_1 = (s / 6.5 + 0.5)
        return f"Расход ткани на производство пальто: {round(self.consump_1, 2)} м."

    @property
    def com_cunsump(self):
        return round(self.consump_1, 2)

class Costume(Clothes):

    def consump_tiss(self, h):
        self.height = h
        self.consump_2 = (2 * h + 0.3)
        return f"Расход ткани на производство пальто: {round(self.consump_2, 2)} м."

    @property
    def com_cunsump(self):
        return round(self.consump_2, 2)

coat = Coat()
costume = Costume()
print(coat.consump_tiss(46))
print(costume.consump_tiss(1.75))
print(f"Суммарный расход ткани: {round((coat.com_cunsump + costume.com_cunsump), 2)} м.")



#_____________________________Задание 3______________________________
class Cells:
    def __init__(self, am):
        self.amount = am

    def __str__(self):
        return f"Число ячеек общей клетки: {self.amount}."

    def __add__(self, other):
        return Cells(self.amount + other.amount)

    def __sub__(self, other):
        return Cells(self.amount - other.amount) if self.amount - other.amount > 0 else "Разность меньше нуля!"

    def __mul__(self, other):
        return Cells(self.amount * other.amount)

    def __truediv__(self, other):
        return Cells(self.amount / other.amount) if self.amount % other.amount == 0 else "Вы вводите неподходящие данные!"

    def make_order (self, row):
        while self.amount >= row:

            if self.amount % row == 0 and self.amount != 0:
                self.amount -= row
                print(f"{(chr(42) * (row + 1))}")
            else:
                self.amount -= row
                print(f"{(chr(42) * row)}")
        print(f"{(chr(42) * (self.amount % row))}")

cell_1 = Cells(60)
cell_2 = Cells(108)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(11))
print(cell_2.make_order(11))

