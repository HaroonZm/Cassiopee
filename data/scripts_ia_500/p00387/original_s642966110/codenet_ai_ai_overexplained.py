# On commence par demander à l'utilisateur d'entrer deux nombres séparés par un espace.
# La fonction input() lit une ligne de texte entrée par l'utilisateur sous forme de chaîne de caractères (string).
# La méthode split() découpe cette chaîne en une liste de sous-chaînes, en utilisant par défaut l'espace comme séparateur.
# Par exemple, si l'utilisateur tape "3 10" la méthode split() renverra la liste ["3", "10"].
# La fonction map() applique la fonction int (qui transforme une chaîne de caractères en nombre entier) à chaque élément de cette liste.
# Ainsi, map(int, input().split()) transforme chaque élément de la liste de chaînes en un entier.
# Enfin, on attribue ces deux entiers à deux variables, A et B, qui contiennent donc respectivement les deux nombres donnés par l'utilisateur.
A, B = map(int, input().split())

# Nous voulons effectuer un calcul ensuite.
# L'expression (B + A - 1) // A utilise l'opérateur // qui fait une division entière.
# Cela signifie que le résultat sera la partie entière du quotient, sans la partie décimale.
# L'idée de cette formule est d'effectuer un "arrondi supérieur" de la division B / A sans utiliser de fonction supplémentaire.
# En effet, en ajoutant (A - 1) avant la division entière, on s'assure que toute division avec un reste sera arrondie vers le haut.
# Par exemple, si B = 10 et A = 3, alors (10 + 3 - 1) = 12, et 12 // 3 = 4, ce qui correspond au quotient arrondi vers le haut de 10 / 3.
# Enfin, on affiche le résultat avec print(), qui affiche une valeur dans la console.
print((B + A - 1) // A)