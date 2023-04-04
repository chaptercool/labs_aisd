# zadanie 1
# fibL = []
# n = int(input("Podaj rozmiar ciągu Fibonacciego: \n"))
#
# for i in range(n):
#     if i == 0:
#         fibL.append(i)
#     elif i == 1:
#         fibL.append(i)
#     else:
#         fibL.append(fibL[i - 1] + fibL[i - 2])
#
# print(fibL)

#zadanie 2
# n = int(input("Podaj rozmiar ciągu Fibonacciego: \n"))
# fibL = [[0] * n for i in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i > 0 and j == 0:
#             fibL[i][j] = 0
#         elif i == 0 and j > 0:
#             fibL[i][j] = 1
#         else:
#             fibL[i][j] = (fibL[i - 1][j] + fibL[i][j - 1]) / 2
#
#
# for row in fibL:
#     print('    '.join([str(elem, 2) for elem in row]))

# zadanie 3
n = int(input("Podaj liczbę do obliczenia: \n"))
s = []
for i in range(n):
    if i == 0:
        s.append(1)
    elif i == 1:
        s.append(1)
    else:
        s.append(s[2 * (i - 1)] - s[i - 2])
print(s)