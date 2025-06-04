# Solution complète en Python pour le problème "Surface Area of Cubes".
# L'approche est la suivante :
# 1. On considère initialement un parallélépipède plein de dimensions A x B x C.
#    Sa surface totale est : 2*(A*B + B*C + C*A)
# 2. On retire N cubes donnés.
#    Pour chaque cube retiré, il faut enlever sa contribution à la surface :
#    - Enlever la contribution totale de ce cube s'il était présent (6 faces),
#    - Remettre la contributions des faces partagées avec des voisins qui deviennent désormais exposés du fait du retrait.
# 3. On utilise un set pour stocker les positions des cubes retirés pour un accès en O(1).
# 4. Pour chaque cube retiré, on vérifie ses 6 voisins adjacents.
#    - S'il y avait un cube à côté (non retiré), on enlève 2 faces (la face entre les 2 cubes était cachée,
#      le retrait du cube la rend visible du côté du cube voisin).
#    - S'il n'y avait pas de cube à côté (ou hors du volume), on enlève seulement 1 face (celle du cube retiré),
#      car avant le cube était là, maintenant il n'y est plus.
# 5. On calcule ainsi la surface finale.
# Cette approche est performante même si A, B, C sont très grands car on ne manipule que N cubes retirés, avec N max 1000.

import sys

def main():
    input = sys.stdin.readline

    # Lecture des dimensions et du nombre de cubes retirés
    A, B, C, N = map(int, input().split())

    # Ensemble des cubes retirés, pour accès rapide
    removed = set()
    for _ in range(N):
        x, y, z = map(int, input().split())
        removed.add((x, y, z))

    # Calcul de la surface totale initiale (parallélépipède plein)
    surface = 2 * (A*B + B*C + C*A)

    # Directions des voisins (6 faces adjacentes)
    directions = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

    # Pour chaque cube retiré, on va :
    # - enlever sa contribution complète (6 faces)
    # - puis ajouter les faces qui deviennent visibles sur les cubes voisins,
    #   et enlever celles cachées par les cube retirés.
    #
    # Attention : comme on enlève 6 faces par cube retiré, il faut réajuster en fonction des voisins
    #
    # Une meilleure approche est de considérer la surface de l'objet final = surface initial - contribution des cubes retirés + faces internes exposées

    # Calculons la contribution des cubes retirés à la surface (faces qui "manquent" car cubes retirés)
    # Chaque cube retiré enlève 6 faces, mais pour chaque voisin retiré aussi,
    # on enlève 2*number_of_adjacent_faces (car face cachée 2 fois)
    # Comme ces cubes sont manquants, leur faces ne comptent pas, donc on doit ajouter à la surface ces faces intérieures entre cubes retirés car elles deviennent des faces internes exposées?

    # En fait il est plus simple de raisonner :
    # Surface finale = somme des surfaces de tous les cubes présents
    # Initialement tous présents => surface = 2*(A*B + B*C + C*A)
    # On enlève N cubes => surface finale = surface initiale - 6*N + 2*(nombre de contacts entre cubes retirés)
    # (car les faces entre cubes retirés sont comptées en moins 2 fois dans les -6*N, il faut les rajouter une fois par face)
    #
    # Ensuite, il faut aussi prendre en compte que sur la surface globale, les cubes retirés font apparaître des faces nouvelles visibles sur des cubes restants voisins.
    # Or c’est inclus dans la formule, car on part de la surface initiale (total plein) et retire les 6 faces des cubes retirés.

    # Donc pour trouver les contacts entre cubes retirés, on va compter chaque paire de cubes retirés adjacents

    adjacent_pairs = 0

    for (x,y,z) in removed:
        for dx,dy,dz in directions:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < A and 0 <= ny < B and 0 <= nz < C:
                if (nx, ny, nz) in removed:
                    adjacent_pairs += 1

    # Chaque paire est comptée deux fois (cube1->cube2 et cube2->cube1)
    adjacent_pairs //= 2

    # Surface finale selon la formule :
    surface_final = surface - 6 * N + 2 * adjacent_pairs

    print(surface_final)

if __name__ == "__main__":
    main()