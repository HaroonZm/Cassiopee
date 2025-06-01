N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
P.sort()

su = 0
S = -P[0][0]
ans = float('-inf')

for tup in P:
    a, b = tup
    S = min(S, su - a)
    temp = su + b - a - S
    if temp > ans:
        ans = temp
    su += b

print(ans)