n = 7
pgv = ["@1", "@2", "@3", "@1", "@2", "@2", "@3"]
print(f"Число записей в тетради Дениса: {n}")
print("Записи: ",*pgv)

a, b, c = 0, 0, 0
for x in pgv:
    if x == "@1":
        a += 1
    if x == "@2":
        b += 1
    if x == "@3":
        c += 1

res = ("@1" if a > c else "@3") if a > b else ("@2" if b > c else "@3")
print(f"Самый популярный вид пингвинов: {res}")