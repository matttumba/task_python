# На вход программе подаются два предложения. Напишите программу, которая 
# определяет, являются они анаграммами или нет. 
# Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

# Формат входных данных
# На вход программе подаются два предложения, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.

# Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки 
# препинания .,!?:;-. Других символов в тексте нет.

str1, str2 = input().lower().strip(), input().lower().strip()
clear_word1, clear_word2 = [], []

for char in str1:
    clear1 = char.strip('.,?-!;: ')
    clear_word1.append(clear1)
for char in str2:
    clear2 = char.strip('.,?-!;: ')
    clear_word2.append(clear2)

for i in range(len(clear_word1) - 1, -1, -1):
    if clear_word1[i] == '':
        del clear_word1[i]
for j in range(len(clear_word2) - 1,-1, -1):
    if clear_word2[j] == '':
        del clear_word2[j]

dict1, dict2 = dict(), dict()

for char1 in clear_word1:
    dict1[char1] = dict1.get(char1, 0) + 1
for char2 in clear_word2:
    dict2[char2] = dict2.get(char2, 0) + 1

if dict1 == dict2:
    print("YES")
else: 
    print("NO")