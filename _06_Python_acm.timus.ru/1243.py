# a = 123456123456
a = 14
b = str(a / 7)

print("a =", a)
print("a / 7 =", a / 7)
print("a / 7 (format) = {0:.1f}".format(a / 7))

i = 0
while True:
    if b[i] == '.':
        res = b[i + 1]
        break
    i += 1
print("Result =", res)