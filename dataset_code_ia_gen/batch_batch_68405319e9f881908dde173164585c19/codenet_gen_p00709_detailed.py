import sys
sys.setrecursionlimit(10**7)

def can_place_carpet(floor, x, y, size, W, H):
    """
    Vérifie si un carré de dimension 'size' peut être posé,
    avec le coin supérieur gauche en (x,y).
    Conditions :
    - Tous les panneaux dans ce carré doivent être rayés (1).
    - Le carré doit être entièrement contenu dans le plancher.
    """
    if x + size > W or y + size > H:
        return False
    for dy in range(size):
        for dx in range(size):
            if floor[y+dy][x+dx] == 0:  # panneau intact, ne peut pas couvrir
                return False
    return True

def place_carpet(floor, x, y, size, val):
    """
    Pose ou enlève un tapis de dimension 'size' en (x,y).
    Met la valeur 'val' sur tous les panneaux du tapis.
    val = 0 pour enlever le tapis (restaurer rayé),
    val = -1 pour marquer comme couvert (ou tout autre valeur négative).
    """
    for dy in range(size):
        for dx in range(size):
            floor[y+dy][x+dx] = val

def find_first_scratched(floor, W, H):
    """
    Trouve le premier panneau rayé (avec la valeur 1).
    Retourne les coordonnées (x,y), ou None si aucun panneau rayé n'est trouvé.
    """
    for y in range(H):
        for x in range(W):
            if floor[y][x] == 1:
                return x, y
    return None

def dfs(floor, W, H, carpets_used, best):
    """
    Recherche en profondeur avec backtracking pour trouver le nombre minimal de tapis.
    - floor : matrice modifiée en place, -1 = recouvert
    - carpets_used : nombre de tapis posés
    - best : la meilleure solution trouvée (int)
    Retourne la meilleure solution trouvée à partir de l'état actuel.
    """
    # Si on a déjà dépassé le meilleur score connu, on stoppe cette branche
    if carpets_used >= best[0]:
        return

    # Cherche premier panneau rayé à recouvrir
    pos = find_first_scratched(floor, W, H)
    if pos is None:
        # Tous recouverts
        best[0] = carpets_used
        return

    x, y = pos

    # On essaye toutes tailles possibles de tapis à ce point (descendant)
    max_size = min(W - x, H - y)
    for size in range(max_size, 0, -1):
        if can_place_carpet(floor, x, y, size, W, H):
            # Pose le tapis
            place_carpet(floor, x, y, size, -1)
            dfs(floor, W, H, carpets_used+1, best)
            # Retire le tapis (backtrack)
            place_carpet(floor, x, y, size, 1)

def main():
    while True:
        line = ''
        # Lire une ligne non vide
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return  # Fin fichier
        W, H = map(int, line.strip().split())
        if W == 0 and H == 0:
            break
        floor = []
        for _ in range(H):
            row = list(map(int, sys.stdin.readline().strip().split()))
            floor.append(row)

        # Recherche solution par backtracking DFS
        best = [W*H]  # meilleure solution (min tapis)
        dfs(floor, W, H, 0, best)
        print(best[0])

if __name__ == "__main__":
    main()