import math

def sieve(n):
    prime = [0, 0]
    prime += [1 for _ in range(n - 1)]
    ub = math.sqrt(n) + 1
    d = 2
    while d <= ub:
        if prime[d] == 0:
            d += 1
            continue
        prod = 2
        while d * prod <= n:
            prime[d * prod] = 0
            prod += 1
        d += 1
    return prime

prime = sieve(50000)

while True:
    m, a, b = map(int, raw_input().split(" "))
    if (m, a, b) == (0, 0, 0):
        break
    rect_max = (0, 0, 0)
    q = m // 2
    while q >= 2:
        if prime[q] == 0:
            q -= 1
            continue
        p = min(m // q + 1, q)
        while p * b >= q * a:
            if prime[p] == 0 or p * q > m:
                p -= 1
                continue
            if rect_max[0] <= p * q:
                rect_max = (p * q, p, q)
            p -= 1
        q -= 1
    print rect_max[1], rect_max[2]