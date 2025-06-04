from itertools import cycle, islice, accumulate
from functools import reduce

N, M = map(int, input().split())
init = lambda x: [x*2, x*2]

def elegant_one(n, m):
    a, b = init(n), init(m)
    def f(x):
        if x[1] <= 0 or x[0] <= 0: return x
        ap = min(n, x[0])
        b1 = x[1] - ap
        x1 = (x[0], b1)
        if b1 <= 0: return (x[0], b1)
        bp = (b1+1)//2
        a2 = x[0] - bp
        x2 = (a2, b1)
        return x2
    x = (a[0], b[1])
    k = 0
    while min(x) > 0:
        x = (x[0], x[1])
        # step1
        ap = min(n, x[0])
        b1 = x[1] - ap
        if b1 <= 0: break
        k += 1
        # step2
        bp = (b1+1)//2
        a2 = x[0] - bp
        if a2 <= 0: break
        k += 1
        x = (a2, b1)
    return k

def elegant_two(n, m):
    a, b = init(n), init(m)
    x = (a[0], b[1])
    k = 0
    while min(x) > 0:
        ap = (x[0]+1)//2
        b1 = x[1] - ap
        if b1 <= 0: break
        k += 1
        bp = min(m, b1)
        a1 = x[0] - bp
        if a1 <= 0: break
        k += 1
        x = (a1, b1)
    return k

print(min(elegant_one(N, M), elegant_two(N, M)))