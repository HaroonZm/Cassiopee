from heapq import heappop, heappush

OUT = 0
IN = 1

def P(i):
    if i % 5 == 1:
        return 31
    else:
        return 3

def M(i):
    return 17 * (i % 2) + 3 * (i % 3) + 19

def check(c, n):
    for i in range(16):
        if ((c >> i) & n) == 0:
            return i
    return None

ans = [-1] * 100 + [0]

eq = []
for i in range(100):
    heappush(eq, (i * 5, i, IN, None))

c = 1 << 17

while len(eq) > 0:
    m, n, et, i = heappop(eq)

    if et == IN:
        p = P(n)
        i2 = check(c, p)
        if n > 0 and ans[n-1] != -1 and i2 is not None:
            c = c | (p << i2)
            ans[n] = m - n * 5
            heappush(eq, (m + M(n), n, OUT, i2))
        else:
            heappush(eq, (m + 1, n, IN, None))
    else:
        p = P(n)
        c = c ^ (p << i)

while True:
    try:
        n = int(input())
        print(ans[n])
    except:
        break