import sys

def gcd(m, n):
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m

def read_input():
    return sys.stdin.readline()

def solve():
    def to_seconds(h, m, s):
        return 3600*h + 60*m + s

    line = read_input()
    if not line:
        return False
    values = line.split()
    if len(values) < 4:
        return False
    H, h, m, s = map(int, values)
    if H == 0:
        return False

    initial_seconds = to_seconds(h, m, s)
    M = to_seconds(H, 0, 0)
    results = []
    for hour in range(H):
        for minute in range(60):
            p = 3600*hour + 60*minute + 60*H*minute
            q = 119*H - 1
            for d in [-3600*H, 0, 3600*H]:
                p1 = p + d
                q1 = q
                g = gcd(p1, q)
                if g == 0:
                    continue
                p1 = p1 // g
                q1 = q1 // g
                if 0 <= p1 < 60 * q1:
                    left = H * (60 * minute * q1 + p1)
                    right = q1 * (3600 * hour + 60 * minute) + p1
                    if left != right:
                        val = to_seconds(hour, minute, 0) + p1 / q1
                        results.append((val, hour, minute, p1, q1))
    if not results:
        return False
    results.sort(key=lambda x: (x[0] - initial_seconds) % M)
    best = results[0]
    sys.stdout.write("%d %d %d %d\n" % (best[1], best[2], best[3], best[4]))
    return True

while solve():
    pass