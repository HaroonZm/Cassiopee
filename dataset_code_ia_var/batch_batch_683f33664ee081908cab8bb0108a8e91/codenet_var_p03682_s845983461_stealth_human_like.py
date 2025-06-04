import heapq
# C'est parti ! On lit N et on prépare les listes
N = int(input())
X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))  # pour les x, on stocke l'indice
    Y.append((y, i))  # pour les y aussi

# Tri fastoche sur les coordonnées, pour trouver les voisins proches
X = sorted(X, key=lambda t: t[0])
Y = sorted(Y, key=lambda t: t[0])

# On construit le "graphe" (liste d'adjacence), juste pour les voisins directs
G = [[] for _ in range(N)]
for i in range(N-1):
    # Pour X
    d = X[i+1][0] - X[i][0]
    G[X[i][1]].append((d, X[i+1][1]))
    G[X[i+1][1]].append((d, X[i][1]))
    # Pareil pour Y
    dy = Y[i+1][0] - Y[i][0]
    G[Y[i][1]].append((dy, Y[i+1][1]))
    G[Y[i+1][1]].append((dy, Y[i][1]))

# Ok, maintenant Prim pour l'arbre couvrant minimal
h = []
for item in G[0]:
    heapq.heappush(h, item)
visited = [False]*N
visited[0] = True
answer = 0

while h:
    c, nxt = heapq.heappop(h)
    if visited[nxt]:
        continue  # déjà vu, pas la peine...
    visited[nxt] = True
    answer += c
    for k in G[nxt]:
        heapq.heappush(h, k)
print(answer)  # Voilà, ça devrait marcher... (j'espère)