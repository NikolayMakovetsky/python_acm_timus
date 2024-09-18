k = 5
bums = [2, 7, 5, 0]
print(len(bums), k)
print(*bums)

drs = list([k] * len(bums))
# print(*drs)

live_b = 0
live_d = 0

for i in range(len(drs)):
    if drs[i] >= bums[i]:
        live_d += (drs[i] - bums[i])
    else:
        live_b += (bums[i] - drs[i])

print("-------------Результат-------------\n", live_b, live_d)