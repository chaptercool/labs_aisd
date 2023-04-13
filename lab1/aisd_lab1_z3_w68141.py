l = [[1, 3, 5], [2, 4, 6]]
s = int(input("Którą liczbę szukasz?\n"))

for i in l[0]:
    if i == s:
        print(f"{s} znajduje się w liście.")

    else:
        continue

for j in l[1]:
    if j == s:
        print(f"{s} znajduje się w liście.")

    else:
        continue