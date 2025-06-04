#!/usr/bin/env python3

import copy

def rdp_connect() -> bool:
    """
    Lit les dimensions de la grille (n, m) depuis l'entrée standard et la grille elle-même.
    Met à jour les variables globales n, m et c.

    Returns:
        bool: False si l'entrée est '0 0' indiquant la fin des données, sinon True.
    """
    global n, m, c
    n, m = map(int, input().split())
    if n == m == 0:
        return False  # Condition de terminaison
    # Lecture de la grille de caractères
    c = [list(input()) for _ in range(n)]
    return True

def rdp_check() -> bool:
    """
    Vérifie si un chemin fermé (circuit) valide existe autour de la grille, commençant et finissant au même point,
    en parcourant le contour dans le sens des aiguilles d'une montre en évitant les obstacles ('#').
    Modifie la grille globale à chaque étape pour marquer le chemin suivi.

    Returns:
        bool: True si un tel chemin fermé est possible, sinon False.
    """

    # Déplacements de direction (Est, Sud, Ouest, Nord)
    DY = (0, 1,  0, -1)
    DX = (1, 0, -1,  0)

    def refresh(d: int, x1: int, y1: int, x2: int, y2: int) -> tuple:
        """
        Parcourt la grille depuis (x1, y1) jusqu'à (x2, y2) en suivant le contour
        dans une direction donnée et marque le chemin suivi. Utilise la "règle de la main droite"
        pour rester au bord du parcours.

        Args:
            d (int): La direction initiale (0=Est, 1=Sud, 2=Ouest, 3=Nord).
            x1 (int): Colonne de départ
            y1 (int): Ligne de départ
            x2 (int): Colonne d'arrivée
            y2 (int): Ligne d'arrivée

        Returns:
            tuple: (dernière direction utilisée, succès du trajet booléen)
        """
        global c
        # Création d'une copie profonde de la grille pour conserver l'état original pour la suite
        st = copy.deepcopy(c)

        # Position courante
        y, x = y1, x1
        flag = True  # Au premier tour de boucle, on force l'entrée
        while flag or not ((y, x) == (y1, x1) or (y, x) == (y2, x2)):
            # Marquer la position comme visitée
            st[y][x] = '#'
            for _ in range(4):
                # Calculer les positions à droite et en face
                fy, fx = y + DY[d], x + DX[d]
                ly, lx = y + DY[(d + 3) % 4], x + DX[(d + 3) % 4]
                # Essayer de tourner à droite si possible
                if 0 <= ly < n and 0 <= lx < m and c[ly][lx] == '.':
                    y, x = ly, lx
                    d = (d + 3) % 4  # Tourner à droite
                    flag = False
                    break
                # Sinon, aller tout droit si possible
                elif 0 <= fy < n and 0 <= fx < m and c[fy][fx] == '.':
                    y, x = fy, fx
                    flag = False
                    break
                # Sinon, pivoter vers la gauche
                d = (d + 1) % 4
            if flag:
                # Si aucun mouvement n'est possible, échouer
                return d, False
        # Démarquer le point de départ (pour ne pas contaminer la suite du parcours)
        st[y1][x1] = '.'
        # Mettre à jour l'état global de la grille
        c = st
        # Retourner la nouvelle direction et indicateur de succès (si on a bien atteint la bonne case)
        return d, (y, x) == (y2, x2)

    # Début du circuit : coin supérieur gauche vers coin supérieur droit
    d, flag = refresh(0, 0, 0, m - 1, 0)
    if not flag:
        return False
    # Coin supérieur droit vers coin inférieur droit
    d, flag = refresh(d, m - 1, 0, m - 1, n - 1)
    if not flag:
        return False
    # Coin inférieur droit vers coin inférieur gauche
    d, flag = refresh(d, m - 1, n - 1, 0, n - 1)
    if not flag:
        return False
    # Coin inférieur gauche vers coin supérieur gauche (point de départ)
    return refresh(d, 0, n - 1, 0, 0)[1]

if __name__ == '__main__':
    """
    Boucle principale : répète la lecture de grilles et la vérification du contour
    jusqu'à ce que '0 0' soit saisi en entrée, puis affiche 'YES' ou 'NO' selon la validité du contour.
    """
    while rdp_connect():
        if rdp_check():
            print('YES')
        else:
            print('NO')