import sys

def build_matrix(m, n, d):
    """
    Pré-calculer la matrice d'incidence M (n*m x n*m)
    où chaque colonne correspond à un interrupteur (pièce)
    et chaque ligne à une lumière.
    M[i,j] = 1 si le toggling de l'interrupteur j affecte la lumière i, sinon 0.
    Indices linéaires i,j sont calculés par i = x*n + y (row-major).
    """
    size = n * m
    M = [[0] * size for _ in range(size)]
    # Pour chaque interrupteur (xj, yj)
    for xj in range(n):
        for yj in range(m):
            col = xj * m + yj
            # Affecte la lumière (xi, yi) si distance de Manhattan = d
            for xi in range(n):
                for yi in range(m):
                    row = xi * m + yi
                    dist = abs(xi - xj) + abs(yi - yj)
                    if dist == d or dist == 0:
                        M[row][col] = 1
    return M

def gauss_jordan(M, b):
    """
    Résolution du système linéaire mod 2 Mx = b
    utilisant l'élimination de Gauss-Jordan sur GF(2).
    M est une matrice carrée carrée (size x size),
    b est un vecteur taille size.
    Retourne True si solution existe, False sinon.
    """
    size = len(M)
    # Travail sur une copie locale pour préserver l'original
    A = [row[:] for row in M]
    B = b[:]

    row = 0
    for col in range(size):
        pivot = -1
        # Trouver pivot en ligne >= row avec un 1 dans la colonne col
        for r in range(row, size):
            if A[r][col] == 1:
                pivot = r
                break
        if pivot == -1:
            # Pas de pivot dans cette colonne, passer à la suivante
            continue
        # Échanger lignes pivot et row
        if pivot != row:
            A[row], A[pivot] = A[pivot], A[row]
            B[row], B[pivot] = B[pivot], B[row]
        # Eliminer 1 dans cette colonne pour toutes les autres lignes
        for r in range(size):
            if r != row and A[r][col] == 1:
                # XOR des lignes
                for c in range(col, size):
                    A[r][c] ^= A[row][c]
                B[r] ^= B[row]
        row += 1
    # Après réduction en forme échelonnée,
    # vérifier la consistance du système
    for r in range(row, size):
        if B[r] == 1:
            # 0 = 1 impossible => pas de solution
            return False
    return True

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        # Lire m, n, d
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if line == '':
            continue
        m, n, d = map(int, line.split())
        if m == 0 and n == 0 and d == 0:
            break
        # Lire l'état initial des lumières
        lights = []
        for _ in range(n):
            row = list(map(int, input_lines[idx].strip().split()))
            idx += 1
            lights.append(row)
        # Construire la matrice d'incidence
        M = build_matrix(m, n, d)
        # Transformer l'état initial en vecteur b linéaire (mod 2)
        b = []
        for i in range(n):
            for j in range(m):
                # 1 = lumière allumée (besoin d'éteindre -> toggler avantageux)
                b.append(lights[i][j])
        # Résoudre Mx = b mod 2
        can_turn_off = gauss_jordan(M, b)
        print(1 if can_turn_off else 0)

if __name__ == '__main__':
    main()