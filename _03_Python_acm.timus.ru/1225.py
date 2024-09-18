print('Для выхода введите: 0')
while True:
    N = int(input('Введите N: '))
    m = [2,2]
    for x in range(N-2):
        m.append(m[-2]+m[-1])
    if N != 0:
        print(m[-1])
    else:
        break
print('Благодарим за использование нашего ПО!')
