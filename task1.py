# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

given_text = 'О сколько абвблинкак нам мгновений мабвнофбва чудных абвххех многабвукв'
print(given_text)

my_string = given_text.split

print (' '.join(filter(lambda my_string: not 'абв' in my_string, my_string())))
