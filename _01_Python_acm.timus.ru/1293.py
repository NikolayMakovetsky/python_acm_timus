S = 0
N, A, B = map(int, input().split())

if (1 <= N <= 100) and (1 <= A <= 100) and (1 <= B <= 100):
    S = (A * B) * N * 2
    print(S)
else:
    print('Данные введены некорректно')

print('Задача решена верно 11.05.2022')