import itertools

n, k = map(int, input().split())

l = range(n)
combs = list(itertools.combinations(l, k))

sumlist = []
for comb in combs:
    total = 0
    for c in comb:
        total += pow(2, c)
    sumlist.append(total)

z = zip(sumlist, combs)
z = sorted(z)

sumlist, combs = zip(*z)

for total, comb in zip(sumlist, combs):
    c_str = ' '.join(str(c) for c in comb)
    print(str(total) + ": " + c_str)