



"""
    Задача 1:
        Научится распознавать прямоугольный треугольник

        Подзадача 1.1:
            Создать функцию, которая распознает треугольник, при данных, ограниченных, условиях.

        Подзадача 1.2:
            Создать функцию, которая преобразует любой данный ей треугольник в треугольник, подходящий
            под условия под первую подзадачу и с помощью функции с первой подзадачи решает его.
"""



import matplotlib.pyplot as plt
import numpy as np
import random







class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    # функция для отображения треугольника на декартовой системе коордиант
    def triangle_show(self):
        pass



# функция проверяет соблюдены ли ограничения
def is_conditions_met(triangle):
    pass



# прямоугольный ли треугольник
def is_right_triangle(triangle):
    pass



# функция преобразовывает треугольник к формату, чтобы он проходил функцию "is_conditions_met()"
def triangle_transformation(triangle):
    pass