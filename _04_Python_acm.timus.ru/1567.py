spam = "pokupaite gvozdi tolko v kompanii gvozdederov i tovarischi!"
a = "adgjmpsvy. "
b = "behknqtwz,"
c = "cfilorux!"

rub = 0
for x in spam:
    if a.find(x) >= 0:
        rub += 1
        continue
    elif b.find(x) >= 0:
        rub += 2
        continue
    elif c.find(x) >= 0:
        rub += 3
        continue
    else:
        print("В сообщении недопустимый символ!")
        break
else:
    print(rub)
