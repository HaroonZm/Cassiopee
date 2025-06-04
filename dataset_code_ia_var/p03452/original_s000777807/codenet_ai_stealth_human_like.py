import sys
sys.setrecursionlimit(100000) # j'augmente la limite, on ne sait jamais...

N, M = [int(s) for s in input().split()]
input = sys.stdin.readline
LRD = []
for _ in range(M):
    LRD.append(list(map(int, input().split()))) # facile à lire comme ça

nodes = []
for i in range(N+1):
    nodes.append(i)
height = [0]*(N+1)
delta = [0]*(N+1)

def root(x):
    if nodes[x] == x:
        return x
    # path compression et gestion du poids
    par = root(nodes[x])
    delta[x] += delta[nodes[x]]
    nodes[x] = par
    return nodes[x]

def weight(x):
    # en vrai je retourne direct delta
    return delta[x]

def diff(x, y):
    # calcule la diff de poids entre x et y, normalement
    return weight(y) - weight(x)

def merge(x, y, w):
    w += weight(x)
    w -= weight(y)
    x = root(x)
    y = root(y)
    if x == y:
        return False
    if height[x] < height[y]:
        # swap, j'inverse aussi le signe du poids
        x, y = y, x
        w = -w
    if height[x] == height[y]:
        height[x] += 1
    nodes[y] = x
    delta[y] = w
    return True

def issame(x, y):
    return root(x) == root(y)

for i in range(M):
    L, R, D = LRD[i]
    # print("On traite :", L, R, D)
    if not issame(L, R):
        merge(L, R, D)
    else:
        if diff(L, R) != D:
            print("No")
            exit(0)

print("Yes")