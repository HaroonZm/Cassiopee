# Définition de la variable R comme un alias de range pour simplifier l'écriture ultérieure.
R = range

# Lecture de deux entiers depuis l'entrée standard, séparés par un espace.
# map applique int à chaque élément obtenu via input().split(), ce qui récupère N et K.
N, K = map(int, input().split())

# Création de la séquence Q, qui sera utilisée pour itérer de 0 à N, inclus.
# range(N+1) génère les entiers de 0 à N inclus.
Q = R(N+1)

# Création d'une liste "d" contenant N+1 sous-listes.
# Chaque sous-liste a une longueur de 2 à la puissance de son indice 'i' (c’est-à-dire 2**i).
# Chaque sous-liste de "d" est remplie de zéros au départ.
d = [[0]*2**i for i in Q]

# Création d'une autre liste "f", de mêmes dimensions et initialement remplie de zéros.
f = [[0]*2**i for i in Q]

# Remplissage de la table "d" à partir de l'entrée de l'utilisateur.
for i in Q:
    # On lit une chaîne de caractères pour la ligne i.
    # 'enumerate(input())' parcourt chaque caractère de la chaîne avec son index 'j'.
    for j, c in enumerate(input()):
        # Conversion du caractère c en entier (vaudra 0 ou 1 car on suppose l'entrée binaire).
        # Stockage dans d[i][j].
        d[i][j] = int(c)

# Remplissage de la table "f", qui pré-calcule une information sur les motifs binaires des indices.
# Pour chaque i de 1 à N, on examine chaque nombre binaire possible sur i bits.
for i in R(1, N+1):
    # Pour chaque entier j dont la représentation binaire tient sur i bits (de 0 à 2^i - 1), on va calculer f[i][j].
    for j in R(1 << i):
        # Détermination de la valeur du bit à l’indice (i-1) dans j.
        # >> décale de (i-1) bits vers la droite, &1 extrait le bit de poids faible.
        t = (j >> (i-1)) & 1
        # Initialisation de r à zéro. r va compter le nombre de bits consécutifs égaux à t, à partir du haut.
        r = 0
        # On incrémente r tant que les bits extraits successivement correspondent à t.
        while r < i and ((j >> (i-1-r)) & 1) == t:
            r += 1
        # On enregistre la valeur trouvée dans f[i][j].
        f[i][j] = r

# Traitement principal sur la table "d" pour combiner les données et y accumuler des compteurs.
for i in Q:
    # On considère chaque sous-table de taille correspondante à i.
    for k in R(i+1, N+1):
        # Calcul de la distance z entre les deux niveaux de tables i et k.
        z = k - i
        # m est un masque binaire de z bits à 1 (exemple : si z=3, m=0b111=7).
        m = (1 << z) - 1
        # Pour tout indice binaire j sur k bits.
        for j in R(1 << k):
            # On ajoute la valeur d[k][j] à l'entrée correspondante de d[i] après décale à droite de z bits.
            d[i][j >> z] += d[k][j]
            # r est le nombre de bits consécutifs au début (sur z bits) valant le même bit (0 ou 1).
            r = f[z][j & m]
            # Si r n’atteint pas z (c’est-à-dire qu’il s’arrête avant la fin),
            # on redistribue d[k][j] dans une table d’au niveau k-r, à l’indice construit ainsi :
            # - On prend les bits de haut poids de j (au-delà des z bits) et on les décale
            # - On ajoute les bits de faible poids de j (jusqu’au bit z-r-1)
            if r != z:
                d[k-r][(j >> z) << (z-r) | (j & ((1 << (z-r)) - 1))] += d[k][j]
    # Recherche du premier indice (j) dans d[i] dont la valeur dépasse ou égale à K.
    for j in R(1 << i):
        if d[i][j] >= K:
            I = i  # On mémorise la valeur de i, la taille de la sous-table.
            J = j  # On mémorise l’indice j.
            break  # On arrête dès qu’on a trouvé le premier.

# Affichage du résultat final.
# Si I==0 et J==0, on affiche la chaîne vide ''.
# Sinon, on convertit J en binaire, omettant le préfixe '0b', et on complète à gauche par des zéros pour obtenir un mot de I bits.
print('' if I == J == 0 else bin(J)[2:].zfill(I))