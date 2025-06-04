while True:
    n = int(input())
    n3 = n ** 3
    mn = n3
    if n3 == 0:
        break
    i = 0
    while True:
        i = i + 1
        i3 = i ** 3
        rem = n3 - i3
        if rem < 0:
            break
        j = int((rem) ** (1.0/3))
        if j < i:
            break
        m = n3 - i3 - (j ** 3)
        if m < mn:
            mn = m
    print(mn)