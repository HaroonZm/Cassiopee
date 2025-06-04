# Demande à l'utilisateur de saisir trois valeurs séparées par des espaces
# La fonction input() attend la saisie de l'utilisateur depuis le clavier. 
# Par exemple, l'utilisateur peut entrer : 3 4 5
# split() sépare cette saisie en une liste de chaînes ['3', '4', '5'] en utilisant l'espace comme séparateur par défaut.
# map(int, ...) applique la fonction int() à chaque élément de la liste résultante pour les convertir en entiers.
# Enfin, on utilise un "unpacking" pour attribuer les trois entiers obtenus aux variables AB, BC et CA respectivement.
AB, BC, CA = map(int, input().split())

# Calcule l'aire du triangle connaissant deux côtés et l'angle droit entre eux.
# Ici, l'expression AB*BC calcule le produit des deux côtés adjacents à l'angle droit.
# La division par 2 permet d'obtenir la surface du triangle rectangle de bases AB et BC.
# Attention : AB*BC/2 réalise une division flottante (le résultat est potentiellement un nombre décimal).
area = AB * BC / 2

# La fonction int() convertit éventuellement le résultat en entier, en supprimant toute partie décimale (troncature).
# Cela permet d'obtenir un affichage sous forme d'entier.
# On utilise print() pour afficher le résultat à l'écran.
print(int(area))