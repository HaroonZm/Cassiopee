# Demander à l'utilisateur de saisir un entier et convertir ce qui a été saisi (qui est de type str) en un entier avec int().
# Cela va représenter le nombre de colonnes du "damier" (N).
N = int(input())

# Prendre la première ligne de l'entrée utilisateur, qui correspond à une chaîne de caractères, et la convertir en un tuple.
# Chaque caractère de la chaîne devient un élément distinct du tuple. Cela représente la première ligne du damier (S1).
S1 = tuple(input())

# Même opération pour la deuxième ligne : on demande une nouvelle saisie, on la convertit en tuple.
# Cela représente la deuxième ligne du damier (S2).
S2 = tuple(input())

# Initialisation d'une liste vide appelée domino.
# Cette liste va stocker des informations sur l'orientation des dominos à chaque colonne.
# 1 (ou True) pour une tuile verticale, 0 (ou False) pour une tuile horizontale.
domino = []

# Initialisation du compteur de colonne à 0.
c = 0

# Boucle while qui va parcourir les colonnes tant que c est strictement inférieur à N.
while c < N:
    # Vérifier si pour la colonne c, les deux cases (haut et bas) ont le même caractère.
    # Cela signifie qu'une domino vertical est possible.
    if S1[c] == S2[c]:
        # Ajouter 1 à la liste domino pour indiquer une orientation verticale.
        domino.append(1)
        # On avance le compteur de colonne de 1 pour passer à la suivante.
        c += 1
    else:
        # Si les caractères sont différents, c'est une tuile horizontale qui couvre deux colonnes.
        # Ajouter 0 à la liste domino pour indiquer une orientation horizontale.
        domino.append(0)
        # On avance le compteur de colonne de 2 car la tuile horizontale en recouvre deux à la fois.
        c += 2

# On va maintenant calculer le nombre total de façons possibles de placer les dominos.
# Pour cela, on initialise la variable de résultat res en fonction de l'orientation du premier domino.
# Si le premier domino de la liste est vertical (valeur 1), il y a 3 possibilités initiales.
if domino[0]:
    res = 3
else:
    # Sinon (il est horizontal, valeur 0), il y a 6 possibilités.
    res = 6

# On parcourt le reste des dominos pour mettre à jour le résultat selon les orientations précédentes et courantes.
for n in range(1, len(domino)):
    # Si le domino courant est vertical (valeur 1).
    if domino[n]:
        # Si le domino précédent était aussi vertical (donc deux verticaux consécutifs).
        if domino[n-1]:
            # On multiplie le nombre de possibilités par 2.
            res *= 2
        # Si le domino précédent était horizontal, rien n'est fait ici (pas de modification du résultat).
    else:
        # Ici, le domino courant est horizontal (valeur 0).
        # Si le précédent domino était vertical.
        if domino[n-1]:
            # On multiplie le nombre de possibilités par 2.
            res *= 2
        else:
            # Si le précédent était aussi horizontal, on multiplie par 3 cette fois.
            res *= 3

# On affiche le résultat final en prenant le modulo 1000000007 pour éviter les dépassements de capacité
# et pour que le résultat reste dans la plage des entiers généralement autorisée en programmation compétitive.
print(res % 1000000007)