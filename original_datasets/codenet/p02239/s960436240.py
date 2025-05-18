n = int(input())

m = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    com = list(map(int, input().split()))
    for j in range(com[1]):
        m[i][com[j+2]-1] = 1

color = ["white" for i in range(n)]

from collections import deque
queue = deque()

d = [-1 for i in range(n)]

def bfs():
    color[0] = "gray"
    d[0] = 0
    queue.append(0)
    while len(queue) != 0:
        u = queue.popleft()
        for i in range(n):
            if m[u][i] and color[i] == "white":
                color[i] = "gray"
                d[i] = d[u] + 1
                queue.append(i)
        color[u] = "black"

bfs()
for i in range(n):
    print(i+1, d[i])