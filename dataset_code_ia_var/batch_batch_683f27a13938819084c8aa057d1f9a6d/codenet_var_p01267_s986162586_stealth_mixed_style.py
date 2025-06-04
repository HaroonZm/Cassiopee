def nxtX(xx, aa, bb, cc):
  return (aa*xx + bb) % cc

while True:
    n, a, b, c, x = [int(v) for v in input().split()]
    if n == 0:
        break
    vals = input().split()
    D = []
    for thing in vals:
        D += [int(thing)]
    res, cnt = -1, 0
    i = 0
    while i < 10001:
        if len(D) > 0 and x == D[0]:
            D.pop(0)
        if not D:
            print(i)
            break
        x = nxtX(x, a, b, c)
        i += 1
    else:
        for _ in range(1):
            print(-1)