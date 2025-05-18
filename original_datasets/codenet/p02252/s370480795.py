N, W = map(int, input().split())
R = []
for i in range(N):
    v, w = map(int, input().split())
    R.append((v/w, v, w))
R.sort(reverse=1)
ans = 0
for _, v, w in R:
    c = min(w, W)
    W -= c
    ans += c * v / w
print(ans)