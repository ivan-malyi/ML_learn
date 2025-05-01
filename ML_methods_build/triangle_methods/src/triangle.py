



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





class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    # функция, возвращает точки теругольника
    def get_points(self):
        return (self.point_1, self.point_2, self.point_3)

    # функция для отображения треугольника на декартовой системе коордиант
    def triangle_show(self):

        # возвращаемся, в конце к первой точке
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]

        # возвращаемся, в конце к первой точке
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]


        # Рисуем треугольник
        plt.plot(x, y, marker='o')

        # Подписываем вершины
        plt.text(self.point_1.x, self.point_1.y, 'A', fontsize=12, ha='right')
        plt.text(self.point_2.x, self.point_2.y, 'B', fontsize=12, ha='left')
        plt.text(self.point_3.x, self.point_3.y, 'C', fontsize=12, va='bottom')


        # Сетка и оси
        plt.grid(True)
        plt.axis('equal')  # сохраняем пропорции
        plt.title("Треугольник по трём точкам")

        plt.show()


# функция проверяет соблюдены ли ограничения
def is_conditions_met(triangle):
    # точки треугольника
    points = triangle.get_points()

    # чтобы отслеживать были ли у нас такая точка или нет
    x_points = [] # все точки абцисс
    y_points = [] # все точки ординат

    for point in points:
        # если у нас уже была точка с такой же абциссой или ординатой - значит
        # они лежат на одной прямой оси и нам это подходит
        if point.x in x_points or point.y in y_points:
            return True

        x_points.append(point.x)
        y_points.append(point.y)

    return False




# прямоугольный ли треугольник, соответсвенно выполненим условиям
def is_right_triangle(triangle):

    # треугольник обязан пройти провреку
    if is_conditions_met(triangle):

        # точки треугольника
        points = triangle.get_points()

        # чтобы отслеживать были ли у нас такая точка или нет
        x_points = [] # все точки абцисс
        y_points = [] # все точки ординат



        for index, point in enumerate(points):
            if point.x in x_points:

                if index == 1: # если совпала вторая точка с первой
                    y_points.append(point.y) # добавляем ординату текущей точки в список ординат

                    if points[2].y in y_points: # провреям сходство по ординатам, хотя бы с одной из двух точек
                        return True
                    else:
                        return False

                else: # если точка третья и совпала с первой или второй
                    # определяем какая точка совпала с нами по абциссам (первая или вторая)
                    point_index = x_points.index(point.x)

                    if point_index == 0: # если это первая точка

                        if x_points[1] == point.x: # если еще и вторая точка сходится по абциссам с третьей
                            return False # это или три точки в одной (с общими координатами) или прямая

                        # тогда вторая точка будет условной вершиной и должна быть индентичной по ординатам
                        # с какой то из двух точек (для условия прямого угла)
                        available_y = [points[0].y, points[2].y]
                        if points[1].y in available_y:
                            return True
                        else:
                            # если никакая точка не сходится по ординатам со второй - прямой угол не образуется
                            return False
                    else: # иначе третья точка сходится со второй - тогда она уже не сошлась с первой
                        # тогда первая точка условная вершина
                        available_y = [points[1].y, points[2].y]
                        if points[0].y in available_y:
                            return True
                        else:
                            return False



            # по факту тот же код, что и в случае совпадаения по абциссам, но изменненынй под совпаданеия по ординатам
            elif point.y in y_points:

                if index == 1:  # если совпала вторая точка с первой
                    x_points.append(point.x)  # добавляем абциссу текущей точки в список абсцисс

                    if points[2].x in x_points:  # провреям сходство по абциссам, хотя бы с одной из двух точек
                        return True
                    else:
                        return False

                else:  # если точка третья и совпала с первой или второй
                    # определяем какая точка совпала с нами по ординатам (первая или вторая)
                    point_index = y_points.index(point.y)

                    if point_index == 0:  # если это первая точка

                        if y_points[1] == point.y:  # если еще и вторая точка сходится по ординатам с третьей
                            return False  # это или три точки в одной (с общими координатами) или прямая

                        # тогда вторая точка будет условной вершиной и должна быть индентичной по абциссам
                        # с какой то из двух точек (для условия прямого угла)
                        available_x = [points[0].x, points[2].x]
                        if points[1].x in available_x:
                            return True
                        else:
                            # если никакая точка не сходится по ординатам со второй - прямой угол не образуется
                            return False
                    else:  # иначе третья точка сходится со второй - тогда она уже не сошлась с первой
                        # тогда первая точка условная вершина
                        available_x = [points[1].x, points[2].x]
                        if points[0].x in available_x:
                            return True
                        else:
                            return False
            else:
                # если совпадений нет - просто добавляем абциссу и ординату точки в соответсвующий список
                x_points.append(point.x)
                y_points.append(point.y)


        # списки абцисс и ординат - полны, соответсвенно не произошло совпадений
        return False

    # если треугольник не прошел проверку
    else:
        TypeError("Трегуольник не преобразован в надлежащий формат")
        return False








# функция преобразовывает треугольник к формату, чтобы он проходил функцию "is_conditions_met()"
# и соответвенно корректно обрабатывались функцией "is_right_triangle()"
def triangle_transformation(triangle):
    pass



A = Point(-3, 4)
B = Point(4, 3)
C = Point(0, 0)

my_triangle = Triangle(A, B, C)
# my_triangle.triangle_show()
result = is_conditions_met(my_triangle)
# print(result)