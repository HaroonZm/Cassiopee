# Programme pour résoudre le problème "Patisserie ACM"
# L'objectif est de découper une forme bizarre d'une barre de chocolat en
# un nombre minimal de rectangles, en coupant uniquement le long des
# rainures (lignes et colonnes où il n'y a pas de chocolat).
#
# Approach:
# 1. Analyser la grille donnée, où '#' est un segment de chocolat,
#    '.' est un vide (rainure).
# 2. Trouver toutes les lignes horizontales où une coupe peut être faite.
#    Une ligne horizontale est coupable si, pour chaque colonne qui contient
#    du chocolat, la position correspondante dans cette ligne est aussi une rainure ('.').
# 3. Faire de même pour les colonnes verticales.
# 4. Après avoir trouvé les positions où on peut faire des coupes horizontales
#    et verticales on découpe la barre en rectangles formés par ces coupes.
# 5. Compter combien de telles rectangles contiennent du chocolat. C’est
#    le nombre minimal de pièces rectangulaires après découpe.

def main():
    while True:
        # Lire les dimensions h (hauteur) et w (largeur)
        h, w = map(int, input().split())
        if h == 0 and w == 0:
            break

        # Lire la grille du chocolat
        grid = [input() for _ in range(h)]

        # trouver les lignes horizontales où on peut couper
        # c'est-à-dire les indices i où toutes les colonnes de la ligne i sont '.' 
        # dans les colonnes où il y a du chocolat dans la barre.
        # On ne peut couper qu'entre les segments -> on teste les lignes entre i et i+1 (0-based)
        # Pour cela, on regarde la ligne i (lignes entre 1 et h-1 pour la coupe)

        # La coupe horizontale est possible entre la ligne i et i+1 si pour toute colonne j 
        # où il existe du chocolat dans la barre, grid[i][j] == '.'

        # mais il faut plutôt regarder la ligne i,
        # car on coupe *entre* deux lignes entières, donc on regarde la ligne i (0<=i<h-1)
        horizontal_cuts = [False] * (h-1)
        for i in range(h-1):
            possible = True
            for j in range(w):
                # Si dans cette colonne existe au moins un chocolat (on test plus bas)
                # Il faut que grid[i][j] == '.' pour que la coupe soit possible
                # En fait, on peut couper que s'il y a chocolat sur la colonne :
                # pour savoir ça, on peut pré-calculer la colonne s'il y a du chocolat
                pass # Calcul dans l'étape suivante

        # pour faciliter la recherche des colonnes contenant du chocolat, on crée un tableau
        chocolate_in_column = [False]*w
        for j in range(w):
            for i in range(h):
                if grid[i][j] == '#':
                    chocolate_in_column[j] = True
                    break

        # Déterminer les lignes horizontales où on peut couper
        for i in range(h-1):
            possible = True
            for j in range(w):
                if chocolate_in_column[j]:
                    if grid[i][j] != '.':
                        possible = False
                        break
            horizontal_cuts[i] = possible

        # De même pour les colonnes où on peut couper verticalement
        # On regarde la colonne j (0<=j<w-1) pour savoir si on peut couper entre j et j+1
        chocolate_in_row = [False]*h
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '#':
                    chocolate_in_row[i] = True
                    break

        vertical_cuts = [False] * (w-1)
        for j in range(w-1):
            possible = True
            for i in range(h):
                if chocolate_in_row[i]:
                    if grid[i][j] != '.':
                        possible = False
                        break
            vertical_cuts[j] = possible

        # En pratique la découpe verticale est possible si la colonne j (entre j et j+1)
        # a pour chaque ligne i ou il y a du chocolat grid[i][j] == '.'
        # mais la colonne i pour la chocolat_in_row n'est pas utile,
        # il faut plutot savoir si chaque ligne contient au moins un chocolat, on l'a.
        # Après on vérifie sur la colonne j que grid[i][j] == '.' si cette ligne a du chocolat

        # Correction d'analyse : Les vertical cuts se font entre les colonnes j et j+1,
        # donc la colonne à regarder est j (lignes i)
        # il faut tester à chaque ligne i ou on a chocolat si grid[i][j] == '.'

        # Recalcule vertical_cuts correctement:
        for j in range(w-1):
            possible = True
            for i in range(h):
                if grid[i][j] == '#':
                    # impossible de couper ici car du chocolat a la limite
                    possible = False
                    break
            vertical_cuts[j] = possible

        # De même pour horizontal_cuts on devrait faire:
        for i in range(h-1):
            possible = True
            for j in range(w):
                if grid[i][j] == '#':
                    possible = False
                    break
            horizontal_cuts[i] = possible

        # Maintenant on connaît les lignes et colonnes où on peut couper.
        # Le découpage minimal se fait donc en tronçons lignes délimités par ces cuts, pareil pour colonnes.

        # Trouvons les indices des segments blocs horizontaux
        horizontal_segments = []
        start = 0
        for i in range(h-1):
            if horizontal_cuts[i]:
                horizontal_segments.append((start, i))
                start = i+1
        horizontal_segments.append((start, h-1))

        # Trouvons les indices des segments blocs verticaux
        vertical_segments = []
        start = 0
        for j in range(w-1):
            if vertical_cuts[j]:
                vertical_segments.append((start, j))
                start = j+1
        vertical_segments.append((start, w-1))

        # Chaque combinaison d'un segment horizontal et un segment vertical forme un rectangle.
        # On compte combien de ces rectangles contient au moins un '#' (segment chocolat)
        # et on les compte.

        piece_count = 0
        for (r_start, r_end) in horizontal_segments:
            for (c_start, c_end) in vertical_segments:
                # Vérifier si ce rectangle contient au moins un '#'
                contains_chocolate = False
                for i in range(r_start, r_end+1):
                    for j in range(c_start, c_end+1):
                        if grid[i][j] == '#':
                            contains_chocolate = True
                            break
                    if contains_chocolate:
                        break
                if contains_chocolate:
                    piece_count += 1

        print(piece_count)

if __name__ == "__main__":
    main()