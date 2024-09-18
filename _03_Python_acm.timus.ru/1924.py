n = int(input("Введите целое число 1 <= n <= 50: "))
uneven = 0

nums = []
for i in range(n):
    nums.append(int(i+1))

for i in nums:
    if i % 2 != 0:
        uneven += 1

if uneven % 2 == 0:
    print('black')
else:
    print('grimy')
