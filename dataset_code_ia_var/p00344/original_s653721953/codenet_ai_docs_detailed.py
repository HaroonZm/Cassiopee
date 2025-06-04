import sys

# Augmente la limite de récursion pour permettre des DFS profonds sur de grands graphes
sys.setrecursionlimit(1000000)

# Lecture du nombre de sommets dans le graphe
n = int(input())

# Lecture des déplacements associés à chaque sommet
alst = list(map(int, input().split()))

# Initialisation de la liste d'adjacence des arcs (arêtes dirigées)
edges = [[] for _ in range(n)]

# Initialisation de la liste d'adjacence des arcs inverses
rev_edges = [[] for _ in range(n)]

# Construction du graphe et de son graphe inversé
for i in range(n):
    # Calcul du sommet d'arrivée en appliquant le déplacement modulo n
    to_node = (i + alst[i]) % n
    edges[i].append(to_node)                   # Ajoute l'arête i -> to_node
    rev_edges[to_node].append(i)               # Ajoute l'arête to_node -> i pour le graphe inverse

def dfs(x, ret, edges, visited):
    """
    Parcours en profondeur classique pour collecter l'ordre post-ordre des sommets.
    
    Args:
        x (int): Le sommet à visiter.
        ret (list): Liste où enregistrer l'ordre post-ordre des sommets.
        edges (list): Liste d'adjacence du graphe.
        visited (list): Liste booléenne marquant les sommets déjà visités.
    """
    visited[x] = True
    # Parcourt toutes les arêtes sortantes du sommet courant
    for e in edges[x]:
        if not visited[e]:
            dfs(e, ret, edges, visited)
    # Ajoute le sommet à la liste une fois tous ses descendants visités
    ret.append(x)

def dfs_rev(x, cycles, rev_edges, visited):
    """
    Parcours en profondeur sur le graphe inversé pour collecter les sommets d'une composante fortement connexe (cycle).
    
    Args:
        x (int): Le sommet à visiter.
        cycles (set): Ensemble qui va contenir tous les sommets appartenant à un cycle.
        rev_edges (list): Liste d'adjacence du graphe inversé.
        visited (list): Liste booléenne marquant les sommets déjà visités dans ce DFS.
    """
    visited[x] = True
    flag = False
    for e in rev_edges[x]:
        if not visited[e]:
            # Ajoute le sommet à l'ensemble de cycles
            cycles.add(e)
            dfs_rev(e, cycles, rev_edges, visited)
            flag = True
        elif x == e:
            # Détecte un auto-cycle (boucle sur lui-même)
            flag = True
    if flag:
        # Si un cycle a été détecté, ajoute le sommet courant à cycles
        cycles.add(x)

# Phase 1 : effectue un DFS pour déterminer l'ordre post-ordre des sommets
order = []
visited = [False] * n
for i in range(n):
    if not visited[i]:
        dfs(i, order, edges, visited)
order.reverse()  # L'ordre inversé du post-ordre donne l'ordre de traitement pour Kosaraju

# Phase 2 : effectue un DFS sur le graphe inversé pour identifier les cycles
visited = [False] * n
cycles = set()  # Ensemble pour stocker tous les sommets appartenant à un cycle
for i in order:
    if not visited[i]:
        dfs_rev(i, cycles, rev_edges, visited)

# Affiche le nombre de sommets appartenant à au moins un cycle
print(len(cycles))