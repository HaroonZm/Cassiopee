import sys

def solve(data, w, h):
    """
    Calcule la mesure d'illumination visible d'une carte hexagonale représentée par une grille.

    Chaque cellule de la grille peut être occupée (valeur 1) ou vide (valeur 0). Le calcul différencie
    les zones de vide accessibles depuis l'extérieur (zones visibles) des zones enfermées par des cellules occupées
    (zones invisibles).

    Le principe est d'explorer tous les espaces vides pour déterminer s'ils sont connectés à l'extérieur du champ,
    puis de compter, pour chaque cellule occupée, combien de ses côtés sont adjacents à une zone visible.

    Args:
        data (List[List[int]]): Grille 2D représentant la carte, avec 0 pour vide et 1 pour occupé.
        w (int): Largeur de la grille.
        h (int): Hauteur de la grille.

    Returns:
        int: Somme des côtés visibles (exposés) des cellules occupées.
    """
    invisible_area = set()  # Ensemble des coordonnées des zones vides enfermées
    visible_area = set()    # Ensemble des coordonnées des zones vides visibles depuis l'extérieur
    visited = set()         # Coordonnées visitées lors des explorations

    # Itérer sur toutes les positions de la grille
    for y in range(h):
        for x in range(w):
            visited.add((x, y))
            # Si la cellule est occupée, l'ajouter au groupe invisible (car non vide)
            if data[y][x] == 1:
                invisible_area.add((x, y))
            # Si la position est déjà dans une zone connue, on évite de la retraiter
            if (x, y) in invisible_area or (x, y) in visible_area:
                continue

            # Exploration par pile : on cherche à déterminer si la zone connectée au point (x, y) est visible depuis l'extérieur
            area = {(x, y)}  # Coordonnées appartenant à la zone explorée
            stack = [(x, y)]
            is_visible = False  # Indicatif si la zone touche l'extérieur (donc visible)

            while stack:
                cx, cy = stack.pop()
                visited.add((cx, cy))

                # Déplacement sur une grille hexagonale selon la parité de la ligne
                if cy % 2 == 0:
                    # Déplacements pour les lignes paires
                    dxy = ((cx, cy-1), (cx+1, cy-1), (cx-1, cy), (cx+1, cy), (cx, cy+1), (cx+1, cy+1))
                else:
                    # Déplacements pour les lignes impaires
                    dxy = ((cx-1, cy-1), (cx, cy-1), (cx-1, cy), (cx+1, cy), (cx-1, cy+1), (cx, cy+1))

                for nx, ny in dxy:
                    # Si un voisin est hors de la grille, la zone est en contact avec l'extérieur => visible
                    if not (0 <= nx < w) or not (0 <= ny < h):
                        is_visible = True
                    # Si voisin valide, vide et non visité, on l'ajoute à l'exploration
                    elif data[ny][nx] == 0 and (nx, ny) not in visited:
                        stack.append((nx, ny))
                        area.add((nx, ny))

            # Après exploration complète, on classe la zone comme visible ou invisible
            if is_visible:
                visible_area |= area
            else:
                invisible_area |= area

    # Calcul final : somme sur toutes les cellules occupées du nombre de côtés donnant sur une zone visible
    ans = 0
    for cy in range(h):
        for cx in range(w):
            if data[cy][cx] == 1:
                # Voisins selon la parité de la ligne (hexagone)
                if cy % 2 == 0:
                    dxy = ((cx, cy-1), (cx+1, cy-1), (cx-1, cy), (cx+1, cy), (cx, cy+1), (cx+1, cy+1))
                else:
                    dxy = ((cx-1, cy-1), (cx, cy-1), (cx-1, cy), (cx+1, cy), (cx-1, cy+1), (cx, cy+1))

                # Chaque cellule hexagonale possède 6 côtés; on compte combien sont adjacents à une zone invisible,
                # celles-ci ne contribuent pas à la surface visible
                adjacent_invisible = sum((nx, ny) in invisible_area for nx, ny in dxy)
                ans += 6 - adjacent_invisible

    return ans


def main(args):
    """
    Fonction principale d'entrée pour la lecture des données, le calcul et l'affichage du résultat.

    Le format d'entrée attendu est:
    - Une ligne avec deux entiers w et h séparés par un espace, correspondant à la largeur et la hauteur.
    - h lignes suivantes, chacune comportant w entiers 0 ou 1 décrivant la grille.

    Args:
        args (list): Arguments de la ligne de commande (non utilisés ici).

    Effectue:
        Affiche sur la sortie standard le résultat calculé.
    """
    w, h = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(h)]
    ans = solve(data, w, h)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])