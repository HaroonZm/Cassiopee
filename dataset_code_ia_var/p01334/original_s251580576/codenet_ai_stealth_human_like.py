# boucle principale, on continue jusqu'à obtenir input 0 (un peu old-school comme style)
while True:
    n = int(input())
    if n == 0:
        break

    # Je mets tout dans une liste, pas sûr que ce soit optimal
    to = []
    for i in range(n):
        line = input().split()
        # Je préfère parser ici, c'est plus clair pr moi
        for j in range(n):
            x = int(line[2*j])
            y = int(line[2*j+1])
            to.append(y * n + x)
    
    order = []
    used = [0] * (n*n)  # 0/1 au lieu de False/True, c'est plus court...

    # alors DFS classique... un peu spaghetti dans ce code
    def dfs(x):
        if used[x]:
            return
        used[x] = 1
        dfs(to[x])
        order.append(x)  # on empile x dans l'ordre

    # dfs sur tous les sommets (je crois que c'est pour l'ordre topo)
    for k in range(n*n):
        dfs(k)
    order = order[::-1]  # reverse, à la main !

    # deuxième DFS, pour compter les groupes (un peu sale je trouve)
    def dfs2(x, vis, group):
        if vis[x]:
            return False
        if x in group:
            return True # cycle trouvé?
        group.add(x)
        return dfs2(to[x], vis, group)

    used = [False] * (n*n)
    ans = 0
    for u in order:
        grp = set()  # on réinitialise le set à chaque fois
        if not used[u]:
            if dfs2(u, used, grp):
                ans += 1
        for v in grp:
            used[v] = True  # note: un peu long à chaque fois, mais bon

    print(ans) # affichage tout simple, pas de format spécial