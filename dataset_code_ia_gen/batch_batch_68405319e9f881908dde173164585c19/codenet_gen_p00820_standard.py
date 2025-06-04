import sys
import math

def count_representations(n):
    limit = int(math.isqrt(n))
    count = 0
    # a^2 <= n
    for a in range(1, limit+1):
        a2 = a*a
        if a2 == n:
            count += 1
            continue
        for b in range(a, limit+1):
            s = a2 + b*b
            if s > n:
                break
            if s == n:
                count += 1
                continue
            for c in range(b, limit+1):
                t = s + c*c
                if t > n:
                    break
                if t == n:
                    count += 1
                    continue
                d2 = n - t
                d = int(math.isqrt(d2))
                if d >= c and d*d == d2:
                    count += 1
    return count

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(count_representations(n))