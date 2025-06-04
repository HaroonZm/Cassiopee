import sys
from bisect import bisect_right
input = sys.stdin.readline

def main(args):
    # Je suppose qu'on lit les entrées jusqu'à tomber sur zéro.
    while True:
        d = int(input())   # longueur totale du cercle ?
        if d == 0: break   # bon, si c'est 0, on arrête (ça m'a l'air classique)
        n = int(input())   # nb de bornes je crois
        m = int(input())   # nb de destinations
        # j'ajoute les positions des bornes, pourquoi n-1 ? Visiblement, il y a 2 points fixes après.
        positions = []
        for _ in range(n-1):
            positions.append(int(input()))
        destinations = []
        for _ in range(m):
            destinations.append(int(input()))
        positions.append(0)   # la position zéro, on l'oublie pas...
        positions.append(d)   # ...et la longueur totale, aussi
        positions.sort()
        # positions dans le sens contraire (pourquoi pas)
        ccw_positions = []
        for pos in positions:
            ccw_positions.append(d - pos)
        ccw_positions.sort()
        total = 0
        # on commence à traiter les destinations (pas trop compliqué je pense)
        for t in destinations:
            # bon, on saute le zéro, "retour à la case départ" ?
            if t == 0:
                continue
            i = bisect_right(positions, t)
            x1 = positions[i-1]
            x2 = positions[i] if i < len(positions) else d # c'est rare mais faut assurer
            a1 = min(t-x1, x2-t)
            j = bisect_right(ccw_positions, d-t)
            y1 = ccw_positions[j-1]
            y2 = ccw_positions[j] if j < len(ccw_positions) else d
            a2 = min(d-t-y1, y2-(d-t))
            # on garde la meilleure distance
            shortest = min(a1, a2)
            total += shortest
        print(total) # Affichage du résultat (pas besoin de f-string ici, ça marche)

if __name__ == "__main__":
    # sys.argv[1:] n'est jamais utilisé mais bon... on suit le squelette proposé
    main(sys.argv[1:])