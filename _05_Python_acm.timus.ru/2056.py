"""Дано"""
mks = [5, 5, 5]
# mks = [3, 3, 3]
# mks = [5,4,3,4,4,3,3,4,5,4]

print("Число экзаменов:", len(mks), "\nОценки:")
tmp = 0
for i in mks:
    tmp += i
    print(i)
av_score = tmp / len(mks)
print("Средний балл: {0:.1f}".format(av_score))


print("-----------------Result-------------------")
for i in mks:
    if i == 3:
        print("None")
        break
else:
    if av_score == 5.0:
        print("Named")
    elif av_score >= 4.5:
        print("High")
    else:
        print("Common")

