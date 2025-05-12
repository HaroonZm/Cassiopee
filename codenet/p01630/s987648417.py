def root(x):
    if x == par[x]:return x
    par[x] = root(par[x])
    return par[x]

def unite(x, y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]: x,y = y,x
    if rank[x] == rank[y]: rank[x] += 1
    par[y] = x

def init(n):
    x = [None] * s
    for i in range(s):
        x[i] = (a[2 * i], a[2 * i + 1])
        if (a[2 * i] == a[2 * i + 1] == "0"):par[s + i] = ss
        if (a[2 * i] == a[2 * i + 1] == "1"):par[s + i] = ss + 1
    for i in range(s):
        for k in range(i + 1, s):
            if x[i] == x[k]:unite(s + i, s + k)

def union(k):
    s = 1 << k
    ss = 1 << k + 1
    x = [None] * (s)
    for l in range(s):
        x[l] = (root(ss + 2 * l), root(ss + 2 * l + 1))
        if (root(ss + 2 * l) == root(ss + 2 * l + 1)):unite(ss + 2 * l, s + l)
    for i in range(s):
        for l in range(i + 1, s):
            if x[i] == x[l]:
                if root(i) != root(l):unite(s + i, s + l)

n = int(input())
s = 1 << n - 1
ss = 1 << n 
par = [i for i in range(ss)] + [ss, ss + 1]
rank = [0] * (ss + 2)
a = input()
init(n)

for k in range(n - 2, -1, -1):union(k)

print(len(list(set(par))) - 3)