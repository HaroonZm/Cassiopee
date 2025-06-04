# Demande à l'utilisateur d'entrer un entier, puis convertit l'entrée en type int et assigne à la variable n
n = int(input())

# Crée une matrice n x n remplie de zéros pour représenter le graphe (liste d'adjacence)
# Utilise des compréhensions de liste imbriquées
# La liste intérieure : [0 for i in range(n)] crée une ligne de n zéros
# La liste extérieure répète cette ligne n fois pour créer la matrice
m = [[0 for i in range(n)] for j in range(n)]

# Boucle sur chaque nœud du graphe, les indices i vont de 0 à n-1
for i in range(n):
    # Lit une ligne d'input représentant les connexions du nœud i
    # Chaque ligne est : numéro_du_nœud nombre_de_voisins voisin1 voisin2 ...
    # map(int, ...) convertit chaque valeur de la chaîne en entier
    # list(...) transforme cela en liste
    com = list(map(int, input().split()))
    # com[1] = nombre de voisins pour ce nœud, donc on boucle sur chaque voisin
    for j in range(com[1]):
        # com[j+2]-1 correspond à l'indice du voisin (car l'entrée est en base 1, donc -1 pour base 0)
        # On place un 1 dans la matrice pour indiquer la présence d'une arête de i vers ce voisin
        m[i][com[j+2]-1] = 1

# Initialise une liste pour garder la couleur de chaque nœud dans le BFS
# "white" : non découvert, "gray" : découvert mais pas terminé, "black" : terminé
# La liste est de taille n, chaque valeur initialement "white"
color = ["white" for i in range(n)]

# Importe deque de la bibliothèque collections, un type de file efficace pour les BFS
from collections import deque

# Crée une instance de deque pour servir de file d'attente durant l'exploration BFS
queue = deque()

# Initialise une liste pour garder les distances du nœud source vers tous les autres nœuds
# Chaque distance initialement -1 pour signifier qu'elle n'a pas encore été visitée
d = [-1 for i in range(n)]

# Définit la fonction BFS (Breadth First Search), ne prend pas d'arguments
def bfs():
    # Marque le nœud source (indice 0) comme découvert (gray)
    color[0] = "gray"
    # La distance du nœud source à lui-même est 0
    d[0] = 0
    # Ajoute le nœud source (indice 0) à la file d'attente
    queue.append(0)
    # Tant que la file d'attente n'est pas vide, on continue la recherche
    while len(queue) != 0:
        # Retire et retourne le premier élément de la file, le nœud u en cours de traitement
        u = queue.popleft()
        # Parcourt tous les nœuds du graphe pour vérifier s'ils sont voisins
        for i in range(n):
            # Si m[u][i] est vrai (>0 : il y a une arête) ET que le nœud n'a pas encore été découvert
            if m[u][i] and color[i] == "white":
                # Marque le nœud comme découvert (gray)
                color[i] = "gray"
                # La distance à ce nœud est la distance à u plus 1
                d[i] = d[u] + 1
                # Ajoute ce nœud à la file d'attente pour exploration future
                queue.append(i)
        # Marque u comme terminé (black), on n'a plus à s'occuper de lui
        color[u] = "black"

# Appelle la fonction BFS pour effectuer la recherche à partir du nœud 0
bfs()

# Parcourt tous les nœuds du graphe avec des indices i de 0 à n-1
for i in range(n):
    # Affiche l'indice du nœud (en base 1, donc i+1) et la distance du nœud source à ce nœud
    print(i+1, d[i])