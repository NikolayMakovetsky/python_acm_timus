f = 1
while 1 <= f <= 11:
    f = int(input())
    if ((12 - f) * 3 / 4) <= 4 and f < 12:
        print("YES")
    elif ((12 - f) * 3 / 4) > 4 and f > 0:
        print("NO")
    else:
        print("Некорректный ввод числа")
