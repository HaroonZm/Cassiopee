import sys

# lecture d'entrée et récupération des valeurs
line = sys.stdin.readline()
A, B = map(int, line.split())

MOD = 10 ** 9 + 7

# pré-calcul des combinaisons (pas besoin de numpy ici)
U = 2001
comb = [[0] * U for _ in range(U)]
comb[0][0] = 1
for n in range(1, U):
    for k in range(n + 1):
        comb[n][k] = comb[n-1][k]
        if k > 0:
            comb[n][k] = (comb[n][k] + comb[n-1][k-1]) % MOD

# cumul des combinaisons le long de l'axe 1 (colonnes)
comb_cum = [[0]*U for _ in range(U)]
for n in range(U):
    s = 0
    for k in range(U):
        s = (s + comb[n][k]) % MOD
        comb_cum[n][k] = s

# calcul du tableau S
S = [[0]*U for _ in range(U)]
for k in range(U):
    if k == 0:
        for a in range(U):
            S[k][a] = 1
    else:
        s = 0
        for a in range(U):
            s = (s + comb_cum[k-1][a]) % MOD
            S[k][a] = s

# calcul de la réponse finale
x = 0
for k in range(A+1):
    s = 0
    for j in range(A - k + 1):
        s = (s + S[k][j]) % MOD
    val = (comb[B-1][k] * s) % MOD
    x = (x + val) % MOD

print(x)