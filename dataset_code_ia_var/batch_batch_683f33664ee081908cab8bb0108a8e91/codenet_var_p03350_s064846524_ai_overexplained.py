# La variable R est un alias pour la fonction range, qui génère une séquence d'entiers.
R = range

# Les deux valeurs N et K sont extraites de l'entrée utilisateur, séparées par un espace.
# int() convertit les chaînes en entiers.
# split() découpe la chaîne en fonction des espaces.
N, K = map(int, input().split())

# Q est un objet range allant de 0 à N inclus (car range(N+1) s'arrête à N).
Q = R(N + 1)

# Création d'une matrice d, initialisée avec des zéros.
# d est de taille (N+1) x (2^N).
# Chaque sous-liste de d représente un niveau différent,
# et chaque cellule représente une combinaison possible de bits.
d = [[0] * 2 ** N for _ in Q]

# Création d'une matrice f, initialisée avec des zéros.
# f est également de taille (N+1) x (2^N).
# Cette matrice va stocker une valeur de "run length" pour des patterns binaires.
f = [[0] * 2 ** N for _ in Q]

# Remplissage de la matrice d à partir de l'entrée utilisateur.
# On itère i de 0 à N inclus.
for i in Q:
    # Lecture d'une ligne d'entrée.
    for j, c in enumerate(input()):  # enumerate() donne l'index j et le caractère c.
        d[i][j] = int(c)  # Convertit chaque caractère c en entier et l'affecte dans d[i][j].

# Construction de la matrice f.
# Pour chaque i de 1 à N inclus (c'est-à-dire pour chaque longueur de bits).
for i in R(1, N + 1):
    # Pour chaque j de 0 à (2^i) - 1 inclus.
    for j in R(1 << i):
        # Extraction du bit de poids fort dans j (celui d'indice i-1 en partant de la droite).
        t = (j >> (i - 1)) & 1  # Le bit le plus à gauche dans les i bits.
        r = 0  # Compteur pour la longueur du 'run'.
        # Boucle pour déterminer la longueur du run de bits identiques à t, à partir du bit de poids fort.
        while r < i and ((j >> (i - 1 - r)) & 1) == t:
            r += 1  # Incrémente r tant que les bits rencontrés restent égaux à t.
        f[i][j] = r  # Stocke la longueur trouvée de ce 'run' en début de la séquence.

# Algorithme de regroupement et de propagation des valeurs dans d.
for i in Q:
    # Pour chaque k de i+1 à N inclus (i < k <= N).
    for k in R(i + 1, N + 1):
        z = k - i  # Calcul de la différence d'indice.
        m = (1 << z) - 1  # Masque binaire qui sélectionne les z bits de droite.
        # Itère tous les patterns possible de k bits.
        for j in R(1 << k):
            # Ajoute la valeur d[k][j] à la densité correspondante dans d[i][j >> z], ce qui revient à agréger selon le préfixe gauche.
            d[i][j >> z] += d[k][j]
            # Utilise le run length f[z][j&m] pour obtenir la longueur d'une séquence de bits identiques dans le suffixe z bits.
            r = f[z][j & m]
            # Si r n'est pas égal à z (c'est-à-dire que la séquence suffixe n'est pas identique).
            if r != z:
                # Propagation de la densité vers la case correspondante dans d en remontant de k à k-r,
                # en concoctant un nouveau pattern qui conserve les (z-r) bits de préfixe et le suffixe r bits.
                d[k - r][((j >> z) << (z - r)) | (j & ((1 << (z - r)) - 1))] += d[k][j]

    # Recherche la première occurrence (dans l'ordre croissant des patterns) où le total dans d[i][j] est au moins K.
    for j in R(1 << i):
        if d[i][j] >= K:
            I = i  # On mémorise l'indice i, la longueur du pattern.
            J = j  # On mémorise le pattern j lui-même.
            break  # On s'arrête dès qu'on a trouvé une telle occurrence.

# Affichage du résultat :
# Si I et J sont égaux à 0, on affiche une chaîne vide.
# Sinon, on convertit J en binaire (sous forme de chaîne sans le préfixe '0b'),
# puis on complète par des zéros à gauche pour obtenir une chaîne de longueur I.
print('' if I == J == 0 else bin(J)[2:].zfill(I))  # [2:] retire le préfixe '0b', zfill(I) complète les zéros.