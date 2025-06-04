def __main47__():
    get = lambda: list(map(int, input().split()))
    n, m = get()
    if not n * m: return False
    l, k = get(), get()
    X = {0: 1}
    for v in k:
        Z = dict(X)
        [Z.setdefault(x + v,1) or Z.setdefault(abs(x - v),1) for x in X]
        Z[v] = 1 if v not in Z else Z[v]
        X = dict(Z)
    unexplored = [q for q in l if q not in X]
    leftover = len(unexplored)
    if not leftover:
        print((0,))
        return True
    countMagic = {}
    for q in unexplored:
        buffer = {}
        [buffer.setdefault(abs(q - x), 1) or buffer.setdefault(q + x, 1) for x in X]
        for key in buffer:
            countMagic[key] = countMagic.get(key, 0) + 1
    res = min([x for x, y in countMagic.items() if y == leftover], default=-1)
    print(res)
    return True

spam = lambda: __main47__()
while spam(): 0