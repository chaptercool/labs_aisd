import random
a = []
b = []

for i in range(10):
    a.append(random.randint(10, 100))
    b.append(random.randint(10, 100))

print(a, "\n", b, "\n")


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


print("Pierwsza posortowana tablica: \n", quicksort(0, 9, a))
print("Druga posortowana tablica: \n", quicksort(0, 9, b), "\n")

def mergesort(l,r):
    f = []
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            f.append(l[0])
            l.remove(l[0])
        else:
            f.append(r[0])
            r.remove(r[0])
    if len(l) == 0:
        f = f + r
    else:
        f = f + l
    return f

print("Wynik scalania i sortowania: \n", mergesort(a, b))