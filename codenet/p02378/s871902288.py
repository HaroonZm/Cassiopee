#!/usr/bin/env python

"""
input:
3 4 6
0 0
0 2
0 3
1 1
2 1
2 3

output:
3
"""

import sys

def generate_adj_table(_edges):
    for edge in _edges:
        vx, vy = map(int, edge)
        init_adj_table[vx].add(vy)

    return init_adj_table

def graph_dfs(current, matching, visited):
    for target in range(y_num):
        if (not visited[target]) and (target in adj_table[current]):
            visited[target] = True
            # matching[target] = -1: target not assigned to any of x
            # graph_dfs(matching[target], matching, visited) = True
            # indicates that source in x has been already assigned to another target in y
            if matching[target] == -1 or graph_dfs(matching[target], matching, visited):
                matching[target] = current
                return True
    return False

def mbm():
    matching = [-1] * y_num
    res = 0
    for source in range(x_num):
        visited = [False] * y_num
        if graph_dfs(source, matching, visited):
            res += 1
    # print(matching)
    return res

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    x_num, y_num, e_num = map(int, _input[0].split())
    edges = map(lambda x: x.split(), _input[1:])

    init_adj_table = [set() for _ in range(x_num)]
    adj_table = generate_adj_table(edges)
    print(mbm())