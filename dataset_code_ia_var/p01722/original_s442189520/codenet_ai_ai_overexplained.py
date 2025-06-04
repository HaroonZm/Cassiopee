# Demande à l'utilisateur de saisir une valeur au clavier.
# La fonction input() lit cette valeur en tant que chaîne de caractères (string).
# La fonction int() convertit cette chaîne en entier (integer).
# Le résultat de cette conversion est assigné à la variable n.
n = int(input())

# On vérifie si la valeur de n est strictement supérieure à 3.
# Le symbole ">" signifie "supérieur à".
if n > 3:
    # Si la condition précédente est vraie (c'est-à-dire que n > 3),
    # on force la variable n à prendre la valeur 3,
    # peu importe ce que l'utilisateur avait entré initialement.
    n = 3

# Création d'une liste contenant quatre éléments: 1, 2, 1, et 0, dans cet ordre.
# Une liste en Python est un conteneur qui peut stocker plusieurs objets,
# séparés par des virgules, et placés entre crochets [].
# On utilise l'opérateur [] après la liste pour accéder à l'élément situé
# à l'index n de la liste. Les indices commencent à 0 en Python.
# Par exemple, si n vaut 0, [1,2,1,0][0] vaut 1.
# Si n vaut 1, [1,2,1,0][1] vaut 2, ainsi de suite jusqu'à n vaut 3.
# Le résultat de cette récupération d'élément est passé à la fonction print(),
# qui affiche alors la valeur à l'écran, suivie d'un retour à la ligne.
print([1, 2, 1, 0][n])