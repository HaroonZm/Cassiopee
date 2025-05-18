N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
P.sort()

su = 0
S = -P[0][0]
ans = -10**19
for a, b in P:
    S = min(S, su - a)
    ans = max(ans, su + b - a - S)
    su += b
print(ans)