# Cycle Detection for a Directed Graph
[vertex, edge] = list(map(int, input("").split()))
array = [[0 for j in range(vertex)] for i in range(vertex)]

for i in range(edge):
    data = list(map(int, input("").split()))
    array[data[0]][data[1]] = 1

visited = [0 for j in range(vertex)]
result = 0

def dfs(node, goal):
    for t in range(vertex):
        visited[node] = 1
        if array[node][t] != 0 and t == goal:
            global result
            result = 1
        if array[node][t] != 0 and visited[t] == 0:
            dfs(t, goal)

for i in range(vertex):
    visited = [0 for j in range(vertex)]
    dfs(i,i)
    if result == 1:
        print(1)
        break

if result == 0:
    print(0)