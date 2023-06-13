def quicksort(l, r, list): #na początku robimy sortowanie dla uproszczenia działań
    if l >= r:
        return

    v = list[r]
    p = l

    for i in range(l, r):
        if list[i] < v:
            list[p], list[i] = list[i], list[p]
            p += 1

    list[p], list[r] = list[r], list[p]

    quicksort(l, p - 1, list)
    quicksort(p + 1, r, list)
    return list


lista = [98, 16, 39, 55, 65, 5, 44, 74, 87, 47]

print(f"Nieposortowana tablica: {lista} \n")
print(f"Posortowana tablica: {quicksort(0, 9, lista)} \n")
sort_list = quicksort(0, 9, lista)
minimum = sort_list[0]
maksymum = sort_list[-1]

print(f"Wartość minimalna to {minimum}, a maksymalna - {maksymum} \n")

sort_list[0], sort_list[-1] = sort_list[-1], sort_list[0]
sort_list[0], sort_list[-2] = sort_list[-2], sort_list[0]

print(sort_list)