from heapq import heappop, heappush
OUT, IN = 0, 1
def P(i):
    return 31 if i % 5 == 1 else 3
def M(i):
    return 17 * (i % 2) + 3 * (i % 3) + 19
def check(c, n):
    for i in xrange(16):
        if (c >> i) & n == 0:
            return i
    return None
ans = [-1] * 100 + [0]
eq = map(lambda i: (i * 5, i, IN, None), xrange(100))
c = 1 << 17
while len(eq) != 0:
    m, n, et, i = heappop(eq)
    if et == IN:
        p = P(n)
        i = check(c, p)
        if ans[n-1] != -1 and i is not None:
            c = c | (p << i)
            ans[n] = m - n * 5
            heappush(eq, (m + M(n), n, OUT, i))
        else:
            heappush(eq, (m + 1, n, IN, None))
    else:
        p = P(n)
        c = c ^ (p << i)
while True:
    try:
        n = input()
        print ans[n]
    except:
        break