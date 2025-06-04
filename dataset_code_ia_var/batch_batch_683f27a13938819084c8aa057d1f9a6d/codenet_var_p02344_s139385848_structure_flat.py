line = input()
n, q = list(map(int, line.split()))
rel = {}
i = 0
while i < n:
    rel[i] = []
    i += 1
parent = [i for i in range(n)]
rank = [0] * n
weight = [0] * n

def find(x):
    px = x
    path = []
    while parent[px] != px:
        path.append(px)
        px = parent[px]
    for k in path:
        weight[k] += weight[parent[k]]
        parent[k] = px
    return px

_ = 0
while _ < q:
    line = input()
    query = list(map(int, line.split()))
    if query[0] == 0:
        x, y, z = query[1], query[2], query[3]
        rx = find(x)
        ry = find(y)
        if rx != ry:
            if rank[rx] < rank[ry]:
                parent[rx] = ry
                weight[rx] = z - weight[x] + weight[y]
            else:
                parent[ry] = rx
                weight[ry] = -z - weight[y] + weight[x]
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
    elif query[0] == 1:
        x, y = query[1], query[2]
        rx = find(x)
        ry = find(y)
        if rx == ry:
            print(weight[x] - weight[y])
        else:
            print("?")
    _ += 1