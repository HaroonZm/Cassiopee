# Demande à l'utilisateur d'entrer une valeur et convertit cette valeur en entier
n = int(input())  # Lecture du nombre n, doit être un entier

# Crée une liste dp qui va contenir des valeurs représentant le "coût minimum" pour chaque indice de 0 à n inclus
# La liste est initialisée avec la valeur positive infinie (float('inf')) pour signifier que le coût est inconnu ou très élevé
dp = [float('inf')] * (n + 1)  # n+1 éléments pour inclure 0 jusqu'à n

# Le coût pour atteindre 0 est de 0, car on part du point 0
dp[0] = 0

# Création d'une liste "cost" qui va stocker les coûts individuels.
# Il y a n-1 coûts à lire, on utilise une compréhension de liste pour lire n-1 entiers depuis l'utilisateur
cost = [int(input()) for _ in range(n - 1)]  # n-1 entrées à lire, une pour chaque coût

# Boucle principale, part de 1 jusqu'à n-1 inclus (range(1, n)), soit n-1 itérations au total
for i in range(1, n):
    # Boucle interne sur toutes les valeurs de 'j', allant de 0 inclus à i exclu
    for j in range(i):
        # dp[i-j] + cost[i-1] : coût pour aller de l'indice courant et marcher "i-j" pas,
        # puis payer le coût associé à la position i-1
        # On vérifie si ce coût nouvellement calculé est inférieur au coût connu (actuel) dp[j]
        # Si oui, alors il est logique de mettre à jour dp[j] avec la valeur la plus basse (l'optimum)
        if dp[i-j] + cost[i-1] < dp[j]:
            dp[j] = dp[i-j] + cost[i-1]  # Mise à jour de la valeur minimale trouvée pour dp[j]
            # Cette écriture équivaut à : dp[j] = min(dp[j], dp[i-j]+cost[i-1])

        # dp[j] + cost[i-1] : cette fois-ci, on part de dp[j], et on ajoute le coût en position i-1
        # On vérifie si le coût nouvellement calculé est inférieur dp[i-j] actuel
        if dp[j] + cost[i-1] < dp[i-j]:
            dp[i-j] = dp[j] + cost[i-1]  # Mise à jour de dp[i-j] pour garder la plus petite valeur
            # Équivaut à : dp[i-j] = min(dp[i-j], dp[j]+cost[i-1])
    # À la fin de chaque itération principale (pour chaque i), on pourrait afficher la liste dp,
    # mais cette ligne est commentée (invalide, car #print(dp))

# Après toutes les mises à jour de la liste dp, on affiche la valeur à l'indice spécifié
# Le problème demande d'afficher dp[n//2], c'est-à-dire à la position n divisé par 2 (division entière)
print(dp[n // 2])  # Affichage de la valeur du coût minimal pour l'indice n//2