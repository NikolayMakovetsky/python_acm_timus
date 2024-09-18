# bil = '715068'
# bil = '445219'
# bil = '012200'
# bil = '001999'
# bil = '000000'

while True:
    bil = input("Введите номер билета из 6 цифр:")
    if bil.isdigit() and len(bil) == 6:
        break

bil_a = bil[:3]
bil_b = bil[3:]
# print(bil_a, bil_b)

a_sum = 0
for i in bil_a:
    a_sum += int(i)
# print(a_sum)


b_prev = str(int(bil_b) - 1)
b_next = str(int(bil_b) + 1)
# print(b_prev, b_next)

b_sum = 0
for i in bil_b:
    b_sum += int(i)
# print(b_sum)

b_prev_sum = 0
if b_prev != '-1':
    for i in b_prev:
        b_prev_sum += int(i)
else:
    b_prev_sum = -1
# print(b_prev_sum)

b_next_sum = 0
if len(b_next) <= 3:
    for i in b_next:
        b_next_sum += int(i)
else:
    b_next_sum = -1
# print(b_next_sum)

if a_sum == b_sum:
    print("Это счастливый билет!")
elif a_sum == b_prev_sum:
    print("Предыдущий билет был счастливым=/")
elif a_sum == b_next_sum:
    print("Следующий билет - счастливый! ;)")
else:
    print("Это простой билет")
