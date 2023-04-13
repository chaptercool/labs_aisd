n = [2, 4, -1, 5, 8, -5, 6, -3]
licz = 0

for i in n:
    if i > 0:
        continue
    else:
        licz += 1

print(f"{licz} elementa(ów) w liście są ujemne")