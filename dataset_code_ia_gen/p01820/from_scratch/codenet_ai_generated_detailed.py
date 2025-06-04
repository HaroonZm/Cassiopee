import sys
sys.setrecursionlimit(10**7)

# Nous avons n points de force, chacun avec une position (x, y) et un type indiquant la nouvelle direction
# imaginable ('>', 'v', '<', '^'). Le proton peut commencer n'importe où avec vitesse 1 et direction arbitraire.
# Chaque point de force ne peut être utilisé qu'une seule fois, et accélère le proton (Double vitesse et direction
# devient celle du point). On veut maximiser la vitesse finale, soit maximiser le nombre de points visités (chaque
# accélération double la vitesse donc vitesse finale = 2^(nombre de points visités)).

# Pour résoudre, on remarque que par construction, de la position d'un point de force, il faut pouvoir
# rejoindre un autre point de force suivant la direction imposée par ce point.
# On va construire un graphe dirigé où chaque noeud représente un point de force, et il existe un arc vers
# un point j si on peut aller de i à j avec la direction donnée par le point i.
# Le proton peut commencer n'importe où et n'importe quelle direction, donc en pratique on cherche la chaîne
# la plus longue dans ce graphe (chemin dirigé simple) en partant de n'importe quel point.

# La direction de mouvement est l'une des 4 canoniques : positive x ('>'), positive y ('v'),
# négative x ('<'), négative y ('^').
# Pour que le proton accède à un point j à partir d'un point i, il doit pouvoir aller tout droit depuis i
# vers j selon la direction actuelle.
# Cela signifie qu'un mouvement uniquement dans la direction définie par le point i,
# donc soit la même coordonnée sur l'axe orthogonal (ex: déplacement horizontal => y_i == y_j)
# et la position de j doit être strictement en avant dans la direction donnée (ex: '>': x_j > x_i).
# On relie donc i->j si j est sur la bonne ligne/colonne et dans la bonne direction.

# Algorithme:
# 1. Lire les points et leur direction
# 2. Pour chaque point i, déterminer tous les points j accessibles directement et faire graphe i->j
# 3. Trouver la longueur maximale de chemin simple dans ce graphe (pas de cycle possible ici car on avance toujours
#    dans une direction stricte => DAG)
# 4. La longueur du chemin plus 1 (car nombre de points visités inclut le départ) donne le nombre d'accélérations,
#    la sortie est donc cette longueur.

# Complexité O(n^2) car on compare chaque point à chaque autre pour constituer les arcs.
# n<=3000, cela reste acceptable.

# On stocke les trajets dans une liste d'adjacence.
# Puis on utilise une DP sur DAG pour obtenir la longueur max du chemin.

def main():
    n = int(sys.stdin.readline())
    points = []
    for _ in range(n):
        x, y, d = sys.stdin.readline().split()
        x, y = int(x), int(y)
        points.append((x, y, d))

    # Construire graphe
    # Pour chaque point i, on cherche j tels que:
    # - Selon la direction d_i:
    #   - '>': y_i == y_j and x_j > x_i
    #   - 'v': x_i == x_j and y_j > y_i
    #   - '<': y_i == y_j and x_j < x_i
    #   - '^': x_i == x_j and y_j < y_i
    graph = [[] for _ in range(n)]

    # Afin d'optimiser la recherche des arcs (éviter O(n^2) trop brut), on peut indexer les points selon x et y
    # mais contraintes très large (-1e9 à 1e9) donc tri et balayage suffisent ici.
    # On trie les points par coordonnées pour faciliter la recherche des candidats dans la bonne direction

    # On va procéder par direction pour ajouter arcs:

    # Pour '>' et '<' (mouvement horizontal), on regroupe par y, trions par x et ensuite on connecte uniquement vers la droite '>' ou gauche '<'
    from collections import defaultdict

    points_by_y = defaultdict(list)
    for i, (x, y, d) in enumerate(points):
        points_by_y[y].append((x, i, d))
    # trier chaque liste par x croissant
    for y in points_by_y:
        points_by_y[y].sort()

    # Pour '^' et 'v' (mouvement vertical), on groupe par x, trie par y
    points_by_x = defaultdict(list)
    for i, (x, y, d) in enumerate(points):
        points_by_x[x].append((y, i, d))
    for x in points_by_x:
        points_by_x[x].sort()

    # Pour chaque point i on ajoute successeurs suivant sa direction
    for i, (x, y, d) in enumerate(points):
        if d == '>':
            # chercher points à même y avec x_j > x_i
            arr = points_by_y[y]
            # trouver position de i dans arr
            # arr trié par x croissant, on peut binsearch pour x_i
            from bisect import bisect
            pos = bisect(arr, (x, i, d))
            # tous les points à partir de pos ont x_j > x_i
            for xx, j, dj in arr[pos:]:
                graph[i].append(j)
        elif d == '<':
            # même y, x_j < x_i
            arr = points_by_y[y]
            # arr trié croissant donc points avant x_i
            from bisect import bisect_left
            pos = bisect_left(arr, (x, i, d))
            # points avec index < pos ont x_j < x_i, on ajoute arcs vers eux
            for k in range(pos - 1, -1, -1):
                xx, j, dj = arr[k]
                graph[i].append(j)
        elif d == 'v':
            # même x, y_j > y_i
            arr = points_by_x[x]
            from bisect import bisect
            pos = bisect(arr, (y, i, d))
            for yy, j, dj in arr[pos:]:
                graph[i].append(j)
        else:  # d == '^'
            # même x, y_j < y_i
            arr = points_by_x[x]
            from bisect import bisect_left
            pos = bisect_left(arr, (y, i, d))
            for k in range(pos - 1, -1, -1):
                yy, j, dj = arr[k]
                graph[i].append(j)

    # DP pour trouver la plus longue chaîne dans le graphe
    # On fait un dfs avec mémorisation
    dp = [-1] * n

    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        max_len = 1  # on compte le point u lui-même
        for v in graph[u]:
            res = dfs(v) + 1
            if res > max_len:
                max_len = res
        dp[u] = max_len
        return max_len

    ans = 1
    for i in range(n):
        length = dfs(i)
        if length > ans:
            ans = length

    # la vitesse finale v_max = 2^ans donc on affiche ans
    print(ans)


if __name__ == "__main__":
    main()