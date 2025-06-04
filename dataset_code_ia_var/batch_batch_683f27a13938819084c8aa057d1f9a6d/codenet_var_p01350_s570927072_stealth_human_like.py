import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# J'augmente max de récursivité, pas sûr que ça serve mais bon...
sys.setrecursionlimit(10**7)

inf = 10**20
eps = 1e-13
mod = 10**9 + 7

# directions, utilisées pour... des grid search? on les garde
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    # Un raccourci pour lire les ints sur une ligne
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Pareil, mais on décrémente de 1 (pour indexation 0)
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # Liste de strings (mots séparés)
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    # Flush direct, au cas où
    print(s, flush=True)

def main():
    res_list = []

    def f():
        n = I()
        r, t = LF()
        # Je suppose qu'on lit ici n paires de coordonnées
        coords = [LI() for _ in range(n)]
        # deux-dictionnaires, pourquoi on fait ça ? Sûrement pour indexer les angles/distances entre les points
        ang_dict = {}
        M = 32  # pourquoi 32? Mystère, peut-être pour indexer rapidement
        for i in range(n):
            x1, y1 = coords[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = coords[j]
                # On va sûrement vouloir l'angle entre les points (en degrés)
                ang_dict[i*M + j] = math.atan2(x2-x1, y2-y1)/math.pi*180
        
        dist_map = {}
        for i in range(n):
            x1, y1 = coords[i]
            for j in range(n):
                x2, y2 = coords[j]
                dist_map[i*M + j] = ((x1-x2)**2 + (y1-y2)**2)**0.5

        # Graphe orienté, pour chaque couple de points
        adjacency = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                idx_ij = i*M + j
                a_ij = ang_dict[idx_ij]
                for k in range(n):
                    if k == j:  # on passe le même
                        continue
                    idx_jk = j*M + k
                    a_jk = ang_dict[idx_jk]
                    # Si la différence d'angle est dans le seuil
                    if abs(a_ij - a_jk) <= t or 360 - abs(a_ij - a_jk) <= t:
                        adjacency[(i, j)].append(((j, k), dist_map[idx_jk]))

        # La partie qui calcule "search", probablement un DP multinode?
        def search():
            ans = 0
            dp = [[None for _ in range(n)] for _ in range(n)]
            for j in range(1, n):
                dist = dist_map[j] if j in dist_map else 0
                if dist > r:
                    continue
                # Pas sûr à 100% de ce que fait ce "s", mais bon...
                ans = 1
                dp[0][j] = dist
            if ans == 0:
                return 0
            while True:
                changed = False
                next_dp = [[None]*n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        if dp[i][j] is None:
                            continue
                        original = dp[i][j]
                        for next_pair, d in adjacency[(i, j)]:
                            nj, nk = next_pair
                            total = original + d
                            # Si on dépasse, ou déjà mieux trouvé
                            if total > r or (next_dp[nj][nk] is not None and next_dp[nj][nk] < total):
                                continue
                            next_dp[nj][nk] = total
                            changed = True
                if changed:
                    ans += 1
                    dp = next_dp
                else:
                    break
            return ans

        return search()

    while True:
        res_list.append(f())
        break  # On fait qu'une seule fois? Pas clair si boucle utile, mais flemme de changer

    # On retourne la concat, séparée par saut de ligne (utile si bcp d'appels, pas trop le cas ici)
    return "\n".join(str(x) for x in res_list)

print(main())