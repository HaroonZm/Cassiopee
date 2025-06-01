N, A, B, C, *D = map(int, open(0).read().split())
D.sort(reverse=True)
ans = C // A
s = 0
for i in range(N):
    s += D[i]
    ans = max(ans, (C + s) // (A + (i + 1) * B))
print(ans)