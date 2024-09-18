# N, M и Y (0 < N < 999, 1 < M < 999, 0 < Y < 999)
# ищем все целые числа X в диапазоне [0, M – 1]

# N, M, Y = 1, 3, 4
N, M, Y = 1, 2, 0
# N, M, Y = 2, 6, 4


print(N, M, Y)

res = []
for x in range(0, M):
    if (x ** N) % M == Y:
        res.append(x)

print(*res) if len(res) > 0 else print(-1)