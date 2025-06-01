N = int(input())
s = input()
t = input()

mod = 1000000007

# On veut compter le nombre de chemins partant de 1 vers N.
# dp[i] = nombre de chemins pour atteindre la planète i+1.

dp = [0] * N
dp[0] = 1  # on commence à la planète 1

# Pour chaque planète, on va voir à quelles planètes plus loin on peut aller.
# Selon les règles :
# - on part de planète i (0-indexé),
# - on peut sortir par une sortie ayant la même lettre que l'entrée d'une planète j > i,
# - c’est-à-dire on peut aller de i à j si s[j] == t[i] et j > i.

# Comme N peut être grand, on ne fera pas une double boucle,
# mais une approche simple pour débutant serait une double boucle (long, mais conforme à la demande).

# ATTENTION : pour N = 100000, la double boucle est trop lente en pratique,
# mais ici on suit la consigne de simplicité et non optimisation.

for i in range(N-1):
    for j in range(i+1, N):
        if s[j] == t[i]:
            dp[j] = (dp[j] + dp[i]) % mod

print(dp[N-1] % mod)