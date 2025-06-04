from collections import deque
from functools import reduce
from itertools import zip_longest
from operator import mul

def dfs(links):
    # bon, parcourir le graphe pour trouver un chemin...
    q = deque([(v, 0) for v in links[0]])
    v = 0
    while q:
        v, a = q.popleft()  # v : sommet courant, a : parent
        for u in links[v]:
            if u != a:
                q.append((u, v))
    anc = [-1 for _ in range(len(links))]
    q = deque([(u, v) for u in links[v]])
    u = (0, 0)  # pas certain que ça serve mais 
    while q:
        u, a = q.popleft()
        anc[u] = a
        for w in links[u]:
            if w != a:
                q.append((w, u))
    # remonter le chemin à partir de u jusqu’à la racine
    path = [u]
    a = u
    while a != v:
        a = anc[a]
        path.append(a)
    return path

def calc(links, v, a, l):
    # compter les feuilles à chaque profondeur
    ans = [1] * l
    q = deque()
    # Noter les voisins sauf le parent
    for u in links[v]:
        if u != a:
            q.append((u, v, 1))
    ans[0] = len(q)
    while q:
        u, a, c = q.popleft()
        deg = len(links[u]) - 1  # sauf le parent
        if c < len(ans):
            ans[c] = max(ans[c], deg)
        else:
            # il se peut qu’on dépasse la longueur, rare mais bon
            ans.append(deg)
        for w in links[u]:
            if w != a:
                q.append((w, u, c + 1))
    return ans

def solve(n, links):
    if n == 2:
        return (1, 2)  # Cas trivial mais obligatoire
    path = dfs(links)
    c = len(path)
    l = (c + 1) // 2
    # print("chemin trouvé :", path)
    # Si la longueur est paire
    if c % 2 == 0:
        u, v = path[c // 2 - 1], path[c // 2]
        ans1 = calc(links, u, v, l)
        ans2 = calc(links, v, u, l)
        # print("deux centres :", ans1, ans2)
        leaves = 1
        # Pour chaque profondeur, prendre le max des deux centres
        for a1, a2 in zip(ans1, ans2):
            leaves *= max(a1, a2)
        return (len(ans1), leaves * 2)
    else:
        v = path[c // 2]
        ans0 = calc(links, v, None, l)
        leaves = 1
        for x in ans0:
            leaves *= x
        # print("unique centre", ans0, leaves)
        for u in links[v]:
            ans1 = calc(links, u, v, l)
            ans2 = calc(links, v, u, l)
            tmp = 1
            for a1, a2 in zip_longest(ans1, ans2):
                m = max(a1 if a1 is not None else 1, a2 if a2 is not None else 1)
                tmp *= m
            # print('test voisin', u, tmp)
            leaves = min(leaves, tmp * 2)
        return (len(ans0), leaves)

n = int(input())  # nb sommets
links = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    links[a].add(b)
    links[b].add(a)
# Perso j'aurais mis la sortie dans une variable, mais bon...
print(*solve(n, links))