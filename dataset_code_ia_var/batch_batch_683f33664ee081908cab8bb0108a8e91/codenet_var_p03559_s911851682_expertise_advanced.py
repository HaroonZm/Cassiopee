import sys
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(1 << 25)
readline = sys.stdin.buffer.readline

n = int(readline())
a = sorted(map(int, readline().split()))
b = sorted(map(int, readline().split()))
c = sorted(map(int, readline().split()))

# Pour chaque bi, compter les ci strictement supérieurs à bi
check = [n - bisect_right(c, x) for x in b]
# cumuler les résultats pour accès rapide
cumsum = list(accumulate(reversed(check), initial=0))

ans = sum(cumsum[n - bisect_right(b, x)] for x in a)
print(ans)