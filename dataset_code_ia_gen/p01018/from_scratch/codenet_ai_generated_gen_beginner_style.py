L, n = map(int, input().split())
warps = []
for _ in range(n):
    P, D, T = map(int, input().split())
    warps.append((P, D, T))

# Pour chaque position, on va calculer le temps min pour y arriver.
# Comme L peut être grand, on ne peut pas parcourir tout de 0 à L directement.
# On utilise seulement les positions importantes : 0, L et les positions de départ et arrivées des warps.

points = set([0, L])
for P, D, T in warps:
    points.add(P)
    points.add(P + D)

points = sorted(points)

# On crée un dictionnaire pour savoir l'indice d'une position dans la liste points
pos_index = {p: i for i, p in enumerate(points)}

# On initialise les temps à très grand
INF = 10**15
dp = [INF] * len(points)
dp[0] = 0  # temps pour arriver à 0 est 0

for i in range(len(points)):
    if i < len(points) - 1:
        # temps pour marcher jusqu'à la prochaine position
        dist = points[i+1] - points[i]
        if dp[i] + dist < dp[i+1]:
            dp[i+1] = dp[i] + dist
    # On regarde si on peut warper depuis cette position
    cur_pos = points[i]
    for P, D, T in warps:
        if P == cur_pos:
            dest = P + D
            if dest in pos_index:
                j = pos_index[dest]
                if dp[i] + T < dp[j]:
                    dp[j] = dp[i] + T

print(dp[pos_index[L]])