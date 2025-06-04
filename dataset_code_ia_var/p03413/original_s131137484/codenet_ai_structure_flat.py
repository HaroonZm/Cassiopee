import numpy as np

n = int(input())
a = [int(x) for x in input().split()]
best = int(-1e10)
solution = []

for p in range(2):
    c = a.copy()
    indexes = list(range(p, n, 2))
    if len(indexes) == 0:
        continue
    maks = max([c[i] for i in indexes])
    if maks <= 0:
        chosen = set([next((i for i in indexes if c[i] == maks))])
    else:
        chosen = set([i for i in indexes if c[i] > 0])
    is_chosen = [(i in chosen) for i in range(n)]
    tot = sum([c[i] for i in chosen])
    res = []
    i = n - 1
    while i >= 0:
        if not is_chosen[i]:
            if i == 0 or i + 1 == len(c):
                res += [i]
                del c[i]
                del is_chosen[i]
            elif is_chosen[i - 1] == is_chosen[i + 1]:
                res += [i]
                c[i - 1] += c[i + 1]
                del c[i + 1]
                del c[i]
                del is_chosen[i + 1]
                del is_chosen[i]
        i -= 1
        if i >= len(c):
            i = len(c) - 1
    for end in (0, ):
        while len(c) > 1 and not is_chosen[end]:
            res += [end]
            del c[end]
            del is_chosen[end]
    if tot > best:
        best = tot
        solution = (np.array(res) + 1).tolist()

print(best)
print(len(solution))
for x in solution:
    print(x)