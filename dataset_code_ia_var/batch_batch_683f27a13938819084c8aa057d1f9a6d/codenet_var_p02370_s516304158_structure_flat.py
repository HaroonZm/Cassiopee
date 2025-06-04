from collections import deque

v, e = map(int, input().split())
color = ["white" for _ in range(v)]
indeg = [[0, []] for _ in range(v)]
out = []

for _ in range(e):
    s, t = map(int, input().split())
    indeg[s][0] += 1
    indeg[t][1].append(s)

Q = deque([])
for i in range(v):
    if indeg[i][0] == 0 and color[i] == "white":
        Q.append(i)
        color[i] = "gray"
        while Q:
            u = Q.popleft()
            out.append(u)
            for j in indeg[u][1]:
                indeg[j][0] -= 1
                if indeg[j][0] == 0 and color[j] == "white":
                    color[j] = "gray"
                    Q.append(j)

for i in out[::-1]:
    print(i)