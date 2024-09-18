n = 6
sek =['1 4 4 4 1 1']
# sek =['1 4 1 5 56 6 1 1 2']

print(n)
print(*sek)

sek_str = str(sek).strip("[]")

import re
numbers = re.findall('\d+',sek_str)

digs = list(map(int, numbers))

door = []
composition = 0
i = 0
while i < len(digs):
    if i == 0 or i == 1:
        composition += digs[i]
        i += 1
    else:
        composition += digs[i]
        door.append(composition)
        del digs[0:1]
        composition = 0
        i = 0
print(door)
print(max(door), door.index(max(door))+2)
