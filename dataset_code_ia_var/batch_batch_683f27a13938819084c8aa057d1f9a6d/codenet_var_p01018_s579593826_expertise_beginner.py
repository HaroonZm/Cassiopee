INF = 10 ** 20
l, n = map(int, input().split())
lst = []
for i in range(n):
    a, b, c = map(int, input().split())
    lst.append([a, b, c])
lst.append([l, 0, INF])
lst.sort()
score = {}
for i in range(len(lst)):
    score[lst[i][0]] = lst[i][0]
for i in range(n + 1):
    p = lst[i][0]
    d = lst[i][1]
    t = lst[i][2]
    for j in range(i + 1, n + 1):
        to_p = lst[j][0]
        if to_p >= p + d:
            cost1 = score[p] + t + to_p - p - d
            cost2 = score[p] + to_p - p
            score[to_p] = min(score[to_p], cost1, cost2)
        else:
            score[to_p] = min(score[to_p], score[p] + to_p - p)
print(score[l])