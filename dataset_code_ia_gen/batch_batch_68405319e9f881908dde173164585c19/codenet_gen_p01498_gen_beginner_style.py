import sys
sys.setrecursionlimit(10**7)

N, W, H = map(int, input().split())
slimes = [tuple(map(int, input().split())) for _ in range(N)]

# On veut le minimum de mouvements pour unir toutes les slime, en déplaçant un slime à la fois.
# Chaque slime peut se déplacer en ligne droite jusqu'à rencontrer un autre slime ou un mur.

# Remarque: une approche simple est d'utiliser l'arbre couvrant minimum (MST) complet avec la distance 
# de Manhattan comme poids. Ici la distance est un peu spéciale car un slime peut aller jusqu'à toucher 
# un autre slime sans s'arrêter entre. 
# Mais en déplaçant chaque slime en ligne droite, la distance minimale entre deux slimes est 
# la distance de Manhattan entre eux moins 1 (parce qu'ils s'unissent dès qu'ils se rencontrent).
# Pour des déplacements jusqu'au mur ou jusqu'à toucher un slime, cela donne une distance effective égale 
# à la distance de Manhattan entre deux slimes moins 1.

# Donc on considère un graphe complet entre slimes avec poids = distance Manhattan - 1
# Le nombre minimum de moves est le poids total d'un MST sur ce graphe.

# Implémentation naïve pour débutant: calculer toutes les distances et faire un MST via Kruskal.
# Cela sera lent mais acceptable comme solution naïve.

# Calcul des arêtes
edges = []
for i in range(N):
    x1, y1 = slimes[i]
    for j in range(i+1, N):
        x2, y2 = slimes[j]
        dist = abs(x1 - x2) + abs(y1 - y2) - 1
        edges.append((dist, i, j))

# Tri des arêtes par poids
edges.sort()

# Union-Find simple pour MST
parent = [i for i in range(N)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    parent[b] = a
    return True

result = 0
count = 0
for dist, a, b in edges:
    if union(a, b):
        result += dist
        count += 1
        if count == N - 1:
            break

print(result)