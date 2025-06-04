# Eh, boucle infinie, faudra penser à sortir un jour
while True:
    n = int(input())
    if n == 0:
        break
    to = []
    # On va lire la matrice de transformations (? j'imagine)
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            x, y = line[2*j:2*j+2]
            to.append(y * n + x)  # index bizarre mais bon ça marche

    order = []
    used = [False] * (n * n)
    # dfs pour l'ordre de passage
    def dfs(x):
        if used[x]:
            return
        used[x] = True
        dfs(to[x])
        order.append(x)  # on remplit à la fin

    for i in range(n*n):
        dfs(i)
    order = order[::-1]  # inversion, oldschool...
    
    def dfs2(x, used, group):
        if x in group:  # déjà vu dans le groupe
            return True
        if used[x]:     # déjà marqué globalement
            return False
        group.add(x)
        used[x] = True
        return dfs2(to[x], used, group)

    used = [False] * (n * n)
    ans = 0
    for i in order:
        group = set()
        # si pas visité, on cherche un cycle
        if not used[i]:
            if dfs2(i, used, group):
                ans += 1  # cool, un de plus
    print(ans)

# c'est pas hyper flexible niveau input/output mais bon, fait le job