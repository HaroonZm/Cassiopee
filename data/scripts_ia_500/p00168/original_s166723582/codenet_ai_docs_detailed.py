from math import ceil

# Définition d'une constante représentant une très grande valeur pour initialiser le tableau DP
INF = int(1e18)

# Initialisation d'un tableau DP (programmation dynamique) de taille 32, rempli avec la valeur INF
DP = [INF for _ in range(32)]

# Initialisation des premières conditions de base pour la suite définie :
# DP[1], DP[2] et DP[3] sont fixés manuellement selon le problème
DP[1] = 1
DP[2] = 1
DP[3] = 2

# Remplissage du tableau DP pour les indices de 4 à 31 inclus
# Chaque valeur DP[i] est la somme des trois valeurs précédentes : DP[i-1], DP[i-2] et DP[i-3]
for i in range(4, 32):
    DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]

def calculate_result(n: int) -> int:
    """
    Calcule le résultat selon une règle basée sur la suite DP pré-calculée.

    Args:
        n (int): L'entier d'entrée pour lequel calculer le résultat.

    Returns:
        int: Le résultat calculé, qui correspond au plafond de DP[n+1] divisé par 3650.
    """
    # On récupère DP[n+1], puis on divise par 3650 et on applique ceil pour arrondir vers le haut
    return ceil(DP[n + 1] / 3650)


# Boucle principale pour traiter plusieurs entrées jusqu'à la lecture de 0
while True:
    # Lecture d'un entier au clavier
    n = int(input())
    
    # Condition d'arrêt : si l'entrée est 0, on quitte la boucle
    if n == 0:
        break

    # Affichage du résultat calculé pour l'entrée lue
    print(calculate_result(n))