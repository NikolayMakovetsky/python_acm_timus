# 3
# Ted+one
# Robin
# Barney
# 6
# Alice+one
# Bob+one
# carl
# Debora+one
# Enrique+one
# FRED+one
Sum = 0

while True:
    n = int(input('Введите число друзей от 1 до 20: '))
    if 1 <= n <= 20:
        break
guests = list('' for i in range(n))

names = []
for i in range(n):
    while True:
        names = input('Ответ на приглашение: ')
        if len(names) > 20:
            print('Введите заново')
            continue
        else:
            guests[i] = names
            break

for i in range(n):
        if guests[i].count('+one') == 0:
            Sum +=1
        else:
            Sum +=2

print(guests)
if (Sum+2) != 13:
    print((Sum+2)*100)
if (Sum+2) == 13:
    print((Sum+3)*100)