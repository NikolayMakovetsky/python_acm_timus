n = 4
senders = ('@3', '@26', '@2', '@13')
print("У Дональда писем:", n, "\nИмена отправителей:")
for x in senders:
    print(x)

"""Печать шкафов с подписями"""
cases = []
cs = []
k = 1
for i in range(3):
    for j in range(9):
        cs.append(f'@{k}')
        k += 1
    cases.append(cs.copy())
    cs.clear()

for x in range(len(cases)):
    print(f"Шкаф с ящиками №{x+1}: ", cases[x])

"""Подходы Дональда к шкафам для укладки писем"""
steps = [1]
for x in range(n):
    for i in range(len(cases)):
        for j in range(len(cases[i])):
            if cases[i][j] == senders[x]:
                # print(senders[x])
                steps.append(i+1)
            else:
                continue

"""Подсчет числа шагов"""
res = []
for i in range(len(steps)):
    if steps[i] == steps[-1]:
        break
    res.append(abs(steps[i] - steps[i+1]))

print(f"Для раскладки по ящикам данных {n} писем Дональду потребуется {sum(res)} шагов")