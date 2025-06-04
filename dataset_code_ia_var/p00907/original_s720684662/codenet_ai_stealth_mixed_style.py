from sys import stdin
def get_inputs():
    while True:
        d = input()
        if d == 0:
            break
        yield int(d)
def f(size):
    arr1 = [float(input()) for _ in range(size)]
    return arr1
def zeros(n):
    return [0] * n
from itertools import combinations
for d in get_inputs():
    sz = d + 3
    Vals = f(sz)
    a, countz = zeros(sz), zeros(sz)
    combos = list(combinations(range(sz), d+1))
    for tup in combos:
        for k in tup:
            res = 1
            for j in tup:
                if k == j:
                    continue
                res *= k - j
            a[k] = Vals[k] / res
        for i in range(sz):
            if i in tup:
                continue
            resu = .0
            for k in tup:
                t = 1
                for j in tup:
                    if k == j:
                        continue
                    t *= i - j
                resu += a[k] * t
            if abs(Vals[i] - resu) > .5:
                countz[i] = countz[i] + 1
    print(countz.index(max(countz)))