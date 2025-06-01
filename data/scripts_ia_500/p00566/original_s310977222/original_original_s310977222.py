h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = 1010101010

for i in range(h):
    for j in range(w):
        now = 0
        for k in range(h):
            for l in range(w):
                now += min(abs(i - k), abs(j - l)) * a[k][l]
        
        ans = min(ans, now)

print(ans)