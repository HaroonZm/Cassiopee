# Demander à l'utilisateur de saisir deux valeurs séparées par un espace via l'entrée standard (input).
# L'entrée retournée par input() est une chaîne de caractères. La méthode split() sépare cette chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur par défaut.
# La fonction map(int, ...) applique la fonction int() à chaque élément de la liste, transformant ainsi les sous-chaînes en entiers.
# Les deux entiers obtenus sont ensuite attribués respectivement aux variables 'a' et 's' à l'aide de l'affectation multiple.
a, s = map(int, input().split())

# Tester si le produit de a et de s est supérieur ou égal à zéro.
# Cela revient à vérifier que 'a' et 's' ont le même signe (tous deux positifs, tous deux négatifs, ou l'un d'eux est zéro).
if a * s >= 0:
    # Si 'a' et 's' ont le même signe (ou qu'un des deux vaut zéro), alors la division entière (//) de 'a' par 's' donne le résultat attendu par l'utilisateur mathématiquement.
    # L'opérateur // réalise une division entière (division euclidienne), c'est-à-dire qu'il donne le quotient sans la partie décimale et arrondi vers moins l'infini.
    print(a // s)
else:
    # Si 'a' et 's' n'ont pas le même signe, cela signifie que la division devrait être négative.
    # On prend la valeur absolue de 'a' avec abs(a) afin de s'assurer que le nombre est positif, et de même pour abs(s).
    # Le quotient entier des valeurs absolues est alors calculé (abs(a)//abs(s)), puis on applique un signe négatif au résultat pour refléter le fait que la division doit être négative.
    print(-(abs(a) // abs(s)))