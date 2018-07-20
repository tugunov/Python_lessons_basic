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

        self.AB = math.sqrt((bx-ax)**2 + (by-ay)**2) #длина стороны AB
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

#isoscelles trapezoid

class IsoTrapezoid:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

        self.AB = bx-ax, by-ay, math.sqrt((bx-ax)**2 + (by-ay)**2)
        self.BC = cx-bx, cy-by, math.sqrt((cx-bx)**2 + (cy-by)**2)
        self.CD = dx-cx, dy-cy, math.sqrt((dx-cx)**2 + (dy-cy)**2)
        self.AD = dx-ax, dy-ay, math.sqrt((dx-ax)**2 + (dy-ay)**2)


    def isIsoTr(self): # проверка на равнобедренную трапецию
        if (self.BC[0]*self.AD[1] - self.BC[1]*self.AD[0] == 0) & (self.AB[2] == self.CD[2]):
            return True # векторное произведение двух противолежащих сторон равно нулю, другие равны
        else:
            return False

    def len(self): #длина сторон
        return self.AB[2], self.BC[2], self.CD[2], self.AD[2]

    def P(self): #периметр
        return self.AB[2] + self.BC[2] + self.CD[2] + self.AD[2]

    def S(self): #площадь
        return 0.5 * (self.BC[2]+self.AD[2]) * math.sqrt(self.AB[2]**2 - \
              (((self.AD[2]-self.BC[2])**2 + self.AB[2]**2 - self.CD[2]**2) / \
                (2*(self.AD[2]-self.BC[2])))**2)



tr = IsoTrapezoid(0, 0, 1, 4, 4, 4, 5, 0)
if not tr.isIsoTr():
    print('Четырехугольник не является равнобедренной трапецией')
else:
    print('Является равнобедренной трапецией')
    print('Длина сторон: AB = {}, BC = {}, CD = {}, AD = {}'.\
        format(round(tr.AB[2],2), round(tr.BC[2],2), round(tr.CD[2],2), round(tr.AD[2],2)))
    print('Периметр равен {}'.format(round(tr.P(),2)))
    print('Площадь равна {}'.format(round(tr.S(),2)))



