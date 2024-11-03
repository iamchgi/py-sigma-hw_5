# --------------------------- Homework_4  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Homework_5
З використанням механізмів модульного та функціонального програмування
реалізувати програмну архітектуру проекту python
до функцій застосувати архітектурну побудову з дотриманням вимог РЕР;
здійснити анотування / документування функцій.

Package Version
------- -------
numpy 2.1.2
pip 23.2.1

"""

import fizz_buzz as fb
import area2d as ar2
import curriculum_vitae as cv

# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    # ------------------------  CV ----------------------------
    my_cv_dict = cv.create_cv() # формування
    cv.print_cv(my_cv_dict)  #  друк
    cv.save_cv(my_cv_dict)  # зберігання

    # ------------------------ Розрахунок площі паралелограма ----------------------------
    print("Розрахунок площі паралелограма, за двома сторонами і кутом між ними.")
    pg_prop = ar2.input_two_sides_angle()
    area = ar2.calc_parallelogram_two_sides_angle(pg_prop["a"], pg_prop["b"],pg_prop["angle"])
    print(f"Площа паралелограма: {area} \n")

    # ------------------------ Демонстрація роботи алгоритму FizzBuzz ----------------------------
    source = tuple(range(1, 16))
    destination = fb.fizz_buzz(source)
    print(f"Вхідний набір чисел: \n {source}")
    print(f"Результат, вихідний набір:\n {destination}")

''' 
РЕЗУЛЬТАТ

------------------------ формування CV ---------------------------
name  :  Taras Boolba
birth  :  1976
age  :  48
----------------------------
programming_languages
Python Pascal Java VB PHP 
----------------------------
soft_skills
комунікабельність вміння працювати в команді креативність пунктуальність врівноваженість 
----------------------------
hard_skills
набір тексту на комп'ютері використання комп'ютерних програм водіння автомобіля читання математика знання іноземної мови 
----------------------------
languages
Українська English Русский 

------------------------ запис CV у файл "Hryhorii Chernolutskyi.txt" ----------------------
CV was saved successfully in file "Hryhorii Chernolutskyi.txt"
Writing file module finished its work with current file "Hryhorii Chernolutskyi.txt".

------------------------ запис CV у файл "Hryhorii Chernolutskyi.csv" ----------------------
CV was saved successfully in file "Hryhorii Chernolutskyi.csv"
Writing file module finished its work with current file "Hryhorii Chernolutskyi.csv".

------------------------ запис CV у файл "Hryhorii Chernolutskyi.dict" ----------------------
CV was saved successfully in file "Hryhorii Chernolutskyi.dict"
Writing file module finished its work with current file "Hryhorii Chernolutskyi.dict".

Розрахунок площі паралелограма, за двома сторонами і кутом між ними.
Введіть значення сторони а ->10
Введіть значення сторони b ->20
Введіть значення кута між сторонами а і b ->89
Площа паралелограма: 199.97

Вхідний набір чисел:
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
Результат, вихідний набір:
(1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz')

'''
