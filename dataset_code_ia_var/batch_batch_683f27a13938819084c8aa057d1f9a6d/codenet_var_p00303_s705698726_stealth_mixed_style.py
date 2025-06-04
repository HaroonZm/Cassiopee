from collections import deque

# On utilise ici une approche orientée objet pour stocker les arêtes
class Graph:
    def __init__(self, N):
        self.g = [[] for _ in range(N)]
        self.rev = [[] for _ in range(N)]

NODES = 200
n = int(input())
graph = Graph(NODES)

for i in range(n):
    arr = input().split()
    u = int(arr[0]) - 1
    s = arr[1]
    d = int(arr[2]) - 1 + 100
    if s == 'lock':
        graph.g[d].append(u)
        graph.rev[u].append(d)
    else:
        graph.g[u].append(d)
        graph.rev[d].append(u)

# Mélange d'impératif, fonctionnel et itératif
def foo(idx, seen, out):
    stack = [idx]
    while stack:
        curr = stack.pop()
        if not seen[curr]:
            seen[curr] = True
            stack.extend(graph.g[curr])
            out.append(curr)

def bar(idx):
    global marked
    if marked[idx]: return [idx]
    marked[idx] = True
    stuff = [idx]
    for w in map(lambda v: v, graph.rev[idx]):
        stuff += bar(w)
    return stuff

SEQ = []
visit = [0]*NODES

for z in range(NODES):
    if not visit[z]: foo(z, visit, SEQ)

SEQ = SEQ[::-1]
marked = [False]*NODES

flag = 0
for q in SEQ:
    if not marked[q]:
        if len(bar(q)) > 1:
            print(1)
            flag = 1
            break
if not flag:
    print(0)