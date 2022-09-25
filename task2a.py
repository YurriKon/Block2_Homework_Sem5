import sys
import time
import random

print('Игра с конфетами. Человек против бота')

print('Сыграем в игру...')
time.sleep(1)
s = int(input('Сколько конфет перед вами? '))
print('За один ход можно забрать не более чем 28 конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')

for i in range(s):
    i = int(input('Бери конфеты, человек... '))
    if i > 28:
        print('Нет-нет, это слишком много!')
        break
    s -= i
    print(f'Осталось {s} конфет')
    if s <= 28:
        print('Похоже, все конфеты твои, железяка!')
        sys.exit()
    for j in range(s):
        print('Теперь ход железяки... ')
        time.sleep(1)
        j = random.randint(1,28)
        print(j)
        s -= j
        print(f'Осталось {s} конфет')
        if s <= 28:
            print('Похоже, все конфеты твои, человек!')
            sys.exit()
        break

