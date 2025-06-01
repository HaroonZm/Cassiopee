N = int(input())
times = [int(input()) for _ in range(N - 1)]

half = N // 2

# Nous devons choisir un ensemble de coupures dont la somme des longueurs est N/2,
# Chaque coupure correspond à une position i (1 ≤ i ≤ N-1), signifiant que le premier morceau se termine à i mm.
# Il faut que la somme des longueurs de morceaux pour chacun des deux personnes soit N/2.
# Si on choisit un ensemble de coupures pour la première personne à positions p1 < p2 < ... < pk, alors les longueurs des morceaux sont p1, p2-p1, ..., N - pk
# Nous pouvons utiliser une DP pour vérifier les sous-ensembles de coupures qui permettent de faire une longueur cumulative de half.

# On va créer un DP où dp[i][s] = la somme minimale des temps de coupure pour atteindre la longueur s avec les coupures considérées jusqu'à i
# positions.

# C'est un problème de somme partielle (subset sum) avec poids (temps), on veut trouver un sous-ensemble de coupures avec somme des longueurs = half, 
# et minimiser la somme des temps de ces coupures.

# La liste des positions des coupures est 1..N-1 (indexation 0..N-2 dans "times")

# On initialise dp avec None (inf)
dp = [None] * (half + 1)
dp[0] = 0  # 0 temps pour longueur 0

for i, t in enumerate(times, start=1):
    # on itère sur les positions de coupures i (1.. N-1)
    # on parcourt dp en sens inverse pour éviter de réutiliser la même coupure plusieurs fois
    for s in range(half, i - 1, -1):
        if dp[s - i] is not None:
            val = dp[s - i] + t
            if dp[s] is None or val < dp[s]:
                dp[s] = val

# dp[half] donne le minimum total pour couper en morceaux dont un fait la moitié (l'autre aussi par définition)
print(dp[half])