"""Исходные данные"""
# tbl_1 = [[1, 2], [16, 3], [11, 2], [20, 3]]
tbl_1 = [[1, 2], [16, 3], [11, 2], [20, 3], [3, 5], [26, 4], [7, 1], [22, 4]]
# tbl_1 = [[0, 0]]

"""Вывод исходных данных на печать"""
tsks = []
print(len(tbl_1))
for i in range(len(tbl_1)):
    print(*tbl_1[i])
    tsks.append(tbl_1[i][1])

tsks.sort(reverse=True)
# print(tsks)

print("--------------Решение задачи------------")

for j in tsks:
    for k in range(len(tbl_1)):
        if tbl_1[k][1] == j:
            print(*tbl_1[k])
            tbl_1.remove(tbl_1[k])
            break
        else:
            continue