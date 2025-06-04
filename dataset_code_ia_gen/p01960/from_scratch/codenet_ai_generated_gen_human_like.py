import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# Pour chaque sommet, on calcule le nombre d'arêtes dans la composante médiane si on coupe cette arête.
# On réalise un DP sur l'arbre où dp[u] est la taille du sous-arbre de u.
# L'idée est de supposer que le chemin P est une simple arête (u,v), on coupe cette arête et on regarde les composantes.
# Pour le problème, il faut choisir deux sommets u,v distincts et retirer le chemin entre ces deux.
# En réalité, retirer le chemin P entre u et v supprime une chaîne d'arêtes.
# Pour simplifier, on va utiliser une approche avec un parcours DFS où on calcule, pour chaque arête, les composants générés si elle est coupée.
# Puis on cherche le chemin P qui maximise la somme des composantes de taille >= K dans la forêt résultante.

# Cette approche est complexe pour N=1e5. On va adopter une solution avec la suppression d'une arête sur le chemin qui maximise le nombre de composantes grandes.
# La suppression d'un chemin P est équivalente à la suppression de l'union des sommets de P.
# Puisque on veut maximiser le nombre de composantes de taille >= K après suppression, on peut, pour chaque sommet, compter le nombre de composantes dépassant K si on supprime uniquement ce sommet,
# ensuite étendre à un chemin (on limite à la suppression d'un chemin), et on va tenter de trouver la meilleure suppression de chemin.

# Une solution efficace est de considérer l'arbre et ses centres. En effet, retirer un chemin du centre coupe l'arbre efficacement.
# Or centrer l'arbre nous permet d'évaluer rapidement.

# Implantation :
# - Calculer la taille du sous-arbre pour chaque sommet.
# - Pour chaque sommet, faire DFS et recueillir les tailles des sous-arbres enfants.
# - L'idée est de choisir un chemin qui va couper le plus de grandes composantes.

# Cependant, le problème est complexe, une solution efficace pour ce problème est de calculer le nombre maximal de composants de taille >= K obtenus
# en supprimant un chemin quelconque.
# Une approach est de réaliser une DP en double DFS pour trouver la meilleure combinaison.

# Ici on va faire une solution basée sur la suppression d'une arête qui maximise la somme des composantes de taille >= K.

# Calculer la taille de chaque sous-arbre
subtree_size = [0]*N
def dfs_size(u, p):
    s = 1
    for w in graph[u]:
        if w == p:
            continue
        s += dfs_size(w, u)
    subtree_size[u] = s
    return s
dfs_size(0, -1)

# Pour chaque arête (u,v), on calcule la taille des deux parties si on la supprime :
# partie_v = taille sous-arbre de v dans u->v
# partie_u = N - partie_v
# On compte combien de ces deux parties ont la taille >= K

# On cherche la valeur max sur toute les arêtes, en plus on peut retirer un chemin qui n'est pas forcément une arête,
# mais en retirant une seule arête on a au moins une idée.

# Ensuite on peut essayer d'élargir au cas où le chemin P est plus grand, mais ici on va faire le maximum local sur les arêtes.

ans = 0
for u in range(N):
    for v in graph[u]:
        if v < u:
            continue
        # Supposons que v est un enfant de u (on s'assure en faisant dfs)
        # On utilise dfs_size avec un parent défini
        # Il faut savoir qui est plus haut dans l'arbre
        # Pour ça, on fait d'abord un dfs pour obtenir parents et depths
parents = [-1]*N
depth = [0]*N
def dfs_parents(u, p):
    for w in graph[u]:
        if w == p:
            continue
        parents[w] = u
        depth[w] = depth[u] + 1
        dfs_parents(w, u)
dfs_parents(0, -1)

ans = 0
for u in range(N):
    for v in graph[u]:
        if u < v:
            # On veut que u soit le parent de v
            if parents[v] == u:
                part_v = subtree_size[v]
                part_u = N - part_v
            elif parents[u] == v:
                part_u = subtree_size[u]
                part_v = N - part_u
            else:
                continue
            cnt = 0
            if part_u >= K:
                cnt += 1
            if part_v >= K:
                cnt += 1
            if cnt > ans:
                ans = cnt

