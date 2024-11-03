# --------------------------- Homework_4  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль
роботи з "CV":
Створення, друк, збереження

Package Version
------- -------
numpy 2.1.2
pip 23.2.1

"""

import numpy as np


# Створення словника з даними "CV"
def create_cv() -> dict:
    """
    :return: my_cv_dict словник з даними резюме
    """
    print('------------------------ формування CV ---------------------------')
    my_name = "Taras Boolba"  # строка
    my_birth = "1976"
    age = "48"
    my_programming_languages = ["Python", "Pascal", "Java", "VB", "PHP"]  # список
    my_soft_skills = ('комунікабельність', 'вміння працювати в команді', 'креативність',
                      'пунктуальність', 'врівноваженість')  # кортеж
    my_hard_skills = {'набір тексту на комп\'ютері', 'водіння автомобіля', 'читання', 'математика',
                      'знання іноземної мови', 'використання комп\'ютерних програм'}  # множина

    my_languages = np.array(['Українська', 'English', 'Русский'])  # масив

    my_cv_dict = dict({'name': my_name,
                       'birth': my_birth,
                       'age': age,
                       'programming_languages': my_programming_languages,
                       'soft_skills': my_soft_skills,
                       'hard_skills': my_hard_skills,
                       'languages': my_languages})  # словник
    return my_cv_dict


# Друк на консоль вмісту словника з CV
def print_cv(cv: dict) -> None:
    """
    :param cv: словник з даними резюме
    :return: None
    """
    for item in cv:
        if type(cv[item]) == str:
            print(item, " : ", cv[item])
        else:
            print("----------------------------")
            print(item)
            # print(type(my_cv_dict[item]))
            for i in (cv[item]):
                print(i, end=" ")
            print("")
    print("")


# Перетворення даних типу словник в формат текст , csv, текст-словник
def generate_cv_file_data(cv: dict, data_file_type: str) -> tuple:
    """
    :param cv: Заповнене резезюме
    :param data_file_type: тип файлу для якого буде генеруватись вміст(дані)
    :return: Згенеровані дані для збереження в файл
    """
    result = list()
    match data_file_type:
        case 'txt':
            for item in cv:
                if type(cv[item]) == str:
                    result.append(item + " : " + cv[item])
                else:
                    result.append("----------------------------")
                    result.append(item)
                    current_str = ""
                    for i in (cv[item]):
                        current_str += i + ", "
                    current_str = current_str[:-2]
                    result.append(current_str)
        case 'csv':
            csv_caption = ""
            csv_data = ""
            for key in cv:
                csv_caption += str(key) + ","
                csv_data += str(cv[key]) + ","
            result.append(csv_caption[:-1])
            result.append(csv_data[:-1])
        case 'dict':
            for key, value in cv.items():
                result.append(f'{key} : {value}')
        case _:
            raise Exception('OK. it will be saved to file for next time. \n'
                            'It seems error !!!')
    return tuple(result)


# Збереження у файл даних типу строки
def save_cv_to_file(file_name: str, data: tuple) -> None:
    """
    :param file_name: ім'я файлу у який зберігаємо CV
    :param data: дані для зберігання у файл
    :return: None
    """
    try:
        print(f'------------------------ запис CV у файл \"{file_name}\" ----------------------')
        with open(file_name, "w", encoding="UTF-8") as file:
            for line in data:
                file.write(line + "\n")
    except PermissionError:
        print("Sorry, you have no access to this file")
    except Exception as error:
        print(f"It looks like something has happened. This is {error}")
    else:
        print(f"CV was saved successfully in file \"{file_name}\"")
    finally:
        print(f"Writing file module finished its work with current file \"{file_name}\".\n")

    # ------------------------ запис CV у файли ----------------------------
def save_cv(cv :dict) -> None:
    file_types = ('txt', 'csv', 'dict')
    for file_type in file_types:
        current_file_name = cv['name'] + "." + file_type
        current_data = generate_cv_file_data(cv, file_type)
        save_cv_to_file(current_file_name, current_data)
    return