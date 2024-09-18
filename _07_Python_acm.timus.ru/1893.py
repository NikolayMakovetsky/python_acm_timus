
"""--------ПРОВЕРКА ВВОДИМЫХ ДАННЫХ-------"""

seat_val_ec = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
seat_val_bz = ['A', 'B', 'C', 'D', 'E', 'F']
seat_val_pr = ['A', 'B', 'C', 'D']
seat_val = []

row_status = False
sp_status = False

while row_status == False or sp_status == False:
    seat = input("Введите ряд и место в формате 1А/65К:")
    seat_row = seat[:-1]
    seat_place = seat[-1]

    if seat_row.isdigit():
        seat_row = int(seat_row)
        if seat_row < 1 or seat_row > 65:
            print("Неверно введен ряд. Ряд может быть задан от 1 до 65.")
        else:
            row_status = True
    else:
        print("Неверно введен ряд. Ряд представляет собой число от 1 до 65.")
        continue

    if len(seat_place) != 1:
        print("Неверно введено место. Место состоит из одного латинского символа.")
        row_status = False
        continue

    if 0 < seat_row < 3:
        seat_val = seat_val_pr
        for i in seat_val:
            if seat_place == i:
                print(f"ряд = {seat_row}, место = {seat_place}")
                sp_status = True
                break
        else:
            print(f"ряд = {seat_row} - введено верно, место = {seat_place} - введено неверно\n"
                  f"Для рядов 1-2 возможные места: A,B,C,D")
            row_status = False
            continue
    elif 2 < seat_row < 21:
        seat_val = seat_val_bz
        for i in seat_val:
            if seat_place == i:
                print(f"ряд = {seat_row}, место = {seat_place}")
                sp_status = True
                break
        else:
            print(f"ряд = {seat_row} - введено верно, место = {seat_place} - введено неверно\n"
                  f"Для рядов 3-20 возможные места: A,B,C,D,E,F")
            row_status = False
            continue
    elif 20 < seat_row < 66:
        seat_val = seat_val_ec
        for i in seat_val:
            if seat_place == i:
                print(f"ряд = {seat_row}, место = {seat_place}")
                sp_status = True
                break
        else:
            print(f"ряд = {seat_row} - введено верно, место = {seat_place} - введено неверно\n"
                  f"Для рядов 21-65 возможные места: A,B,C,D,E,F,G,H,J,K")
            row_status = False
            continue

"""--------------Вывод результатов-------------"""
print("-----------------------------")

if 0 < seat_row < 3:
    if seat_place == "A" or seat_place == "D":
        print("window")
    else:
        print("aisle")
elif 2 < seat_row < 21:
    if seat_place == "A" or seat_place == "F":
        print("window")
    else:
        print("aisle")
elif 20 < seat_row < 66:
    if seat_place == "A" or seat_place == "K":
        print("window")
    elif seat_place == "C" or seat_place == "D" or seat_place == "G" or seat_place == "H":
        print("aisle")
    else:
        print("neither")


