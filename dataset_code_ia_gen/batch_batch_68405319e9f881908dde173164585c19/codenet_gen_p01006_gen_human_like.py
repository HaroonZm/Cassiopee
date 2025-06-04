from sys import stdin

# Clavier en grille 3x3
keyboard = [
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
]

# Trouver la position du caractère c sur le clavier
def find_positions(c):
    positions = []
    for r in range(3):
        for col in range(3):
            if keyboard[r][col] == c:
                positions.append((r, col))
    return positions

# Vérifier si la séquence peut être tracée en une seule ligne selon les règles
def can_draw(sequence):
    n = len(sequence)
    if n == 1:
        return True  # un seul caractère est valide
    
    # Vérifier que deux caractères identiques ne soient pas consécutifs
    for i in range(n-1):
        if sequence[i] == sequence[i+1]:
            return False
    
    # Dictionnaire position de tous les caractères
    positions_map = {}
    for ch in set(sequence):
        positions_map[ch] = find_positions(ch)
        if not positions_map[ch]:
            return False  # caractère hors du clavier (devrait pas arriver)
    
    # Pour débuter, récupérer toutes les positions possibles du premier caractère
    possibilities = [(positions_map[sequence[0]][i], 0) for i in range(len(positions_map[sequence[0]]))]
    
    # Parcourir la sequence à partir du 2e caractère
    for i in range(1, n):
        ch = sequence[i]
        new_possibilities = []
        # Pour chaque position possible du caractère précédent
        for (pr, pc), idx in possibilities:
            # Pour chaque position possible du caractère courant
            for (nr, nc) in positions_map[ch]:
                # Il faut que (nr, nc) soit à 4 directions adjacentes (Haut, Bas, Gauche, Droite)
                if abs(nr - pr) + abs(nc - pc) == 1:
                    new_possibilities.append(((nr,nc), i))
        if not new_possibilities:
            return False
        possibilities = new_possibilities
    
    return True

# Lecture des 1000 chaînes
lines = [line.strip() for line in stdin.readlines()]
for line in lines:
    if can_draw(line):
        print(line)