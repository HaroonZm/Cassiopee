n = int(input())
D = [int(input()) for i in range(n)]
S = {}
s = 0
ans = 0
S[0] = -1
for i in range(n):
    s += D[i]
    if s in S:
        if i - S[s] > ans:
            ans = i - S[s]
    else:
        S[s] = i
print(ans)