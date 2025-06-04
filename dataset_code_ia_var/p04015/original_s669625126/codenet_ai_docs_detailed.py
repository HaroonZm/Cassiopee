def makelist2(n, m):
    """
    Crée une liste bidimensionnelle de taille n x m remplie de zéros.

    Args:
        n (int): Nombre de lignes.
        m (int): Nombre de colonnes.

    Returns:
        list: Liste bidimensionnelle (liste de listes) de zéros.
    """
    # Utilise une compréhension de liste pour générer chaque ligne de la matrice
    return [[0 for k in range(m)] for i in range(n)]

# Lecture des entrées de l'utilisateur : n (taille du tableau) et a (valeur de référence)
n, a = map(int, input().split())

# Lecture de la liste d'entiers x
x = list(map(int, input().split()))

# Recherche de la valeur maximale entre les éléments de x et a
X = max(x)
X = max(X, a)

# Construction d'une nouvelle liste b contenant les différences entre chaque x[i] et a
b = []
for i in range(n):
    b.append(x[i] - a)

# Initialisation de la table dp : il s'agit d'une matrice de taille (n+1) x (2*n*X+1)
# dp[j][t] indiquera, pour les j premiers éléments, le nombre de sous-ensembles dont
# la somme des (x[i]-a) vaut (t - n*X), décalé pour gérer les sommes négatives
dp = makelist2(n + 1, 2 * n * X + 1)

# Initialisation de dp[0][n*X] à 1 : il y a une façon d'obtenir une somme de 0 avec 0 éléments
dp[0][n * X] = 1

# Remplissage de la table dp via une programmation dynamique
for j in range(n + 1):  # Pour chaque nombre d'éléments utilisés
    for t in range(2 * n * X + 1):  # Pour chaque somme possible décalée
        if j >= 1 and (t - b[j - 1] < 0 or t - b[j - 1] > 2 * n * X):
            # Si on ne peut pas retirer b[j-1] sans sortir des bornes, 
            # on ne prend pas le j-ème élément, donc héritage de la solution précédente
            dp[j][t] = dp[j - 1][t]
        elif j >= 1:
            # Sinon, somme des façons de faire sans et avec le j-ème élément
            dp[j][t] = dp[j - 1][t] + dp[j - 1][t - b[j - 1]]

# Affichage du résultat final :
# dp[n][n*X] : nombre de sous-ensembles dont la somme des (x[i]-a) est 0
# On retire 1 pour ne pas compter le sous-ensemble vide
print(dp[n][n * X] - 1)