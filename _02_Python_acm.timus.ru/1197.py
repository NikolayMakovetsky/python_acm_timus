while True:
    N = int(input('Введите целое число тестов (от 1 до 64): '))
    if 1<= N <= 64:
        break

dos = [[2,3,4,4,4,4,3,2],
       [3,4,6,6,6,6,4,3],
       [4,6,8,8,8,8,6,4]]

res = list(0 for i in range(N))

for i in range(N):
    x, y = input('Введите номер ячейки: ')
    y = int(y)
    #s = input('Введите номер ячейки: ')
    #x = s[0]
    #y = int(s[1])

    if x == 'a' or x == 'h':
        res[i] = dos[0][y-1]
    elif x == 'b' or x == 'g':
        res[i] = dos[1][y-1]
    elif x == 'c' or x == 'd' or x == 'e' or x == 'f':
        res[i] = dos[2][y-1]
    else:
        print('Введено неверное значение!')
        break

for j in res:
    print(j)

