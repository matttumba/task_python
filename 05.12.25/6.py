# Напишите программу для расшифровки секретного слова методом частотного анализа.

# Формат входных данных
# В первой строке задано зашифрованное слово. Во второй строке задано одно 
# целое число nn – количество букв в словаре. В следующих nn строках 
# записано, сколько раз конкретная буква алфавита встречается 
# в этом слове – <буква>: <частота>.

# Формат выходных данных
# Программа должна вывести дешифрованное слово.

encryp_word = input()
encryp_list = list(encryp_word)
encryp_dict = dict()

for char in encryp_word:
    encryp_dict[char] = encryp_dict.get(char, 0) + 1

n = int(input())
list1 = []

for i in range(n):
    symbol_count = input().replace(':', '').split()
    list1.append(symbol_count)

for j in range(len(list1)):
    list1[j][0], list1[j][1] = list1[j][1], list1[j][0]

symbol_dict = dict()

for item in list1:
    symbol_dict[item[0]] = item[1]

for t in range(len(encryp_list)):
    encryp_list[t] = symbol_dict.get(str(encryp_dict[encryp_list[t]]), encryp_list[t])
print(''.join(encryp_list))


