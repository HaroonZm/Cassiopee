from typing import Tuple

def gcd(a: int, b: int) -> int:
    """
    Calcule le plus grand commun diviseur (PGCD) de deux entiers a et b
    en utilisant l'algorithme d'Euclide récursif.

    Args:
        a (int): Le premier entier.
        b (int): Le second entier.

    Returns:
        int: Le PGCD de a et b.
    """
    # Si a est divisible par b, b est le PGCD.
    if a % b == 0:
        return b
    # Sinon, on continue la division par reste.
    return gcd(b, a % b)

def 数学は最強也(a: int, b: int) -> int:
    """
    Pour deux entiers a et b, calcule une valeur basée sur leur PGCD :
    Soit q = PGCD(a, b), la fonction retourne :
      q * ((a // q) + (b // q) - 1)

    Args:
        a (int): Le premier entier (typiquement une différence de coordonnées).
        b (int): Le second entier (typiquement une différence de coordonnées).

    Returns:
        int: Résultat du calcul selon la formule donnée.
    """
    q = gcd(a, b)
    # Calcule selon la formule donnée dans le code initial.
    return q * ((a // q) + (b // q) - 1)

if __name__ == "__main__":
    # Lecture de quatre entiers séparés par des espaces sur une même ligne.
    a, b, c, d = map(int, input().split())
    # Calcul des distances absolues entre les coordonnées a et c, puis b et d.
    diff1 = abs(a - c)
    diff2 = abs(b - d)
    # Application de la fonction principale pour obtenir le résultat et affichage.
    print(数学は最強也(diff1, diff2))