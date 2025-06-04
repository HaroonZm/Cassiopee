# Ce code résout un problème d’optimisation géométrique en utilisant une variante de la recherche ternaire sur deux dimensions.
# Les commentaires qui suivent expliquent en détail chaque partie, y compris les notions de base.

# On importe le module sys pour pouvoir lire l'entrée standard (stdin, c'est-à-dire l'entrée clavier ou redirigée).
import sys

# On définit une petite valeur epsilon appelée MI, ici utilisée pour déterminer la précision d'arrêt des boucles d'approximation.
# 1e-6 représente 0.000001 et sert comme critère de convergence pour la recherche ternaire.
MI = 1e-6

# Fonction 'calc' qui prend trois arguments :
#   x et y : coordonnées d'un point dans le plan,
#   b : une liste de listes, chaque sous-liste contient trois valeurs représentant un centre (bx, by) et un rayon l.
# Cette fonction calcule, pour le point (x, y), la plus petite valeur de l'expression l**2 - (x-bx)**2 - (y-by)**2
# sur tous les cercles de la liste b.
def calc(x, y, b):
    # Initialisation de la variable 'res' à une très grande valeur (ici 90000).
    # Cela permet de trouver ensuite le minimum entre res et les valeurs calculées.
    res = 90000
    # On boucle sur chaque élément de la liste b
    for bx, by, l in b:
        # On calcule la différence entre le carré du rayon et la distance carrée entre (x, y) et (bx, by)
        d = l**2 - (x - bx)**2 - (y - by)**2
        # Si la valeur obtenue est plus petite que la valeur courante de 'res', on met à jour 'res'
        if d < res:
            res = d
    # Après la boucle, on retourne la plus petite valeur trouvée
    return res

# Fonction 'search_y' qui fixe la coordonnée x et cherche la coordonnée y donnant la plus petite valeur possible.
def search_y(x, b):
    # On initialise la liste p avec 4 valeurs correspondant à des bornes et des points intermédiaires pour y
    p = [-100, -33, 33, 100]
    # On effectue jusqu'à 100 itérations pour raffiner l'approximation. 
    for t in range(100):
        # Si la différence entre la première et la dernière valeur de p devient suffisamment petite, 
        # on considère que la recherche a convergé
        if abs(p[0] - p[3]) < MI:
            # On retourne la moyenne de la valeur de calc pour les deux extrémités
            return (calc(x, p[0], b) + calc(x, p[3], b)) / 2
        # On calcule la fonction objectif pour les deux points intérieurs
        l = calc(x, p[1], b)
        r = calc(x, p[2], b)
        # Selon la comparaison, on élimine une portion de l'intervalle (logique d'une recherche ternaire)
        if l < r:
            # Si la valeur à gauche est plus petite, on élimine le tiers gauche
            p[0] = p[1]
        else:
            # Sinon, on élimine le tiers droit
            p[3] = p[2]
        # On redéfinit les points intermédiaires selon la nouvelle borne
        p[1] = (2 * p[0] + p[3]) / 3
        p[2] = (p[0] + 2 * p[3]) / 3
    # Si la boucle se termine sans converger (peu probable), on retourne toujours la moyenne des extrémités
    return (calc(x, p[0], b) + calc(x, p[3], b)) / 2

# Fonction 'search' qui trouve le meilleur x (et indirectement y via search_y) pour minimiser la fonction
def search(b):
    # On définit à nouveau un intervalle pour x avec des valeurs initiales similaires à search_y
    p = [-100, -33, 33, 100]
    # Jusqu'à 100 itérations pour l'affinement
    for t in range(100):
        # Si l'écart entre les bornes devient assez faible, on estime avoir trouvé une solution assez précise
        if abs(p[0] - p[3]) < MI:
            # On retourne la moyenne de la meilleure valeur pour x aux deux extrémités
            return (search_y(p[0], b) + search_y(p[3], b)) / 2
        # On évalue l'objectif via la recherche de y optimale aux deux points internes de x
        l = search_y(p[1], b)
        r = search_y(p[2], b)
        # Recherche ternaire sur x similaire à la recherche sur y
        if l < r:
            p[0] = p[1]
        else:
            p[3] = p[2]
        # Mise à jour des points du tiers gauche et droit
        p[1] = (2 * p[0] + p[3]) / 3
        p[2] = (p[0] + 2 * p[3]) / 3
    # Retourne la moyenne des deux extrémités évaluées à la fin
    return (search_y(p[0], b) + search_y(p[3], b)) / 2

# Fonction principale pour traiter un cas de test avec n cercles
def solve(n):
    # On construit la liste b qui contiendra n listes, chaque sous-liste contenant trois entiers lus sur stdin
    b = [[int(x) for x in sys.stdin.readline().split()] for i in range(n)]
    # Initialisation d'une variable ans (non utilisée ensuite, elle pourrait être retirée)
    ans = 0
    # On appelle la fonction search pour trouver la meilleure valeur possible (positive ou négative),
    # puis on affiche la racine carrée de cette valeur,
    # car la recherche a été faite sur des carrés pour plus de facilité numérique
    print(search(b) ** 0.5)

# Boucle de traitement des jeux de données jusqu'à ce que zéro soit saisi
while 1:
    # Lecture d’un entier n en entrée
    n = int(sys.stdin.readline())
    # Si n == 0, on sort de la boucle (fin du programme)
    if n == 0:
        break
    # Sinon, on appelle solve pour traiter le cas de test courant
    solve(n)