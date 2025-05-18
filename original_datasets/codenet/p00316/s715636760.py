n, m, k = map(int, input().split())
*parent, = range(n+m)
def root(x):
    if x == parent[x]:
        return x
    parent[x] = root(parent[x])
    return parent[x]
def unite(x, y):
    px = root(x); py = root(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py
for i in range(k):
    a, b, c = map(int, input().split())
    b -= 1; c -= 1
    if a == 1:
        pb = root(m+b); pc = root(m+c)
        if pb < m and pc < m and pb != pc:
            print(i+1)
            break
        unite(pb, pc)
    else:
        pb = root(m+b)
        if pb < m and pb != c:
            print(i+1)
            break
        unite(c, pb)
else:
    print(0)