M, N = map(int, input().split())
S = input()
T = input()

# Prétraitement : on ne peut enchaîner que des wagons alternant entre 'I' et 'O'
# et la première et dernière lettre doivent être 'I'.
# Le train est formé en choisissant un ordre intercalé à partir des deux dépôts.

INF = -10**9

# dp[i][j][k] = longueur max de train possible en ayant pris i wagons de S, j wagons de T,
# avec k = 0 si le dernier wagon pris vient de S, 1 si du T, 2 si on n'a pas encore commencé à prendre
dp = [[[INF]*(3) for _ in range(N+1)] for __ in range(M+1)]

# On peut commencer un train uniquement si la première voiture est 'I', et on commence à partir
# de la voiture 0 de S ou de T
for i in range(M):
    if S[i] == 'I':
        dp[i+1][0][0] = 1
    else:
        break
for j in range(N):
    if T[j] == 'I':
        dp[0][j+1][1] = 1
    else:
        break

# Fonction pour savoir si on peut enchaîner deux wagons (c1, c2)
def can_connect(c1, c2):
    return c1 != c2

for i in range(M+1):
    for j in range(N+1):
        for last in range(3):
            if dp[i][j][last] < 0:
                continue
            length = dp[i][j][last]
            # On peut essayer de prendre un nouveau wagon de S si possible
            if i < M:
                c = S[i]
                if last == 2:
                    # pas encore commencé, on l'a déjà géré, on ne doit pas arriver ici
                    pass
                elif last == 0:
                    # dernier wagon vient de S, on doit alterner donc c doit être différent de S[i-1]
                    prev = S[i-1]
                    if can_connect(prev, c):
                        dp[i+1][j][0] = max(dp[i+1][j][0], length+1)
                elif last == 1:
                    # dernier wagon vient de T, on doit alterner avec T[j-1]
                    if j > 0:
                        prev = T[j-1]
                        if can_connect(prev, c):
                            dp[i+1][j][0] = max(dp[i+1][j][0], length+1)
                    else:
                        # si j==0, alors la train ne vient que de S for now, donc alterner avec aucune est ok? Non, il faut qu'il y ait un wagon
                        # Donc on ne peut pas prendre S tout de suite dans ce cas
                        pass

            # On peut essayer de prendre un nouveau wagon de T si possible
            if j < N:
                c = T[j]
                if last == 2:
                    # idem pas encore commencé
                    pass
                elif last == 1:
                    # dernier wagon de T, on doit alterner avec précédent de T
                    prev = T[j-1]
                    if can_connect(prev, c):
                        dp[i][j+1][1] = max(dp[i][j+1][1], length+1)
                elif last == 0:
                    # dernier wagon de S, on doit alterner avec S[i-1]
                    if i > 0:
                        prev = S[i-1]
                        if can_connect(prev, c):
                            dp[i][j+1][1] = max(dp[i][j+1][1], length+1)
                    else:
                        # i==0, donc on n'a rien en S donc pas de problème mais on doit alterner...
                        pass

# Pour la partie mixte (commencer à prendre des wagons après avoir déposé certains),
# on peut aussi considérer commencer à prendre un nouveau wagon directement ici si last == 2

# En réalité, on doit pouvoir commencer à n'importe quel point dans S et T:

for i in range(M+1):
    for j in range(N+1):
        if i < M and S[i] == 'I': # commencer ici
            dp[i+1][j][0] = max(dp[i+1][j][0], 1)
        if j < N and T[j] == 'I':
            dp[i][j+1][1] = max(dp[i][j+1][1], 1)

# On applique une boucle pour tenter de prolonger de manière fiable :

# Nous réitérons plusieurs fois pour propager les améliorations (DP avec alternance)
for _ in range(max(M,N)):
    updated = False
    for i in range(M+1):
        for j in range(N+1):
            for last in range(2):
                if dp[i][j][last] < 0:
                    continue
                length = dp[i][j][last]
                # Essayer d'ajouter un wagon à partir de S
                if i < M:
                    c = S[i]
                    if last == 0:
                        prev = S[i-1]
                        if can_connect(prev, c):
                            if dp[i+1][j][0] < length + 1:
                                dp[i+1][j][0] = length + 1
                                updated = True
                    elif last == 1:
                        if j > 0:
                            prev = T[j-1]
                            if can_connect(prev, c):
                                if dp[i+1][j][0] < length + 1:
                                    dp[i+1][j][0] = length + 1
                                    updated = True
                    else:
                        if c == 'I':
                            if dp[i+1][j][0] < 1:
                                dp[i+1][j][0] = 1
                                updated = True
                # Essayer d'ajouter un wagon à partir de T
                if j < N:
                    c = T[j]
                    if last == 1:
                        prev = T[j-1]
                        if can_connect(prev, c):
                            if dp[i][j+1][1] < length + 1:
                                dp[i][j+1][1] = length + 1
                                updated = True
                    elif last == 0:
                        if i > 0:
                            prev = S[i-1]
                            if can_connect(prev, c):
                                if dp[i][j+1][1] < length + 1:
                                    dp[i][j+1][1] = length + 1
                                    updated = True
                    else:
                        if c == 'I':
                            if dp[i][j+1][1] < 1:
                                dp[i][j+1][1] = 1
                                updated = True
    if not updated:
        break

# On doit s'assurer que le train finis par un wagon 'I'
# donc on ne compte que dp[i][j][last] où la dernière wagon est 'I'

ans = 0
for i in range(M+1):
    for j in range(N+1):
        for last in range(2):
            length = dp[i][j][last]
            if length <= 0:
                continue
            # dernier wagon est dans S si last==0, T si last==1
            if last == 0:
                if i > 0 and S[i-1] == 'I':
                    if length > ans:
                        ans = length
            else:
                if j > 0 and T[j-1] == 'I':
                    if length > ans:
                        ans = length

print(ans)