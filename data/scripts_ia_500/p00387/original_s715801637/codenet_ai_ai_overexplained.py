# Demander à l'utilisateur de saisir deux nombres entiers séparés par un espace
# input() lit une ligne de la saisie standard (par exemple, clavier) sous forme de chaîne de caractères
# .split() divise cette chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur
# map(int, ...) applique la fonction int à chacun des éléments de la liste pour les convertir en entiers
# Les deux entiers résultants sont ensuite associés aux variables A et B respectivement via l'affectation multiple
A, B = map(int, input().split())

# Calculer le résultat de l'expression entière suivante : (B + A - 1) // A
# Les parenthèses permettent de changer l'ordre des opérations
# Ici on additionne B + A puis on soustrait 1 du résultat
# L'opérateur // effectue une division entière, c'est-à-dire qu'il retourne le quotient sans la partie décimale
# Ce calcul permet d'obtenir le nombre minimum de fois que A doit être ajouté pour atteindre au moins B
# Enfin, print() affiche la valeur calculée sur la sortie standard (généralement l'écran)
print((B + A - 1) // A)