# Напишите функцию mean(), которая принимает произвольное количество аргументов и 
# возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов. 
# Если числовых аргументов не будет, функция должна вернуть 0.

def mean(*args):
    int_or_float = list()
    for num in args:
        if type(num) == int or type(num) == float:
            int_or_float.append(num)
    if len(int_or_float) > 0:
        return sum(int_or_float)/len(int_or_float)
    elif len(int_or_float) == 0:
        return float(0)
