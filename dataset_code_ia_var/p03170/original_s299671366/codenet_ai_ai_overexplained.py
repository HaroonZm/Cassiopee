import sys  # Importe le module sys, qui fournit un accès à certaines variables et fonctions utilisées ou maintenues par l’interpréteur Python

input = sys.stdin.readline  # Remplace la fonction d'entrée standard input() par sys.stdin.readline, qui lit une ligne entière plus rapidement

n, k = map(int, input().split())
# Prend une ligne d'entrée, la découpe sur les espaces, convertit chaque morceau en entier
# Les deux premiers entiers lus sont respectivement stockés dans n (nombre d'éléments) et k (somme cible du jeu)

a = tuple(map(int, input().split()))
# Prend la ligne suivante d'entrée, la découpe sur les espaces, convertit chaque morceau en entier, puis la transforme en tuple (tableau immuable)
# Cela donne la liste de coups possibles que chaque joueur peut jouer à chaque tour

dp = [False] + [True] * k
# On crée une liste appelée dp (abréviation de « dynamic programming ») pour mémoriser les états gagnants/perdants jusqu'à la somme k
# dp[i] vaudra True si la position i est une position gagnante pour le joueur courant, et False sinon
# On initialise dp[0] = False, car si aucune pierre n'est présente (i.e., 0), le joueur courant ne peut pas jouer (= il perd), donc c'est une position perdante
# Les autres positions (de 1 à k) sont initialisées à True de façon temporaire (elles seront recalculées dans la boucle)

for i in range(1, k + 1):  # Parcours toutes les sommes de 1 jusqu'à k (inclus) pour remplir la table dp
    judge = False  # On initialise une variable juge (judge) à False ; elle indiquera si au moins un coup mène à une position perdante pour l'adversaire
    for j in range(n):  # On parcourt tous les coups possibles (il y a n coups)
        # On regarde si le coup a[j] est possible (i.e., ne descend pas en dessous de zéro)
        # et si, après avoir effectué ce coup, la position obtenue est une position perdante pour l'adversaire
        if i - a[j] >= 0 and not dp[i - a[j]]:
            # Si c'est le cas, cela signifie que depuis l'état i, le joueur courant peut forcer son adversaire à une position perdante
            # Donc l'état i est une position gagnante pour le joueur courant
            judge = True  # On l’indique en mettant judge à True
            # On ne fait pas de break car il faut vérifier tous les coups possibles, même si ce n'est pas strictement nécessaire ici
    dp[i] = judge  # Après avoir testé tous les coups pour l'état i, on stocke le résultat dans dp[i]

# Après avoir rempli la table dp jusqu'à l'indice k, on vérifie si la position de départ (somme k) est gagnante ou perdante

if dp[k]:  # Si dp[k] est True, alors le joueur qui joue en premier peut gagner avec la somme k
    print('First')  # Affiche 'First' pour indiquer que le premier joueur a une stratégie gagnante
else:  # Sinon, le joueur qui commence n’a pas de stratégie gagnante
    print('Second')  # Affiche 'Second' pour indiquer que c’est le deuxième joueur qui peut gagner s’il joue de façon optimale