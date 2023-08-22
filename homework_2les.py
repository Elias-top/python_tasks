import random

num_monets = int(input("введите количество монеток: "))
index = 0
monets_gerb_num = 0
monets_reshka_num = 0

while(index < num_monets):
    rand_state_monet = random.randint(0, 1)
    if(rand_state_monet == 1):
        monets_gerb_num += 1
    else:
        monets_reshka_num += 1
    print(f"{rand_state_monet}, ", end = '')
    index += 1

print('\n Необходимо перевернуть:')

if(monets_gerb_num > monets_reshka_num):
    print(monets_reshka_num)
else:
    print(monets_gerb_num)