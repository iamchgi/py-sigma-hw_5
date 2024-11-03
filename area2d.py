# --------------------------- Homework_4  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль обчислення площі 2d фігур

Package Version
------- -------
pip 23.2.1
"""

import math


#  обчислення площі паралелограма за двома сторонами і кутом між ними
def calc_parallelogram_two_sides_angle(a, b, angle: float) -> float:
    """
    :param a: сторона паралелограма
    :param b: сторона паралелограма
    :param angle: кут між двома сторонами (в градусах)
    :return: square площа трикутника
    """
    try:
        angle_in_radians = math.radians(angle)
        square = a * b * math.sin(angle_in_radians)
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
    else:
        return round(square, 2)


#  введення значень двох сторін і кута між ними
def input_two_sides_angle() -> dict:
    """
    :return: dict де "а", "б" значення сторін і "angle" кут між ними
    """
    try:
        a = float(input('Введіть значення сторони а ->'))
        b = float(input('Введіть значення сторони b ->'))
        angle = float(input('Введіть значення кута між сторонами а і b ->'))
    except ValueError:
        print("Error, некоректні вхідні дані")
    else:
        figure_properties = dict([("a",a), ("b",b), ("angle",angle)])
        return figure_properties
