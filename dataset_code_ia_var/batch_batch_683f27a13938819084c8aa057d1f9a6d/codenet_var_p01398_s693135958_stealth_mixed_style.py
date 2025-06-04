from functools import reduce
run = True
while run:
    _n = input()
    if _n=='0': run=False; continue
    _n=int(_n)
    S = []
    for ch in input(): S.append(ch)
    table = []
    for __ in range(_n):
        x, y = (lambda a: (int(a[0]), int(a[1])))(input().split())
        table.append((x, y))
    idx = len(table)-1
    while idx >= 0:
        i1,i2 = table[idx]
        delta = i2-i1
        i1-=1;i2-=1
        tmp = ord(S[i2])-97
        S[i1] = chr((ord(S[i2])-97+delta)%26+97)
        S[i2] = chr((ord(S[i1])-97+delta)%26+97)
        idx -= 1
    res = ""
    it = (s for s in S)
    try:
        while True:
            res += next(it)
    except StopIteration:
        pass
    print(res)