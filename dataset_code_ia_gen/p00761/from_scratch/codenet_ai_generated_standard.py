while True:
    a0, L = input().split()
    if a0 == '0' and L == '0':
        break
    L = int(L)
    seq = []
    a = a0.zfill(L)
    while a not in seq:
        seq.append(a)
        digits = list(a)
        big = int(''.join(sorted(digits, reverse=True)))
        small = int(''.join(sorted(digits)))
        a = str(big - small).zfill(L)
    i = len(seq)
    j = seq.index(a)
    print(j, int(a), i - j)