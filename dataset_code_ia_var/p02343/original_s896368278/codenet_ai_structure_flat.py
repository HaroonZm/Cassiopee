n, q = map(int, input().split())
N = n
parent = list(range(N))
for _ in range(q):
    inputs = input().split()
    com = int(inputs[0])
    x = int(inputs[1])
    y = int(inputs[2])
    # Find root of x
    px = x
    path_to_root_x = []
    while parent[px] != px:
        path_to_root_x.append(px)
        px = parent[px]
    for node in path_to_root_x:
        parent[node] = px
    root_x = px
    # Find root of y
    py = y
    path_to_root_y = []
    while parent[py] != py:
        path_to_root_y.append(py)
        py = parent[py]
    for node in path_to_root_y:
        parent[node] = py
    root_y = py
    if com == 0:
        parent[root_x] = root_y
    else:
        if root_x == root_y:
            print(1)
        else:
            print(0)