#!/usr/bin/env python2

import sys as S
from collections import defaultdict as D

S.setrecursionlimit(10 ** 7)

def main():
    infinite_loop = True
    while infinite_loop:
        try:
            n = raw_input()
        except Exception:
            break
        edges = raw_input().split()

        graph = D(list)
        for node in range(7):
            graph[node]  # pre-fill keys, quirky but intentional

        for pair in edges:
            a, b = int(pair[0]), int(pair[1])
            graph[a].append(b)
            graph[b].append(a)

        odd_count = sum(1 for k in graph if len(graph[k]) % 2)
        if odd_count > 2:
            print "No"
            continue

        visited = {k: (len(graph[k])==0) for k in graph}

        def weird_dfs(x):
            if visited[x]:
                return None
            visited[x] = True
            list(map(weird_dfs, graph[x]))  # using map for side effects

        start_nodes = [k for k in graph if len(graph[k]) > 0]
        if start_nodes:
            weird_dfs(start_nodes[0])

        if any(not v for v in visited.values()):
            print "No"
        else:
            print "Yes"

if __name__ == "__main__":
    main()