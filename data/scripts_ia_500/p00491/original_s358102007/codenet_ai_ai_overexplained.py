N, K = map(int, input().split())  # Lire deux entiers depuis l'entrée standard, assigner à N (longueur) et K (nombre de contraintes)
S = [-1] * N  # Initialiser une liste S de taille N remplie de -1, représentant des valeurs non fixées pour chaque position

for _ in [0] * K:  # Répéter K fois pour lire les contraintes fournies à l'entrée
    a, b = map(int, input().split())  # Lire deux entiers a et b, correspondants à l'indice et la valeur imposée
    S[a - 1] = b - 1  # Ajuster les indices pour qu'ils commencent à 0 et stocker la valeur imposée dans S à la position a-1

dp = [0] * 9  # Initialiser une liste dp de taille 9, représentant tous les états possibles du problème dynamique; 9 = 3 * 3
st, nd = S[:2]  # Extraire les deux premières valeurs de S, st et nd, qui peuvent être fixées ou non (-1)

if st + 1:  # Vérifier si st est fixé (st >= 0 en pénalisant -1 qui donne 0)
    if nd + 1:  # Vérifier si nd est fixé
        dp[st * 3 + nd] = 1  # Il y a exactement 1 moyen d'avoir l'état avec st et nd fixés, donc dp à cet état devient 1
    else:
        # Si nd n'est pas fixé, alors pour les 3 valeurs possibles de nd, assigner 1 dans dp pour la combinaison st, nd
        dp[st * 3:st * 4] = [1] * 3  # Slice dp entre indices st*3 et st*4 (3 éléments), mettre 1 pour chacune
elif nd + 1:  # Si st n'est pas fixé mais nd est fixé
    # Pour chaque état du premier élément (0 à 2), fixer nd et mettre 1 dans dp
    dp[nd::3] = [1] * 3  # Affecter à dp aux indices nd, nd+3, nd+6 (pas de st fixé, nd fixé)
else:
    dp = [1] * 9  # Ni st ni nd fixés, alors tous les 9 états sont initialement valides, donc 1 chacun

# Boucle pour calculer dp à partir du troisième élément jusqu'au dernier (placement dynamique)
for i in range(2, N):  # Parcourir les indices de 2 jusqu'à N-1 (0-based)
    cur = S[i]  # Prendre la valeur fixée à la position actuelle, ou -1 si non fixé
    tmp = [0] * 9  # Créer une nouvelle liste temporaire pour stocker les états prochains

    if cur + 1:  # Si la valeur actuelle est fixée (cur >= 0)
        for k in range(3):  # Pour chaque valeur possible du 1er élément d'une paire (0,1,2)
            # Calculer le nombre de façons pour position i:
            # Somme des dp au rang k dans chaque 3 éléments (dp[k::3])
            # Soustraire si la valeur cur est égale à k (pour éviter une double comptabilisation)
            tmp[k * 3 + cur] = sum(dp[k::3]) - dp[cur * 4] * (k == cur)
            # dp[cur * 4] correspond à l'élément diagonal dp[cur*3 + cur], qui doit être soustrait si k == cur
    else:  # Si la valeur actuelle n'est pas fixée, essayer toutes les valeurs possibles pour cur
        for cur in range(3):  # Pour chaque valeur possible de cur (0,1,2)
            for k in range(3):  # Pour chaque valeur possible de k
                # Même calcul que ci-dessus mais pour tous les cur possibles
                tmp[k * 3 + cur] = sum(dp[k::3]) - dp[cur * 4] * (k == cur)
    dp = tmp[:]  # Mettre à jour dp avec la liste calculée tmp

print(sum(dp) % 10000)  # Afficher la somme des valeurs de dp modulo 10000, résultat final du calcul dynamique