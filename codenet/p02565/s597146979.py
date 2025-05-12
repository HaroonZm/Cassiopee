import sys

sys.path.append("/home/contestant/.local/lib/python3.8/site-packages")

import networkx as nx

import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, D = [int(x) for x in input().split()]
XY = [[int(x) for x in input().split()] for i in range(N)]

graph = nx.DiGraph()
for i in range(2 * N):
    graph.add_node(i)

# f_i = 0 means choose x for flag i, f_i = 1 means choose y
# Node i is (f_i==0), node (i+N) is (f_i==1)
for i, (x1, y1) in enumerate(XY):
    for j in range(N):
        if i != j:
            x2, y2 = XY[j]
            if abs(x1 - x2) < D:
                # f_i==0 => f_j==1
                graph.add_edge(i, j + N)
            if abs(x1 - y2) < D:
                # f_i==0 => f_j==0
                graph.add_edge(i, j)
            if abs(y1 - x2) < D:
                # f_i==1 => f_j==1
                graph.add_edge(i + N, j + N)
            if abs(y1 - y2) < D:
                # f_i==1 => f_j==0
                graph.add_edge(i + N, j)

SCC = nx.algorithms.components.strongly_connected_components(graph)
assignment = {}
for comp in SCC:
    for x in comp:
        if (x < N and x + N in comp) or (x >= N and x - N in comp):
            print("No")
            exit()
        if x not in assignment:
            assignment[x] = True
            assignment[(x + N) % (2 * N)] = False

print("Yes")
for i in range(N):
    print(XY[i][0] if assignment[i] else XY[i][1])