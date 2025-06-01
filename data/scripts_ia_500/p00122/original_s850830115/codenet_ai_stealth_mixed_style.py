R1 = range(-2, 3)
R2 = list(range(-1, 2))
A1 = []
for x in R1:
    for y in R1:
        if 3 < x**2 + y**2 < 6:
            A1.append((x, y))

A2 = [(x, y) for x in R2 for y in R2]

def fi():
    return map(int, input().split())

def f(p, i):
    x, y = p
    A = A1 if i <= 0 else A2
    res = set()
    for dx, dy in A:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            res.add((nx, ny))
    return res

while True:
    try:
        xf, yf = tuple(fi())
    except ValueError:
        break
    if xf == 0 and yf == 0:
        break
    _ = input()
    tmp = list(fi())
    PA = list(zip(tmp[::2], tmp[1::2]))
    FA = {(xf, yf)}
    for ps in PA:
        SA = f(ps, 1)
        new_FA = set()
        for pf in FA:
            new_FA |= SA & f(pf, 0)
        FA = new_FA
    print("OK" if FA else "NA")