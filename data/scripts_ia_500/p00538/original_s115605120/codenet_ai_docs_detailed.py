# Lecture du nombre d'éléments
n = int(input())

# Lecture des valeurs dans une liste a
a = [int(input()) for _ in range(n)]

# Initialisation d'une matrice dp pour stocker les résultats intermédiaires
# dp[i][j] représente la valeur maximale pour un segment circulaire allant de i à j
dp = [[
    # Si i == j, le segment est d'une seule case, donc on prend la valeur a[i]
    a[i] if i == j else
    # Si j est l'élément suivant de i (segment de deux éléments), on prend le max des deux valeurs a[i] et a[j]
    max(a[i], a[(i + 1) % n]) if (i + 1) % n == j else
    # Sinon, la valeur est initialisée à 0
    0
    for j in range(n)]
    for i in range(n)
]

# Parcours des longueurs possibles de segments sur un cercle, en sautant deux éléments à chaque fois.
# Si n est pair, commencer à 3, sinon commencer à 2
for i in range(3 if n % 2 == 0 else 2, n, 2):
    for l in range(n):
        # Calcul de la borne droite r du segment circulaire à l en avançant i positions
        r = (l + i) % n

        # Liste pour stocker les différentes valeurs candidates pour dp[l][r]
        pat = []
        # On considère deux configurations possibles en bordure de segment (gauche/droite) pour déterminer la solution optimale
        for x, nextl, nextr in [(l, (l + 1) % n, r), (r, l, (r + n - 1) % n)]:
            # Choix entre avancer la borne gauche ou reculer la borne droite en fonction de la valeur des éléments adjacents
            if a[nextl] > a[nextr]:
                nextl = (nextl + 1) % n
            else:
                nextr = (nextr + n - 1) % n

            # On ajoute la valeur courante a[x] plus la meilleure solution du sous-segment défini par nextl à nextr
            pat.append(a[x] + dp[nextl][nextr])

        # On mémorise la meilleure valeur possible pour le segment circulaire de l à r
        dp[l][r] = max(pat)

# Impression du résultat final: la meilleure valeur possible parmi tous les segments circulaires voisins
print(max(dp[(i + 1) % n][i] for i in range(n)))