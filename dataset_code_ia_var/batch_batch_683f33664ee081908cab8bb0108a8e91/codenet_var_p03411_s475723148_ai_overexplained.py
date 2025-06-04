# Demande à l'utilisateur d'entrer une valeur au clavier. La fonction input() récupère cette saisie sous forme de chaîne de caractères.
# int() convertit cette chaîne de caractères en un entier, qui est affecté à la variable n.
n = int(input())

# Crée une liste vide ab qui va stocker n tuples d'entiers.
# La compréhension de liste [ ... for _ in range(n)] va exécuter l'instruction n fois.
# input() lit une ligne de texte pour chaque itération, qui est ensuite découpée en morceaux à l'aide de split().
# map(int, ...) convertit chaque élément de cette liste en entier. tuple(...) transforme la liste d'entiers en tuple.
ab = [tuple(map(int, input().split())) for _ in range(n)]

# Même principe que pour ab mais pour une autre liste, cd. Chaque tuple est aussi obtenu à partir de l'entrée utilisateur.
cd = [tuple(map(int, input().split())) for _ in range(n)]

# Prépare un dictionnaire gr représentant un graphe.
# Les clés sont les entiers de 0 à 2*n - 1 (inclus), chaque valeur associée est une liste vide.
# Cela crée 2*n sommets pour le graphe, dont les n premiers correspondent aux éléments de ab, les n suivants à ceux de cd.
gr = {i:[] for i in range(2 * n)}

# Pour chaque élément de ab (indexé par i), on va parcourir tous les éléments de cd (indexé par j)
for i in range(n):
    # Décompacte le tuple ab[i] en deux entiers ai et bi
    ai, bi = ab[i]
    for j in range(n):
        # Décompacte le tuple cd[j] en deux entiers cj et dj
        cj, dj = cd[j]
        # Si ai < cj ET bi < dj, alors on considère que ab[i] peut être couplé à cd[j]
        if ai < cj and bi < dj:
            # Ajoute n + j (l'indice du sommet cd correspondant) dans la liste d'adjacence du sommet ab correspondant (i)
            gr[i].append(n + j)
            # Ajoute i dans la liste d'adjacence du sommet cd correspondant (n + j). Cela permet de rendre le graphe non orienté.
            gr[n + j].append(i)

# Initialise le compteur de réponses à 0. C'est le nombre de paires maximales qui peuvent être faites.
ans = 0

# Trie la liste ab par ordre décroissant, puis inverse l'ordre avec reversed() pour avoir l'ordre croissant, et la transforme en liste.
ab = list(reversed(sorted(ab)))

# Trie la liste cd par ordre croissant. sorted() retourne une nouvelle liste triée.
cd = list(sorted(cd))

# Crée une liste booléenne "used" de longueur 2*n, initialisée à "False" partout.
# "used[i]" indiquera si le sommet i a déjà été visité lors de la recherche de couplage.
used = [False for _ in range(2 * n)]

# Crée une liste "match" de longueur 2*n, initialisée à -1 partout.
# "match[v]" indique l'indice du sommet auquel "v" est actuellement apparié, ou -1 s'il n'est couplé à aucun sommet.
match = [-1 for _ in range(2 * n)]

# Définit une fonction récursive pour chercher un couplage parfait en profondeur (DFS - Depth First Search).
def dfs(v):
    # Utilise les variables globales "used", "n", "gr", "match" dans la fonction.
    global used, n, gr, match
    # Marque le sommet v comme visité (True) pour éviter de revisiter ce sommet dans la recherche courante.
    used[v] = True
    # Parcourt toutes les cases adjacentes au sommet v dans le graphe gr.
    for u in gr[v]:
        # w désigne le sommet auquel u est déjà apparié (s'il l'est), ou -1 sinon (donc non apparié)
        w = match[u]
        # Si w est négatif (c’est-à-dire u n’est couplé à personne)
        # OU bien (w n’a pas encore été visité ET il est possible de trouver un couplage pour w en continuant la recherche dfs(w))
        if w < 0 or (not used[w] and dfs(w)):
            # Apparie v avec u : match[v] pointe sur u, et match[u] sur v
            match[v] = u
            match[u] = v
            # Signale qu'un couplage a été trouvé en retournant True
            return True
    # Aucun couplage n'a pu être fait depuis ce sommet v
    return False

# Tente d'apparier chaque sommet (de 0 à 2*n - 1 inclus) tant qu'il n'est pas déjà apparié à un autre sommet.
for v in range(2 * n):
    # Si le sommet v n'est pas déjà apparié (match[v] == -1)
    if match[v] < 0:
        # Remet tous les sommets comme "non visités" avant chaque recherche par DFS.
        used = [False for _ in range(2 * n)]
        # Si dfs(v) réussit à trouver un couplage pour v
        if dfs(v):
            # Incrémente le compteur d'appariements trouvés.
            ans += 1

# Affiche le nombre maximal de paires possibles selon la règle énoncée.
print(ans)