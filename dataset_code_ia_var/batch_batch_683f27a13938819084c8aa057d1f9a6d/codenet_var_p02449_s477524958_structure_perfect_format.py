from itertools import permutations

n = int(input())
a = tuple(map(int, input().split()))
p = list(permutations(sorted(a), n))

for i in p:
    if a == i:
        j = p.index(i)
        if j != 0:
            print(*p[j-1])
        print(*i)
        if j + 1 < len(p):
            print(*p[j+1])