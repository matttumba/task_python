# Дополните приведенный ниже код так, чтобы в переменной result хранился словарь, 
# в котором для каждого символа строки text будет подсчитано количество его вхождений.
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for char in text:
    result[char] = result.get(char, 0) + 1