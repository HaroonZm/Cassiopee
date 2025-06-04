# Lecture des dimensions N (lignes) et M (colonnes)
N, M = map(int, input().split())

# Lecture du plateau A : liste de chaînes de caractères
A = [input() for _ in range(N)]

# Lecture du plateau B : liste de chaînes de caractères
B = [input() for _ in range(N)]

# Initialisation du compteur de cases différentes
differences = 0

# Parcours de chaque case du plateau
for i in range(N):
    for j in range(M):
        # Comparaison des caractères correspondants dans A et B
        if A[i][j] != B[i][j]:
            differences += 1

# Affichage du nombre de différences
print(differences)