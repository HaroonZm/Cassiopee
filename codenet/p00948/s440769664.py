n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]

ans = [1] * (n + 1)

prev = [0] * (n + 1)

xy.sort()
for x, y in xy:

    temp = ans[y] + ans[y + 1] - prev[y]
    ans[y] = temp
    ans[y + 1] = temp
    prev[y] = temp

print(" ".join(list(map(str, ans[1:]))))