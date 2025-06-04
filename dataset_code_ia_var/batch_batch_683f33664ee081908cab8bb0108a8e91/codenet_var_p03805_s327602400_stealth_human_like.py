import sys
from collections import deque

# Je vais garder ces trucs pour lire plus vite (pas sûr que readline soit très utile ici mais bon...)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, w = map(int, readline().split())  # n = nombre de sommets, w = nombre d'arêtes
g = []  # le graphe vide au début, sera une liste d'adjacence

for _ in range(n):
    g.append([])  # On met n listes vides, une pour chaque sommet

# Ajouter les arêtes
for _ in range(w):
    line = readline().split()
    # On stocke les sommets en commençant à 0 (Python oblige)  
    x, y = map(int, line)
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)  # Graphe non orienté (sinon enlever cette ligne hein)

def dfs():  # un dfs un peu chelou, en fait c'est du BFS avec un deque, mais bon
    total = 0
    # On part du sommet 0, chemin initial : juste le 0
    queue = deque()
    queue.append([0])  # commence toujours par 0 (à changer sinon)

    while queue:
        path = queue.popleft()
        if len(path) == n:
            total += 1
            continue
        # pour chaque voisin
        last = path[-1]
        for v in g[last]:
            # Si déjà dans le chemin, on l'ignore par principe (risque de boucle sinon)
            if v not in path:
                queue.append(path + [v]) # Ajoute le nouveau sommet à la suite du chemin

    return total

print(dfs())
# Bon, ça marche normalement, mais je ne suis pas sûr pour les très grands graphes...