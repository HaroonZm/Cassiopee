import sys
sys.setrecursionlimit(100000)

while True:
    n = int(input())
    if n == 0:
        break

    par = [i for i in range(n + 1)]
    rank = [0 for i in range(n + 1)]

    cell_list = []
    for i in range(n):
        cell = list(map(float, input().split()))
        cell_list.append(cell)

    distance_list = []
    for i in range(n):
        for j in range(i + 1, n):
            cell1 = cell_list[i]
            cell2 = cell_list[j]
            c_dis = 0
            for k in range(3):
                c_dis += (cell1[k] - cell2[k]) ** 2
            c_dis = c_dis ** 0.5 - (cell1[3] + cell2[3])
            if c_dis > 0:
                distance_list.append([c_dis, i, j])
            else:
                distance_list.append([0, i, j])

    distance_list.sort()
    total_dis = 0

    def root(x):
        while par[x] != x:
            x = par[x]
        return x

    def is_same(x, y):
        return root(x) == root(y)

    def unite(x, y):
        x = root(x)
        y = root(y)
        if x != y:
            if rank[x] < rank[y]:
                par[x] = y
            elif rank[x] > rank[y]:
                par[y] = x
            else:
                par[x] = y
                rank[y] += 1

    for dis in distance_list:
        if not is_same(dis[1], dis[2]):
            unite(dis[1], dis[2])
            total_dis += dis[0]

    print(format(total_dis, ".3f"))