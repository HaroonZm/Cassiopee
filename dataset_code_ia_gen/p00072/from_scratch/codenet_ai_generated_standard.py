import sys
import math

for line in sys.stdin:
    n = line.strip()
    if not n:
        continue
    n = int(n)
    if n == 0:
        break
    m = int(sys.stdin.readline())
    total = 0
    for _ in range(m):
        a,b,d = sys.stdin.readline().strip().split(',')
        d = int(d)
        total += d // 100 - 1
    print(total)