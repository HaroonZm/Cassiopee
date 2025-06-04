import sys

input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    N, M = map(int, line.split())
    idols = []
    for _ in range(N):
        name = input().rstrip('\n')
        C, V, D, L = map(int, input().split())
        idols.append((C, V, D, L))

    # dp[cost] = (voc, dnc, lks) max sums achievable with cost 'cost'
    dp = [(-1, -1, -1)] * (M + 1)
    dp[0] = (0, 0, 0)
    for C, V, D, L in idols:
        for cost in range(C, M + 1):
            prev = dp[cost - C]
            if prev[0] == -1:
                continue
            cand = (prev[0] + V, prev[1] + D, prev[2] + L)
            cur = dp[cost]
            if cur[0] == -1 or max(cand) > max(cur):
                dp[cost] = cand

    ans = 0
    for voc, dnc, lks in dp:
        if voc == -1:
            continue
        ans = max(ans, max(voc, dnc, lks))
    print(ans)