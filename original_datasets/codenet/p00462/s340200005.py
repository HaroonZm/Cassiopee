import bisect
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve():
    d = int(input())
    if d == 0:
        return False
    n = int(input())
    m = int(input())
    stores = [int(input()) for _ in range(n-1)]
    stores = [0]+sorted(stores)+[d]

    ret = 0
    for _ in range(m):
        dest = int(input())
        l = bisect.bisect_right(stores, dest)
        dist = min(stores[l]-dest, dest-stores[l-1])
        ret += dist
    return ret

ans = []
while True:
    a = solve()
    if a:
        ans.append(a)
    else:
        break
print("\n".join(map(str, ans)))