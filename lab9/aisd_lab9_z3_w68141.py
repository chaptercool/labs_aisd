import numpy as np


def kreator_grafow():
    typ_grafu = input("Jakiego rodzaju graf chcesz zbudować? (skierowany/nieskierowany): \n")
    ilosc_wierz = int(input("Podaj liczbę wierzchołków: \n"))
    polaczenia = []

    print("Podaj połączenia między wierzchołkami: \n")
    for i in range(ilosc_wierz):
        polaczone_wierz = input(f"Podaj wierzchołki połączone z wierzchołkiem {i + 1} (oddzielone przecinkami): \n")
        polaczenia.append(list(map(int, polaczone_wierz.split(","))))

    return typ_grafu, ilosc_wierz, polaczenia


def druk_macierz_sasiadztwa(typ_grafu, ilosc_wierz, polaczenia):
    print("\nMacierz sąsiedztwa:")
    macierz_sasiadztwa = np.zeros((ilosc_wierz, ilosc_wierz))

    for i in range(ilosc_wierz):
        for j in polaczenia[i]:
            macierz_sasiadztwa[i][j - 1] = 1

    print(macierz_sasiadztwa)


def druk_lista_sasiadztwa(typ_grafu, ilosc_wierz, polaczenia):
    print("\nLista sąsiedztwa:")

    for i in range(ilosc_wierz):
        print(f"Wierzchołek {i + 1}: {polaczenia[i]}")


def malowania_grafu(typ_grafu, ilosc_wierz, polaczenia):
    print("\nInterpretacja graficzna:")
    if typ_grafu == "skierowany":
        symbol_krawedzia = "->"
    else:
        symbol_krawedzia = "--"

    for i in range(ilosc_wierz):
        for j in polaczenia[i]:
            print(f"{i + 1} {symbol_krawedzia} {j}")


typ_grafu, ilosc_wierz, polaczenia = kreator_grafow()
druk_macierz_sasiadztwa(typ_grafu, ilosc_wierz, polaczenia)
druk_lista_sasiadztwa(typ_grafu, ilosc_wierz, polaczenia)
malowania_grafu(typ_grafu, ilosc_wierz, polaczenia)
