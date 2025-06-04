import sys

def main():
    """
    Lit la taille de la matrice N, l'exposant K, la matrice d, puis calcule
    la somme de tous les éléments de la matrice d élevée à la puissance K, modulo 10^9+7.
    Le résultat est affiché à la sortie standard.
    """
    input = sys.stdin.readline

    # Lecture de N (taille de la matrice) et K (exposant) à partir de l'entrée standard
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7  # Modulo donné pour toutes les opérations

    # Lecture de la matrice d (N x N) depuis l'entrée standard
    d = [list(map(int, input().split())) for _ in range(N)]

    # Détermine le nombre de bits nécessaires pour représenter K
    ln = K.bit_length()

    # Convertit K en binaire et prépare une liste de bits (ordre du moins significatif au plus)
    bn = list(bin(K)[2: ])
    bn.reverse()

    # Initialise la matrice identité de taille N comme matrice de résultat
    res = [[int(i == x) for i in range(N)] for x in range(N)]

    # Exponentiation rapide de matrices via les bits de K
    for i in range(ln):
        if int(bn[i]):
            res = ArrayMultiple(res, d, mod)
        d = ArrayMultiple(d, d, mod)

    # Calcule la somme de tous les éléments de la matrice résultante modulo mod
    rres = 0
    for r in res:
        for x in r:
            rres += x
            rres %= mod
    print(rres)

def ArrayMultiple(a, b, mod):
    """
    Effectue la multiplication de deux matrices carrées a et b de taille n,
    avec réduction modulo mod.

    Args:
        a (List[List[int]]): Première matrice à multiplier (n x n)
        b (List[List[int]]): Deuxième matrice à multiplier (n x n)
        mod (int): Modulo à appliquer à chaque opération

    Returns:
        List[List[int]]: Résultat de la multiplication matricielle, modulo mod
    """
    n = len(a)
    # Initialise la matrice résultat c avec des zéros
    c = [[0] * n for _ in range(n)]
    # Effectue la multiplication standard de matrices
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= mod  # Réduction après chaque addition/multiplication
    return c

if __name__ == "__main__":
    main()