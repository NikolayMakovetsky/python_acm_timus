import math

# dano = '2 4'
dano = '1 3'
m = int(dano[0])
n = int(dano[2])
print(m , n)

if m < n:
    x = float(m)
    y = float(n)
else:
    y = float(m)
    x = float(n)

moves = .0
while x != 1:
    x = math.ceil(x / 2)
    moves += 1

while y != 1:
    y = math.ceil(y / 2)
    moves += 1
b = int(moves)

# Тернарный условный оператор
print("[:=[first]") if moves % 2 != 0 else print("[second]=:]")
