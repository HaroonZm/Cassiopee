import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Pas de wrappers d'I/O, gestion brute dans le bloc principal: on reste plat
rr = []

while True:
    line = sys.stdin.readline()
    if not line:
        break
    nms = line.strip().split()
    if not nms:
        continue
    n, m = int(nms[0]), int(nms[1])
    if n == 0:
        break
    a = []
    for _ in range(m):
        l = sys.stdin.readline().split()
        c, t, s = int(l[0]), int(l[1]), int(l[2])
        a.append([c, s, t])
    a.sort(reverse=False)
    # Union-Find plat
    size = n+1
    table = [-1 for _ in range(size)]
    def find(x):
        while table[x] >= 0:
            if table[table[x]] < 0:
                x = table[x]
                break
            table[x] = table[table[x]]
            x = table[x]
        return x
    def union(x, y):
        s1 = find(x)
        s2 = find(y)
        if s1 != s2:
            if table[s1] <= table[s2]:
                table[s1] += table[s2]
                table[s2] = s1
            else:
                table[s2] += table[s1]
                table[s1] = s2
            return True
        return False
    b = 0
    ans = -1
    for c, s, t in a:
        if union(s, t):
            b += 1
            if b > (n-1) // 2:
                ans = c
                break
    rr.append(ans)

print('\n'.join(map(str, rr)))