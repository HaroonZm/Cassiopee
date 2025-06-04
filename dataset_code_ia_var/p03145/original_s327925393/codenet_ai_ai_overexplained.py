# Demande à l'utilisateur d'entrer plusieurs valeurs séparées par des espaces dans la console.
# La fonction input() attend que l'utilisateur saisisse des données et appuie sur Entrée.
# input() renvoie une chaîne de caractères (str) représentant ce que l'utilisateur a tapé.

# split() découpe la chaîne de caractères en une liste d'éléments, chaque élément étant séparé par des espaces.
# Par exemple, si l'utilisateur tape "3 4 5", input().split() renverra ["3", "4", "5"].

# map() applique la fonction int à chaque élément de cette liste, convertissant les chaînes de caractères en entiers.
# map(int, input().split()) crée un itérable où chaque élément est un entier (int).

# a, b, c = ... utilise l'affectation multiple pour stocker les trois entiers dans les variables a, b et c.
# Cela signifie que la première valeur va dans 'a', la deuxième dans 'b', et la troisième dans 'c'.

a, b, c = map(int, input().split())

# Calcule le produit de 'a' et 'b' en utilisant l'opérateur de multiplication '*'.
# (a * b) multiplie la valeur de 'a' par la valeur de 'b'. Par exemple, si a=3 et b=4, alors (a * b) vaut 12.

# L'opérateur // est la division entière (division avec troncature du résultat vers 0).
# Cela signifie que le résultat sera un entier, même si la division n'est pas exacte.
# Par exemple, 5 // 2 donnera 2 (et non 2.5), car le résultat est traité comme un entier.

# En combinant tout cela, (a * b) // 2 calcule le produit de 'a' et 'b', puis le divise par 2, 
# en ne gardant que la partie entière du résultat.

# print() affiche le résultat final à l'écran.
# Le résultat de l'expression (a * b) // 2 est passé en argument à la fonction print(),
# qui convertit la valeur en chaîne de caractères et l'affiche dans la console.

print((a * b) // 2)