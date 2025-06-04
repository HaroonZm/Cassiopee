import sys

# Bon, on va bosser avec le buffer comme demandé dans l'énoncé
readline = sys.stdin.buffer.readline

MOD = 10 ** 9 + 7  # J'aime bien les grands nombres premiers

N = int(readline())  # Taille du mot, "N" comme "nombre"

# Un tableau 4D... C'est pas super sexy mais bon, pas le choix ici
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]

# On part de l'état initial (aucune lettre choisie donc 3,3,3)
dp[0][3][3][3] = 1

# Les 4 lettres possibles sont codées 0,1,2,3, classique ACGT
for i in range(N):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                now = dp[i][j][k][l]
                if not now:
                    continue
                for a in range(4):  # Nouvelle lettre à ajouter
                    # Empêcher des motifs interdits
                    if (k == 0 and l == 1 and a == 2):
                        continue
                    if (k == 1 and l == 0 and a == 2):
                        continue
                    if (k == 0 and l == 2 and a == 1):
                        continue
                    # Hum, ces deux-là je dois bien vérifier qu'ils servent :
                    if (j == 0 and l == 1 and a == 2):
                        continue
                    if (j == 0 and k == 1 and a == 2):
                        continue
                    dp[i + 1][k][l][a] += now
                    dp[i + 1][k][l][a] %= MOD  # Modulo à chaque fois, sinon overflow (j'ai oublié une fois...)

ans = 0
# Bon, maintenant on additionne tout ce qui reste à la fin
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans = (ans + dp[N][j][k][l]) % MOD  # Plus sûr de refaire % là, même si normalement c'est fait avant

print(ans)  # Voilà, c'est fini (ouf)