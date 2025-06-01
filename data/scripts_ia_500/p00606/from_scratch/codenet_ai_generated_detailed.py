# Solution complète en Python pour le problème "Cleaning Robot" de Dr. Asimov

# Le problème modélise un déplacement aléatoire d'un robot dans une maison de 9 pièces disposées en une grille 3x3 (lettres A à I).
# Le robot a une batterie avec n points, et il commence dans une pièce s.
# À chaque étape, tant qu'il reste de la batterie, il choisit au hasard une des 4 directions (nord, sud, est, ouest).
# Si la pièce dans cette direction existe et n'est pas la pièce "junk" b, le robot s'y déplace.
# Sinon, il reste dans sa pièce actuelle.
# À chaque étape (qu'il se déplace ou non), la batterie diminue de 1 point.
# Le robot s'arrête quand la batterie est épuisée (0 points).
# La question : Quelle est la probabilité que le robot s'arrête dans la pièce batterie t.

# Approche :
# - Modéliser la maison comme un graphe 3x3 avec pièces A à I.
# - Créer un tableau de transition des positions possibles selon la direction choisie et les contraintes junk/limites.
# - Utiliser une programmation dynamique avec mémorisation (cache) pour calculer la probabilité d'être dans chaque pièce
#   avec x points de batterie restants.
# - L'état est défini par (battery_left, current_room).
# - Au départ : probabilité 1 au (n, s).
# - À chaque étape :
#     La probabilité de chaque position avec batterie-1 est la somme pondérée (1/4) des probabilités des états pouvant y conduire.
# - Au final, la probabilité cherchée est la probabilité d'être en t au moment où battery = 0.

# Note: On peut également simuler à rebours : pour battery=0, prob=1 si position=t, 0 sinon,
#   puis aller vers battery=n en remontant, mais la méthode forward est la plus naturelle ici.

# Implementation de la méthode forward pour calculer probabilité.

# Détail des pièces en grille 3x3 :
# A B C
# D E F
# G H I

# Lettres en indices 0..8 pour simplifier.

# Code :

from sys import stdin

# Mapping letter -> index 0..8 et inverse
letter_to_index = {c: i for i, c in enumerate('ABCDEFGHI')}
index_to_letter = {i: c for c, i in letter_to_index.items()}

# Directions avec vecteurs (dx, dy)
directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1)
}

# Coordonnées de chaque pièce dans la grille 3x3
# Index i: (row, col)
pos_coord = {i: (i // 3, i % 3) for i in range(9)}

def next_room(current_idx, direction, junk_idx):
    """Retourne l'index de la pièce atteinte depuis current_idx en allant dans direction.
       Si mouvement impossible (hors grille ou pièce junk), retourne current_idx (pas de déplacement)."""
    r, c = pos_coord[current_idx]
    dr, dc = directions[direction]
    nr, nc = r + dr, c + dc
    # Vérifie bornes
    if 0 <= nr < 3 and 0 <= nc < 3:
        nidx = nr * 3 + nc
        if nidx == junk_idx:
            # Pièce junk, ne peut pas entrer
            return current_idx
        else:
            return nidx
    # Hors grille
    return current_idx

def solve(n, s, t, b):
    """
    Calcule la probabilité que le robot s'arrête dans la pièce batterie t,
    partant dans la pièce s avec n points de batterie,
    b est la pièce junk.
    """
    s_idx = letter_to_index[s]
    t_idx = letter_to_index[t]
    b_idx = letter_to_index[b]

    # dp[battery][room] = probabilité d'être dans "room" avec "battery" points avant déplacement
    # on démarre à batterie n au départ, à la position s_idx : prob=1
    # À chaque étape, on consomme 1 point de batterie pour un déplacement (ou tentative)
    # On arrête quand battery=0, alors on regarde dp[0][t_idx]

    # Comme on calcule en forward, dp dimension (n+1) x 9
    dp = [[0.0]*9 for _ in range(n+1)]
    dp[n][s_idx] = 1.0

    # Pour battery points de 0 (arrêt) on ne bouge plus — on calcule pour battery de n down to 1
    # car la batterie diminue à chaque étape
    for battery in range(n, 0, -1):
        for room in range(9):
            prob = dp[battery][room]
            if prob == 0.0:
                continue
            # Depuis "room" avec "battery" points, les 4 mouvements possibles
            for d in directions:
                nr = next_room(room, d, b_idx)
                # Diminution batterie de 1
                dp[battery-1][nr] += prob * 0.25

    # Après la dernière étape (battery=0), dp[0][r] est la probabilité d'être en r après épuisement
    # On retourne la probabilité d'être dans la pièce batterie t_idx à ce moment
    return dp[0][t_idx]

def main():
    while True:
        line = ''
        # Ignore lignes vides
        while line.strip() == '':
            line = stdin.readline()
            if not line:
                return
        n = int(line.strip())
        if n == 0:
            break
        line2 = stdin.readline().strip()
        s, t, b = line2.split()
        ans = solve(n, s, t, b)
        print(f"{ans:.8f}")

if __name__ == "__main__":
    main()