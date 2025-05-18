import itertools
a = list(map(int, input().split()))
b = sum(a)
comb = itertools.combinations(a, 2)
sa = []
for i in comb:
    sa.append(abs(b - 2 *sum(i)))
print(min(sa))