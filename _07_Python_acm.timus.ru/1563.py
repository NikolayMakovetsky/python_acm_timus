shps = ["ESPRIT", "Nice Connection", "Camelot",
        "Adilisik", "Lady and Gentleman City", "MEXX",
        "Camelot", "Sultanna Frantsuzova", "Camaieu",
        "MEXX", "Axara", "Camelot"]

print(len(shps))
for i in shps:
        print(i)

shps_set = set(shps)
print("Непосещенных Анжелой магазинов:",len(shps) - len(shps_set))