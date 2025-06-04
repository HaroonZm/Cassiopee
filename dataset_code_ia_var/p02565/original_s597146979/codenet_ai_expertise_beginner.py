import sys

sys.path.append("/home/contestant/.local/lib/python3.8/site-packages")

import networkx as nx
import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
line = input()
N, D = [int(x) for x in line.split()]
XY = []
for i in range(N):
    row = input()
    arr = [int(x) for x in row.split()]
    XY.append(arr)

g = nx.DiGraph()
for i in range(2 * N):
    g.add_node(i)

for i in range(N):
    x1, y1 = XY[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2 = XY[j]
        if abs(x1 - x2) < D:
            g.add_edge(i, j + N)
        if abs(x1 - y2) < D:
            g.add_edge(i, j)
        if abs(y1 - x2) < D:
            g.add_edge(i + N, j + N)
        if abs(y1 - y2) < D:
            g.add_edge(i + N, j)

components = list(nx.algorithms.components.strongly_connected_components(g))
result = {}
for comp in components:
    for x in comp:
        if x < N and (x + N) in comp:
            print("No")
            sys.exit()
        if x >= N and (x - N) in comp:
            print("No")
            sys.exit()
        if x not in result:
            result[x] = True
            other = (x + N) % (2 * N)
            result[other] = False

print("Yes")
for i in range(N):
    if result[i]:
        print(XY[i][0])
    else:
        print(XY[i][1])