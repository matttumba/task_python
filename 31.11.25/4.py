# Дополните приведенный ниже код так, чтобы он вывел наиболее часто встречающееся слово строки s. 
# Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

my_list = s.split()
result= {}

for word in my_list:
    result[word] = result.get(word, 0) + 1

max_k = []
maxx = max(result.values())
for key, value in result.items():
    if value == maxx:
        max_k.append(key)
min_k = min(max_k)

print(min_k)