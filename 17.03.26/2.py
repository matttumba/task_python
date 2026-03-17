# Напишите функцию greet(), которая принимает произвольное количество строк-имен 
# (как минимум одну) и возвращает приветствие в соответствии с тестовыми данными.

def greet(first_name, *args):
    all_names = (first_name,) + args
    if len(all_names) == 1:
        return f"Hello, {all_names[0]}!"
    elif len(all_names) > 1:
        return f"Hello, {' and '.join(all_names)}!"
