
"""
    Задачи файла:

        1. Провести прямую между двумя данными точками треугольника.

            1.1  Провести обратную прямую, к условной точке S, которая лежит на границе (со стороны
            оси абцисс или оси ординат или на их пересечении) квадранта. Если направление роста функции устремлен
            в бессконечность - то дойти до какой-то границы, хранящейся в x_lim и y_lim соотвественно.

        2. Подойти к процессу обучения через аналитическую геометрию, намеряно не идя путями более легкими.

        3. Функция должна возвращать точку, куда она пришла. В последствии по этой точке мы сможем определять
        корректность работы функции.

"""



import numpy as np
import matplotlib.pyplot as plt
import math
from triangle import Point





# лимиты по осям
X_LIM = 10
Y_LIM = 10


def main_show():
    # общий вывод
    plt.axhline(0, color='black', lw=1)  # ось X (более заметная)
    plt.axvline(0, color='black', lw=1)  # ось Y (более заметная)
    plt.grid(True)
    plt.legend()
    plt.title("Декартова система координат")
    plt.xlabel("x")
    plt.ylabel("y")

    # Устанавливаем пределы для всех 4 квадрантов
    plt.xlim(-X_LIM, X_LIM)
    plt.ylim(-Y_LIM, Y_LIM)

    # Добавляем подписи квадрантов
    plt.text(X_LIM / 2, Y_LIM / 2, "I квадрант", ha='center', va='center')
    plt.text(-X_LIM / 2, Y_LIM / 2, "II квадрант", ha='center', va='center')
    plt.text(-X_LIM / 2, -Y_LIM / 2, "III квадрант", ha='center', va='center')
    plt.text(X_LIM / 2, -Y_LIM / 2, "IV квадрант", ha='center', va='center')

    plt.gca().set_aspect('equal')  # чтобы не искажалось
    plt.show()



def show_two_point_with_line(point_i, point_j, x_list, y_list):
    plt.figure(figsize=(12, 10))  # размерность окна

    plt.plot(x_list, y_list, 'm-o', label="f(x) = xk")

    plt.plot(point_i.x, point_i.y, 'bo', label="$Point_i$")
    plt.plot(point_j.x, point_j.y, 'ro', label="$Point_j$")

    main_show()


def points_info_print(x_steps_list, y_steps_list, point_i, point_j, k_x, k_y, end_point):

    x_direction = ""
    y_direction = ""

    if k_x > 0:
        x_direction = "x_i - увеличивается"
    elif k_x == 0:
        x_direction = "x_i - статический"
    else:
        x_direction = "x_i - уменьшается"



    if k_y > 0:
        y_direction = "y_i - увеличивается"
    elif k_y == 0:
        y_direction = "y_i - статический"
    else:
        y_direction = "y_i - уменьшается"


    print(f"Шаги по абциссе: {x_steps_list}")
    print(f"Шаги по ординате: {y_steps_list}")

    print("-" * 30)

    print(f"P_i = {point_i}; x_i = {point_i.x}; y_i = {point_i.y}")
    print(f"P_j = {point_j}; x_j = {point_j.x}; y_j = {point_j.y}")

    print("-" * 30)

    print(f"k_x = {k_x}")
    print(x_direction)
    print(f"k_y = {k_y}")
    print(y_direction)

    print("-" * 30)
    print(f"{"*" * 15}--ПОЛСЕДНЯЯ ТОЧКА--{"*" * 15}")
    print(f"Point({end_point.x}, {end_point.y})")


# функция, имитирует метод "np.arange()", но создает все более нагляно и подходяще для нас
def list_create(x_i, k, step_count):
    # итоговый список всех точек
    points_list = []

    for i in range(0, step_count + 1):
        points_list.append(float(x_i + (i * k))) # x(y)_i + (i * k_x(y))

    return np.array(points_list)  # конвертируем в numpy формат


# функция определяет на чьи шаги мы будем оринтированться, чтобы не выйти за пределы
def step_choice(point_i, point_j, k_x, k_y, direction=-1, x_lim=None, y_lim=None):
    if direction == -1:

        if point_i.x < 0:
            step_count_for_x = point_i.x if -k_x > 0 else -x_lim - point_i.x
            step_count_for_y = point_i.y if -k_y > 0 else -y_lim - point_i.y
        else:
            step_count_for_x = point_i.x if k_x > 0 else x_lim - point_i.x
            step_count_for_y = point_i.y if k_y > 0 else y_lim - point_i.y

        # проверка для корректности обработки ситуаций, связанных с нулем
        if math.fabs(k_x) == 0 and math.fabs(k_y) != 0 :
            return int(math.fabs(step_count_for_y / k_y))
        elif math.fabs(k_x) != 0 and math.fabs(k_y) == 0:
            return int(math.fabs(step_count_for_x / k_x))
        elif math.fabs(k_x) == 0 and math.fabs(k_y) == 0:
            return 0

        x_step_count = math.fabs(step_count_for_x / k_x)
        y_step_count = math.fabs(step_count_for_y / k_y)

        if x_step_count != 0 and y_step_count != 0:
            return int(min(x_step_count, y_step_count))
        elif x_step_count == 0:
            return int(y_step_count)
        else:
            return int(x_step_count)

    else: # если нужно вычислить расстояние между двумя точками

        if point_j.x != point_i.x and point_j.y != point_i.y:
            return int(math.fabs( (point_j.x - point_i.x) ))
        elif point_j.x == point_i.x and point_j.y != point_i.y:
            return int(math.fabs(point_j.y - point_i.y))
        elif point_j.x != point_i.x and point_j.y == point_i.y:
            return int(math.fabs(point_j.x - point_i.x))
        else: # если точки по абциссам и ординатам одни и те же - то это по сути точка
            return 0






