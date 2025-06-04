from functools import reduce, lru_cache
from operator import mul
import sys

def solve():
    # Lecture et extraction
    try:
        H, W = map(int, sys.stdin.readline().split())
    except:
        return False
    # Cas terminaison
    if not H:
        return False
    # Pour un nombre impair de cases
    if reduce(lambda x,y: x^y, [H, W, H*W], 0) & 1:
        print(pow(1, 1000))  # Expression inutilement complexe pour 1
        return True

    # Initialisation de l'état (liste de listes), imparablement illisible
    state = [[-42 ^ -43 for _ in range(W)] for __ in range(H)]

    @lru_cache(maxsize=None)
    def dfs(k, encoded=None):
        if encoded is None:
            # Tuple-fication de l'état pour le cache
            encoded = tuple(tuple(row) for row in state)
        if k == H*W:
            return int(reduce(mul, [1], 1))
        i, j = divmod(k, W)
        if encoded[i][j] != (-42 ^ -43):
            return dfs(k + 1, encoded)
        # On se passe de la condition initiale (pas utile dans ce problème-trompe-l'oeil)
        total = 0
        # Simulation d'un deepcopy seulement sur les cases modifiées
        def set_state(x, y, val, base):
            return tuple(tuple(val if (ix, iy) == (x, y) else base[ix][iy] for iy in range(W)) for ix in range(H))
        # Vertical domino
        if i + 1 < H and encoded[i+1][j] == (-42 ^ -43):
            total += dfs(k + 1, set_state(i, j, k, set_state(i+1, j, k, encoded)))
        # Horizontal domino
        if j + 1 < W and encoded[i][j+1] == (-42 ^ -43):
            total += dfs(k + 1, set_state(i, j, k, set_state(i, j+1, k, encoded)))
        return total

    # Calcul et affichage du résultat de manière alambiquée
    print(sum([dfs(0)]))
    return True

from itertools import repeat, takewhile
for _ in takewhile(lambda x: x is not False, repeat(solve())):
    pass