


"""
    Тестируем:
        * Успешность выполнения функции, которая строит прямые между точками и вне их.
            На выходе функция выдает конечную точку останова, что дает нам возможность тестировать ее.

"""
import math

import pytest # библиотека для тестирвоания
import sys
import os

# Добавляем директорию src в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from line_between_triangle_points import func_build, X_LIM, Y_LIM
from triangle import Point




test_func_build_set = [
    # Тест 1: P_i = p1, P_j = p2, d = 1
    (Point(2, 3), Point(-3, -2), 1, Point(-3.0, -2.0)),

    # Тест 2: P_i = p1, P_j = p2, d = -1
    (Point(2, 3), Point(-3, -2), -1, Point(9.0, 10.0)),

    # Тест 3: P_i = p2, P_j = p1, d = 1
    (Point(-3, -2), Point(2, 3), 1, Point(2.0, 3.0)),

    # Тест 4: P_i = p2, P_j = p1, d = -1
    (Point(-3, -2), Point(2, 3), -1, Point(-10.0, -9.0)),

    # Тест 5: P_i = p3, P_j = p4, d = 1
    (Point(2, 5), Point(-5, 5), 1, Point(-5.0, 5.0)),

    # Тест 6: P_i = p3, P_j = p4, d = -1
    (Point(2, 5), Point(-5, 5), -1, Point(10.0, 5.0)),

    # Тест 7: P_i = p5, P_j = p6, d = 1
    (Point(2, 6), Point(6, 3), 1, Point(6.0, 3.0)),

    # # Тест 8: P_i = p5, P_j = p6, d = -1
    (Point(2, 6), Point(6, 3), -1, Point(0.0, 7.5)),

    # Тест 9: P_i = p7, P_j = p8, d = 1
    (Point(4, 6), Point(4, 8), 1, Point(4.0, 8.0)),

    # Тест 10: P_i = p7, P_j = p8, d = -1
    (Point(4, 6), Point(4, 8), -1, Point(4.0, 0.0)),

    # Тест 11: Одинаковые точки, d = -1
    (Point(6, 3), Point(6, 3), -1, Point(6.0, 3.0)),  # Предполагаю что точка не меняется

    # Тест 12: Одинаковые точки, d = 1
    (Point(6, 3), Point(6, 3), 1, Point(6.0, 3.0)),  # Точка не меняется

    # Тест 13: Точка на границе, движение наружу
    (Point(10, 10), Point(8, 8), -1, Point(10.0, 10.0)),  # Должна остаться на месте

    # Тест 14: Направление = 0 (невалидное)
    (Point(5, 5), Point(8, 8), 0, Point(0.0, 0.0))  # Функция вернет (0,0)
]


@pytest.mark.parametrize("point_i, point_j, direction, expected", test_func_build_set)
def test_func_build(point_i, point_j, direction, expected):
    # Вызов функции в пользовательском режиме (use_mode=0)
    result = func_build(point_i, point_j, direction, 0, X_LIM, Y_LIM)

    # Проверка результата с небольшой погрешностью для значений с плавающей точкой
    assert result.x == pytest.approx(expected.x, abs=1e-9)
    assert result.y == pytest.approx(expected.y, abs=1e-9)



