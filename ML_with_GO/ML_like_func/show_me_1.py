"""
    Описание примера:
        Пример илюстрирует разные алгоритмы, в виде функций, которые достигают одной и той же
        цели (выходных данных) разными путями.
        Фукнции, приведены в примере простые, и по сути явлвяются векторами, угол наклона которых кореектируется
        путем умножения и деления.
        Обратите внимание на важную деталь - функции исходят из одной и той же точки, что иллюстрирует одинаковые
        изначальные условия (входные данные).
        Функций подбного рода, несмотря на их простоту - бессконечное количество.
"""

import matplotlib.pyplot as plt
import numpy as np


# Примеры алгоритмов (функций), которые по разному, но приходят к цели
x_example_1 = np.arange(0, 6)
y_example_1 = x_example_1 * 2

x_example_2 = np.arange(0, 21)
y_example_2 = x_example_2 / 2

x_example_3 = np.arange(0, 5)
y_example_3 = x_example_3 * 3

x_example_4 = np.arange(0, 16)
y_example_4 = x_example_4 / 1.5


# Медиана - средний алгоритм (функция) из всего множества алгоритмов(функций)
x_med = np.arange(0, 11) # от 0 до 10
y_med = x_med # f(x) = x


# задаем метку. У нас она будет численой, но в реальных проектах она может и скорее всего
# будет каким то объектом - например изображением. Предположиетль мы тоже сможем ее
# представить в виде набора чисел и соответсвенно функции f(x) = c
label_x = np.arange(0,21)
label_y = (label_x * 0) + 10 # например значение нашей метки - 10



# визиализируем
plt.figure(figsize=(12, 10)) # размерность окна

plt.plot(x_med, y_med, 'b-o', label='f(x) = x (median)')
plt.plot(label_x, label_y, 'r-', label='f(x) = c (label example)')
plt.plot(x_example_1, y_example_1, 'g-', label='f(x) = x * 2 (func_1 example)')
plt.plot(x_example_2, y_example_2, 'c-', label='f(x) = x / 2 (func_2 example)')
plt.plot(x_example_3, y_example_3, 'm-', label='f(x) = x * 3 (func_3 example)')
plt.plot(x_example_4, y_example_4, 'y-', label='f(x) = x / 1.5 (func_4 example)')



plt.xlabel('Натуральный ряд')
plt.ylabel('f(x) = x')
plt.title('Эксперименты')
plt.legend()
plt.grid(True)
plt.show()
