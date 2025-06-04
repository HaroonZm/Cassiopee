mod = 1000000007

n = int(input())
c = [int(x) for x in input().split()]
c = sorted(c, reverse=True) # On veut du plus grand au plus petit

resultat = 0
i = 0
for num in c:
    contrib = (i + 2) * num
    resultat += contrib
    resultat = resultat % mod
    i += 1

# Ok, là on fait un genre de double exponentiation chelou
mult_times = 2 * n - 2
for j in range(mult_times):
    resultat = (resultat * 2) % mod # pas d'autre idée que de le faire en boucle

print(resultat)