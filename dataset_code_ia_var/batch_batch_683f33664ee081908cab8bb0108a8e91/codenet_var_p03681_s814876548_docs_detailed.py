import math

def compute_factorial_mod(n, mod):
    """
    Calcule la factorielle de n modulo mod.

    Args:
        n (int): Le nombre dont on veut la factorielle.
        mod (int): Le modulo à appliquer.

    Returns:
        int: La factorielle de n modulo mod.
    """
    return math.factorial(n) % mod

def main():
    """
    Lit deux entiers depuis l'entrée standard, calcule le produit de leurs factorielles
    sous un modulo donné, puis affiche le résultat selon la différence absolue entre les deux entiers.
    La logique est la suivante :
    - Si la différence est supérieure ou égale à 2, affiche 0.
    - Si la différence est exactement 1, affiche (fa * fb) % mod.
    - Si les deux nombres sont égaux, affiche (2 * fa * fb) % mod.
    """
    mod = 10**9 + 7  # Modulo utilisé pour les calculs

    # Lecture des deux entiers a et b depuis l'entrée standard
    a, b = map(int, input().split())

    # Calcul des factorielles de a et b sous modulo
    fa = compute_factorial_mod(a, mod)
    fb = compute_factorial_mod(b, mod)

    # Produit des deux factorielles
    k = fa * fb

    # Détermination du résultat selon la différence absolue entre a et b
    if abs(a - b) >= 2:
        # Si la différence est >= 2, le résultat est 0
        print(0)
    elif abs(a - b) == 1:
        # Si la différence est exactement 1, afficher k modulo mod
        print(k % mod)
    elif abs(a - b) == 0:
        # Si a et b sont égaux, afficher (2 * k) modulo mod
        print((2 * k) % mod)

if __name__ == "__main__":
    main()