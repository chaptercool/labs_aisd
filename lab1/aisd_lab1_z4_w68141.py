def min_w(t):
    w = t[0]

    for i in t:
        if i < w:
            w = i

    return w

t = [19, 8, 4, -2, -97, 3]
print(min_w(t))
