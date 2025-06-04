n, m = map(int, input().split())
parents = [-1] * n
for _ in range(m):
    a, b = map(int, input().split())
    x = a - 1
    y = b - 1
    stack_x = []
    stack_y = []
    tmp = x
    while parents[tmp] >= 0:
        stack_x.append(tmp)
        tmp = parents[tmp]
    root_x = tmp
    tmp = y
    while parents[tmp] >= 0:
        stack_y.append(tmp)
        tmp = parents[tmp]
    root_y = tmp
    if root_x != root_y:
        if parents[root_x] > parents[root_y]:
            root_x, root_y = root_y, root_x
        parents[root_x] += parents[root_y]
        parents[root_y] = root_x
    for node in stack_x:
        parents[node] = root_x
    for node in stack_y:
        parents[node] = root_y
res = 0
for i in range(n):
    tmp = i
    while parents[tmp] >= 0:
        tmp = parents[tmp]
    root = tmp
    size = -parents[root]
    if size > res:
        res = size
print(res)