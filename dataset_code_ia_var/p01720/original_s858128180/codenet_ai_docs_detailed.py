from collections import deque

# Lecture des entrées : nombre de sommets (n), d'arêtes (m), sommet de départ (s), sommet d'arrivée (t)
n, m, s, t = map(int, input().split())
s -= 1  # Conversion en index 0-based
t -= 1

# Construction de la liste d'adjacence du graphe non orienté
edges = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  # Conversion en index 0-based
    y -= 1
    edges[x].append(y)
    edges[y].append(x)

def dist_from(s):
    """
    Calcule la distance minimale de s à tous les autres sommets dans le graphe.

    Args:
        s (int): index du sommet de départ (0-based).

    Returns:
        list[int]: liste des distances minimales, où la position i contient la
                   distance minimale de s à i (ou une valeur très grande si injoignable).
    """
    INF = 10 ** 20  # Représente l'infini pour l'initialisation
    dist = [INF] * n  # Tableau des distances initialisé à l'infini
    dist[s] = 0       # La distance du sommet de départ à lui-même est 0
    que = deque()
    que.append((0, s))  # Ajout du couple (distance, sommet) à la file

    while que:
        score, node = que.popleft()
        for to in edges[node]:  # Parcourt tous les voisins
            if dist[to] > score + 1:  # Si une meilleure distance est trouvée
                dist[to] = score + 1
                que.append((score + 1, to))  # Ajoute le voisin à traiter
    return dist

# Calcul des distances du sommet s vers tous les autres sommets
dist_from_s = dist_from(s)

# Regroupe les sommets selon leur distance à s dans un dictionnaire
dic1 = {}
for i, d in enumerate(dist_from_s):
    if d in dic1:
        dic1[d].add(i)
    else:
        dic1[d] = {i}

# Calcul des distances du sommet t vers tous les autres sommets
dist_from_t = dist_from(t)

# Regroupe les sommets selon leur distance à t dans un dictionnaire
dic2 = {}
for i, d in enumerate(dist_from_t):
    if d in dic2:
        dic2[d].add(i)
    else:
        dic2[d] = {i}

# Distance minimale entre s et t
st_dist = dist_from_s[t]
ans = 0  # Compteur de paires de sommets à ajouter

# Pour chaque classe de distance depuis s (key), on trouve la classe "another_key"
# telle que pour toute paire (u,v), le chemin s-u-v-t fait exactement st_dist+2.
for key in dic1:
    another_key = st_dist - key - 2  # Calcule la distance cible depuis t
    if another_key in dic2:
        # Multiplie le nombre de sommets à distance key de s
        # par le nombre de sommets à distance another_key de t
        add = len(dic1[key]) * len(dic2[another_key])
        # Retire les cas où une arête directe existe déjà entre u et v (pour éviter les doublons)
        for u in dic1[key]:
            for to in edges[u]:
                if to in dic2[another_key]:
                    add -= 1
        ans += add  # Incrémente le total

# Affiche le résultat final
print(ans)