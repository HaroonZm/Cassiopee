n, q = map(int, input().split())
par = [i for i in range(n+1)]
rank = [0] * (n+1)
ans_list = []
for _ in range(q):
    com, x, y = map(int, input().split())
    stack = []
    # find for x
    xi = x
    while par[xi] != xi:
        stack.append(xi)
        xi = par[xi]
    root_x = xi
    for s in stack:
        par[s] = root_x
    # find for y
    stack = []
    yi = y
    while par[yi] != yi:
        stack.append(yi)
        yi = par[yi]
    root_y = yi
    for s in stack:
        par[s] = root_y
    if com == 1:
        ans_list.append(root_x == root_y)
    else:
        if rank[root_x] < rank[root_y]:
            par[root_x] = root_y
        else:
            par[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
for num in ans_list:
    print(int(num))