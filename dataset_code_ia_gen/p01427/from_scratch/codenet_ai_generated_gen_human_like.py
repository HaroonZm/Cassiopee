import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
garden = [input() for _ in range(H)]

# Les roses forment une entité connectée par au moins un point commun (voisinage 8 directions)
# Chaque case rose est '#' sinon '.'
# La balle part du coin bas gauche (H-1,0) et lance une ligne
# Le but est de trouver la droite partant de ce point divisant la forme en un maximum de parties
# Une droite divise une entité en autant de parties que:
# (nombre de blocs de rose traversés par la droite) + 1

# On recherche donc une droite passant par (H-1, 0)
# Chaque droite peut être identifiée par son angle
# On peut calculer pour chaque bloc rose ses coordonnées par rapport au point (H-1,0)
# Chaque droite passant par ce point est identique dans sa pente = (dy/dx)

# Pour chaque bloc, on calcule la direction depuis (H-1,0) vers ce bloc (central)
# Puis on compte combien de blocs ont la même direction (même angle)
# Le maximum de blocs alignés donne le nombre de blocs traversés par la droite
# Le nombre de morceaux sera donc ce nombre + 1

from math import gcd

start_y, start_x = H-1, 0

directions = {}

for y in range(H):
    for x in range(W):
        if garden[y][x] == '#':
            dy = y - start_y
            dx = x - start_x
            # On veut normaliser (dy, dx) pour représenter la même direction pour tous les points alignés
            if dx == 0:
                dir_key = (1, 0)  # verticale montant (par convention)
            elif dy == 0:
                dir_key = (0, 1)  # horizontale droite
            else:
                g = gcd(dy, dx)
                ny = dy // g
                nx = dx // g
                # Pour avoir un unique représentant, on fait en sorte que nx soit toujours positif
                # ou si nx==0, ny>0
                if nx < 0:
                    ny = -ny
                    nx = -nx
                dir_key = (ny, nx)
            directions[dir_key] = directions.get(dir_key, 0) + 1

max_parts = max(directions.values()) + 1
print(max_parts)