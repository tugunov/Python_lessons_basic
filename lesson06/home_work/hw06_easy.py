# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

        self.AB = math.sqrt((bx-ax)**2 + (by-ay)**2)
        self.BC = math.sqrt((cx-bx)**2 + (cy-by)**2)
        self.AC = math.sqrt((cx-ax)**2 + (cy-ay)**2)

    def P(self):
        return self.AB + self.BC + self.AC

    def p(self):
        return self.P()/2

    def S(self):
        return math.sqrt(self.p() * (self.p() - self.AB) * (self.p() - self.BC) *(self.p() - self.AC))

    def hBC(self):
        return 2*self.S()/self.BC

    def hAC(self):
        return 2*self.S()/self.AC

    def hAB(self):
        return 2*self.S()/self.AB


t = Triangle(0, 0, 0, 2, 2, 0)

print('Периметр треугольника: {}'.format(round(t.P(), 2)))
print('Площадь треугольника: {}'.format(round(t.S(), 2)))
print('Высота к стороне AB: {}'.format(round(t.hAB(), 2)))
print('Высота к стороне BC: {}'.format(round(t.hBC(), 2)))
print('Высота к стороне AC: {}'.format(round(t.hAC(), 2)))






# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

