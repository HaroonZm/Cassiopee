import sys
import math

def count_pairs(L):
    res = 1
    n = L
    i = 2
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt > 0:
            res *= (2 * cnt + 1)
        i += 1 if i==2 else 2
    if n > 1:
        res *= 3
    return (res + 1) // 2

for line in sys.stdin:
    L = int(line.strip())
    if L == 0:
        break
    print(count_pairs(L))