n = int(input("Podaj liczbę do obliczenia: \n"))
s = [0, 0, 0, 0, 0, 0]
for i in range(n):
    if i == 0:
        s.append(1)
    elif i == 1:
        s.append(1)
    else:
        s.append(s[2 * (i - 1)] - s[i - 2])
print(s[n])