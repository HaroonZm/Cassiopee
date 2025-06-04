import sys
sys.setrecursionlimit(10**7)

n = int(input())
if n == 1:
    print(0)
    exit()
parents = list(map(int, input().split()))

# Construire l'arbre sous forme de liste d'adjacence
children = [[] for _ in range(n+1)]
for i in range(2, n+1):
    p = parents[i-2]
    children[p].append(i)

for c in children:
    c.sort()

order = []  # ordre de visite selon BFS Foxpower

queue = [1]
idx = 0
while idx < len(queue):
    u = queue[idx]
    idx += 1
    # Ajouter les enfants dans l'ordre
    for v in children[u]:
        queue.append(v)

# Calculer la distance de chaque sommet à la racine
dist = [0]*(n+1)
for i in range(2, n+1):
    dist[i] = dist[parents[i-2]] + 1

# Fonction pour calculer la distance entre deux noeuds donnée leur profondeur et parent
# Pour un arbre non pondéré on peut trouver le plus proche ancêtre commun (LCA),
# mais ici approche débutant, on monte jusqu'à même profondeur
def distance(a, b):
    d = 0
    x = a
    y = b
    # Remonter les deux noeuds jusqu'à même profondeur
    while dist[x] > dist[y]:
        x = parents[x-2]
        d += 1
    while dist[y] > dist[x]:
        y = parents[y-2]
        d += 1
    # Remonter en même temps jusqu'à trouver LCA
    while x != y:
        x = parents[x-2]
        y = parents[y-2]
        d += 2
    return d

total = 0
cur = 1
for i in range(1, len(queue)):
    total += distance(cur, queue[i])
    cur = queue[i]

print(total)