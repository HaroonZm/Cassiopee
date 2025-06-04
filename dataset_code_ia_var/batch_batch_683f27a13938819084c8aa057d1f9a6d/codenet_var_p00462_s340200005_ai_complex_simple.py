import bisect
import sys
from itertools import chain, islice, count
sys.setrecursionlimit(1 << 30)
input = sys.stdin.readline

def solve():
    d = int(input())
    if not d: return False
    n, m = map(int, (input(), input()))
    stores = list(map(int, islice((int(input()) for _ in count()), n - 1)))
    wall = lambda x: [0] + sorted(x) + [d]
    stores = wall(stores)
    ret = 0
    def near(x):
        i = bisect.bisect_right(stores, x)
        return min(stores[i] - x, x - stores[i - 1])
    ret = sum(map(near, (int(input()) for _ in range(m))))
    return ret

from functools import partial, reduce
ans = []
while True:
    res = solve()
    ans.append(res) if res else break
print('\n'.join(map(str, ans)))