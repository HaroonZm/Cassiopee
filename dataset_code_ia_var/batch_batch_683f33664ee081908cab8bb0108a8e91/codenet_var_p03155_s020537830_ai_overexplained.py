# Demande à l'utilisateur de saisir une valeur entière, qui sera assignée à la variable N.
# input() affiche une invite à l'utilisateur et attend qu'il saisisse une entrée au clavier.
# int() convertit la chaîne de caractères obtenue par input() en un entier.
N = int(input())

# Même logique que précédemment. Demande à l'utilisateur de saisir une valeur entière pour la variable H.
# H représentera une hauteur dans le contexte de ce programme.
H = int(input())

# Demande une troisième valeur entière à l'utilisateur, stockée dans la variable W.
# W représentera une largeur dans ce contexte.
W = int(input())

# Calcule la valeur suivante :
#   (N - H + 1) détermine combien de positions possibles il y a verticalement pour placer un objet de hauteur H dans un espace de taille N.
#   (N - W + 1) calcule combien de positions il y a horizontalement pour placer un objet de largeur W dans le même espace.
# Le produit de ces deux valeurs donne le nombre total de façons de placer un objet de dimensions H x W dans un carré de dimensions N x N.
#
# print() affiche le résultat calculé à l'écran. La valeur calculée n'est pas stockée dans une nouvelle variable,
# mais est directement passée à print() pour affichage.
print((N - H + 1) * (N - W + 1))