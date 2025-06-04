import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    P = [int(input()) for _ in range(N)]
    dp = {0}
    for _ in range(4):
        ndp = set(dp)
        for s in dp:
            for p in P:
                if s + p <= M:
                    ndp.add(s + p)
        dp = ndp
    print(max(dp))