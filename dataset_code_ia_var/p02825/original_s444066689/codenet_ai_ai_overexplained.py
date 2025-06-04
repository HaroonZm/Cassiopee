# Demande à l'utilisateur de saisir un entier, puis convertit cette entrée de type chaîne en entier
n = int(input())

# Si l'utilisateur entre 2, il n'y a pas de solution et on affiche -1 puis on arrête le programme immédiatement
if n == 2:
    print(-1)  # Affiche -1 car il n'y a pas de solution pour n = 2
    exit()     # Termine immédiatement le programme

# Si l'utilisateur entre 3, on affiche un motif spécifique et on arrête le programme 
if n == 3:
    print("abb")    # Affiche la première ligne du motif pour n = 3
    print("a.c")    # Affiche la deuxième ligne du motif pour n = 3
    print("ddc")    # Affiche la troisième ligne du motif pour n = 3
    exit()          # Termine immédiatement le programme

# Si l'utilisateur entre 5, on affiche le motif adapté à un carré de taille 5, puis arrêt du programme
if n == 5:
    print("aabbc", "hi..c", "hi..d", "g.jjd", "gffee")  # Affiche les 5 lignes du motif pour n = 5
    exit()          # Termine immédiatement le programme

# Si l'utilisateur entre 7, on affiche le motif adapté à un carré de taille 7, puis arrêt du programme
if n == 7:
    print("..abc..")              # Affiche la première ligne du motif pour n = 7
    print("..abc..")              # Deuxième ligne (identique à la première)
    print("aax..aa")              # Motif particulier à la 3ème ligne
    print("bbx..bb")              # 4ème
    print("cc.yycc")              # 5ème
    print("..abc..")              # 6ème
    print("..abc..")              # 7ème (identique à la 1ère et à la 2ème)
    exit()                        # Termine immédiatement le programme

# Si aucune des conditions précédentes n'est vérifiée,
# on va générer dynamiquement la matrice carré de taille n composée initialement de points ".".
# La compréhension de liste crée une liste de listes, chaque sous-liste représentant une ligne de n caractères, initialisés à "."
a = [n * ["."] for _ in range(n)]

# Si n est impair (vérification du reste de la division euclidienne par 2)
if n % 2:
    # On modifie les 5 dernières lignes et colonnes du carré
    # a[-5] représente l'antépénultième (5ème à partir de la fin) ligne, a[-4] la 4ème à partir de la fin, ...
    # Les indices négatifs sont utilisés pour compter à partir de la fin de la liste
    a[-5][-5], a[-5][-4], a[-5][-3], a[-5][-2], a[-5][-1] = list("aabbc")    # 5ème ligne avant la fin
    a[-4][-5], a[-4][-4], a[-4][-3], a[-4][-2], a[-4][-1] = list("hi..c")    # 4ème
    a[-3][-5], a[-3][-4], a[-3][-3], a[-3][-2], a[-3][-1] = list("hi..d")    # 3ème
    a[-2][-5], a[-2][-4], a[-2][-3], a[-2][-2], a[-2][-1] = list("g.jjd")    # 2ème
    a[-1][-5], a[-1][-4], a[-1][-3], a[-1][-2], a[-1][-1] = list("gffee")    # dernière
    n -= 5  # On diminue n de 5 car les 5 dernières lignes/colonnes sont déjà affectées

# On va remplir la matrice par blocs de 2x2 dans la partie restante (non traitée ci-dessus)
for i in range(0, n, 2):      # De 0 jusqu'à n-1 avec un pas de 2 (on avance de deux lignes et deux colonnes à chaque itération)
    # Remplit la diagonale et la case voisine horizontale avec "a"
    a[i][i], a[i][i+1] = "a", "a"
    # Remplit la ligne suivante de la diagonale et la case voisine horizontale avec "b"
    a[i+1][i], a[i+1][i+1] = "b", "b"

# On sépare maintenant les cas selon un motif de parité de n (divisible par 4 ou non)
if n % 4 == 0:  # Si n est divisible par 4
    for i in range(0, n, 2):  # Parcourt les cases principales des blocs de 2x2 comme plus haut
        # Remplit les deux cases à la fin de la ligne et de la colonne avec "c" et "d"
        a[n-i-2][i], a[n-i-2][i+1] = "c", "d"
        a[n-i-1][i], a[n-i-1][i+1] = "c", "d"
else:          # Si n modulo 4 n'est pas 0
    for i in range(0, n-2, 2):  # On s'arrête à n-4, pour ne pas dépasser les indices lors du placement des "c" et "d"
        a[i][i+2], a[i][i+3] = "c", "d"
        a[i+1][i+2], a[i+1][i+3] = "c", "d"
    # On traite les deux dernières lignes (n-2 et n-1) séparément pour les deux premières colonnes
    a[n-2][0], a[n-2][1] = "c", "d"
    a[n-1][0], a[n-1][1] = "c", "d"

# Enfin, on affiche la matrice ligne par ligne
for i in a:
    # ''.join(i) transforme la liste de caractères en une chaîne de caractères
    print("".join(i))