from collections import deque  # Importation de deque depuis le module collections afin de créer une file efficace pour le parcours en largeur (BFS)

def main():
    # Boucle principale du programme, continue tant qu'une condition de terminaison n'est pas rencontrée
    while True:
        # Lecture de deux entiers séparés par des espaces depuis l'entrée standard puis conversion en entiers
        # W = largeur de la grille, H = hauteur de la grille
        W, H = map(int, input().split())

        # Vérifie si W vaut 0. Si c'est le cas, cela signifie qu'il faut arrêter la boucle et donc arrêter de lire de nouveaux cas
        if not W:
            break

        # Lecture des coordonnées de la "cible" (tx, ty) depuis l'entrée
        tx, ty = map(int, input().split())

        # Lecture des coordonnées du "chevalier" (kx, ky) depuis l'entrée
        kx, ky = map(int, input().split())

        # Création d'une grille (appelée ma) contenant (H+2) lignes et (W+2) colonnes, initialisée avec des valeurs False
        # Cela sert à doubler les bords pour faciliter les vérifications sans risque de sortir des limites
        ma = [[False] * (W + 2) for _ in range(H + 2)]

        # Remplissage de la grille interne (hors bordure) avec les valeurs lues à l'entrée
        for i in range(1, H + 1):  # Parcourt les lignes (1 à H inclus)
            # Lecture d'une ligne depuis l'entrée standard, division en valeurs et énumération
            for j, a in enumerate(input().split()):
                # 'a' est un caractère représentant l'état de la case (normalement "1" ou "0")
                # 1 => mur, 0 => vide ; on convertit en booléen : bool(1-int(a)) => True si c'est une case vide, False sinon
                ma[i][j + 1] = bool(1 - int(a))

        # Initialisation de la file pour l'exploration en largeur (BFS)
        # Chaque élément de la file est une liste contenant :
        # [position_x_cible, position_y_cible, position_x_chevalier, position_y_chevalier, nombre_de_mouvements]
        que = deque([[tx, ty, kx, ky, 0]])

        # Ensemble 'pas' contenant des tuples représentant les positions déjà explorées afin d'éviter les répétitions
        pas = set()

        # Initialisation de la variable de réponse à "NA" (signifiant pas de solution trouvée)
        ans = "NA"

        # Boucle principale du BFS : tant qu'il y a des éléments à explorer dans la file
        while que:
            # Enlève le premier élément de la file et le "dépaquette" dans les variables correspondantes
            tx, ty, kx, ky, c = que.popleft()

            # Vérifie si le nombre d'étapes dépasse 100 ; si oui, on arrête la recherche (limite pour éviter les boucles infinies)
            if c > 100:
                break

            # Si la position de la cible et du chevalier sont identiques, une solution a été trouvée
            if tx == kx and ty == ky:
                ans = c  # Le nombre de mouvements nécessaires pour atteindre cet état
                break  # Arrête la recherche puisque la solution est trouvée

            # Parcourt toutes les directions cardinales (haut, gauche, bas, droite)
            for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                # Calcul du déplacement potentiel de la cible
                # Si la case adjacente dans la direction (dx, dy) depuis (tx, ty) est libre (vrai dans ma), on déplace la cible dans cette direction
                # Sinon, on ne la déplace pas (tdx, tdy = 0, 0)
                if ma[ty + dy][tx + dx]:
                    tdx, tdy = dx, dy
                else:
                    tdx, tdy = 0, 0

                # Calcul du déplacement potentiel du chevalier, dans la direction opposée à celle du déplacement de la cible
                # Si la case correspondante dans la direction opposée est libre, on déplace le chevalier dans l'opposé du mouvement de la cible
                # Sinon, on ne le déplace pas (kdx, kdy = 0, 0)
                if ma[ky - dy][kx - dx]:
                    kdx, kdy = -dx, -dy
                else:
                    kdx, kdy = 0, 0

                # Vérifie si le nouvel état (positions de la cible et du chevalier après mouvement) a déjà été visité pour éviter les répétitions
                if (tx + tdx, ty + tdy, kx + kdx, ky + kdy) in pas:
                    continue  # Passe à la prochaine itération sans rien faire

                # Ajoute le nouvel état à la file d'exploration, en incrémentant le compteur de mouvements
                que.append([tx + tdx, ty + tdy, kx + kdx, ky + kdy, c + 1])

                # Garde une trace de cet état comme déjà visité
                pas.add((tx + tdx, ty + tdy, kx + kdx, ky + kdy))

        # Affiche le résultat, soit le nombre de mouvements trouvés pour atteindre le but, soit "NA" s'il n'existe pas de solution
        print(ans)

# Point d'entrée du programme principal. Vérifie si ce fichier est exécuté directement, et pas importé comme un module
if __name__ == "__main__":
    # Lignes commentées concernant le profiler de ligne
    # prf = LineProfiler()
    # prf.add_function(main)
    # prf.runcall(main)
    # prf.print_stats()
    main()  # Appel la fonction principale pour démarrer le programme