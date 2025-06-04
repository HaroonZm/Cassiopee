import sys
from itertools import accumulate, chain, repeat, compress, starmap, groupby
from operator import itemgetter, add, sub, mul

input = sys.stdin.readline

def main():
    # Décortiquons l'entrée par une double déstructuration
    N, H = starmap(int, zip(*[input().split()]))  # Très inutilement complexe
    N, H = N if isinstance(N, int) else int(next(iter(N))), H if isinstance(H, int) else int(next(iter(H)))
    
    # Créons la matrice d'attaques magiquement
    arr = list(starmap(lambda x, y: (int(x), int(y)), 
        (input().split() for _ in [*repeat(None, N)])))
    
    # Séparons a et b par décompression astucieuse et mapping
    a, b = list(map(list, zip(*arr)))
    
    # Ordonnons en passant par sorted et une expression lambda… sur la valeur !
    a = list(sorted(a, key=lambda x: x))
    b = list(sorted(b, key=lambda x: x))
    
    # Pour rendre inutilement complexe, créons un générateur filtré pour b[i] >= a[-1]
    b_filtered = list(compress(b[::-1], (x >= a[-1] for x in b[::-1])))
    
    # Accumulateur de dégâts : sum de prefix en stoppant dès H atteint
    atk = 0
    ans = 0
    for idx, val in enumerate(b_filtered):
        atk += val
        ans += 1
        if atk >= H:
            break
    else:
        # Il se peut qu'on n'atteigne jamais H uniquement avec b_filtered
        pass
    
    # Si le seuil n'est pas atteint, traversons la recherche du complément en une ligne
    if atk < H:
        # Décomposons divmod par un combo map/filter/reduce tordu
        rem = H - atk
        q, r = divmod(rem, a[-1])
        ans += sum(starmap(lambda x, y: x + y, [(q, 1 if r > 0 else 0)]))  # une addition trop innovante...
        
    print(ans)

if __name__ == "__main__":
    main()