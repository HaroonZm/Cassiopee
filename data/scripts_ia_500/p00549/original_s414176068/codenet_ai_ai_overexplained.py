# Lecture d'une valeur entière depuis l'entrée standard.
# Cette valeur représente la longueur de la chaîne de caractères à lire ensuite.
N = int(input())

# Lecture d'une chaîne de caractères depuis l'entrée standard.
# Cette chaîne contiendra des caractères spécifiquement choisis (typiquement 'J', 'O', 'I').
S = input()

# Initialisation de trois variables entières à zéro.
# a0 comptera le nombre de 'J' rencontrés jusqu'à la position courante.
# a1 comptera le nombre d'apparitions de la sous-séquence 'JO' jusqu'à la position courante.
# a2 comptera le nombre d'apparitions de la sous-séquence 'JOI' jusqu'à la position courante.
a0 = 0
a1 = 0
a2 = 0

# Initialisation d'une liste P de taille N, remplie de zéros.
# Cette liste gardera en mémoire, à chaque index i, la valeur de a0 au moment où on atteint la position i.
P = [0] * N

# Itération sur les index et les caractères de la chaîne S en même temps, grâce à enumerate.
for i, c in enumerate(S):
    # Si le caractère actuel est 'J', on incrémente le compteur a0.
    if c == 'J':
        a0 += 1
    # Si le caractère est 'O', on ajoute à a1 la valeur actuelle de a0.
    # Ceci correspond à compter toutes les paires 'JO' possibles où 'J' est un caractère rencontré avant cet 'O'.
    elif c == 'O':
        a1 += a0
    # Sinon (le cas 'I'), on ajoute à a2 la valeur actuelle de a1.
    # Cela compte toutes les triplets 'JOI' où 'JO' a été rencontré avant cet 'I'.
    else:
        a2 += a1
    # On mémorise à la position i de la liste P la valeur courante de a0.
    P[i] = a0

# Initialisation de trois autres variables à zéro.
# b0 comptera le nombre de 'I' rencontrés depuis la fin de la chaîne.
# b1 comptera le nombre d'apparitions de la sous-séquence 'OI' en parcourant la chaîne à l'envers.
# b2 comptera le nombre d'apparitions d'une éventuelle sous-séquence, mais n'est pas utilisé pour le résultat final.
b0 = 0
b1 = 0
b2 = 0

# Initialisation d'une liste Q de taille N, remplie de zéros.
# Cette liste va enregistrer le nombre de 'I' rencontrés depuis la fin jusqu'à chaque index i.
Q = [0] * N

# Parcours inverse de la chaîne S en la renversant avec reversed.
# enumerate donne ici l'index i sur la chaîne inversée et le caractère c correspondant.
for i, c in enumerate(reversed(S)):
    # Si le caractère rencontré est 'I', on incrémente b0.
    if c == 'I':
        b0 += 1
    # Si c'est 'O', on ajoute à b1 la valeur de b0 (correspondant aux paires 'OI').
    elif c == 'O':
        b1 += b0
    # Sinon (probablement 'J'), on ajoute à b2 la valeur de b1.
    else:
        b2 += b1
    # On sauvegarde à l'index correspondant dans Q la valeur actuelle de b0.
    # L'index dans Q est calculé comme -1 - i pour corriger l'index inversé à l'index normal.
    Q[-1 - i] = b0

# On initialise la variable res avec la plus grande valeur entre a1 (compte 'JO') et b1 (compte 'OI' en sens inverse).
res = max(a1, b1)

# Parcours de tous les indices de 0 à N-1.
for i in range(N):
    # Pour chaque index i, on compare et peut mettre à jour res avec le produit P[i] * Q[i].
    # Cela correspond à une mesure combinée utilisant les compteurs de 'J' à gauche et 'I' à droite.
    res = max(res, P[i] * Q[i])

# Finalement, on affiche la somme de res plus a2.
# a2 comptait les occurrences de 'JOI' dans le parcours normal, ce résultat est donc ajusté en conséquence.
print(res + a2)