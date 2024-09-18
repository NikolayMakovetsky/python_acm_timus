"""Given"""

n = -1
while n < 0 or n >100:
    n = int(input('Введите целое число 0 <= n <= 100: '))
print(f"n = {n}", "Формула: an + bn = cn")
print("Расчет минимальных коэффициентов: ")

if n != 0:
    for i in range(1, 101):
        if (i * n + (i+1) * n == (i + (i+1)) * n) and (i + (i+1)) < 101:
            print(f"a = {i}, b = {i+1}, c = {i + i + 1}")
            break
else:
    print("Статус ошибки =",-1)

