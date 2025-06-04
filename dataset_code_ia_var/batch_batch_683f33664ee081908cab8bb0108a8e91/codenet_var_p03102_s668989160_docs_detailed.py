def count_valid_rows(N, M, C, B, rows):
    """
    Compte le nombre de lignes (ou cas/tests) pour lesquelles la somme pondérée des éléments de la ligne
    et du vecteur B, moins la constante C, est strictement positive.

    Paramètres :
        N (int): Nombre de lignes à traiter.
        M (int): Nombre de colonnes (longueur de chaque ligne ainsi que du vecteur B).
        C (int): Constante à comparer.
        B (list of int): Vecteur de coefficients à utiliser avec chaque ligne.
        rows (list of list of int): Liste contenant N listes, chacune de longueur M.

    Retourne :
        int: Nombre de lignes vérifiant la condition précisée.
    """
    ans = 0  # Compteur du nombre de lignes satisfaisant la condition

    for i in range(N):
        A = rows[i]  # Récupère la i-ème ligne à traiter
        S = 0  # Initialisation de la somme pondérée pour cette ligne

        for j in range(M):
            S += A[j] * B[j]  # Ajoute la contribution pondérée de chaque élément

        # Vérifie si la somme pondérée moins C est strictement positive
        if S > -C:
            ans += 1  # Incrémente le compteur si la condition est satisfaite

    return ans


# Lecture des entrées depuis l'utilisateur

# Lit N, M, et C sur la première ligne
N, M, C = map(int, input().split())

# Lit le vecteur B sur la seconde ligne
B = list(map(int, input().split()))

# Lit ensuite N lignes, chacune avec M entiers
rows = []
for _ in range(N):
    row = list(map(int, input().split()))
    rows.append(row)

# Calcule et affiche le nombre de lignes satisfaisant la condition
result = count_valid_rows(N, M, C, B, rows)
print(result)