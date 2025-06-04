import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall

N = int(input())
graph = []
for i in range(N):
    a_list = list(map(int, input().split()))
    row = []
    for j in range(N):
        if i == j:
            row.append(0)
        else:
            row.append(a_list[j])
    graph.append(row)

for i in range(N):
    for j in range(N):
        if i != j and graph[i][j] == 0:
            graph[i][j] = float("inf")

graph = np.array(graph)
w_graph = floyd_warshall(graph, directed=False)

result = 0
for i in range(N):
    w_graph[i][i] = float("inf")
for i in range(N):
    for j in range(i):
        if i == j:
            continue
        if w_graph[i][j] != graph[i][j]:
            print(-1)
            sys.exit()
        use = True
        for k in range(N):
            if k != i and k != j:
                if w_graph[i][j] > w_graph[i][k] + w_graph[k][j]:
                    use = False
                    break
        if use:
            result += w_graph[i][j]
print(int(result))