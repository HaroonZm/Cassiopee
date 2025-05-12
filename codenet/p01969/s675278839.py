from collections import deque
H,W,s,t = input().split()
H = int(H)
W = int(W)
M = [(".") * (W + 2)]
E = {}

for i in range(0,H):
    a = input()
    M.append("." + a + ".")

M.append((".") * (W + 2))
H = H + 2
W = W + 2

for h in range(0,H):
    for w in range(0,W):
        if M[h][w] not in [".","-","|","o"]:
            E[M[h][w]] = [h,w]

G = {k:[] for k in E.keys()}
for e,(h,w) in E.items():
    if M[h][w+2] == "-":
        i = 2
        while M[h][w+i] == "-":
            i += 1

        G[e].append(M[h][w+i+1])

    if M[h][w - 2] == "-":
        i = 2
        while M[h][w - i] == "-":
            i += 1

        G[e].append(M[h][w - i - 1])

    if M[h + 2][w] == "|":
        i = 2
        while M[h + i][w] == "|":
            i += 1

        G[e].append(M[h + i + 1][w])

    if M[h - 2][w] == "|":
        i = 2
        while M[h - i][w] == "|":
            i += 1

        G[e].append(M[h - i - 1][w])

visited = {k:False for k in E.keys()}
Q = deque([[s,0]])
while Q:
    e,c = Q.popleft()
    visited[e] = True
    for ne in G[e]:
        if ne == t:
            print(c+1)
            Q = []
            break

        if visited[ne] == True:
            continue
        else:
            Q.append([ne,c +1])