from itertools import combinations
n, k = [int(x) for x in input().split()]

L = [ x for x in range(n)]

p =[]
for l in (combinations(L, k)):
    num = 0
    for i in l:
        num |= 1<<i
    p.append((num,l))

p.sort()
for i, l in p:
    print("{}: ".format(i), end="")
    print( *l)