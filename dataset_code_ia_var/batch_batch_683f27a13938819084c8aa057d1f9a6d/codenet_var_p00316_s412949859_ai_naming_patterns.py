num_nodes, num_edges, num_ops = map(int, input().split())
dsu_parent = [i for i in range(num_nodes)]
dsu_club = [-1 for _ in range(num_nodes)]

def dsu_find(node_idx):
    if dsu_parent[node_idx] != node_idx:
        dsu_parent[node_idx] = dsu_find(dsu_parent[node_idx])
    return dsu_parent[node_idx]

for op_idx in range(1, num_ops + 1):
    op_type, node_a, node_b = map(int, input().split())
    idx_a = node_a - 1
    idx_b = node_b - 1

    if op_type == 1:
        root_a = dsu_find(idx_a)
        root_b = dsu_find(idx_b)
        club_a = dsu_club[root_a]
        club_b = dsu_club[root_b]

        if club_a >= 0 and club_b >= 0 and club_a != club_b:
            print(op_idx)
            break
        if club_a < 0 and club_b >= 0:
            dsu_club[root_a] = club_b
        dsu_parent[root_b] = root_a

    else:
        root_a = dsu_find(idx_a)
        if dsu_club[root_a] < 0:
            dsu_club[root_a] = idx_b
        if dsu_club[root_a] >= 0 and dsu_club[root_a] != idx_b:
            print(op_idx)
            break
else:
    print(0)