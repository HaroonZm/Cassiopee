from collections import deque
import sys

def solve_puzzle(start):
    """
    Résout le 7 パズル en trouvant le nombre minimal de déplacements nécessaires
    pour atteindre l'état final [0,1,2,3,4,5,6,7] à partir d'un état initial donné.
    
    Approche :
    - On utilise une recherche en largeur (BFS) pour explorer tous les états possibles.
    - Chaque état est représenté par un tuple des 8 cartes.
    - On identifie la position de la carte '0' (seule carte déplaçable).
    - Les cartes sont placées sur un cadre 2x4 :
      indices des cartes :
      0 1 2 3
      4 5 6 7
    - À chaque étape, on génère les états voisins en échangeant '0' avec chaque carte adjacente (haut, bas, gauche, droite).
    - On utilise un set pour mémoriser les états déjà visités et éviter les répétitions.
    - On retourne la distance minimale (nombre de mouvements) pour atteindre l'état final.

    Paramètres :
    - start : tuple de 8 entiers représentant l’état initial.

    Retourne :
    - un entier représentant le nombre minimal de déplacements.
    """

    # état final cible
    target = (0,1,2,3,4,5,6,7)

    if start == target:
        return 0

    # positions possibles : 2 lignes x 4 colonnes
    rows, cols = 2, 4

    # directions de voisinage (haut, bas, gauche, droite)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # conversion position index -> (ligne, colonne)
    def to_pos(idx):
        return divmod(idx, cols)

    # conversion (ligne, colonne) -> index
    def to_idx(r,c):
        return r*cols + c

    visited = set()
    visited.add(start)

    queue = deque()
    queue.append( (start, 0) )  # (état, distance)

    while queue:
        state, dist = queue.popleft()
        zero_pos = state.index(0)
        r,c = to_pos(zero_pos)

        # explorer voisins échangeables
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor_idx = to_idx(nr,nc)
                # échanger 0 avec la carte à neighbor_idx
                new_state = list(state)
                new_state[zero_pos], new_state[neighbor_idx] = new_state[neighbor_idx], new_state[zero_pos]
                new_state_t = tuple(new_state)
                if new_state_t == target:
                    return dist + 1
                if new_state_t not in visited:
                    visited.add(new_state_t)
                    queue.append( (new_state_t, dist+1) )

    # comme l'énoncé garantit la possibilité d'atteindre target, ceci ne devrait jamais arriver
    return -1

if __name__ == "__main__":
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        start_state = tuple(map(int, line.split()))
        print(solve_puzzle(start_state))