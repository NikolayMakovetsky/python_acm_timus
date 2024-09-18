x1 = [['5'], ['13 20 22 43 146']]
x2 = [['4'], ['13 22 43 146']]
x3 = [['5'], ['13 43 67 89 146']]

print(*x1[0])
print(*x1[1])
print(*x2[0])
print(*x2[1])
print(*x3[0])
print(*x3[1])

# Вытаскиваю строки из списка
str_1 = str(x1[1]).strip("[]")
str_2 = str(x2[1]).strip("[]")
str_3 = str(x3[1]).strip("[]")

# Для нахождения чисел в строке использую функцию re.findall()
import re
numbers = re.findall('\d+',str_1) + re.findall('\d+',str_2) + re.findall('\d+',str_3)
print(numbers)

# На основе списка строк с числами создаю список чисел int
digs = list(map(int, numbers))
digs.sort()
print(digs)

# Для нахождения уникальных елементов использую свойства множеств - set()
res = 0
while len(digs) > 2:
    if len(set(digs[0:3])) == 1:
        res += 1
        digs.pop(0)
    else:
        digs.pop(0)
print(res)

