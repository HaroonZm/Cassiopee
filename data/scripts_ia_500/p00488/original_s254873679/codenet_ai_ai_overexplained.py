# La fonction input() permet de lire une entrée utilisateur sous forme de chaîne de caractères.
# Nous allons lire plusieurs entrées utilisateur, puis calculer le minimum parmi ces entrées.

# Création d'une liste contenant trois entrées utilisateur.
# La compréhension de liste est utilisée ici : [input() for i in [1,1,1]]
# Cela signifie : pour chaque élément 'i' dans la liste [1,1,1] (qui a une longueur de 3),
# appeler input() pour obtenir une entrée utilisateur, puis rassembler ces entrées dans une liste.
# Ainsi, cette expression crée une liste de 3 éléments où chaque élément est une chaîne saisie par l'utilisateur.
liste_trois_entrees = [input() for i in [1,1,1]]

# Calcul du minimum dans la liste des trois entrées utilisateur.
# La fonction min() retourne la plus petite valeur dans la liste selon un ordre lexicographique si ce sont des chaînes.
# Puisque input() renvoie des chaînes, min() choisira la chaîne "la plus petite" selon l'ordre alphabétique.
minimum_trois = min(liste_trois_entrees)

# Création d'une autre liste contenant deux entrées utilisateur.
# De la même façon, on lit deux fois une entrée avec input() dans cette compréhension de liste.
liste_deux_entrees = [input() for i in [1,1]]

# Calcul du minimum dans cette liste de deux entrées.
minimum_deux = min(liste_deux_entrees)

# On effectue une addition des deux minimums, en concaténant les chaînes obtenues.
# Comme les variables minimum_trois et minimum_deux sont des chaînes,
# l'opérateur + concatène les chaînes, il n'effectuera pas une addition numérique.
somme_minimums = minimum_trois + minimum_deux

# Finalement on tente de soustraire 50 à la somme des minimums.
# Cependant, puisque somme_minimums est une chaîne de caractères,
# l'opération 'somme_minimums - 50' n'est pas valide en Python et générera une erreur TypeError.
# Le code original n'est donc pas correct s'il traite des chaînes.
# Supposons que l'intention était de traiter des nombres, il faudrait convertir les entrées en entiers avant.
# Mais ici on respecte le code donné, donc on affiche directement cette expression malgré l'erreur potentielle.

print(somme_minimums - 50)