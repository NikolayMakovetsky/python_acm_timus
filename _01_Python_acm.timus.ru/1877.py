zam_1 = '0a'
zam_2 = '0a'

while zam_1.isdigit() == False or len(zam_1) != 4:
    zam_1 = str(input('Задайте код из 4-х целых чисел для замка №1: '))

while zam_2.isdigit() == False or len(zam_2) != 4:
    zam_2 = str(input('Задайте код из 4-х целых чисел для замка №2: '))

if int(zam_1) % 2 != 0 or int(zam_2) % 2 == 0:
    print('no')

if int(zam_1) % 2 == 0 or int(zam_2) % 2 != 0:
    print('yes')