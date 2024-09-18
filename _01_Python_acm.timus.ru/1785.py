n = 1
while 1 <= n <= 2000:
    n = int(input())
    if n < 0:
        print('Введено отрицательное значение')
    elif n == 0:
        print('Введено нулевое значение')
    elif 1 <= n <= 4:
        print('few')
    elif 5 <= n <= 9:
        print('several')
    elif 10 <= n <= 19:
        print('pack')
    elif 20 <= n <= 49:
        print('lots')
    elif 50 <= n <= 99:
        print('horde')
    elif 100 <= n <= 249:
        print('throng')
    elif 250 <= n <= 499:
        print('swarm')
    elif 500 <= n <= 999:
        print('zounds')
    elif 1000 <= n <= 2000:
        print('legion')
    else:
        print('Введено слишком большое значение')