import bisect
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    if N * M == 0:
        return False
    P = [0] + [int(input()) for _ in range(N)]
    k = [P[i] + P[j] for i in range(N) for j in range(i, N)]
    k = sorted(k)
    ret = 0
    for tmp in k:
        if tmp > M:
            break
        r = M - tmp
        l = bisect.bisect_right(k, r)
        if l >= len(k):
            tmp2 = tmp + k[-1]
        elif l != 0:
            tmp2 = tmp + k[l - 1]
        else:
            tmp2 = tmp
        ret = max(ret, tmp2)
    return ret

ans = []
while True:
    ret = solve()
    if ret:
        ans.append(ret)
    else:
        break
print("\n".join(map(str, ans)))