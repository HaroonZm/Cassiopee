import itertools

n = input()
a = tuple(map(int, input().split()))
p = sorted(list(itertools.permutations(a)))
i = p.index(a)
if i > 0:
    print(*p[i - 1])
print(*p[i])
if i < len(p) - 1:
    print(*p[i + 1])