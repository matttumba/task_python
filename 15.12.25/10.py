# Напишите программу, которая с помощью модуля random генерирует n паролей
#  длиной m символов, состоящих из строчных и прописных английских букв 
# и цифр, кроме тех, которые легко перепутать между собой:

#     «l» (L маленькое);
#     «I» (i большое);
#     «1» (цифра);
#     «o» и «O» (маленькая и большая буквы);
#     «0» (цифра).

# Формат входных данных
# На вход программе подаются два числа nn и mm, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести nn паролей длиной mm символов в соответствии с
#  условием задачи, каждый на отдельной строке.

# Примечание 1. Считать, что числа nn и mm всегда таковы, что требуемые 
# пароли сгенерировать возможно.

# Примечание 2. В каждом пароле необязательно должна присутствовать хотя 
# бы одна цифра и буква в верхнем и нижнем регистре.

import random
import string

count = int(input())
length = int(input())

def generate_password(length):
    password = str()
    excep = [elem for elem in list(string.ascii_letters + string.digits) if elem not in "Il1oO0"]
    for i in range(length):
        password += random.choice(excep)
    return password

def count_passwords(count, length):
    list_passwords = list()
    for j in range(count):
        list_passwords.append(generate_password(length))
    return list_passwords

passwords = count_passwords(count, length)
for pwd in passwords:
    print(pwd)

