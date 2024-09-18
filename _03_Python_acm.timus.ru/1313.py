# N = 1
# old = [[1]]
# N = 2
# old = [[1, 3], [2, 4]]
# N = 3
# old = [[1, 3, 6], [2, 5, 8], [4, 7, 9]]
N = 4
old = [[1, 3, 6, 10], [2, 5, 9, 13], [4, 8, 12, 15], [7, 11, 14, 16]]

print(f'Диагональ матрицы = {N}')
print('Матрица:')
for i in range(N):
    print(*old[i])

"""Раскладка матрицы ДО диагонали, включая и саму диагональ"""
new = []
k = 1
while k < (N+1):
    i = k - 1
    j = 0
    for x in range(k):
        while i >= 0:
            new.append(old[i][j])
            i -= 1
            j += 1
    k += 1

"""Раскладка матрицы после диагонали"""
k = N - 1
while k > 0:
    i = N - 1
    j = N - k
    for x in range(k):
        while j <= (N - 1):
            new.append(old[i][j])
            i -= 1
            j += 1
    k -= 1

print('Результат:', *new)

