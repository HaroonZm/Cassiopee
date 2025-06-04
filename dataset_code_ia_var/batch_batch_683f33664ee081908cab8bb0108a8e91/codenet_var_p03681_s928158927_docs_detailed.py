import sys

def permutation(n, x, mod=10**9+7):
    """
    Calcule le nombre de permutations (nPx), c'est-à-dire le nombre de façons d'arranger 'x'
    éléments distincts parmi 'n', modulo 'mod'.
    
    Par exemple, permutation(5, 2) retournera 20, car il y a 5*4 façons d’arranger 2 éléments parmi 5.
    
    Parameters:
        n (int): Le nombre total d’éléments.
        x (int): Le nombre d’éléments à arranger.
        mod (int, optional): La valeur de modulo à appliquer (défaut: 10**9+7).
    
    Returns:
        int: Le résultat de la permutation nPx modulo 'mod'.
    """
    result = 1
    # Calcul du produit n * (n-1) * ... * (n-x+1), tout en appliquant le modulo à chaque étape
    for i in range(n, n - x, -1):
        result = (result * i) % mod
    return result

# Lecture de l'entrée standard, deux entiers N et M
N, M = map(int, sys.stdin.readline().strip().split())

# Vérification des cas particuliers selon la différence absolue entre N et M
if abs(N - M) > 1:
    # Si la différence est supérieure à 1, il n'existe aucune solution valide.
    print(0)
elif abs(N - M) == 1:
    # S'il y a une différence de 1, le nombre total de configurations est le produit
    # des permutations de N et de M éléments, modulo 10**9+7.
    print(permutation(N, N) * permutation(M, M) % (10**9+7))
else:
    # Si N et M sont égaux, il faut multiplier par 2 pour tenir compte des deux
    # ordres possibles, puis multiplier par les permutations respectives.
    print(2 * permutation(N, N) * permutation(M, M) % (10**9+7))