from itertools import cycle

while True:
    n = int(input())
    if not n:
        break
    qs = {}
    for i in range(n):
        d, t, *q = (int(s) for s in input().split())
        q = q[t:] + q[:t]
        if d not in qs:
            qs[d] = q
        else:
            qs[d] = [a + b for a, b in zip(qs[d], q)]
    L = 16 * 9 * 5 * 7 * 11
    ps = [13, 17, 19, 23, 1]
    psum = sum(max(qs.pop(i, [0])) for i in ps)
    qmax = max(sum(j) for i, j in zip(range(L-1),
                                      zip(*[cycle(q) for q in qs.values()])
                                      )
               )
    print(psum + qmax)