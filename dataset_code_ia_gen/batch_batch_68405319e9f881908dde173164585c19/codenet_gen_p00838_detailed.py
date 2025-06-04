# Solution complète en Python pour le problème Colored Cubes

# Approche :
# 1. Comprendre la rotation des cubes :
#    Un cube a 6 faces avec des couleurs. Deux cubes sont identiques s'il existe une rotation qui aligne leurs couleurs.
#    On doit considérer toutes les rotations possibles du cube.
#
# 2. Notation des faces (numérotation donnée):
#    1: up
#    2: front
#    3: right
#    4: back
#    5: left
#    6: down
#
# 3. Définir toutes les transformations de rotation possible (24 orientations).
#    Pas de symétrie miroir ici, seulement rotations sont valides.
#
# 4. Pour chaque jeu de cubes, essayer de fixer la "forme finale" d'un cube en choisissant,
#    pour chaque cube, une orientation parmi les 24 possible.
#
#    Ensuite, on calcule le nombre de faces à repeindre pour uniformiser toutes les couleurs
#    dans cette configuration possible. La meilleure configuration minimise la somme.
#
# 5. Retourner le nombre minimum de faces à repeindre.

import sys

# On définit les 24 rotations possibles d'un cube.
# Chaque rotation est une permutation des indices des faces (1-based).
# L'index dans cette liste représente une orientation possible.
# On donne les permutations des indices des couleurs pour chaque rotation.
#
# Les indices des faces sont dans l'ordre: [U, F, R, B, L, D]
# Exemple: rotation[0]=[0,1,2,3,4,5] = identité (pas de rotation)
#
# Ces rotations sont standard et on peut les trouver par exemple dans des solutions antérieures ou via la méthode d'orientations classiques.

ROTATIONS = [
    [0,1,2,3,4,5],
    [0,2,4,1,3,5],
    [0,4,3,2,1,5],
    [0,3,1,4,2,5],
    [1,5,2,0,4,3],
    [1,2,5,4,0,3],
    [1,5,4,2,0,3],
    [1,4,0,5,2,3],
    [2,0,4,5,1,3],
    [2,4,5,1,0,3],
    [2,5,1,4,0,3],
    [2,1,0,5,4,3],
    [3,0,1,5,4,2],
    [3,1,5,4,0,2],
    [3,5,4,1,0,2],
    [3,4,0,5,1,2],
    [4,0,3,5,2,1],
    [4,3,5,2,0,1],
    [4,5,2,3,0,1],
    [4,2,0,5,3,1],
    [5,1,2,3,4,0],
    [5,2,4,1,3,0],
    [5,4,3,2,1,0],
    [5,3,1,4,2,0],
]

def get_all_orientations(cube):
    # Génère les 24 orientations possibles d'un cube à partir des ROTATIONS
    # cube est une liste de 6 couleurs dans l'ordre [U,F,R,B,L,D]
    orientations = []
    for rotation in ROTATIONS:
        oriented = [cube[i] for i in rotation]
        orientations.append(oriented)
    return orientations

def min_repaint_for_set(cubes):
    # cubes = liste de n cubes, chaque cube est liste de 6 couleurs
    # On veut trouver la config finale
    # Pour chaque cube, on essaie 24 orientations
    # On cherche la combinaison d'orientations qui minimise le nombre total de faces à repeindre
    
    n = len(cubes)
    
    # Pré-calculer toutes les orientations pour chaque cube
    all_orients = [get_all_orientations(cube) for cube in cubes]
    
    min_repaint = float('inf')
    
    # Pour trouver le minimum, on va tester toutes les combinaisons d'orientations
    # nombre de combinaisons = 24^n, avec n<=4 donc max 24^4=331776, raisonnable.
    
    from itertools import product
    for idx_combo in product(range(24), repeat=n):
        # Construire la liste des cubes dans leur orientation fixée
        oriented_cubes = [all_orients[i][idx_combo[i]] for i in range(n)]
        
        # On veut minimiser le nombre total de faces à repeindre pour que tous soient identiques.
        # Le cube final identique aura pour chacune des 6 faces une couleur apparue au moins une fois.
        # Le bon choix est de fixer la couleur finale d'une face à celle qui minimise la somme des changements.
        # Donc pour chaque face (0..5), on teste chacune des couleurs présentes sur cette face parmi les cubes.
        
        repaint_count = 0
        for face in range(6):
            # Compter la fréquence des couleurs sur cette face parmi cubes orientés
            color_count = {}
            for cube in oriented_cubes:
                c = cube[face]
                color_count[c] = color_count.get(c, 0) + 1
            
            # Choisir la couleur finale qui minimise le nombre de repeints sur cette face:
            # on choisit la couleur la plus fréquente pour cette face
            max_freq = max(color_count.values())
            # nombre à repeindre pour cette face = total cubes - max_freq
            repaint_count += (n - max_freq)
            
            # Si déjà dépasse min_repaint, on peut abandonner cette combinaison
            if repaint_count >= min_repaint:
                break
                
        if repaint_count < min_repaint:
            min_repaint = repaint_count
    
    return min_repaint

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n_line = input_lines[idx].strip()
        idx += 1
        if n_line == '0':
            break
        n = int(n_line)
        cubes = []
        for _ in range(n):
            colors = input_lines[idx].strip().split()
            idx += 1
            cubes.append(colors)
        result = min_repaint_for_set(cubes)
        print(result)

if __name__ == "__main__":
    main()