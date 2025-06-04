# Demande à l'utilisateur d'entrer une valeur par le biais du clavier.
# La fonction input() récupère une chaîne de caractères saisie par l'utilisateur.
# La fonction int() convertit cette chaîne en un entier (nombre sans décimales).
x = int(input())

# On divise la valeur entière x par 11 pour obtenir le nombre de groupes complets de 11.
# L'opérateur / effectue une division flottante.
# int(x/11) convertit le résultat en un entier, ce qui enlève la partie décimale (arrondi à l’inférieur).
# Ensuite, on multiplie ce nombre par 2.
# Le résultat est stocké dans la variable y.
y = int(x / 11) * 2

# L'opérateur % calcule le reste de la division entière de x par 11.
# Cela permet de déterminer combien d'éléments restent après avoir pris tous les groupes complets de 11.
if x % 11 > 6:
    # Si le reste de la division de x par 11 est strictement supérieur à 6,
    # cela veut dire qu'il y a au moins 7 unités supplémentaires.
    # Dans ce cas, on ajoute 2 à la variable y.
    y += 2
elif x % 11 > 0:
    # Si le reste de la division de x par 11 est strictement supérieur à 0 (mais inférieur ou égal à 6),
    # cela veut dire qu'il y a entre 1 et 6 unités en plus.
    # Dans ce cas, on ajoute seulement 1 à y.
    y += 1
# Si x % 11 == 0, alors on n'entre dans aucune des conditions, et on ne modifie pas y.

# La fonction print() affiche la valeur actuelle de y à l'écran (console).
print(y)