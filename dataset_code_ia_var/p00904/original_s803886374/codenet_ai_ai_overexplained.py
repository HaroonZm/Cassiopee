# Début du code
# On utilise une boucle for pour traiter plusieurs cas de test.
# Chaque cas de test consiste à lire deux entiers p et q, puis à effectuer des calculs pour déterminer si on affiche 'P' ou 'C'.
# Pour chaque cas de test, on compte c le nombre de fois qu'une condition particulière est satisfaite dans deux boucles imbriquées.

# On commence une boucle for pour chaque cas de test.
# La variable _ est conventionnelle (on ne l'utilisera pas). On parcourt range(int(input())), donc on lit d'abord un entier N depuis l'entrée standard.
# Cela désigne le nombre de cas de test qu'on souhaite traiter.
for _ in range(int(input())):

    # On lit deux entiers p et q séparés par un espace
    # On utilise input() pour lire une ligne, puis split() pour séparer la chaîne en morceaux selon les espaces, puis map(int, ...) pour convertir chaque morceau en un entier.
    # On utilise l'affectation p, q = ... pour attribuer le premier entier à p et le deuxième à q.
    p, q = map(int, input().split())

    # On initialise la variable c à 0.
    # Cette variable servira de compteur pour compter combien de fois la condition testée à l'intérieur des boucles est vraie.
    c = 0

    # On démarre la première boucle imbriquée avec la variable i.
    # range(143) va de 0 à 142 inclus (143 valeurs).
    for i in range(143):

        # Deuxième boucle imbriquée avec la variable j, également de 0 à 142 inclus.
        for j in range(143):

            # On vérifie si (i > 0 ou j > 0). Ceci permet d'ignorer le cas où i == 0 et j == 0 en même temps, autrement dit on ne prend pas le point (0,0).
            # Ensuite, on vérifie deux autres conditions :
            # (j*p + i*q) % (j*j + i*i) == 0
            # (j*q - i*p) % (j*j + i*i) == 0
            # % est l'opérateur modulo en Python et vérifie si la division est entière sans reste.
            # (j*p + i*q) doit être un multiple de (j*j + i*i), et pareil pour (j*q - i*p).
            # Les parenthèses sont utilisées pour assurer le bon ordre d'évaluation des opérations.
            if (i > 0 or j > 0) and (j * p + i * q) % (j * j + i * i) == 0 and (j * q - i * p) % (j * j + i * i) == 0:
                # Si toutes les conditions sont vérifiées, on incrémente notre compteur c de 1.
                c += 1

    # Après avoir terminé les boucles et compté le nombre de succès dans la variable c,
    # on vérifie si c est inférieur à 5.
    if c < 5:
        # Si c < 5, on affiche 'P' (sans saut de ligne explicite car print() en ajoute un par défaut à la fin).
        print('P')
    else:
        # Sinon, on affiche 'C'.
        print('C')
# Fin du code