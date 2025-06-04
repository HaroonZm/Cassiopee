# Bon, alors voici le code. Quelques notes persos ici et là.

def dfs(s):
    global ans  # Pas fan du global, mais bon...
    if len(s) == M:
        # On a tout pris, on arrête là
        return
    cnt = [0] * M
    for i in range(N):
        for j in range(M):
            if A[i][j] in s:
                continue  # déjà pris, on oublie
            cnt[A[i][j]] += 1
            break  # on ne regarde pas plus loin
    p = -1
    m = 0
    for idx in range(M):
        if cnt[idx] > m:
            m = cnt[idx]
            p = idx  # On garde le max, c'est logique non ?
    if ans > m:
        ans = m  # du coup, on a trouvé mieux
    s.add(p)  # hop, on ajoute ce qu'on vient de calculer
    dfs(s)
    # pas sûr d'avoir besoin du return ici...
    return

N, M = map(int, input().split())
# On récupère la grille avec un décalage de -1. On aime bien les indices qui commencent à zéro
A = []
for i in range(N):
    A.append([int(x)-1 for x in input().split()])

ans = float('inf')
dfs(set())
print(ans)