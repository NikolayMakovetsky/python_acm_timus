ier = "na no ni ki ka ku"
ier_azb = ier.split()
print("Кол-во иероглифов в БД:",len(ier_azb))
for i in ier_azb:
    print(i)

k = input("Введите первый символ нужного иероглифа: ")
print(f"Иероглифы на букву {k}:")
res = []
for i in ier_azb:
    if i[0] == k:
        res.append(i)

res = sorted(res)
for j in res:
    print(j)
