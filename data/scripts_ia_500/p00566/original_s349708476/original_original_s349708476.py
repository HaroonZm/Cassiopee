def cul(x, y):
    res = 0
    for yp in range(H):
        for xp in range(W):
           res += map[yp][xp] * min(abs(y-yp), abs(x-xp))
    return res

H, W = list(map(int,input().split()))
map = [list(map(int,input().split())) for i in range(H)]
ans = cul(0, 0)
for y in range(H):
    for x in range(W):
        ans = min(ans, cul(x, y))
print(ans)