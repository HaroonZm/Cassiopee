n = int(input())
D = []
for i in range(n):
    x = int(input())
    D.append(x)

s = 0
ans = 0
S = {}
S[0] = -1

for i in range(n):
    s = s + D[i]
    if s in S:
        length = i - S[s]
        if length > ans:
            ans = length
    else:
        S[s] = i

print(ans)