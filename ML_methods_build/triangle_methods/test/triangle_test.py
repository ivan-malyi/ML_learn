


"""

    Тестируем первый этап:
        * Передаем примеры треугольников, на которые ожидаем определенный ответ


"""

import pytest # библиотека для тестирвоания
import sys
import os

# Добавляем директорию src в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



from triangle import Point, Triangle, is_conditions_met, is_right_triangle




# точки для тестирования класса "Point"
point_create_test = [(0,0), (1,5), (-10,-3), (0.5, -7.2)]

@pytest.mark.parametrize("x,y", point_create_test)
# функция тестирвоания создания точки
def test_point_create(x, y):
    create_result = Point(x, y)
    # проверяем сам факт создания
    assert isinstance(create_result, Point)

    # проврека абциссы и ординаты
    assert create_result.x == x
    assert create_result.y == y




# треугольники для тестирования класса "Tringle"
triangle_create_test = [
            ( Point(1,1), Point(5,6), Point(7, 1) ),
            ( Point(1,6), Point(5,3), Point(1,1) ),
            ( Point(1,5), Point(1,1), Point(-3,1) ),
            ( Point(2,6), Point(5,3), Point(1,1) ),
            ( Point(1,2), Point(5,6), Point(7,1) ),
            ]

@pytest.mark.parametrize("p1, p2, p3", triangle_create_test)
# функция тестирвоания создания треугольника
def test_triangle_create(p1, p2, p3):
    create_result = Triangle(p1, p2, p3)

    # проверяем сам факт создания
    assert isinstance(create_result, Triangle)

    # проверяем сами точки
    assert create_result.point_1 == p1
    assert create_result.point_2 == p2
    assert create_result.point_3 == p3



# треугольники для тестирования функции "is_conditions_met()"
cond_met_test = [
            ( Triangle( Point(1,1), Point(5,6), Point(7, 1) ), True ),
            ( Triangle( Point(1,6), Point(5,3), Point(1,1) ) , True ),
            ( Triangle( Point(1,5), Point(1,1), Point(-3,1) ), True ),
            ( Triangle( Point(2,6), Point(5,3), Point(1,1) ), False ),
            ( Triangle( Point(1,2), Point(5,6), Point(7,1) ), False ),
            ]

@pytest.mark.parametrize("triangle, expected", cond_met_test)
# функция тестирвоания функции проверки условий
def test_is_conditions_met(triangle, expected):
    func_result = is_conditions_met(triangle)
    assert expected == func_result


# треугольники для тестирования функции "is_right_triangle()"
right_triangle_test = [
            ( Triangle( Point(1,1), Point(5,6), Point(7, 1) ), False ),
            ( Triangle( Point(1,6), Point(5,3), Point(1,1) ) , False ),
            ( Triangle( Point(1,5), Point(1,1), Point(-3,1) ), True ),
            ( Triangle( Point(2,6), Point(5,3), Point(1,1) ), False ),
            ( Triangle( Point(1,2), Point(1,-3), Point(6,-3) ), True ),
            ( Triangle( Point(-5, -3), Point(2, -3), Point(2, 3) ), True),
            ]


@pytest.mark.parametrize("triangle, expected", right_triangle_test)
# функция для тестирования функции определения прямоугольного треугольника
def test_is_right_triangle(triangle, expected):
    func_result = is_right_triangle(triangle)
    assert expected == func_result