# Solution au problème "Origami, or the art of folding paper"
# L'idée générale est de modéliser la façon dont le papier est plié, 
# puis, pour chaque point de perforation, calculer combien de couches de papier 
# se superposent à cette position avant le pliage, afin de connaître 
# le nombre total de trous résultant du poinçonnage.
#
# Approche détaillée :
# 1. On part de la forme finale (après tous les pliages) et un point poinçonné.
# 2. On remonte les pliages dans l'ordre inverse pour retrouver tous les points 
#    correspondants dans la forme initiale non pliée.
# 3. Chaque pliage peut dupliquer la position dans le papier non plié 
#    (par symétrie autour de la ligne de pliure).
# 4. La taille du papier change avec chaque pliage, ce que nous suivons pour 
#    référencer les coordonnées.
# 5. Au final, pour chaque point poinçonné, on obtient le nombre de points dans
#    le papier initial qui correspondent à ce point plié, ce qui correspond au nombre
#    de trous.
#
# Contraintes :
# - Largeur et hauteur au départ ≤ 32
# - Nombre de pliages ≤ 20
# - Nombre de perforations ≤ 20
# Cela permet une recherche exhaustive/traversée sans problème de performance.

import sys

def main():
    # Lecture des jeux de données
    for line in sys.stdin:
        if line.strip() == '':
            continue
        n_m_t_p = line.strip().split()
        if len(n_m_t_p) < 4:
            # Lire la ligne suivante si incomplète
            n_m_t_p += sys.stdin.readline().strip().split()
        n, m, t, p = map(int, n_m_t_p)
        if n == 0 and m == 0 and t == 0 and p == 0:
            # Fin des données
            break

        folds = []
        for _ in range(t):
            d_i, c_i = map(int, sys.stdin.readline().split())
            folds.append((d_i, c_i))
        punches = []
        for _ in range(p):
            x_i, y_i = map(int, sys.stdin.readline().split())
            punches.append((x_i, y_i))

        # Taille du papier après les pliages successifs (initialement n x m)
        width = n
        height = m

        # Une fonction pour calculer, pour un point final (x, y),
        # la liste des points dans le papier à l'état initial non plié
        # correspondants à ce point, en remontant les pliages en sens inverse.
        def reverse_fold(x, y, index):
            # Si on a remonté tous les pliages, on retourne le point dans la forme initiale
            if index < 0:
                return [(x, y)]

            d_i, c_i = folds[index]
            points = []

            if d_i == 1:
                # Pliage vertical : plier la partie gauche sur la droite
                # Le papier avant pliage a une largeur plus grande que c_i
                # Le pliage est à c_i, la partie à gauche (x < c_i) est pliée vers droite.
                # Soit le papier avant pliage a largeur Wpre
                # Après pliage width = c_i
                # x varie de 0 à width-1

                # On calcule la largeur avant pliage
                Wpre = width + c_i
                # On remplace la largeur par Wpre pour la prochaine étape
                nonlocal width, height

                # Pour un point (x,y) dans papier après pliage :
                # Si x < c_i => point dans partie droite originale
                # - alors point avant pliage est (x + c_i, y)
                # Sinon
                # - point avant pliage est (c_i - (x - c_i) - 1, y) (point reflété gauche)

                if x < c_i:
                    # point dans droite intacte
                    points += reverse_fold(x + c_i, y, index -1)
                if x < c_i or x >=0:  # en fait x>=0 toujours vrai
                    # correspond aussi au double (si point dans plié)
                    # on doit considérer le reflet gauche seulement si x < c_i
                    reflect = c_i - (x - c_i) - 1  # attention au calcul de reflet
                    # calcule reflétée uniquement si reflet dans papier initial
                    if 0 <= reflect < Wpre:
                        points += reverse_fold(reflect, y, index -1)
            else:
                # Pliage horizontal : plier la partie basse sur la partie haute
                # Taille avant pliage : Hpre = height + c_i
                Hpre = height + c_i
                nonlocal width, height

                # On transforme height pour la prochaine étape remontée
                # Même raison que ci-dessus

                if y < c_i:
                    # point dans partie haute intacte
                    points += reverse_fold(x, y + c_i, index -1)
                if y < c_i or y >= 0:
                    reflect = c_i - (y - c_i) - 1
                    if 0 <= reflect < Hpre:
                        points += reverse_fold(x, reflect, index -1)

            return points

        # Cependant la fonction ci-dessus a un bug possible car on modifie width et height inside recursion: to avoid cette erreur, il faut gérer largeur et hauteur par un tableau mémoire externe.
        # Il est plus simple de mémoriser les tailles du papier après chaque pliage.

        # Calculer la taille du papier après chaque pliage en allant vers l'avant
        widths = [n]
        heights = [m]
        for d_i, c_i in folds:
            if d_i == 1:
                # pli vertical : width_after = c_i
                w_prev = widths[-1]
                h_prev = heights[-1]
                widths.append(c_i)
                heights.append(h_prev)
            else:
                # pli horizontal : height_after = c_i
                w_prev = widths[-1]
                h_prev = heights[-1]
                widths.append(w_prev)
                heights.append(c_i)

        # Maintenant refaire la fonction reverse_fold en passant aussi l'indice pour taille :
        # On descend dans folds de t à 0

        from functools import lru_cache

        sys.setrecursionlimit(10000)
        @lru_cache(maxsize=None)
        def reverse_fold(x, y, idx):
            # idx : indique le pliage courant auquel on doit revenir avant.
            # Si idx ==0 => aucun pliage, papier initial
            if idx == 0:
                return [(x,y)]
            d_i, c_i = folds[idx-1]
            Wpre = widths[idx-1]
            Hpre = heights[idx-1]
            points = []

            if d_i ==1:
                # pli vertical
                # papier avant pliage : largeur Wpre
                # pli à la distance c_i du bord gauche

                # x dans [0, widths[idx])
                # widths[idx] = c_i

                if x < c_i:
                    # côté droit stable
                    points += reverse_fold(x + c_i, y, idx -1)
                # côté gauche replié + miroir
                reflect = c_i - (x - c_i) -1
                if 0 <= reflect < Wpre:
                    points += reverse_fold(reflect, y, idx -1)

            else:
                # pli horizontal
                # hauteur avant pliage Hpre
                # pli à la distance c_i du bord inférieur

                if y < c_i:
                    points += reverse_fold(x, y + c_i, idx -1)
                reflect = c_i - (y - c_i) - 1
                if 0 <= reflect < Hpre:
                    points += reverse_fold(x, reflect, idx -1)

            return points

        # Pour chaque poinçonnage, on calcule le nombre de points dans papier initial associés
        for (x_p, y_p) in punches:
            pts = reverse_fold(x_p, y_p, t)
            # Le nombre de trous correspond au nombre de points trouvés
            print(len(pts))


if __name__ == "__main__":
    main()