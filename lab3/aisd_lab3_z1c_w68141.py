def nwdrek2(a, b):
    if b != 0:
        return nwdrek2(b, a % b)
    return a

print(nwdrek2(12, 18))