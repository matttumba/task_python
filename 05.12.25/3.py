# Вам дан словарь, состоящий из пар слов-синонимов. 
# Повторяющихся слов в словаре нет. Напишите программу, которая для одного 
# данного слова определяет его синоним.

# Формат входных данных
# На вход программе подается количество пар синонимов nn. 
# Далее следует nn строк, каждая строка содержит два слова-синонима. 
# После этого следует одно слово, синоним которого надо найти.

# Формат выходных данных
# Программа должна вывести одно слово, синоним введенного

n = int(input())
my_list = []

for i in range(n):
    synonim = input().split()
    my_list.append(synonim)

my_dict1 = {}
my_dict2 = {}

for para1 in my_list:
    my_dict1[para1[0]] = para1[1]

for para2 in my_list:
    my_dict2[para2[1]] = para2[0]

word = input()

if word in my_dict1:
    for key1, value1 in my_dict1.items():
        if key1 == word:
            print(value1)
            break
elif word in my_dict2:
    for key2, value2 in my_dict2.items():
        if key2 == word:
            print(value2)
            break
