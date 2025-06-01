def d_init(n):
    """
    Initialise la matrice des distances D entre toutes les paires d'éléments.

    Cette fonction parcourt toutes les paires distinctes d'indices dans D, 
    calcule la distance absolue entre leurs valeurs associées, et stocke 
    ces distances dans D pour les deux sens (i,j) et (j,i).

    Args:
        n (int): Nombre total d'éléments.
    """
    c = 0
    A = list(D.items())  # Récupération des items de D sous forme de liste pour slicing
    for i, e in A:
        c += 1
        # Pour chaque paire (i, j) distincte, calculer la distance absolue
        for j, f in A[c:]:
            tmp = abs(e - f)
            D[(i, j)] = tmp  # Distance de i vers j
            D[(j, i)] = tmp  # Distance de j vers i, symétrique
    return


def solve(idx, visited, weight):
    """
    Résout le problème de parcours optimal en utilisant la programmation dynamique.

    Cette fonction cherche à minimiser un coût total défini en fonction 
    des distances accumulées et des poids rencontrés sur la route. 
    Elle utilise un encodage binaire (bitmask) pour représenter l'ensemble des 
    sommets visités.

    Args:
        idx (int): Indice du noeud courant.
        visited (int): Bitmask représentant les noeuds déjà visités.
        weight (float): Poids total accumulé jusqu'au noeud courant.

    Returns:
        tuple:
            float: Coût minimal pour compléter le parcours à partir de idx.
            list: Liste ordonnée des noms correspondant au chemin optimal à partir de idx.
    """
    # Cas de base : si tous les noeuds ont été visités, retourner 0 et le nom actuel
    if visited == (1 << n) - 1:
        return 0, name[idx]

    tmp1, tmp2 = dp[idx][visited]
    # Si l'état a déjà été calculé, retourner la valeur mémorisée
    if tmp1 != 1e12:
        return tmp1, tmp2

    x1 = 1e12  # Initialisation du coût minimal très élevé
    x2 = []

    # Parcourir tous les noeuds pour en trouver un non visité
    for i in range(n):
        i1 = 1 << i
        if (visited & i1) == 0:  # Si le noeud i n'a pas encore été visité
            # Calculer récursivement le coût pour visiter i
            tmp1, tmp2 = solve(i, visited | i1, weight + W[i])
            # Ajouter le coût d'aller de idx à i selon la formule donnée
            tmp1 += D[(i, idx)] / 2000.0 * (weight + 70.0)
            # Si ce chemin est meilleur, le mémoriser
            if x1 > tmp1:
                x1 = tmp1
                x2 = tmp2
    # Construire la route en ajoutant le nom du noeud courant en tête
    x2 = name[idx] + x2
    dp[idx][visited] = [x1, x2]  # Mémoriser le résultat dans la table de programmation dynamique
    return x1, x2


# Initialisation des variables globales et lecture des données d'entrée
name = {}  # Dictionnaire pour stocker le nom (liste avec un entier) de chaque noeud
D = {}     # Dictionnaire pour stocker les distances (initialement un scalaire pour chaque noeud, puis les distances entre pairs)
W = {}     # Dictionnaire pour stocker les poids multipliés par 20
n = int(input())  # Nombre de noeuds (entier)

# dp est une matrice 2D avec n lignes et 2^n colonnes, initialisée avec un coût très élevé (1e12)
# et une liste vide pour garder le chemin
dp = [[[1e12, []] for _ in range(1 << n)] for _ in range(n)]

# Lecture des données pour chaque noeud : a (nom), b (distance initiale), c (poids)
for i in range(n):
    a, b, c = map(int, raw_input().split())
    name[i] = [a]  # Le nom est une liste contenant un entier (pour pouvoir concaténer facilement)
    D[i] = b       # Distance initiale associée au noeud (sera réutilisée dans d_init)
    W[i] = c * 20  # Poids multiplié par 20 comme précisé dans le problème

# Calcul des distances entre tous les noeuds
d_init(n)

# Recherche de la solution optimale parmi toutes les starts possibles
ans1 = 1e12  # Coût minimal initial très élevé
route = []   # Chemin correspondant à ce coût minimal

for i, e in W.items():
    tmp1, tmp2 = solve(i, 1 << i, e)  # Résoudre pour chaque noeud de départ
    if ans1 > tmp1:
        ans1 = tmp1
        route = tmp2

# Affichage du chemin optimal sur une seule ligne, séparé par des espaces
for e in route[:-1]:
    print(str(e), end=' ')
print(str(route[-1]))