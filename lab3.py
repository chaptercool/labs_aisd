#zadanie pierwsze (wersja liniowa niezoptymaizowana)
# def nwditer(a ,b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
#
# nwditer(a, b)

#wersja niezoptymalizowana rekurencyjna
# def nwdrek(a, b):
#     while a != b:
#         if a > b:
#             return nwdrek(a - b, b) #a = a - b
#         else:
#             return nwdrek(a, b - a) #b = b - a
#     return a
#
# print(nwdrek(12, 18))

# wersja zoptymalizowana liniowa
# def nwditer2(a, b):
#     while b != 0:
#         temp = b
#         b = a % b
#         a = temp
#     return a
#
# print(nwditer2(12, 18))

#wersja zoptymalizowana rekurencyja
# def nwdrek2(a, b):
#     if b != 0:
#         return nwdrek2(b, a % b)
#     return a
#
# print(nwdrek2(12, 18))

#silnia
# def silnia(n):
#   if n == 0: return 1
#   else: return n * silnia(n - 1)

#zadanie 4
# def zamiana(liczba):
#     if liczba == 0:
#         return "0"
#     elif liczba == 1:
#         return "1"
#     else:
#         return zamiana(liczba // 2) + str(liczba % 2)
#
# a = int(input("Podaj liczbę dziesiętną: \n"))
# print("Wynik: \n", zamiana(a))