from functools import reduce
from itertools import chain, groupby, repeat, starmap, islice, filterfalse
while True:
    n = int(input())
    if n == 0: break
    genial = lambda: (w for msg in (input().split() for _ in range(n)) for w in msg)
    dic = dict()
    list(map(lambda w: dic.__setitem__(w, dic.get(w, 0) + 1), genial()))
    alpha = input()
    pairs = list(dic.items())
    comparator = lambda z: (z[1], z[0])
    sorted_pairs = sorted(pairs, key=comparator, reverse=True)
    answer = list(map(lambda p: p[0], filter(lambda x: x[0][0] == alpha, enumerate(sorted_pairs))))
    print(" ".join(answer) if answer else "NA")