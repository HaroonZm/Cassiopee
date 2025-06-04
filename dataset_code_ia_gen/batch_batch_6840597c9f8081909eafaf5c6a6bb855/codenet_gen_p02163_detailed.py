# Solution complète en Python avec commentaires détaillés

import sys

def main():
    input = sys.stdin.readline

    N = int(input())
    # On modélise la transformation de la valeur initiale x0 en la valeur finale xN
    # au travers d'une fonction affine : xN = a * x0 + b
    # Initialement, a = 1, b = 0 (xN = x0)
    a, b = 1, 0

    for _ in range(N):
        q, x = map(int, input().split())
        # Selon le type de requête, on met à jour a et b
        if q == 1:
            # multiplier par x : new_x = xN * x = (a * x0 + b)*x = (a*x)*x0 + b*x
            a *= x
            b *= x
        elif q == 2:
            # ajouter x : new_x = xN + x = a*x0 + b + x = a*x0 + (b + x)
            b += x
        else:
            # soustraire x : new_x = xN - x = a*x0 + b - x = a*x0 + (b - x)
            b -= x

    # Le magicien veut exprimer x0 en fonction de xN:
    # x0 = (xN + A) / B
    # on a xN = a*x0 + b => x0 = (xN - b) / a
    # en identifiant, on trouve A = -b, B = a
    A = -b
    B = a

    # La contrainte précise que B != 0 et la solution est unique
    print(A, B)

if __name__ == "__main__":
    main()