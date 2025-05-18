#!/usr/bin/env python

"""
input:
3 3
0 1
0 2
1 2

output:
0
"""

import sys

def generate_graph_table(edges):
    for edge in edges:
        source, target = map(int, edge)
        init_adj_table[source].append(target)

    return init_adj_table

def graph_dfs(current, visited, stack):
    if not visited[current]:
        visited[current] = True
        stack[current] = True

        for adj in adj_table[current]:
            if not visited[adj] and graph_dfs(adj, visited, stack):
                return True
            elif stack[adj]:
                return True

    stack[current] = False
    return False

def check_cyclic():
    visited, stack = ([False] * v_num for _ in range(2))
    for v in range(v_num):
        if graph_dfs(v, visited, stack):
            return True
    return False

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    v_num, e_num = map(int, _input[0].split())
    c_edges = map(lambda x: x.split(), _input[1:])

    init_adj_table = tuple(list() for _ in range(v_num))
    adj_table = generate_graph_table(c_edges)

    print(int(check_cyclic()))