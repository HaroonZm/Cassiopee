n, m, x = map(int, input().split())
CA = [tuple(map(int, input().split())) for _ in range(n)]

minimum = float("inf")
for i in range(2**n):
    select = [0] * n
    a = [0] * m
    money = 0
    for j in range(n):
        if (i>>j)&1:
            select[n-1-j] = 1
    for i, v in enumerate(select):
        if v == 1:
            money += CA[i][0]
            for j, u in enumerate(CA[i][1:]):
                a[j] += u
    if all(l >= x for l in a):
        minimum = min(minimum, money)
print(-1 if minimum == float("inf") else minimum)