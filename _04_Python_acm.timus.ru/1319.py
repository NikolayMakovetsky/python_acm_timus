"""Дано: (N - сторона квадратной матрицы, которую необходимо построить)"""
N = 3
print(N)

"""Инициализация всей матрицы для дальнейшего заполнения"""
matrix = []
mat = []
for i in range(N):
    for j in range(N):
        mat.append(0)
    matrix.append(mat.copy())
    mat.clear()
# print(matrix)


"""Подготовка индексов для верхней половины матрицы, включая диагональ"""
tmp = []
for i in range(N):
    tmp.append(i)

tmp_il1 = []
for j in range(1, N+1):
    tmp_il1.append(tmp[:j])

il1 = []
for x in tmp_il1:
    il1 += x
# print(il1)

tmp_jl1 = []
for j in range(1, N+1):
    tmp_jl1.append(tmp[-j:])

jl1 = []
for x in tmp_jl1:
    jl1 += x
# print(jl1)

"""Подготовка значений для верхней половины матрицы"""
cell_num = []
for i in range(int(N * N - ((N * N - N)/2))):
    cell_num.append(i + 1)
# print(cell_num)


"""Заполнение верхней половины матрицы"""
for x in range(len(cell_num)):
    matrix[il1[x]][jl1[x]] = cell_num[x]
# print(matrix)


"""Подготовка индексов для нижней половины матрицы"""
tmp2 = []
for i in range(N):
    tmp2.append(i)
# print(tmp2)

tmp_il2 = []
for j in range(1, N):
    tmp_il2.append(tmp2[j:])

il2= []
for x in tmp_il2:
    il2 += x
# print(il2)

tmp_jl2 = []
for j in range(1, N):
    tmp_jl2.append(tmp2[:-j])

jl2 = []
for x in tmp_jl2:
    jl2 += x
# print(jl2)

"""Подготовка значений для нижней половины матрицы"""
cell_num2 = []
for i in range(int((N * N - N)/2)):
    cell_num2.append(int(cell_num[-1]) + i + 1)
# print(cell_num2)


"""Заполнение нижней половины матрицы"""
for x in range(len(cell_num2)):
    matrix[il2[x]][jl2[x]] = cell_num2[x]
# print(matrix)

"""Вывод матрицы на печать"""
for x in matrix:
    print(*x)