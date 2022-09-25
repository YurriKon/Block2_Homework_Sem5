import sys
import time
import random
print('==========================================')
print('= Игра с конфетами. Человек против SkyNet =')
print('==========================================')
time.sleep(1)
print('Сыграем в игру...')
time.sleep(1)
s = int(input('Сколько конфет перед вами? '))
print('За один ход можно забрать не более чем 28 конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
k = s
for i in range(s):
    i = int(input('Ход человека... '))
    if i > 28:
        print('Нет-нет, это слишком много!')
        break
    s -= i
    print(f'Осталось {s} конфет')
    if s <= 28:
        print('Похоже, все конфеты достались SkyNet')
        sys.exit()
    for j in range(s):
        print('Теперь ход SkyNet... ')
        time.sleep(1)
        if i == k%29:
            print('Похоже, все конфеты твои, человек!')
            sys.exit()
        j = k%29
        print(j)
        s -= j
        print(f'Осталось {s} конфет')
        break
    break

for i in range(1, s):
    i = int(input('Ход человека... '))
    if i > 28:
        print('Нет-нет, это слишком много!')
        break
    s -= i
    print(f'Осталось {s} конфет')
    if s <= 28:
        print('Похоже, все конфеты достались SkyNet')
        sys.exit()
    for j in range(1, s):
        print('Теперь ход SkyNet... ')
        time.sleep(1)
        if s > 86:
            j = random.randint(10,28)
        elif 57 < s < 87:
            j = s - 57
        elif 29 < s < 58:
            j = s - 29
        print(j)
        s -= j
        print(f'Осталось {s} конфет')
        if s <= 28:
            print('Похоже, все конфеты твои, человек!')
            sys.exit()
        break

