def zamiana(liczba):
    if liczba == 0:
        return "0"
    elif liczba == 1:
        return "1"
    else:
        return zamiana(liczba // 2) + str(liczba % 2)

a = int(input("Podaj liczbę dziesiętną: \n"))
print("Wynik: \n", zamiana(a))