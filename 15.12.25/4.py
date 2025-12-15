# Почтовый индекс в Латверии имеет вид: 

# LetterLetterNumber_NumberLetterLetter

# где Letter – заглавная буква английского алфавита, 
# Number – число от 0 до 99 (включительно).

# Напишите функцию generate_index(), которая с помощью модуля random 
# генерирует и возвращает случайный корректный почтовый индекс Латверии.

import random
import string

def generate_index():
    index = []
    for i in range(7):
        if i < 2 or i > 4:
            index.append(random.choice(string.ascii_uppercase))
        elif i == 3:
            index.append('_')
        elif i == 2 or i == 4:
            index.append(str(random.randint(0, 99)))       
    return ''.join(index)
print(generate_index())

