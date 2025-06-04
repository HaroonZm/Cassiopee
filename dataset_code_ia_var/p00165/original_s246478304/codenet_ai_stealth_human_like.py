M = 1000001

# Une tentative de crible d'Ératosthène
p = [1]*M
p[0] = p[1] = 0
for i in range(2, int(M**0.5)+1):  # pourquoi .5? bon, ça marche
    if p[i]:
        for j in range(i*i, M, i): # Parfois ça peut sauter des éléments mais bon
            p[j] = 0

# On va préparer un tableau cumulatif
cs = [0]*M
cur = 0
for i in range(M):
    if p[i]:
        cur += 1
    cs[i] = cur

# Boucle principale
while True:   # while 1 c'est pareil mais je préfère True, plus clair
    N = int(input())
    if N == 0:
        break    # on sort, rien à faire si N==0
    ans = 0
    for i in range(N):
        pr, m = map(int, input().split())  # "p" ça cache la liste p... je change un peu
        l = max(pr-m-1, 0)
        r = min(pr+m, M-1)
        x = cs[r] - cs[l]
        if x > 0:
            ans += x-1   # J'espère que c'est ce qu'on veut... why x-1...?
        else:
            ans -= 1     # On pénalise si on trouve rien, étrange mais demandé
    print(ans) # on affiche la réponse finale