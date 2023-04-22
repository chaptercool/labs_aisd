max = 0
n = 1
while n > 0:
    n = int(input("Podaj liczbę: \n"))
    if max < n:
        max = n
        print(max)
print("Znależono maksymalną liczbę spośród podanych przez ciebie: \n", max)