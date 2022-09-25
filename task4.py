# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def encode(s):
    encoding = "" 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding
 

my_file = open('Initial_String.txt', 'r')
file_content1 = my_file.read()
print(file_content1)
my_file.close()

s1 = file_content1
print(encode(s1))

my_file = open('Encoded_String.txt', 'w')
my_file.write(encode(s1))
my_file.close()

print('=' * 12)

def decode(s):
    decode = ''
    count = ''
    for i in s:
        if i.isdigit():
            count += i
        else: 
            decode += i * int(count)
            count = ''   
    return decode

my_file = open('Encoded_String.txt', 'r')
file_content2 = my_file.read()
print(file_content2)
my_file.close()

s2 = file_content2
print(decode(s2))

my_file = open('Decoded_String.txt', 'w')
my_file.write(decode(s2))
my_file.close()
