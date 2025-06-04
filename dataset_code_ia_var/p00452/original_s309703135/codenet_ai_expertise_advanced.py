import sys
import bisect
from itertools import combinations_with_replacement, islice

sys.setrecursionlimit(1 << 30)
input = sys.stdin.readline

def solve():
    try:
        N, M = map(int, input().split())
    except ValueError:
        return None
    if not (N and M):
        return None

    P = [0, *islice((int(input()) for _ in range(N)), N)]

    k = sorted({P[i] + P[j] for i, j in combinations_with_replacement(range(N + 1), 2)})
    ret = 0
    for s in k:
        if s > M:
            break
        idx = bisect.bisect_right(k, M - s)
        best = s + k[idx - 1] if idx else s
        ret = max(ret, best)
    return ret

def main():
    results = []
    while True:
        res = solve()
        if res is None:
            break
        results.append(res)
    print(*results, sep='\n')

if __name__ == '__main__':
    main()