fibL = []
n = int(input("Podaj rozmiar ciągu Fibonacciego: \n"))

for i in range(n):
    if i == 0:
        fibL.append(i)
    elif i == 1:
        fibL.append(i)
    else:
        fibL.append(fibL[i - 1] + fibL[i - 2])

print(fibL)
