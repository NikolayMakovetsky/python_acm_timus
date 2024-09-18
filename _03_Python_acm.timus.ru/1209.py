N = 4
k = [3, 14, 7, 6]

print(N)
for i in range(len(k)):
    print(k[i])

str01 = '1'
num = 1
while len(str01) < 231:
    num *= 10
    str01 += str(num)
print(str01)


ind_01_num = []
for i, d in enumerate(str01):
    if d == '1':
        ind_01_num.append(i+1)

print(ind_01_num)

res = []
for x in k:
    if x in ind_01_num:
        res.append(1)
    else:
        res.append(0)
print(*res)