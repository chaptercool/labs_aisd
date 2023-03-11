# Proszę odkomentowywać kod, żeby go zatestować

#zadanie1
# import math
#
# a = int(input("Podaj element a: "))
# b = int(input("Podaj element b: "))
# c = int(input("Podaj element c: "))
#
# if a != 0:
#     delta = b * b - 4 * a * c
#
#     if delta > 0:
#         x1 = ((-b - math.sqrt(delta)) / (2 * a))
#         x2 = ((-b + math.sqrt(delta)) / (2 * a))
#         print(x1, x2)
#     elif delta == 0:
#         x11 = -b / 2 * a
#         print(x11)
#
#     else:
#         print("Brak rozwiązań rzeczywistych")

# zadanie2
# n = [2, 4, -1, 5, 8, -5, 6, -3]
# licz = 0
#
# for i in n:
#     if i > 0:
#         continue
#     else:
#         licz += 1
#
# print(f"{licz} elementa(ów) w liście są ujemne")

# zadanie3
# l = [[1, 3, 5], [2, 4, 6]]
# s = int(input("Którą liczbę szukasz?\n"))
#
# for i in l[0]:
#     if i == s:
#         print(f"{s} znajduje się w liście.")
#
#     else:
#         continue
#
# for j in l[1]:
#     if j == s:
#         print(f"{s} znajduje się w liście.")
#
#     else:
#         continue

# zadanie4
# def min_w(t):
#     w = t[0]
#
#     for i in t:
#         if i < w:
#             w = i
#
#     return w
#
# t = [19, 8, 4, -2, -97, 3]
# print(min_w(t))
