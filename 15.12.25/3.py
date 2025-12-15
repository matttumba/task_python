# IP-адрес состоит из четырех чисел из диапазона от 00 до 255255 
# (включительно) разделенных точкой.

# Напишите функцию generate_ip(), которая с помощью модуля random 
# генерирует и возвращает случайный корректный IP-адрес.

import random

def generate_ip():
    ip = str()
    for i in range(4):
        octet = str(random.randint(0, 255))
        if i > 0:
            ip += '.'
        ip += octet
    return ip



