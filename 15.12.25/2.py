# Напишите программу, которая с помощью модуля random генерирует 
# случайный пароль. Программа принимает на вход длину пароля и выводит 
# случайный пароль, содержащий только символы английского алфавита 
# a..z, A..Z (в нижнем и верхнем регистре).

import random

length = int(input())    # длина пароля

password = str()

for i in range(length):
    p = random.randint(0, 1)
    if p == 1:
        q = random.randint(65, 90)
        q = chr(q)
        password += q
    elif p == 0:
        j = random.randint(97, 122)
        j = chr(j)
        password += j
print(password)

