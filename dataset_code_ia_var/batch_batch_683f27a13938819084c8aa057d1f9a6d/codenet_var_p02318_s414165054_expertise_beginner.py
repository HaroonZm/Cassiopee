def levenshtein_dist(a, b):
    m = len(a)
    n = len(b)
    # Création de la matrice
    dp = []
    for i in range(n+1):
        row = []
        for j in range(m+1):
            row.append(0)
        dp.append(row)
    # Initialisation des bords
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    # Calcul des distances
    for i in range(1, n+1):
        for j in range(1, m+1):
            if b[i-1] == a[j-1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i-1][j] + 1,    # Suppression
                dp[i][j-1] + 1,    # Insertion
                dp[i-1][j-1] + cost # Remplacement
            )
    return dp

a = input()
b = input()
# Conversion en listes de caractères
a_list = []
for c in a:
    a_list.append(c)
b_list = []
for c in b:
    b_list.append(c)
# Calcul et affichage
res = levenshtein_dist(a_list, b_list)
print(res[-1][-1])