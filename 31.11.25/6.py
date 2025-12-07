# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
input_string = input().lower().split()
clear_word = []
for char in input_string:
    clear = char.strip('.,?-!;:')
    clear_word.append(clear)

result= {}

for word in clear_word:
    result[word] = result.get(word, 0) + 1

min_k = []
minn = min(result.values())
for key, value in result.items():
    if value == minn:
        min_k.append(key)
min_ASCII = min(min_k)
print(min_ASCII)
