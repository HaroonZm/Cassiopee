import itertools

n = int(input())
L = [i for i in range(1, n + 1)]

p = itertools.permutations(L)
L2 = sorted(p)

for i in range(len(L2)):
    print(*L2[i])