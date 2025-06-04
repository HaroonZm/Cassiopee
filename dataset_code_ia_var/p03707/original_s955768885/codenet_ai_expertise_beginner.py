n, m, q = map(int, input().split())
grid = []
for i in range(n):
    row = input()
    grid.append(row)

node = []
edge_x = []
edge_y = []

node.append([0] * (m + 1))
edge_x.append([0] * m)
edge_y.append([0] * (m + 1))

for i in range(1, n + 1):
    nlist = [0]
    exlist = [0]
    eylist = [0]
    for j in range(1, m + 1):
        # Pour node
        count = nlist[-1] + node[i-1][j] - node[i-1][j-1]
        if grid[i-1][j-1] == "1":
            count += 1
        nlist.append(count)

        # Pour edge_x
        if j < m:
            count_ex = exlist[-1] + edge_x[i-1][j] - edge_x[i-1][j-1]
            if grid[i-1][j-1] == "1" and grid[i-1][j] == "1":
                count_ex += 1
            exlist.append(count_ex)

        # Pour edge_y
        if i < n:
            count_ey = eylist[-1] + edge_y[i-1][j] - edge_y[i-1][j-1]
            if grid[i-1][j-1] == "1" and grid[i][j-1] == "1":
                count_ey += 1
            eylist.append(count_ey)
    node.append(nlist)
    edge_x.append(exlist)
    if i < n:
        edge_y.append(eylist)

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())

    total_nodes = node[x2][y2] - node[x1-1][y2] - node[x2][y1-1] + node[x1-1][y1-1]

    total_edge_y = edge_y[x2-1][y2] - edge_y[x1-1][y2] - edge_y[x2-1][y1-1] + edge_y[x1-1][y1-1]

    total_edge_x = edge_x[x2][y2-1] - edge_x[x1-1][y2-1] - edge_x[x2][y1-1] + edge_x[x1-1][y1-1]

    total_edge = total_edge_x + total_edge_y

    ans = total_nodes - total_edge
    print(ans)