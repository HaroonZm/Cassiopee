h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = min(
    sum(
        min(abs(i - k), abs(j - l)) * a[k][l]
        for k in range(h)
        for l in range(w)
    )
    for i in range(h)
    for j in range(w)
)

print(ans)