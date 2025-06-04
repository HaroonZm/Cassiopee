import itertools
n = input()
a = tuple(map(int, input().split()))
p = sorted(list(itertools.permutations(a)))
i = 0
for idx, val in enumerate(p):
    if val == a:
        i = idx
        break
if i > 0:
    for val in p[i-1]:
        print(val, end=' ')
    print()
for val in p[i]:
    print(val, end=' ')
print()
if i < len(p)-1:
    for val in p[i+1]:
        print(val, end=' ')
    print()