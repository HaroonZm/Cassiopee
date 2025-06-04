n, q = map(int, input().split())
par = [-1] * (n + 1)
size = [1] * (n + 1)

for _ in range(q):
    com, x, y = map(int, input().split())
    # Find roots of x and y
    idx1 = x
    while par[idx1] != -1:
        if par[par[idx1]] != -1:
            par[idx1] = par[par[idx1]]
        idx1 = par[idx1] if par[idx1] != -1 else idx1
    root_x = idx1

    idx2 = y
    while par[idx2] != -1:
        if par[par[idx2]] != -1:
            par[idx2] = par[par[idx2]]
        idx2 = par[idx2] if par[idx2] != -1 else idx2
    root_y = idx2

    if com == 0:
        if root_x != root_y:
            if size[root_x] >= size[root_y]:
                size[root_x] += size[root_y]
                par[root_y] = root_x
            else:
                size[root_y] += size[root_x]
                par[root_x] = root_y
    else:
        if root_x == root_y:
            print(1)
        else:
            print(0)