import sys
from collections import deque

get_input = lambda: sys.stdin.readline()

n, m = [int(s) for s in get_input().split()]
W = [0]
for elem in get_input().split():
    W.append(int(elem))

edges = []
for _ in range(m):
    edges += [tuple(map(int, get_input().split()))]

start = 1

elist = [[] for _ in range(n+1)]
eweight = [0] * (n+1)

def build_graph(edgelist, adjacency, node_degrees):
    for a, b in edgelist:
        for (x, y) in [(a, b), (b, a)]:
            adjacency[x].append(y)
            node_degrees[x] += 1

build_graph(edges, elist, eweight)

# We will use a 'used' list and a queue in an old-fashioned way
used = [0 for _ in range(n+1)]
Q = deque()
for idx in range(1, n+1):
    if eweight[idx] == 1 and idx != start:
        Q.append(idx)
        used[idx] = 1

eweight[start] += 1 << 50
used[start] = True

while len(Q) > 0:
    v = Q.pop()
    eweight[v] -= 1
    for nbr in elist[v]:
        if used[nbr]:
            continue
        eweight[nbr] -= 1
        if eweight[nbr] == 1 and not used[nbr]:
            Q.append(nbr)
            used[nbr] = 1

loop_nodes = [] ; answer = 0
for i in range(1, n+1):
    if eweight[i] != 0:
        loop_nodes.append(i)
        answer += W[i]

score_board = [0]*(n+1)
state = [0]*(n+1)
for ll in loop_nodes:
    score_board[ll] = answer
    state[ll] = 1

Q = deque(loop_nodes)
while Q:
    node = Q.pop()
    for nb in elist[node]:
        if state[nb]:
            continue
        score_board[nb] = W[nb] + score_board[node]
        Q.append(nb)
        state[nb] = 1

final_result = 0
i = 0
while i < len(score_board):
    final_result = max(final_result, score_board[i])
    i += 1

print(final_result)