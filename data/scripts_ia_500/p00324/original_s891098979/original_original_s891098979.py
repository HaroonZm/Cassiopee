n = int(input())
D = [int(input()) for i in range(n)]
S = {}

s = ans = 0
S[0] = -1
for i in range(n):
    s += D[i]
    if s in S:
        ans = max(i - S[s], ans)
    else:
        S[s] = i
print(ans)