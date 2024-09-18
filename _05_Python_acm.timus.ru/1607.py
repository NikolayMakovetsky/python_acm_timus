# a, b, c, d = 150, 50, 1000, 100
a, b, c, d = 1, 1, 10, 1

while True:
    a += b
    c -= d
    if a > c:
        print(a)
        break