# функция написана, чтобы корректно обрабатыватть ситуации деления на 0
def step_calculate(point_i, point_j):
    step_by_x = 0
    step_by_y = 0


    if point_j.x != point_i.x and point_j.y != point_i.y:
        step_by_x = (point_j.x - point_i.x) / (math.fabs(point_j.x - point_i.x))  # x_j - x_i / |x_j - x_i|
        step_by_y = (point_j.y - point_i.y) / (math.fabs(point_j.x - point_i.x))  # y_j - y_i / |x_j - x_i|
    elif point_j.x == point_i.x and point_j.y != point_i.y:
        step_by_x = 0
        step_by_y = (point_j.y - point_i.y) / math.fabs((point_j.y - point_i.y)) # y_j - y_i / |y_j - y_i|
    elif point_j.x != point_i.x and point_j.y == point_i.y:
        step_by_x = (point_j.x - point_i.x) / math.fabs((point_j.x - point_i.x)) # x_j - x_i / |x_j - x_i|
        step_by_y = 0

    return (step_by_x, step_by_y)




# функция выполняет весь функционал из пунктов 1 и 1.1
# use_mode - режим использования функции: 1 - для разработчика, иначе - пользовательский
def func_build(point_i, point_j, direction=-1, use_mode=0, x_lim=10, y_lim=10):
    """
    :param point_i: P_i; point_1.x Э {Z}; point_1.y Э {Z}
    :param point_j: P_j; point_2.x Э {Z}; point_2.y Э {Z}
    :param direction: направление движения функции - от P_j(-1) или к P_j(+1)
    :return: конечнкую точку нашей функции (для последующей проверки)
    """

    x_step, y_step = step_calculate(point_i, point_j)
    points_count = step_choice(point_i, point_j, x_step, y_step, direction, x_lim, y_lim)


    if direction == -1:
        local_x_steps_list = list_create(point_i.x, -x_step, points_count) # -x_step - т.к учитываем знак направления
        local_y_steps_list = list_create(point_i.y, -y_step, points_count)


        if use_mode == 1:
            # логирования
            end_point = Point(local_x_steps_list[-1], local_y_steps_list[-1])
            points_info_print(local_x_steps_list, local_y_steps_list, point_i, point_j, x_step, -y_step, end_point)

            # графика
            show_two_point_with_line(point_i, point_j, local_x_steps_list, local_y_steps_list)

        return Point(local_x_steps_list[-1], local_y_steps_list[-1])



    elif direction == 1: # если направление выбрано к точке P_j

        local_x_steps_list = list_create(point_i.x, x_step, points_count) # -x_step - т.к учитываем знак направления

        local_y_steps_list = list_create(point_i.y, y_step, points_count)

        if use_mode == 1:
            # логирования
            end_point = Point(local_x_steps_list[-1], local_y_steps_list[-1])
            points_info_print(local_x_steps_list, local_y_steps_list, point_i, point_j, x_step, y_step, end_point)

            # графика
            show_two_point_with_line(point_i, point_j, local_x_steps_list, local_y_steps_list)

        return Point(local_x_steps_list[-1], local_y_steps_list[-1])



    else:
        return Point(0,0) # возвращаем пустой кортеж







# тестирование

# P_i = p1, P_j = p2:
#       d = 1: Point(-3.0, -2.0); d = -1: Point(9.0, 10.0)
# P_i = p2, P_j = p1:
#     d = 1: Point(2.0, 3.0); d = -1: Point(-10.0, -9.0)

p1 = Point(2,3)
p2 = Point(-3,-2)

# P_i = p3, P_j = p4:
#   d = 1: Point(-5.0, 5.0); d = -1: Point(10.0, 5.0)

p3 = Point(2,5)
p4 = Point(-5, 5)

# d = 1: Point(6, 3) ; d = -1: Point(4.0, 0.0)
p5 = Point(2, 6)
p6 = Point(6, 3)

# d = 1: Point(4.0, 8.0); d = -1: Point(4.0, 0.0)
p7 = Point(4, 6)
p8 = Point(4, 8)

p9 = Point(4, 6)
p10 = Point(4, 8)

p11 = Point(2, 6)
p12 = Point(6, 3)


# func_build(p11, p12, -1, 1, X_LIM, Y_LIM)


