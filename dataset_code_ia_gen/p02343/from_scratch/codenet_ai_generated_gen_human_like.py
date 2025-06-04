n, q = map(int, input().split())

parent = [i for i in range(n)]
rank = [0] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return
    
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1

for _ in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        unite(x, y)
    else:
        print(1 if find(x) == find(y) else 0)