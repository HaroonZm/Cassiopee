import sys
from math import isinf
from collections import deque

def generate_adj_table(v_table, init_adj_table):
    for each in v_table:
        source, target, cost = map(int, each)
        init_adj_table[source][target] = cost
        init_adj_table[target][source] = cost
    return init_adj_table

def graph_bfs(current, v_num, adj_table):
    queue = deque()
    distance = [float('inf')] * v_num
    distance[current] = 0
    queue.appendleft(current)
    while queue:
        current = queue.popleft()
        for adj, cost in adj_table[current].items():
            if isinf(distance[adj]):
                distance[adj] = distance[current] + cost
                queue.append(adj)
    return distance

def calc_tree_diameter(v_num, adj_table):
    init_v = 0
    distance_1 = graph_bfs(init_v, v_num, adj_table)
    diameter, bridge_v = 0, 0
    for v, dis_1 in enumerate(distance_1):
        if isinf(dis_1):
            continue
        elif diameter < dis_1:
            diameter = dis_1
            bridge_v = v
    distance_2 = graph_bfs(bridge_v, v_num, adj_table)
    diameter = 0
    for dis_2 in distance_2:
        if isinf(dis_2):
            continue
        diameter = max(diameter, dis_2)
    return diameter

def solve():
    _input = sys.stdin.readlines()
    v_num = int(_input[0])
    edges = map(lambda x: x.split(), _input[1:])
    init_adj_table = tuple(dict() for _ in range(v_num))
    adj_table = generate_adj_table(edges, init_adj_table)
    ans = calc_tree_diameter(v_num, adj_table)
    print(ans)
    return None

if __name__ == '__main__':
    solve()