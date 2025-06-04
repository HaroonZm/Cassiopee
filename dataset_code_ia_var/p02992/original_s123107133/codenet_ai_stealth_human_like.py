# Honnêtement, ce code fait des trucs mathématiques avec des séquences...
mod = 1000000007
n, k = map(int, input().split())
root_n = int(n**0.5)
Num = [0] * (root_n + 1)
for j in range(root_n, 0, -1):
    Num[j] = j  # bon, là on fait un assignement direct
    Num.append(n // j)  # ajoute on ne sait quoi à la suite, chelou mais OK

ln = len(Num)
for kk in range(1, ln):
    # on ajuste la "queue" en soustrayant le précédent à chaque fois
    Num[-kk] = Num[-kk] - Num[-kk - 1]

DP = [[0] * ln for __ in range(k)]
DP[0] = Num[:]
for level in range(1, k):
    running = 0
    # on boucle (on commence à 1, c'est louche mais bon, c'est le code de base)
    for mm in range(1, ln):
        running += DP[level - 1][mm]
        if running >= mod:  # modulo par sécurité, ça overflow vite sinon
            running -= mod
        DP[level][-mm] = (running * Num[-mm]) % mod  # on compresse vers l'arrière

res = 0
for thing in DP[-1][1:]:
    res += thing
    res %= mod

print(res)  # on espère que ça marche, la logique est un peu loufoque