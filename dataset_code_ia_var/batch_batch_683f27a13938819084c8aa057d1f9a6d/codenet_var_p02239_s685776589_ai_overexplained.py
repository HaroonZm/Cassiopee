# Importation de la classe deque depuis le module collections.
# 'deque' est une structure de données optimisée pour ajouter/retirer des éléments à ses deux extrémités.
from collections import deque

# Définition de la fonction BFS (Breadth-First Search).
# Prend en paramètres:
#  - A : une matrice d'adjacence représentant le graphe,
#  - d : une liste des distances initialisées à -1 (ce qui signifie que le sommet n'a pas encore été visité).
def bfs(A, d):
    # Création d'une nouvelle file (deque) pour gérer les nœuds à explorer lors du parcours BFS.
    dq = deque()
    # On ajoute le sommet 0 (le premier sommet, numéroté à partir de 0) à la file.
    dq.append(0)
    # On indique que la distance pour atteindre le sommet 0 depuis lui-même est 0.
    d[0] = 0
    # On continue tant qu'il reste des éléments (nœuds à explorer) dans la file dq.
    while len(dq):
        # On retire (pop) un élément de la fin de la file dq (fonctionne comme une file FIFO à cause de appendleft plus bas).
        v = dq.pop()
        # On parcourt tous les sommets (i) potentiellement connectés à v,
        # en partant du dernier sommet vers le premier (parcours en ordre inverse).
        for i in range(len(A[v]) - 1, -1, -1):
            # On récupère la valeur dans la matrice d'adjacence, qui indique s'il existe un arc entre v et i.
            f = A[v][i]
            # Si la valeur est 1 (donc il existe un arc de v vers i) et que i n'a pas encore été visité (d[i] == -1)
            if f == 1 and d[i] == -1:
                # On met à jour la distance pour atteindre i : c'est la distance de v + 1 (on est à un voisin).
                d[i] = d[v] + 1
                # On insère i au début de la file dq pour l'explorer par la suite.
                dq.appendleft(i)

# Lecture du nombre total de sommets dans le graphe à partir de l'entrée utilisateur.
n = int(input())
# Création d'une liste vide pour accueillir la matrice d'adjacence.
A = []
# On parcourt chaque ligne pour chaque sommet pour construire le graphe.
for _ in range(n):
    # Lecture de la ligne courante d'entrée utilisateur, transformation de chaque élément en entier.
    ss = list(map(int, input().split()))
    # ss[0] correspond au numéro du sommet (1-indexé dans l'entrée), on le convertit en 0-indexé.
    u = ss[0] - 1
    # Initialisation d'une ligne de la matrice d'adjacence remplie de 0 (signifiant aucune connexion).
    row = [0 for _ in range(n)]
    # ss[1] indique le nombre de voisins pour ce sommet.
    for i in range(ss[1]):
        # L'indice 2 + i dans ss contient le numéro du voisin (toujours 1-indexé), on convertit en 0-indexé.
        idx = 2 + i
        # On marque dans la matrice d'adjacence qu'il existe une connexion de u à ce voisin.
        row[ss[idx] - 1] = 1
    # On ajoute la ligne complète décrivant les connexions de u à la matrice d'adjacence.
    A.append(row)

# Initialisation de la liste des distances, -1 signifie que le sommet n'a pas encore été visité.
d = [-1 for _ in range(n)]
# Appel de la fonction BFS pour lancer le parcours du graphe à partir du sommet 0.
bfs(A, d)

# Parcours de la liste des distances 'd' (après BFS)
# La variable i est l'indice du sommet (entre 0 et n-1), t est la distance trouvée.
for i, t in enumerate(d):
    # On affiche le numéro du sommet (on ajoute 1 pour revenir à l'indexation à partir de 1), puis sa distance.
    print(i + 1, t)