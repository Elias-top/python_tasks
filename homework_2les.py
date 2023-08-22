# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# import random

# num_monets = int(input("введите количество монеток: "))
# index = 0
# monets_gerb_num = 0
# monets_reshka_num = 0

# while(index < num_monets):
#     rand_state_monet = random.randint(0, 1)
#     if(rand_state_monet == 1):
#         monets_gerb_num += 1
#     else:
#         monets_reshka_num += 1
#     print(f"{rand_state_monet}, ", end = '')
#     index += 1

# print('\n Необходимо перевернуть:')

# if(monets_gerb_num > monets_reshka_num):
#     print(monets_reshka_num)
# else:
#     print(monets_gerb_num)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# sum_num = int(input("скажи сумму чисел: "))
# mult_num = int(input("скажи произведение чисел: "))
# num_1 = 0
# num_2 = 0

# for x in range (1, 1001):
#     num_1 = x
#     num_2 = sum_num - num_1
#     if(((num_1 * num_2) == mult_num) & ((num_1 + num_2) == sum_num)):
#         break
#     print(num_1)
# print(num_1, num_2)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# user_num = int(input("введи число: "))
# result = 0
# k = 0
# while(True):
#     result = 2 ** k
#     k += 1
#     if(result < user_num):
#         print(result)
#     else:
#         break