# Voilà, je vais un peu changer le style, ajouter quelques commentaires perso,
# et ne pas trop optimiser comme ferait quelqu'un d'humain un peu distrait.

while True:
    n = int(input())
    if n == 0:
        break

    to = []
    fr = []
    for _ in range(n * n):
        fr.append([])  # on remplit à la main, c'est ok

    # On lit les coordonnées
    for i in range(n):
        line = input().split()
        line = [int(x) for x in line] # je préfère comme ça
        for j in range(n):
            x = line[2 * j]
            y = line[2 * j + 1]
            to.append(y * n + x)
            fr[y * n + x].append(i * n + j)

    order = []
    used = [False for k in range(n * n)]

    # DFS, basique mais ça marche
    def dfs(x):
        if used[x]:
            # déjà fait, on saute
            return
        used[x] = True
        dfs(to[x])
        order.append(x)

    for idx in range(n * n):
        dfs(idx)

    def dfs2(node, used2, group):
        if used2[node]:
            return
        used2[node] = True
        for f in fr[node]:
            dfs2(f, used2, group)
        group.append(node)

    used2 = [False] * (n * n)
    ans = 0

    # On traite dans l'ordre inverse pour SCC
    for pos in order:
        group = []
        if not used2[pos]:
            dfs2(pos, used2, group)
        if len(group) > 0:
            # Je suppose qu’il faut compter tout de même, même les singletons
            ans = ans + 1

    print(ans)
    # c'est tout, pas besoin de plus je crois