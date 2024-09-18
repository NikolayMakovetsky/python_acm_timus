# A, B = 1, 5
A, B = 100, 200

i = 0
for j in range(A, B+1):
    if j % 2 != 0:
        i += 1
    else:
        continue
print(i)