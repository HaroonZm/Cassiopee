# Lecture de deux entiers séparés par un espace à partir de l'entrée standard.
# map applique la fonction int à chaque élément résultant du découpage de la chaîne lue (input()) selon les espaces.
N, K = map(int, input().split())

# Calcul de la variable D comme N + 1.
# D représente une taille liée à des séquences binaires de longueur N.
D = N + 1

# Initialisation d'une matrice 'd' de taille D x (2^N).
# Chaque élément d[i][j] sera initialisé à 0.
# (1 << N) vaut 2 à la puissance N, ce qui donne le nombre total de séquences binaires de longueur N.
d = [[0] * (1 << N) for _ in range(D)]

# Initialisation d'une matrice 'f' de taille D x (2^N).
# Chaque élément f[i][j] sera également initialisé à 0.
# Cette matrice va probablement stocker des valeurs liées à des longueurs de séquences particulières.
f = [[0] * (1 << N) for _ in range(D)]

# Remplissage de la matrice 'd' avec les valeurs provenant des entrées suivantes.
# Pour chaque i de 0 à D-1 (soit D lignes de la matrice),
for i in range(D):
    # input() lit une chaîne de 0 et 1.
    # enumerate renvoie à la fois l'indice j et le caractère c pour chaque position.
    for j, c in enumerate(input()):
        # Si le caractère c est '1', on place 1 dans d[i][j], sinon l'élément reste à 0.
        if c == '1':
            d[i][j] = 1

# Construction de la matrice f.
# Cette matrice va stocker la longueur de la plus longue séquence de bits consécutifs, identiques, au début de la représentation binaire de j.
# On itère sur chaque i de 1 à D-1, représentant la longueur de séquences binaires considérées.
for i in range(1, D):
    # Pour chaque nombre j possible avec i bits (allant de 0 à 2^i - 1)
    for j in range(1 << i):
        # t récupère la valeur du bit le plus à gauche (bit de poids fort) de j.
        # On décale j vers la droite de i-1 positions, puis on effectue un ET binaire avec 1 pour isoler le bit.
        t = (j >> (i - 1)) & 1
        # r compte le nombre de bits initiaux (à partir du bit de poids fort) qui valent t.
        r = 0
        # On parcourt les bits du plus significatif au moins, tant que c'est égal à t.
        while r < i and ((j >> (i - 1 - r)) & 1) == t:
            r += 1
        # f[i][j] reçoit la longueur de ce préfixe homogène.
        f[i][j] = r

# On cherche à identifier le plus court préfixe dont la somme atteint au moins K.
# On itère sur tous les i de 0 à D-1 (longueurs de préfixes).
for i in range(D):
    # ii parcourt tous les indices strictement supérieurs à i jusqu'à D-1.
    for ii in range(i + 1, D):
        # z est la différence entre ii et i, c'est-à-dire la longueur de la séquence supplémentaire.
        z = ii - i
        # mask permet d'extraire les z derniers bits de j.
        mask = (1 << z) - 1
        # On parcourt tous les j possibles de longueur ii (de 0 jusqu'à 2^ii - 1).
        for j in range(1 << ii):
            # On ajoute à d[i][j >> z] la valeur de d[ii][j].
            # Cela correspond à regrouper par le préfixe de longueur i.
            d[i][j >> z] += d[ii][j]
            # r est la longueur du préfixe homogène, calculée sur les z derniers bits de j.
            r = f[z][j & mask]
            # Si r != z, cela signifie que la fin de j n'est pas complètement homogène.
            if r != z:
                # On ajoute d[ii][j] à la case correspondant à un préfixe plus court non homogène.
                # On "compacte" j en ramenant la séquence d'indice ii à une séquence de longueur ii - r, 
                # On déplace le préfixe de j >> z et on garde les (z - r) bits restants, 
                # ce qui permet de comptabiliser les séquences qui n'ont pas un préfixe homogène complet.
                d[ii - r][((j >> z) << (z - r)) | (j & ((1 << (z - r)) - 1))] += d[ii][j]
    # Après ces étapes de propagation, on teste pour chaque j de longueur i :
    for j in range(1 << i):
        # Si le nombre d'occurrences d[i][j] est supérieur ou égal à K
        if d[i][j] >= K:
            # On garde i et j, car c'est le plus court préfixe (parcours par i croissant)
            I = i
            J = j
            # On s'arrête dès qu'on a trouvé un préfixe valide (break sort de la boucle sur j)
            break

# Affichage du résultat.
# Si I et J sont tous deux égaux à 0, alors on affiche la chaîne vide,
# Sinon, on affiche la représentation binaire de J sur I caractères (avec des zéros ajoutés à gauche si besoin).
if I == J == 0:
    # Affichage d'une chaîne vide si on a une solution "vide".
    print('')
else:
    # bin(J) produit une chaîne du genre '0b101'; on prend tout après le '0b', et on complète à gauche avec des zéros pour obtenir I caractères.
    print(bin(J)[2:].zfill(I))