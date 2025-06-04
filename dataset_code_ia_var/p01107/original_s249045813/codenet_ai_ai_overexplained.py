#!/usr/bin/env python3

# Importation du module 'copy' pour permettre de dupliquer des structures de données complexes
import copy

# Déclaration de la fonction rdp_connect qui va lire et traiter l'entrée de l'utilisateur
def rdp_connect() -> bool:
    # Spécifie que les variables n, m, et c sont globales pour être utilisées dans tout le programme
    global n, m, c
    # Lecture de la première entrée de l'utilisateur et conversion en deux entiers n et m
    n, m = map(int, input().split())
    # Vérifie si les deux valeurs sont nulles, indiquant la fin de l'entrée
    if n == m == 0:
        # Retourne False si c'est la fin des entrées
        return False
    # Lecture de la grille : pour chaque ligne, convertit la chaîne de caractères entrée en liste de caractères
    c = [list(input()) for _ in range(n)]
    # Retourne True pour indiquer que la lecture s'est bien déroulée
    return True

# Déclaration de la fonction qui vérifie la validité d'un parcours particulier dans la grille
def rdp_check() -> bool:
    # Définition de deux tuples DY et DX qui représentent les changements respectifs sur l'axe Y et l'axe X pour chaque direction :
    # (droite, bas, gauche, haut)
    DY = (0, 1,  0, -1)  # Changements pour la coordonnée y
    DX = (1, 0, -1,  0)  # Changements pour la coordonnée x

    # Définition d'une fonction imbriquée 'refresh' utilisée pour avancer et marquer un chemin à partir d'une direction et d'un point de départ vers un point d'arrivée
    def refresh(d: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # On précise encore une fois que c est une variable globale
        global c
        # Copie profonde de la grille c dans une nouvelle variable st pour éviter la modification simultanée de la grille principale
        st = copy.deepcopy(c)
        # Initialisation des coordonnées courantes avec celles de départ
        y, x = y1, x1
        # Déclaration d'un indicateur qui permet d'exécuter la boucle au moins une fois
        flag = True
        # On entre dans une boucle qui simule un déplacement dans la grille jusqu'à rencontrer une condition d'arrêt
        while flag or not ((y, x) == (y1, x1) or (y, x) == (y2, x2)):
            # Marquage de la case visitée avec un caractère '#' pour indiquer qu'elle fait partie du chemin
            st[y][x] = '#'
            # On examine toutes les directions possibles (4 au total)
            for _ in range(4):
                # Calcul des coordonnées du point en face ('forward') selon la direction courante
                fy, fx = y + DY[d], x + DX[d]
                # Calcul des coordonnées du point à gauche ('left') relativement à la direction courante
                ly, lx = y + DY[(d + 3) % 4], x + DX[(d + 3) % 4]
                # Vérifie si la case à gauche est un passage libre et dans les limites de la grille
                if 0 <= ly < n and 0 <= lx < m and c[ly][lx] == '.':
                    # Si oui, on se déplace à gauche
                    y, x = ly, lx
                    # On met à jour la direction : un décalage à gauche implique (d + 3) modulo 4
                    d = (d + 3) % 4
                    # On met flag à False pour signaler un déplacement réussi
                    flag = False
                    # On arrête d'examiner les autres directions
                    break
                # Sinon, vérifie si la case en face est libre et dans la grille
                elif 0 <= fy < n and 0 <= fx < m and c[fy][fx] == '.':
                    # Si oui, on avance dans la direction actuelle
                    y, x = fy, fx
                    # La direction ne change pas
                    flag = False
                    break
                # Si ni à gauche ni devant, on tourne à droite (d + 1) modulo 4 pour essayer une nouvelle direction
                d = (d + 1) % 4
            # Si après avoir examiné toutes les directions aucun mouvement n'est possible, on sort de la boucle avec échec
            if flag:
                # Retourne la direction courante et False pour indiquer que la destination n'a pas été atteinte
                return d, False
        # Remet la case de départ à '.' (non bloquée) puisque le chemin part même de là
        st[y1][x1] = '.'
        # Met à jour la grille principale pour prendre en compte le chemin tracé
        c = st
        # Retourne la direction actuelle et True si le point d'arrivée a bien été atteint, False sinon
        return d, (y, x) == (y2, x2)

    # Premier trajet : en partant du coin supérieur gauche (0,0), vers le coin supérieur droit (m-1,0), direction de départ est 0 (vers la droite)
    d, flag = refresh(0, 0, 0, m - 1, 0)
    # Si le trajet n'est pas possible on retourne immédiatement False
    if not flag:
        return False
    # Deuxième trajet : du coin supérieur droit vers le coin inférieur droit, en gardant la direction obtenue du trajet précédent
    d, flag = refresh(d, m - 1, 0, m - 1, n - 1)
    # Si pas possible, retourne False
    if not flag:
        return False
    # Troisième trajet : du coin inférieur droit vers le coin inférieur gauche
    d, flag = refresh(d, m - 1, n - 1, 0, n - 1)
    if not flag:
        return False
    # Quatrième et dernier trajet : du coin inférieur gauche vers le point de départ (coin supérieur gauche)
    return refresh(d, 0, n - 1, 0, 0)[1]

# Point d'entrée principal du programme : ce code ne s'exécute que si le script est lancé directement et non importé
if __name__ == '__main__':
    # Boucle infinie qui permet de traiter plusieurs grilles successivement tant que l'utilisateur fournit des données
    while rdp_connect():
        # Pour chaque grille, on vérifie si le chemin est possible avec rdp_check
        if rdp_check():
            # Affiche "YES" si un chemin correct a été trouvé
            print('YES')
        else:
            # Affiche "NO" si aucun chemin valide n'existe
            print('NO')