# Demander à l'utilisateur de saisir un entier représentant le nombre de jours ou d'étapes
n = int(input())

# Crée une table de programmation dynamique (DP) de taille (n+1) x 3 remplie de zéros
# Chaque ligne représente un jour, et chaque colonne représente une activité possible (par exemple A, B, C)
# dp[i][j] stockera le score maximal possible jusqu'au jour i si l'activité j est choisie le jour i
dp = [[0 for _ in range(3)] for _ in range(n+1)]

# Crée une liste vide pour stocker les valeurs associées à chaque activité pour chaque jour
abc = []

# Boucle pour chaque jour (de 1 à n inclus) afin de remplir la liste 'abc'
for i in range(1, n+1):
    # Lit une ligne d'entrée, sépare les valeurs entrées par l'utilisateur,
    # les convertit en entiers, et les ajoute comme une sous-liste dans 'abc'
    abc.append([int(x) for x in input().split()])

# Boucle principale pour remplir la table de programmation dynamique
# Parcourt chaque jour de 0 à n-1 (puisque 'abc' a des indices de 0 à n-1)
for i in range(n):
    # Parcourt toutes les activités possibles pour le jour actuel (j : activité du jour précédent)
    for j in range(3):
        # Parcourt toutes les activités possibles pour le jour suivant (k : activité du jour actuel)
        for k in range(3):
            # On ne peut pas faire la même activité deux jours de suite,
            # donc si les indices des activités sont identiques, on passe à l'itération suivante sans rien faire
            if j == k:
                continue
            # 'dp[i+1][k]' représente le score maximal si on choisit l'activité k le (i+1)-ième jour
            # On prend le maximum entre la valeur déjà présente dans dp[i+1][k] et
            # la somme du score maximal du jour précédent avec l'activité j (dp[i][j]) et
            # la valeur de l'activité k pour le jour i (abc[i][k])
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + abc[i][k])

# Initialise la variable 'ans' à zéro pour stocker le score maximal final
ans = 0

# Boucle pour vérifier toutes les activités du dernier jour (jour n)
for i in range(3):
    # Met à jour 'ans' si la valeur de dp[n][i] (score maximal en terminant par l'activité i le dernier jour)
    # est supérieure à la valeur actuelle de 'ans'
    ans = max(ans, dp[n][i])

# Affiche le score maximal trouvé après avoir examiné toutes les possibilités
print(ans)