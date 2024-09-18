N = 3
a = []
for n in range(0,N):
    a.append([0 for i in range(0,N)])

for i in range(0,N):
    print (a[i])

S = 0
for n in range(0,N):
    for i in range(0, n+1):
        S += 1
        print(n, i, i, S, N*N - S + 1)

for i in range(0,N):
    print (a[i])
