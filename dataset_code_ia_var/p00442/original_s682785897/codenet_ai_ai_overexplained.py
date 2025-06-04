import sys  # Importe le module système, qui permet de manipuler certaines fonctionnalités propres à l'interpréteur Python

# Change la limite maximale de récursion (nombre d'appels récursifs autorisés avant une erreur)
sys.setrecursionlimit(100000)  # Ceci pourrait être nécessaire pour des graphes très grands utilisant la récursion

# Lecture du nombre de sommets (V) et du nombre d'arêtes (E) du graphe depuis l'entrée standard (stdin)
V = int(input())  # Demande et lit un entier à l'utilisateur : nombre de sommets
E = int(input())  # Demande et lit un entier à l'utilisateur : nombre d'arêtes

# Initialise une liste vide L qui stockera l'ordre topologique des sommets (séquence vide au début)
L = []

# Crée une liste appelée 'visited' contenant V zéros.
# Cette liste sert à savoir si le sommet i a déjà été visité ou non lors du parcours
# Au départ, aucun sommet n'est visité donc tous les éléments sont à 0
visited = [0 for i in range(V)]  # [0, 0, ..., 0] de taille V

# Crée une liste de listes appelée 'edges', de taille V, initialement vide
# Chaque sous-liste contiendra la liste des sommets accessibles à partir du sommet d'indice i (adjacence)
edges = [[] for i in range(V)]  # [[], [], ..., []] de taille V

# Définition d'une fonction récursive appelée 'visit' qui prend un sommet x en argument
def visit(x):
    # Si le sommet x n'a pas encore été visité (c'est-à-dire visited[x] vaut 0, ce qui correspond à False)
    if not visited[x]:
        # Marquer le sommet x comme visité
        visited[x] = 1
        # Parcourt tous les sommets e accessibles à partir de x (i.e., tous les voisins de x)
        for e in edges[x]:
            visit(e)  # Appelle récursivement la fonction sur chaque voisin e
        # Une fois que tous les descendants de x ont été visités, ajoute x à la fin de la liste L
        L.append(x)
    # (Remarque : si x a déjà été visité, on ne fait rien de plus)

# Lecture des arêtes du graphe (boucle répétée E fois, une fois pour chaque arête)
for i in range(E):
    # Il lit une ligne de deux entiers séparés par un espace, représentant une arête du sommet s vers le sommet t
    s, t = map(int, input().split())
    # Ajoute à la liste des voisins du sommet s-1 (indexation de 0) le sommet t-1
    edges[s - 1].append(t - 1)

# Parcours de tous les sommets du graphe
for i in range(V):
    # Si le sommet i n'a pas encore été visité
    if not visited[i]:
        # Appelle la fonction visit sur ce sommet pour explorer toute sa composante connexe atteignable
        visit(i)

# Après avoir visité tous les sommets et rempli L dans l'ordre de post-traitement,
# on inverse la liste L pour obtenir l'ordre topologique (le dernier traité en premier, etc.)
L.reverse()

# Initialise un drapeau 'flag' à 0 (il servira à détecter si une solution recherchée échoue)
flag = 0

# Parcourt la liste L (qui contient V entiers représentant l'ordre topologique)
for i in range(V):
    # Affiche l'indice du sommet en ajoutant 1 (pour revenir à la numérotation utilisateur à partir de 1, pas 0)
    print(L[i] + 1)
    # On vérifie, pour chaque couple de sommets consécutifs (L[i], L[i+1]) dans l'ordre topologique,
    # que le sommet L[i+1] est bien un successeur de L[i] (c'est-à-dire qu'il existe une arête)
    # On fait cela que si on est pas au dernier sommet et que flag n'a pas encore été activé.
    if not flag and i < V - 1 and (L[i + 1] not in edges[L[i]]):
        # Si ce n'est pas le cas, on positionne flag à 1, indiquant que la propriété attendue échoue
        flag = 1

# Enfin, on affiche la valeur de flag (0 si tout va bien, 1 si une propriété est violée)
print(flag)