# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# def get_num_glasnih_in_word(temp_word):
#     list_glasnih = "ауоыиэяюёе"
#     num_glasn = 0
#     for x in list_glasnih:
#         num_glasn += temp_word.count(x)
#     return num_glasn


# def get_ritm(spisok_glasn):
#     for x in range(1,len(spisok_glasn)):
#         if(spisok_glasn[0] != spisok_glasn[x]):
#             return False
#     return True


# prim_string = "пара-ра-рам рам-пам-папам па-ра-па-да-по"

# result = get_ritm(list(map(get_num_glasnih_in_word, prim_string.split())))
# if(result == True):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# def print_operation_table(temp_func, num_rows, num_colums):
#     for x in range(1, num_rows + 1):
#         for y in range(1, num_colums + 1):
#             print(temp_func(x,y), end='\t')
#         print()

# num_row = int(input("Введите количество строк: "))
# num_colums = int(input("Введите количество столбцов: "))
# print_operation_table(lambda x,y: x * y, num_row, num_colums)