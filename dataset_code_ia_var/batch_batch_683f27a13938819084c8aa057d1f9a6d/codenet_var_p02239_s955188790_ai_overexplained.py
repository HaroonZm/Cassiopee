# Demande à l'utilisateur d'entrer un entier n et convertit l'entrée (qui est une chaîne de caractères) en entier
n = int(input())

# Crée une liste vide, G, qui va représenter le graphe comme une liste d'adjacence.
# Pour chaque noeud (il y a n noeuds), on ajoute une liste vide dans G pour stocker ses voisins (ses connexions).
G = [[] for i in range(n)]

# Crée une liste Q qui représente la file d'attente utilisée pour la recherche en largeur (Breadth-First Search, BFS).
# Initialise Q avec 1, ce qui veut dire que l'exploration commence au noeud numéro 1 (noté 1 ici, mais les listes Python utilisent des indices à partir de 0).
Q = [1]

# Crée une liste d qui gardera la distance minimale depuis le noeud source (ici, noeud 1, index 0) jusqu'à chaque noeud.
# Initialise chaque valeur de la liste à -1, ce qui indique que les distances ne sont pas encore calculées.
d = [-1] * n

# Définit la distance du noeud source (noeud 1, index 0) à lui-même comme 0.
d[0] = 0

# Crée une liste visited dont chaque élément indique si le noeud correspondant a déjà été visité.
# Tous les éléments sont initialement False car aucun noeud n'a été visité.
visited = [False] * n

# Marque le noeud source (index 0) comme visité. Important pour ne pas revisiter ce noeud.
visited[0] = True

# Boucle sur chacun des n noeuds pour lire leurs listes d'adjacence depuis l'entrée utilisateur.
for i in range(n):
    # Pour chaque noeud, lit une ligne qui devrait représenter les connexions de ce noeud.
    # .split() sépare la ligne en morceaux (mots, nombres séparés par espace).
    # On prend tout à partir du 3ème élément avec [2:], car en général les deux premiers éléments ne sont pas des voisins.
    arr = [int(x) for x in input().split()[2:]]
    # Ajoute chaque voisin (appelé l ici, pour chaque élément dans arr) à la liste d'adjacence du noeud i.
    for l in arr:
        G[i].append(l)
        # Note : Il y a un commentaire #G[l-1].append(i+1), qui si décommenté rendrait le graphe non orienté.

# Initialise la variable kyori à 0. Cette variable n'est pas utilisée plus loin, mais elle pourrait servir à stocker la distance maximale atteinte.
kyori = 0

# Commence la boucle principale de la BFS, qui continue tant que la file d'attente Q n'est pas vide (c'est-à-dire qu'il reste des noeuds à explorer).
while len(Q) != 0:
    # En option : pouvait imprimer la file Q ou la liste visited pour voir l'avancement.
    # Récupère et enlève le premier élément de Q (Q.pop(0)), c'est le noeud qu'on explore actuellement.
    v = Q.pop(0)
    # Parcourt chaque voisin (chaque j) du noeud courant v-1 (soustraction car liste indexée à 0 mais entrées à partir de 1).
    for j in G[v-1]:
        # Vérifie si ce voisin a déjà été visité.
        if visited[j-1]:
            # Si oui, saute ce voisin sans faire de mise à jour.
            continue
        else:
            # Sinon, on met à jour sa distance comme étant celle du noeud actuel + 1.
            d[j-1] = d[v-1] + 1
            # Ajoute ce voisin à la file Q, ce qui veut dire qu'il sera exploré plus tard.
            Q.append(j)
            # Marque ce voisin comme visité pour éviter de le rajouter plusieurs fois.
            visited[j-1] = True

# Après avoir calculé toutes les distances, boucle sur tous les noeuds.
for a in range(n):
    # Affiche l'indice du noeud (ajoute 1 car les indices commencent à 0) et sa distance depuis le noeud source.
    print(a+1, d[a])