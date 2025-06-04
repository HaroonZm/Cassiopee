import itertools as itr

n, m = map(int, input().split())
a = [list(map(float, input().split())) for _ in range(n)]
ans = 0
for p in itr.combinations(a, m):
    sm = 0
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(3):
                sm += (p[i][k] - p[j][k]) ** 2
    ans = max(ans, sm)
print(ans)