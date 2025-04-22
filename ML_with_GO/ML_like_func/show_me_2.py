"""
    Описание примера:
        Мы рандомно генирируем точки на графике, которые описываются двумя числовыми значениями,
        которые затем храним в 2n векторе, где n - количество точек.
        Затем, с помощью алгоритма мы определяем функцию, которая наиболее оптимально опишет
        их.
"""



import matplotlib.pyplot as plt
import numpy as np
import random



class Vector:
    def __init__(self):
        self.vector = []
        self.len = 0

    # функция добавления
    def push_in(self, value):
        self.vector.append(value)
        self.len += 1


    # функция удаления последнего элемента
    def pop_in(self):
        self.vector.pop(-1)
        self.len -= 1

    # функция удаления всех встречных элементов определнного значения
    def del_val(self, value):
        for index, el in enumerate(self.vector):
            if el == value:
                self.vector.pop(index)
                self.len -= 1

    def clean_vec(self):
        self.vector.clear()
        self.len = 0

    def print_vec(self):
        if self.len == 0:
            print("Нечего показывать...")

        else:
            for number, obj_point in enumerate(self.vector):
                print(f"{number}. x:{obj_point.x}, y:{obj_point.y}")







class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def change_point(self, x=None, y=None):
        if x != None and y != None:
            self.x = x
            self.y = y
        elif x != None and y == None:
            self.x = x
        elif x == None and y != None:
            self.y = y
        else:
            return None



# если функции в val передать 0 - она заполнит все нулями , иначе рандомными значениями
# dimension - размерность вектора
def vec_fill(vector, dimension, x_range=100, y_range=100, val=0):
    if val != 0:
        for _ in range(0, dimension):
            current_x = random.randint(0, x_range)
            current_y = random.randint(0, y_range)
            current_point = Point(current_x, current_y)
            vector.push_in(current_point)
    else:
        vector = [0] * dimension # заполняем вектор нулями
        return vector
    return vector


# готовим вектор
my_vec = Vector()
my_vec.clean_vec()
my_vec = vec_fill(my_vec, 10, 100, 100, 1)
my_vec.print_vec()



def graph_draw(draw_vec):
    # вывод каждой точки
    for point in draw_vec.vector:
        plt.plot(point.x, point.y, 'bo', label=None)


    # общий вывод
    plt.axhline(0, color='gray', lw=0.5)  # ось X
    plt.axvline(0, color='gray', lw=0.5)  # ось Y
    plt.grid(True)
    plt.legend()
    plt.title("График с точками")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().set_aspect('equal')  # чтобы не искажалось
    plt.show()


"""
    Как мы видим, точки действительно разбросаны рандомно и не формируют ничего схожего на группу. 
    Но тем не менее, давайте попробуем написать фукнцию, которая бы подбирала бы наиболее оптимальную прямую 
    для этих точек.   
"""

# Первое что приходит в голову - просуммировать все точки, как двумерные вектора и разделить на n (их количество).
# Мы получим арифметически среднюю точку по отношению к другим, и через нее проведем прямую от 0.
def midpoint(vect):
    suma_x = 0
    suma_y = 0
    n = 0

    # добавляем каждую точку к сумме абцисс и ординат
    for point in vect.vector:
        suma_x += point.x
        suma_y += point.y
        n += 1

    return Point(suma_x / n, suma_y / n)



# функция рисует вектор, через передаваемую точку. Вектор пойдет дальше точки на continuation единиц по х
def draw_vector_through_point(point, continuation=0):
    straight_x = np.arange(0, point.x + continuation)
    step = point.y / point.x # вычисляем шаг для ординаты
    straight_y = straight_x * step # умножаем единицу на шаг
    plt.plot(straight_x, straight_y, 'r-', label='Вектор медианы')




midpoint_obj = midpoint(my_vec)
print(f"Средняя точка будет тут: ({midpoint_obj.x},{midpoint_obj.y} )")

plt.figure(figsize=(12, 10))  # размерность окна
plt.plot(midpoint_obj.x, midpoint_obj.y, 'rs', label='Точка среднего арифметического со всех данных')


draw_vector_through_point(midpoint_obj, 30) # рисуем вектор через арифм. среднее всех точек - точку
graph_draw(my_vec) # рисуем все остальные точки графика
