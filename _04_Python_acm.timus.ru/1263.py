"""Инициализация списка кандидатов"""
N = 3
cands = []
for i in range(1, N+1):
    cands.append(i)

"""Инициализация списка голосов избирателей"""
votes = [1, 2, 3, 2, 1, 1]
M = len(votes)

"""Вывод заданных условий на печать"""
print(N, M)
for i in votes:
    print(i)

cnt = 0
res = .0
for i in cands:
    for j in votes:
        if i == j:
            cnt += 1
        else:
            continue
    res = cnt / M * 100
    print("Кандидат {0} получил {1:.2f} % голосов".format(i, res))
    cnt = 0

