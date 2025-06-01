import sys
sys.setrecursionlimit(10**7)

# Lecture des entrées : A, B sont les nombres de cartes d'Anna et Bruno
A, B = map(int, input().split())
anna = list(map(int, input().split()))
bruno = list(map(int, input().split()))

# But : Trouver la plus grande longueur n telle qu'il existe un sous-ensemble de cartes d'Anna
# (dans l'ordre, sans réarrangement mais avec suppression arbitraire de cartes)
# et un sous-sous-ensemble contigu de cartes de Bruno (sous-séquence contigüe obtenue par suppression
# de cartes d'en haut et en bas) qui sont égaux.
#
# On peut remarquer que pour Bruno, on ne garde qu'un sous-tableau contigü (segment contigu)
# tandis que pour Anna, on peut choisir n'importe quelle sous-séquence (suppression arbitraire de cartes,
# donc ce qui compte c'est trouver une sous-séquence de Anna qui correspond à un segment de Bruno).
#
# Donc le problème est en fait :
# - Trouver la plus longue sous-séquence de anna qui est égale à un segment contigu de Bruno.

# C'est donc une variante de plus longue sous-séquence commune (LCSS),
# mais avec la contrainte que la partie de bruno est un segment contigu.
# Cette taille correspond donc à la plus longue sous-séquence de Anna (avec suppression d'élts)
# et un segment contigu de Bruno.

# Approche efficace:
# Pour chaque début de segment dans Bruno : start
#   Pour chaque fin de segment dans Bruno : end
#     on considère segment Bruno[start:end+1]
# On essaie de trouver la plus grande sous-séquence dans Anna qui correspond à ce segment.

# Cependant, tester tous les segments de Bruno B(B+1)/2 = ~12.5 millions (pour max B=5000),
# ceci est trop coûteux si on fait un DP classique pour chaque segment.

# Optimisation :
# On peut utiliser une DP pour Anna qui se rapproche d'une "longest common substring"
# avec la contrainte qu'Anna peut sauter des éléments (sous-séquence), 
# mais Bruno doit être segment contigu.

# On fait un DP en colonne pour tous les indices de Anna, et on itère sur les indices de Bruno
# mais on doit gérer la possibilité de sauter les cartes d'Anna (dans leur ordre).

# Méthode:
# L'idée est d'utiliser une DP dimensionnée par (position dans Anna, position dans Bruno)
# où dp[i][j] = longueur de la plus longue correspondance commune (qui est un segment contigu de Bruno)
# quand on regarde la sous-séquence d'Anna commençant à i quelque part plus haut (mais dp est calculé de bas en haut).

# On peut construire une DP où:
# - on fait dp[i][j] : longueur de la plus longue sous-séquence finissant en Anna[i] et Bruno[j]
#   pour la situation où on ne supprime pas la carte Bruno[j] (car Bruno doit être segment contigu),
#   mais Anna peut sauter.

# Implémentation:
# On parcourt les indices de Bruno j de 0 à B-1
# et on maintient un tableau aux de dp: longueur de la correspondance pour les préfixes de Anna.

# A chaque étape j (fixe une carte de Bruno), on crée un tableau new_dp pour dp des correspondances
# se terminant au Bruno[j], et on met à jour les longueurs selon si anna[i] == bruno[j].
# Puis on remplace dp par new_dp.

# Mais attention, ici Anna peut sauter, donc dp[i] dépend de dp[i-1] s'il n'y a pas de match,
# mais car Anna peut sauter des cartes, on peut démarrer une sous-séquence à tout moment.
# La contrainte est qu'on a une séquence contiguë dans Bruno, donc on parcourt Bruno de gauche à droite,
# et on essaie d'aligner substring de Bruno avec une sous-séquence de Anna.

# Détail technique:
# Pour chaque position dans Bruno j (progressive),
# dp[i] = longueur de la plus longue correspondance finissant sur Anna[i] et Bruno[j]
# On calcule en partant de i=A-1 à 0 pour ne pas écraser les valeurs utilisées dans la même étape.

# Résultat final: on garde la max longueur trouvée parmi tous les dp[i].

dp = [0]*(A+1)
max_score = 0

# On boucle sur Bruno, colonne par colonne
for j in range(B):
    # new_dp pour cette colonne j (pour correspondance avec bruno[j])
    new_dp = [0]*(A+1)
    # On parcourt Anna à l'envers pour utiliser dp[i-1] de l'itération précédente
    for i in range(A-1,-1,-1):
        if anna[i] == bruno[j]:
            new_dp[i] = dp[i+1] + 1
            if new_dp[i] > max_score:
                max_score = new_dp[i]
        else:
            new_dp[i] = 0
    dp = new_dp

# Affichage du résultat maximal trouvé
print(max_score)