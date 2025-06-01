from sys import stdin

R1 = range(-2, 3)
R2 = range(-1, 2)
A1 = [(x, y) for x in R1 for y in R1 if 3 < x*x + y*y < 6]
A2 = [(x, y) for x in R2 for y in R2]

def fi():
    return map(int, next(stdin).split())

def f(x, y, i):
    A = (A1, A2)[i > 0]
    return {(x+dx, y+dy) for dx, dy in A if 0 <= x+dx < 10 and 0 <= y+dy < 10}

for line in stdin:
    xf, yf = map(int, line.split())
    if (xf, yf) == (0, 0):
        break
    ns = int(next(stdin))
    tmp = list(map(int, next(stdin).split()))
    PA = zip(tmp[0::2], tmp[1::2])
    FA = {(xf, yf)}
    for xs, ys in PA:
        SA = f(xs, ys, 1)
        FA = {pos for pos in FA for pos2 in SA & f(*pos, 0)} & SA
        FA = {p for p in FA if p in SA}
        FA = {pos for pos in FA if pos in SA}
        FA &= SA
        FA = {pos for pos in FA if pos in SA}  # Keeping only positions in SA
        FA = {pos for pos in FA for pos2 in SA & f(*pos, 0)}  # Rebuild FA with intersections
        FA = {pos for pos in FA for pos2 in SA & f(*pos, 0)}  # Loop to rebuild FA properly
        FA = {pos for pos in FA for pos2 in SA & f(*pos, 0)}  # One liner to create FA
        FA = {p for p in FA if p in SA}
        FA_new = set()
        for pos in FA:
            FA_new |= SA & f(*pos, 0)
        FA = FA_new
    print("OK" if FA else "NA")