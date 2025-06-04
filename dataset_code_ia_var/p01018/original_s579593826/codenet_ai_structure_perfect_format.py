INF = 10 ** 20
l, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)] + [[l, 0, INF]]
lst.sort()
score = {}
for p, _, _ in lst:
    score[p] = p
for i in range(n + 1):
    p, d, t = lst[i]
    for j in range(i + 1, n + 1):
        to_p, _, _ = lst[j]
        if to_p >= p + d:
            score[to_p] = min(score[to_p], score[p] + t + to_p - p - d, score[p] + to_p - p)
        else:
            score[to_p] = min(score[to_p], score[p] + to_p - p)
print(score[l])