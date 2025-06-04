from itertools import permutations

n = int(input())
a = tuple(map(int, input().split()))
lst = sorted(a)
p = []
for perm in permutations(lst, n):
    p.append(perm)

j = -1
for idx in range(len(p)):
    ok = True
    for x in range(n):
        if a[x] != p[idx][x]:
            ok = False
            break
    if ok:
        j = idx
        break

if j > 0:
    for v in p[j-1]:
        print(v, end=' ')
    print()
for v in p[j]:
    print(v, end=' ')
print()
if j+1 < len(p):
    for v in p[j+1]:
        print(v, end=' ')
    print()