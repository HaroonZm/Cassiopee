# Lecture des entrées depuis l'utilisateur, supposant que l'utilisateur saisira quatre entiers séparés par des espaces.
# Ces valeurs sont interprétées dans l'ordre : L (limite supérieure d'itération), A (constante de départ),
# B (incrément à chaque itération), M (modulo utilisé dans les calculs, pour éviter des grands nombres).
L, A, B, M = map(int, input().split())

# Définition d'une fonction pour calculer la puissance d'une matrice.
# Cette technique est appelée exponentiation rapide (ou exponentiation binaire).
# Elle permet de calculer efficacement la matrice x élevée à la puissance n.
# Arguments :
#   x : matrice carrée de taille 3x3 (représentant la transformation à appliquer)
#   n : entier (la puissance à laquelle élever la matrice)
def mat_pow(x, n):
    # Création de la matrice identité 3x3 pour l'initialisation de y.
    # La matrice identité est une matrice carrée où tous les éléments de la diagonale principale valent 1,
    # et tous les autres éléments sont 0.
    y = [[0] * 3 for _ in range(3)]
    for i in range(3):
        y[i][i] = 1  # Placer les 1 uniquement sur la diagonale principale

    # Boucle principale d'exponentiation rapide :
    # tant que n > 0 (c'est-à-dire que l'on n'a pas consommé tous les bits de l'exposant)
    while n > 0:
        # Vérification si le bit de poids faible de n est à 1 (n est impair à cette étape)
        # Si oui, on multiplie y par la matrice courante x.
        if n & 1:
            y = mat_mul(x, y)
        # On élève la matrice x au carré à chaque étape (cette opération double l'exposant qu'on multiplie)
        x = mat_mul(x, x)
        # On divise n par 2 en manipulant les bits (opération de décalage à droite)
        n >>= 1

    # Après avoir traité tous les bits de l'exposant, y contient le résultat final
    return y

# Définition d'une fonction pour effectuer la multiplication de matrices modulo M.
# Arguments :
#   a : matrice de taille (I x K)
#   b : matrice de taille (K x J)
#   Résultat : matrice c de taille (I x J) correspondant à (a * b) % M
def mat_mul(a, b):
    # Dimensions des matrices d'entrée :
    # I : nombre de lignes de a
    # J : nombre de colonnes de b
    # K : nombre de colonnes de a (doit être égal au nombre de lignes de b)
    I, J, K = len(a), len(b[0]), len(b)
    # Initialisation de la matrice résultat c avec des zéros (dimensions I x J)
    c = [[0] * J for _ in range(I)]
    # Multiplication classique de matrices (triple boucle imbriquée)
    for i in range(I):
        for j in range(J):
            for k in range(K):
                # On additionne le produit des éléments correspondants selon la règle de multiplication matricielle
                c[i][j] += a[i][k] * b[k][j]
            # On prend le modulo M pour éviter que les nombres deviennent trop grands
            c[i][j] %= M
    return c

# Calcul de n0 et n1, qui sont des indices de début et de fin pour la boucle de chiffres de d chiffres
# -(-(10 ** d - A) // B) fait un arrondi "plafond" pour obtenir le nombre minimal d'itérations nécessaires
n0 = -(-(10 ** 0 - A) // B)  # Pour d=0 (première classe de chiffres)
n1 = -(-(10 ** 1 - A) // B)  # Pour d=1 (suivant)

# Initialisation du vecteur "ret" représentant l'état courant.
# C'est une matrice colonne 3x1.
# Les éléments peuvent représenter des sommes, termes constants, etc., selon la transformation de la matrice.
ret = [[0], [A], [1]]  # Premier terme, terme initial A, et le terme constant 1 (pour l'affine)

# On va itérer sur les longueurs de chiffres d de 1 à 18 inclus (car les entiers de 64 bits ont au plus 18 chiffres)
for d in range(1, 19):
    # Construction de la matrice de transition "mat" pour la longueur d.
    # La matrice encode l'opération d'ajout de B à chaque étape et la montée d'un chiffre en base 10 (puissance).
    mat = [
        [10 ** d, 1, 0],  # Cette ligne gère la propagation de la puissance selon la position de chiffre
        [0, 1, B],        # Cette ligne ajoute B à chaque itération sur l'accumulateur
        [0, 0, 1]         # Cette ligne maintient le terme constant (pour l'affine)
    ]
    # On ajuste n0 dans le cas où la première valeur tombe en dehors du domaine valide
    if n0 < 0 and 0 < n1:
        n0 = 0

    # On travaille uniquement si n0 valide : au moins n0 < n1 (donc il y a quelque chose à faire)
    if 0 <= n0 < n1:
        # On applique (n1 - n0) fois la matrice mat à l'état courant "ret" pour accumuler les effets
        ret = mat_mul(mat_pow(mat, n1 - n0), ret)
    # On déplace n0 et n1 pour la boucle suivante (on "avance" à la plage de chiffres d+1).
    # On borne n1 par L, la limite globale.
    n0, n1 = n1, min(-(-(10 ** (d + 1) - A) // B), L)

# Enfin, après avoir accumulé toutes les contributions, on affiche la valeur finale à l'indice [0][0] du vecteur résultat.
print(ret[0][0])