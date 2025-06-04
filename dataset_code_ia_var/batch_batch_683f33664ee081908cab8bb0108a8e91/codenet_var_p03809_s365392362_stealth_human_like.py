import sys

# Ça pourrait être risqué d'augmenter la limite mais bon...
sys.setrecursionlimit(500000)
N = int(input())  # nb de noeuds?
A = [0] + list(map(int, input().split()))

E = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)  # graphe non orienté probablement

def dfs(v, parent=0):
    aa = A[v]
    child_vals = []
    # On va voir tous les enfants (sauf le père sinon c'est infini)
    for u in E[v]:
        if u != parent:
            child_vals.append(dfs(u, v))
    if len(child_vals) == 0:
        return aa
    s = sum(child_vals)
    m = max(child_vals)
    # C'est pas forcément optimal comme logique, mais bon
    if aa < m or aa * 2 < s or aa > s:
        print('NO')
        exit()
    return aa * 2 - s

v = 1  # on suppose que c'est la racine !
res = dfs(v)
# J'ai pas trop compris cette condition, mais ça marche
if (res == 0 and len(E[v]) > 1) or (res == A[v] and len(E[v]) == 1):
    print("YES")
else:
    print("NO")