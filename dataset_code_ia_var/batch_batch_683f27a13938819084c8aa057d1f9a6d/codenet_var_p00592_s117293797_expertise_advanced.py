from functools import partial

def cv(t):
    return (t // 100) * 60 + t % 100

while True:
    n, p, q = map(int, input().split())
    if n == 0:
        break
    v = [0] * 1440
    for _ in range(n):
        k = int(input())
        a = tuple(map(int, input().split()))
        intervals = zip(a[::2], a[1::2])
        for start, end in intervals:
            for l in range(cv(start), cv(end)):
                v[l] += 1
    p_cv, q_cv = cv(p), cv(q)
    from itertools import groupby
    max_gap = max((len(list(group)) for key, group in groupby((v[i] < n for i in range(p_cv, q_cv))) if key), default=0)
    print(max_gap)