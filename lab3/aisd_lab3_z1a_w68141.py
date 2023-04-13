def nwdrek(a, b):
    while a != b:
        if a > b:
            return nwdrek(a - b, b) #a = a - b
        else:
            return nwdrek(a, b - a) #b = b - a
    return a

print(nwdrek(12, 18))