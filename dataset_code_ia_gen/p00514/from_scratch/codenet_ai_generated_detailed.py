import sys

# On lit les entrées n, m, r
n, m, r = map(int, sys.stdin.readline().split())

# Le problème demande de compter combien de combinaisons de perles de
# taille r, avec n couleurs, contiennent au moins m perles de chaque couleur.
# Chaque perle est identifiée seulement par sa couleur, et l'ordre ne compte pas.
# On compte donc les combinaisons avec répétition sous contrainte.

# La condition 0 <= m < n <= r <= 10000 est donnée.

# On cherche le nombre de solutions entières (x_1, x_2, ..., x_n) telles que :
# x_i >= m pour tout i dans [1..n]
# sum x_i = r

# En posant y_i = x_i - m >= 0, alors :
# sum y_i = r - n*m
# Le nombre de solutions est alors le nombre de combinaisons avec répétition de
# n variables non négatives s'additionnant à (r - n*m).

# S'il arrive que (r - n*m) <0, alors il n'y a pas de solution -> 0.

# Formule standard du nombre de combinaisons avec répétition :
# nombre = C((r - n*m) + n -1, n-1)

# Pour calculer cette combinaison rapidement, on utilise une fonction
# factorielle et fonction de combinaison.

# Implémentation efficace avec calcul direct combinaison sans factorielle pour éviter 
# problems de performances sur grands nombres.

def comb(a, b):
    # calcule C(a,b)
    if b > a or b < 0:
        return 0
    if b > a - b:
        b = a - b
    result = 1
    for i in range(1, b+1):
        result = result * (a - b + i) // i
    return result

# Calcul final
reste = r - n*m
if reste < 0:
    # Pas possible d'avoir au moins m perles de n couleurs dans r perles
    print(0)
else:
    # nombre de combinaisons avec répétition
    # C(reste + n -1, n -1)
    print(comb(reste + n -1, n -1))