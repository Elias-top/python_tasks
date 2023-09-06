# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def get_arefm_prog(f_elem, diff, num_elem):
#     temp_array = []
#     last_elem = f_elem + (num_elem - 1) * diff
#     for x in range(f_elem, last_elem + 1, diff):
#         temp_array.append(x)
#     return temp_array


# first_elem = int(input("Введи первый элемент прогрессии"))
# difference = int(input("Введи разность прогрессии"))
# num_of_elem = int(input("Введи колличество элементов прогрессии"))

# print(*get_arefm_prog(first_elem, difference, num_of_elem))