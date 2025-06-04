from itertools import groupby, product, chain
from operator import itemgetter

R = tuple(range(9))

def f1(M):
    global F
    [F.__setitem__(y, [(" " if sum(1 for v in row if v == row[x]) < 2 else "*") if x<len(row) else " " for x in R]) 
     for y, row in enumerate(M)]
    return

def f2(M):
    global F
    for x in R:
        col = tuple(map(itemgetter(x), M))
        [F[y].__setitem__(x, "*" if col.count(col[y]) >= 2 else F[y][x]) for y in R]
    return

def f3(M):
    global F
    for k in R:
        q, r = divmod(k, 3)
        sq = list(chain.from_iterable(M[q*3 + dy][r*3:r*3+3] for dy in R[:3]))
        for j in R:
            m = ((q*3) + j//3, (r*3) + j%3)
            if sq.count(sq[j]) >= 2:
                F[m[0]][m[1]] = "*"
    return

try: input_fn=raw_input
except NameError: input_fn=input

n=int(input_fn())
while n:
    M = [list(map(int, input_fn().split())) for _ in R]
    F = [list(" "*9) for _ in R]
    f1(M)
    f2(M)
    f3(M)
    [print("".join(sum(zip(F[i], map(str, M[i])), ()))) for i in R]
    if n > 1: print()
    n -= 1