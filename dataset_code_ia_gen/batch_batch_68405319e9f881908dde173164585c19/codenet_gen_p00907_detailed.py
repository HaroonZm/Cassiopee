def gaussian_elimination(A, b):
    """
    Résout un système linéaire Ax = b par élimination de Gauss sans pivot partiel.
    A est une matrice carrée (listes de listes), b un vecteur (liste).
    Renvoie le vecteur solution x.
    """
    n = len(A)
    # Elimination
    for i in range(n):
        # Trouver le pivot
        pivot = A[i][i]
        if abs(pivot) < 1e-15:
            # Si pivot presque nul, on cherche un pivot non nul plus bas (simple gestion)
            for r in range(i+1, n):
                if abs(A[r][i]) > 1e-15:
                    A[i], A[r] = A[r], A[i]
                    b[i], b[r] = b[r], b[i]
                    pivot = A[i][i]
                    break
        for j in range(i+1, n):
            if abs(A[j][i]) < 1e-15:
                continue
            factor = A[j][i]/pivot
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    # Remontée
    x = [0.0]*n
    for i in reversed(range(n)):
        s = b[i]
        for j in range(i+1, n):
            s -= A[i][j]*x[j]
        x[i] = s / A[i][i]
    return x

def evaluate_polynomial(coeffs, x):
    """
    Evalue un polynôme en x, coeffs est la liste des coefficients du terme constant au terme de degré d.
    """
    res = 0.0
    power = 1.0
    for c in coeffs:
        res += c*power
        power *= x
    return res

def find_wrong_value_index(d, values):
    """
    Trouve l'indice de la valeur incorrecte parmi valeurs correspondant aux f(0), f(1), ..., f(d+2)
    pour un polynôme de degré d.
    """
    n_points = d + 3
    # On veut déterminer les coefficients du polynôme f(x) = a0 + a1 x + ... + ad x^d
    # en utilisant tous les points sauf un (le suspecté faux).
    # Puis on vérifie le point exclu.
    #
    # On essaye chaque indice i de 0 à d+2:
    # - construire le système à partir des points sauf i
    # - résoudre pour trouver les coefficients
    # - vérifier la valeur exclue en évaluant le polynôme calculé en x=i
    # - si l'erreur sur ce point exclu est > 1.0, c'est le "faux" point

    for wrong_i in range(n_points):
        # Construire système (d+1) équations pour (d+1) inconnues
        # soit les d+2 points sauf le point wrong_i: on enlève ce point
        A = []
        b = []
        for j in range(n_points):
            if j == wrong_i:
                continue
            row = [1.0]
            for power in range(1, d+1):
                row.append(j**power)
            A.append(row)
            b.append(values[j])
        # Résoudre Ax=b, taille de A = d+2-1=d+1
        coeffs = gaussian_elimination(A, b)
        # Vérifier erreur sur le point exclu
        val_pred = evaluate_polynomial(coeffs, wrong_i)
        err = abs(val_pred - values[wrong_i])
        if err > 1.0:
            return wrong_i
    return -1  # Normalement ne doit pas arriver

def main():
    import sys
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        d_line = line.strip()
        if d_line == '0':
            break
        d = int(d_line)
        n_points = d + 3
        values = []
        for _ in range(n_points):
            val_line = input()
            values.append(float(val_line.strip()))
        wrong_index = find_wrong_value_index(d, values)
        print(wrong_index)

if __name__ == "__main__":
    main()