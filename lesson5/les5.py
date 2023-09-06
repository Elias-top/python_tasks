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

# Задача 32: Определить индексы элементов массива (списка),значения которых принадлежат заданному диапазону [5 : 15](т.е. не
# меньше заданного минимума и не больше заданного максимума)

# import random

# def get_specific_index_from_random_array(array, first_num_range, second_num_range):
#     temp_array = []
#     temp_index = 0
#     for x in array:
#         if(x >= 5 and x <= 15):
#             temp_array.append(temp_index)
#         temp_index += 1
#     return temp_array
            


# rand_array = []
# for x in range(0, 15):
#     rand_array.append(random.randint(-15, 30))

# print(rand_array)
# print(get_specific_index_from_random_array(rand_array, 5, 15))


