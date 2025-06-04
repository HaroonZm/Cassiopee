# Création d'une liste nommée C pour stocker les compteurs
# L'opérateur * permet de créer une liste de 6 zéros : [0, 0, 0, 0, 0, 0]
C = [0] * 6

# La fonction raw_input() demande à l'utilisateur de saisir une chaîne de caractères,
# que l'on convertit en entier avec int() pour obtenir le nombre d'itérations de la boucle for.
# [0] * n crée une liste avec n éléments (tous des 0),
# ce qui permet de boucler n fois grâce à for _ in ...
for _ in [0] * int(raw_input()):
    # À chaque itération, l'utilisateur entre une chaîne contenant un point,
    # par exemple "170.65", que raw_input() lit comme une chaîne de caractères.
    # La méthode split('.') sépare la chaîne en deux parties autour du point,
    # donnant une liste de deux chaînes (ex : ['170', '65']).
    # La fonction map() applique int() à chaque élément de cette liste,
    # transformant par exemple ['170', '65'] en [170, 65].
    # Les deux valeurs sont affectées aux variables a et b.
    a, b = map(int, raw_input().split('.'))
    # Vérifie si la première valeur a (par exemple, la partie entière de la taille) est inférieure à 165.
    if a < 165:
        # Dans ce cas, on compte un élément supplémentaire dans la première case de la liste C,
        # donc on incrémente C[0] (qui correspond à la première catégorie).
        C[0] += 1
    else:
        # Sinon, on répartit les autres valeurs dans la liste C selon la formule (a-160)/5.
        # Cela calcule un indice de 1 à 5 pour placer le comptage dans la bonne tranche/section :
        # ex : si a = 170, (170-160) = 10, 10/5 = 2, donc C[2] est incrémenté.
        # L'utilisation de crochets [] permet d'accéder/modifier la valeur à l'indice calculé.
        C[(a - 160) / 5] += 1

# Une autre boucle for permet d'itérer sur chaque indice i de 0 à 5 (total 6 éléments) :
for i in range(6):
    # Pour chaque case de la liste C, on affiche une ligne au format:
    # numéro de la tranche (i+1 car les indices commencent à 0, mais on veut afficher 1 à 6)
    # puis un deux-points, puis autant d'étoiles '*' que la valeur correspondante dans C[i].
    # La chaîne '%d:%s' contient un espace réservé pour un entier (%d) puis une chaîne (%s)
    # Les valeurs (i+1, '*'*C[i]) sont placées à leurs emplacements respectifs dans la chaîne.
    print '%d:%s' % (i + 1, '*' * C[i])