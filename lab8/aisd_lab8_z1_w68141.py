import random

def quicksort(l, r, list):
    if l >= r:
        return

    v = list[r]
    p = l

    for j in range(l, r):
        if list[j] < v:
            list[p], list[j] = list[j], list[p]
            p += 1

    list[p], list[r] = list[r], list[p]

    quicksort(l, p - 1, list)
    quicksort(p + 1, r, list)
    return list


def binarysearch(l, r, f, lista):
    l = 0
    r = n - 1
    m = (l + r) // 2
    while l <= r:
        m = (l + r) // 2
        if lista[m] == f:
            return m
        elif lista[m] > f:
            r = m - 1
        else:
            l = m + 1

    return -1

while True:
    n = int(input("Podaj ilość elementów: \n"))
    if n > 0:
        print("Podany element jest poprawny. \n")
        break
    else:
        print("Proszę podać element większy od zera. \n")

while True:
    x = int(input("Podaj element x: \n"))
    y = int(input("Podaj element y: \n"))
    if x <= y:
        break
    else:
        print("Proszę podać element poprawny. \n")

lista = [random.randint(x, y) for i in range(n)]
print(f"Wygenerowana lista: {lista} \n")

quicksort(0, n - 1, lista)
print(f"Posortowana lista: {lista}")
#duży przedział żeby pozbyć się duplikatów

z = int(input("Jaką liczbę szukasz? \n"))
print(f"Liczba {z} znajduje się na pozycji ", binarysearch(0, n, z, lista))