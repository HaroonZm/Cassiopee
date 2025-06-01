from sys import stdin

R1 = range(-2, 3)
R2 = range(-1, 2)
A1 = {(x, y) for x in R1 for y in R1 if 3 < x**2 + y**2 < 6}
A2 = {(x, y) for x in R2 for y in R2}

def fi():
    return map(int, next(stdin).split())

def f(p, i):
    x, y = p
    A = (A1, A2)[i > 0]
    return {(x + dx, y + dy) for dx, dy in A if 0 <= x + dx < 10 and 0 <= y + dy < 10}

for line in stdin:
    xf, yf = map(int, line.split())
    if xf == yf == 0:
        break
    next(stdin)  # discard empty line
    tmp = list(map(int, next(stdin).split()))
    PA = zip(tmp[0::2], tmp[1::2])
    FA = {(xf, yf)}
    for ps in PA:
        SA = f(ps, 1)
        FA = {pf for pf in FA for pf_candidate in SA & f(pf, 0)}
        FA &= SA & set(pf for pf in FA for pf_candidate in f(pf,0))
        # optimized update:
        FA = {pf for pf in FA if SA & f(pf, 0)}
    print("OK" if FA else "NA")