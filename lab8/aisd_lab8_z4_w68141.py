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


lista = []
left = 0
right = 9
for i in range(10):
    lista.append(random.randint(10, 300))

while True:
    n = int(input("Dodaj liczbę do sortowania: \n"))
    lista.append(n)
    print(f"Lista z dodaną liczbą do sortowania: {lista} \n")
    right += 1
    print(f"Posortowana tablica z dodaną liczbą: {quicksort(left, right, lista)} \n")
