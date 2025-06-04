# Commence par demander à l'utilisateur d'entrer deux entiers séparés par un espace.
# L'instruction input() lit une ligne de texte depuis l'entrée standard (souvent le clavier).
# split() divise cette chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur (par défaut).
# map(int, ...) convertit chaque sous-chaîne en un entier.
# On affecte ces deux entiers respectivement aux variables n et m :
# n représente le nombre de sommets ou de noeuds.
# m représente le nombre d'arêtes ou de routes.
n, m = map(int, input().split())

# On crée une liste appelée 'roads' qui va contenir, pour chaque sommet, le nombre de routes qui y aboutissent.
# [0 for i in range(n)] crée une liste de zéros de taille n, où chaque élément correspond à un sommet initialisé à zéro.
# La variable 'i' prend chaque valeur de 0 à n-1, mais ici elle n'est pas utilisée à l'intérieur de la compréhension de liste.
roads = [0 for i in range(n)]

# On lance une boucle qui va s'exécuter exactement m fois.
# La variable 'i' prend successivement les valeurs de 0 à m-1.
for i in range(m):
    # À chaque itération, on lit une ligne contenant deux entiers séparés par un espace, qui correspondent aux extrémités d'une route.
    # map(int, input().split()) sépare et convertit cette ligne en deux entiers.
    # On décompose le résultat dans les variables 'a' et 'b'.
    a, b = map(int, input().split())
    
    # On incrémente de 1 la case correspondant au sommet 'a'.
    # En Python, les indices commencent à 0, donc on utilise 'a - 1' pour accéder à la bonne position dans la liste 'roads'.
    roads[a-1] += 1
    
    # De même, on incrémente de 1 la case correspondant au sommet 'b'.
    # Cela prend en compte le fait que la route relie aussi le sommet 'b'.
    roads[b-1] += 1

# Après avoir traité toutes les routes, on souhaite afficher combien de routes (ou connexions) mène à chaque sommet.
# On parcourt la liste 'roads', où chaque élément correspond à un sommet (du 1er au n-ième, selon sa position dans la liste).
for road in roads:
    # Pour chaque valeur (c'est-à-dire pour chaque sommet), on affiche le nombre de routes qui lui sont reliées.
    print(road)