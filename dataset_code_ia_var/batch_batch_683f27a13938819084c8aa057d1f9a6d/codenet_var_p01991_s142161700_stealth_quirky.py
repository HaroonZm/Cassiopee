import sys

# Augmentons l'absurde limite de récursion par curiosité
sys.setrecursionlimit(1234567)

# Alias bizarres pour le fun
vu = lambda x: [False]*x
finito = lambda x: [False]*x
cercle = set()
trace = []

class Fini(Exception): pass

def gogo(G, v, Papa):
    global RRR
    ici[v] = True
    trace.append(v)
    for k in G[v]:
        if k == Papa: continue
        if mort[k]: continue
        if ici[k] and not mort[k]:
            RRR = k
            raise Fini()
        gogo(G, k, v)
    mort[v] = True
    trace.pop()

N = int(input())
GRAFO = [[] for _ in '#' * N]
for _ in range(N):
    aa, bb = map(int, input().split())
    aa -= 1
    bb -= 1
    GRAFO[aa] += [bb]
    GRAFO[bb] += [aa]

ici = vu(N)
mort = finito(N)
RRR = -42

try:
    gogo(GRAFO, 0, 1984)
except Fini:
    pass

for wow in reversed(trace):
    cercle.add(wow)
    if wow == RRR:
        break

Q = 0
for j in input().split():
    if j.strip(): Q = int(j)
    break

i = 0
while i < Q:
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(2 if x in cercle and y in cercle else 1)
    i += 1