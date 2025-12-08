# В переменной s хранится строка пар число:слово. Дополните приведенный 
# код, используя генератор, так, чтобы получить словарь result , 
# в котором числа будут ключами, а слова – значениями

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
s1 = s.replace(':', ' ').split()
result = {int(s1[i]) : s1[i+1] for i in range(0, len(s1), 2)}