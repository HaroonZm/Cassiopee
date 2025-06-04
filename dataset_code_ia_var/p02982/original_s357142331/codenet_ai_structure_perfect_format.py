n, d = map(int, input().split())
l = [[] for _ in range(n)]
for i in range(n):
    l[i] = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        c = 0
        for h in range(d):
            c += (l[i][h] - l[j][h]) ** 2
        if (int(c ** 0.5)) ** 2 == c:
            ans += 1
print(ans)