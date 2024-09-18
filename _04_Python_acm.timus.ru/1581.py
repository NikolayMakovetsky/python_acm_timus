N = 8
tst = '1 1 2 3 3 3 10 10'

lst = tst.split(sep = " ")
print(len(lst))
print(*lst)

res = []
x = lst[1]
i = 1
k = 1
while i < len(lst):
    if x == lst[i]:
        i += 1
        k += 1
    else:
        res.append(k)
        res.append(x)
        x = lst[i]
        i += 1
        k = 1
else:
    res.append(k)
    res.append(x)

print(*res)