# Maintenant on peut tenter d'améliorer :
# En supprimant un chemin plus long, on peut produire plus de composantes.
# Par exemple, si on enleve un chemin qui traverse plusieurs arêtes, cela peut déconnecter plusieurs sous-arbres.

# Nous allons donc faire un second DFS pour calculer pour chaque sommet la somme max des composantes >= K en enlevant un chemin débutant ou terminant dans ce sommet.

# Pour cela, on va calculer, pour chaque arete, la contribution des sous-arbres enfants.

# Pour simplifier, on peut considérer que le chemin P est une chaîne simple,
# et on sélectionne une chaîne P qui maximise la somme des composantes sur tous les sous-arbres disconnectés.

# On effectue un DP bidirectionnel sur l'arbre (comme sur un arbre pour les chemins maximaux).

dp_down = [0]*N  # max nombre de composants >= K dans sous-arbre en coupant un chemin commençant dans ce sous-arbre
def dfs_down(u, p):
    res = 0
    for w in graph[u]:
        if w == p:
            continue
        dfs_down(w, u)
        # Taille du sous-arbre w
        sz = subtree_size[w]
        # Si on coupe le chemin qui commence ici et descend vers w
        # On peut avoir des composantes dans w (dp_down[w]) et si la partie w est assez grande il compte aussi
        val = dp_down[w]
        # Ici on ne coupe pas encore quoi que ce soit, donc on garde la valeur
        res += val
    dp_down[u] = 0
    # On compte combien de sous-arbres enfants ont une taille >= K
    count_large = sum(1 for w in graph[u] if w != p and subtree_size[w] >= K)
    # Si la composante restante (enlevant les sous-arbres enfants) est assez grande on peut l'ajouter
    rest = N - subtree_size[u] if p != -1 else 0
    if rest >= K:
        count_large += 1
    dp_down[u] = max(count_large, res)
dfs_down(0, -1)

# Maintenant dfs_up pour propager à partir du parent
dp_up = [0]*N
def dfs_up(u, p):
    # On récupère les tailles des sous-arbres enfants
    child_subtree_sizes = []
    childs = []
    for w in graph[u]:
        if w == p:
            continue
        child_subtree_sizes.append(subtree_size[w])
        childs.append(w)

    prefix = [0]*(len(childs)+1)
    suffix = [0]*(len(childs)+1)
    # On construit prefix et suffix des dp_down pour accélérer le calcul
    for i in range(len(childs)):
        prefix[i+1] = prefix[i] + (1 if subtree_size[childs[i]] >= K else 0)
    for i in range(len(childs)-1, -1, -1):
        suffix[i] = suffix[i+1] + (1 if subtree_size[childs[i]] >= K else 0)

    for i, w in enumerate(childs):
        # Nombre de sous-arbres enfants autres que w de taille >= K:
        cnt_others = prefix[i] + suffix[i+1]
        # Taille de la composante complementaire (en dehors de u et ses sous-arbres):
        rem = N - subtree_size[w]
        if rem >= K:
            cnt_others += 1
        # dp_up[w] est max entre:
        #   - dp_up[u] (composantes au dessus)
        #   - cnt_others
        dp_up[w] = max(dp_up[u], cnt_others)
        dfs_up(w, u)
dfs_up(0, -1)

# Maintenant on combine dp_down et dp_up:
# Pour chaque sommet u, on peut considérer un chemin P allant jusqu'à u
# Le nombre total de composantes >= K après suppression du chemin P est dp_up[u] + somme des dp_down des sous-arbres non sur le chemin

# En fait, il faut trouver sur le chemin P la meilleure valeur.
# On essaye toutes les arrêtes, ou tous les sommets comme sommet sur le chemin.

answer = 0
for u in range(N):
    # Les composantes de dp_down[u] et dp_up[u] combinées font une estimation grossière
    val = dp_down[u] + dp_up[u]
    if val > answer:
        answer = val

print(answer)