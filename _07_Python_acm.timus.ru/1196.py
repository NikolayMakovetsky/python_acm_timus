prep = [1054, 1492]
stud = [1492, 65536, 1492, 100]

print("Значения в списках как препода, так и студента могут повторяться!")
print(len(prep),", список препода отсортирован по неубыванию:")
for i in prep:
    print(i)
print(len(stud),", список студента не отсортирован:")
for j in stud:
    print(j)

prep_set = set(prep)
k = 0
for i in range(len(stud)):
    for j in range(len(prep_set)):
        if i == j:
            k += 1
print("Кол-во чисел в списке СТУД, которые также содержатся в списке ПРЕП =",k)
