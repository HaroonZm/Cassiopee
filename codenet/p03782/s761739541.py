from bisect import bisect_left, bisect_right
from itertools import accumulate

def solve():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))

    As.sort()
    i = bisect_left(As, K)
    Bs = As[:i]
    M = len(Bs)

    bitsets = [1<<(K-1)]
    bitset = 1<<(K-1)
    for B in Bs:
        bitset |= bitset>>B
        bitsets.append(bitset)
    bitsetRevs = [1<<(K-1)]
    bitset = 1<<(K-1)
    for B in reversed(Bs):
        bitset |= bitset>>B
        bitsetRevs.append(bitset)
    bitsetRevs.reverse()

    def isOK(x):
        B = Bs[x]
        numRevs = [0] * K
        bitset = bitsetRevs[x+1]
        for s in range(K):
            if bitset & (1<<(K-1-s)):
                numRevs[s] = 1
        accNumRevs = list(accumulate([0]+numRevs))
        bitset = bitsets[x]
        for s in range(K):
            if bitset & (1<<(K-1-s)):
                if accNumRevs[K-s] - accNumRevs[max(0, K-s-B)] > 0:
                    return True
        return False

    ng, ok = -1, M
    while abs(ok-ng) > 1:
        mid = (ng+ok) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

solve()