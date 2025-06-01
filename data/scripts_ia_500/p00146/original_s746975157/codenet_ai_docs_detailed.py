def d_init(n):
    """
    Initialise le dictionnaire D avec les distances absolues entre les points.

    Arguments:
    n -- le nombre total de points

    Cette fonction utilise les éléments déjà présents dans le dictionnaire D,
    calcule les distances absolues entre chaque paire et met à jour D de façon symétrique.
    """
    c = 0
    # Récupère une liste des paires (clé, valeur) dans D
    A = list(D.items())
    for i, e in A:
        c += 1
        # Parcourt toutes les paires suivantes pour calculer la distance absolue
        for j, f in A[c:]:
            a = abs(e - f)
            D[(i, j)] = a
            D[(j, i)] = a  # Distance symétrique


def solve(p, v, w):
    """
    Résout le problème par programmation dynamique en cherchant le coût minimum.

    Arguments:
    p -- l'indice du point actuel
    v -- un entier représentant l'ensemble des points visités sous forme de bits (bitmask)
    w -- un poids accumulé (par exemple temps ou coût)

    Retourne:
    un tuple (coût minimum total, liste des points visités ordonnée)
    
    Cette fonction utilise la mémoïsation par dp pour éviter les recalculs.
    """
    # Condition de terminaison : tous les points visités
    if v == (1 << n) - 1:
        return 0, N[p]  # Coût 0, liste associée au point actuel p

    a, b = dp[p][v]  # Récupère résultat mémoïsé
    if a >= 0:
        return a, b  # Renvoie si déjà calculé

    T = 1e10  # Initialise T avec une valeur très élevée pour trouver un minimum
    for i in range(n):
        i1 = 1 << i
        # Si le point i n'a pas encore été visité dans v
        if (v & i1) == 0:
            # Appel récursif en incluant ce point dans l'ensemble visité
            a, b = solve(i, v | i1, w + W[i])
            # Ajoute le coût du déplacement entre p et i, pondéré par w
            a += D[(i, p)] * w
            if T > a:
                T = a  # Mise à jour du coût minimum
                R = b  # Mise à jour de la liste associée
    R = N[p] + R  # Concatène la liste du point p au résultat construit
    dp[p][v] = [T, R]  # Mémoïsation du résultat
    return T, R


# Initialisation des dictionnaires et de la taille de l'instance
N = {}  # Contient une liste associée à chaque point
D = {}  # Distances ou coûts associés
W = {}  # Poids ou temps pour chaque point

# Lecture du nombre de points
n = int(input())

# Initialisation de la table de mémoïsation dp à -1 avec structure [coût, chemin]
# dp[p][v] où p est le point courant et v est un bitmask des points visités
dp = [[[-1, []] for _ in range(1 << n)] for _ in range(n)]

# Lecture des données pour chaque point
for i in range(n):
    a, b, c = map(int, input().split())
    N[i] = [a]                # Liste associée au point i contenant a
    D[i] = b / 2000.0        # Valeur b convertie et stockée (distance initiale)
    W[i] = c * 20            # Pondération calculée et stockée

# Calcul des distances absolues entre points via la fonction d_init
d_init(n)

# Recherche du coût minimal en commençant depuis chaque point possible
minT = 1e10
R = []
for i, e in W.items():
    # Appel de la fonction solve avec point i comme point de départ et trajet initial
    a, b = solve(i, 1 << i, e + 70.0)
    if minT > a:
        minT = a
        R = b

# Affichage du résultat final : la liste des points sous forme de chaînes
for e in R:
    print(str(e), end=' ')