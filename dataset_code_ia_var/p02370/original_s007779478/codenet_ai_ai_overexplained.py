# Demander à l'utilisateur de saisir deux entiers sur une même ligne séparés par un espace
# map applique la fonction int à chaque élément de la liste obtenue par input().split()
# input() lit une ligne de texte, split() scinde cette ligne autour des espaces
N, M = map(int, input().split())

# Initialiser une liste vide G qui contiendra N sous-listes (une pour chaque sommet)
# Utilisation de la compréhension de liste : on crée une liste contenant N listes vides []
G = [[] for i in range(N)]

# Boucle pour lire les M lignes suivantes, correspondant aux arêtes du graphe
for i in range(M):
    # Pour chaque ligne, lire deux entiers s et t, correspondant à une arête dirigée de s vers t
    s, t = map(int, input().split())
    # Ajouter le sommet t à la liste des voisins de s (arête dirigée de s vers t)
    G[s].append(t)

# Initialiser une liste ans vide qui servira à stocker l’ordre des sommets pour le tri topologique
ans = []

# Initialiser un ensemble V vide qui servira à mémoriser les sommets déjà visités
# Un ensemble permet de chercher l’appartenance en temps constant
V = set()

# Définir une fonction récursive dfs qui prend un sommet n en paramètre
def dfs(n):
    # Parcourir tous les voisins e accessibles directement à partir de n
    for e in G[n]:
        # Si le voisin e n’a pas encore été visité
        if e not in V:
            # Appeler récursivement dfs sur ce voisin e
            dfs(e)
    # Une fois tous les voisins traités, ajouter n à la liste ans
    ans.append(n)
    # Ajouter le sommet n à l'ensemble V pour marquer qu’il a été visité
    V.add(n)

# Parcourir tous les sommets du graphe, du sommet 0 jusqu’au sommet N-1 inclus
for i in range(N):
    # Si le sommet i n’a pas encore été visité
    if i not in V:
        # Si le sommet i n’a pas encore été visité (redondant, le même test que précédemment)
        if i not in V:
            # Effectuer un parcours en profondeur en partant du sommet i
            dfs(i)
            # Afficher une ligne vide après chaque exploration depuis un sommet non visité
            print()

# Afficher tous les éléments de la liste ans dans l’ordre inverse, séparés par des retours à la ligne
# Le slicing ans[::-1] renverse la liste ans
# L’opérateur * permet de dépaqueter la liste pour fournir ses éléments un par un à la fonction print
# sep="\n" indique que chaque élément doit être affiché sur une nouvelle ligne
print(*ans[::-1], sep="\n")