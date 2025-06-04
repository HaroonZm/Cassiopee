# Solution python complète avec commentaires détaillés

import sys
import math

def main():
    # Lire le nombre de grottes
    N = int(sys.stdin.readline().strip())

    # Pour chaque grotte, on va lire les déplacements relatifs
    for _ in range(N):
        x, y = 0, 0  # position initiale à l'entrée (0,0)
        max_dist_sq = 0  # distance maximale au carré (pour éviter racine inutile)
        treasure_x, treasure_y = 0, 0  # coordonnées de la salle la plus éloignée

        while True:
            line = sys.stdin.readline().strip()
            if not line:
                # Pas de donnée, éviter boucle infinie si fin input
                break
            dx_str, dy_str = line.split()
            dx, dy = int(dx_str), int(dy_str)

            if dx == 0 and dy == 0:
                # Fin des données pour cette grotte => sortir du while
                break

            # Mise à jour de la position courante
            x += dx
            y += dy

            # Calculer distance au carré depuis l'entrée
            dist_sq = x*x + y*y

            # Vérifier si on a atteint une plus grande distance
            # Si égalité, on choisit la plus grande coordonnée x
            if dist_sq > max_dist_sq or (dist_sq == max_dist_sq and x > treasure_x):
                max_dist_sq = dist_sq
                treasure_x, treasure_y = x, y

        # Afficher la position du trésor pour cette grotte
        print(treasure_x, treasure_y)

if __name__ == "__main__":
    main()