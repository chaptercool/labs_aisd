def nwditer2(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(nwditer2(12, 18))