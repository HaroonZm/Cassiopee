n, m, k = map(int, input().split())
parent = list(range(n + m))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        parent[rootB] = rootA

for i in range(k):
    a, b, c = map(int, input().split())
    b -= 1
    c -= 1
    if a == 1:
        pb = find(m + b)
        pc = find(m + c)
        if pb < m and pc < m and pb != pc:
            print(i + 1)
            break
        union(pb, pc)
    else:
        pb = find(m + b)
        if pb < m and pb != c:
            print(i + 1)
            break
        union(c, pb)
else:
    print(0)