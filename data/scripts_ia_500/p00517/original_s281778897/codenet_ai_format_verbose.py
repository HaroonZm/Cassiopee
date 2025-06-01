largeur_fenetre, hauteur_fenetre, nombre_points = map(int, raw_input().split())

coord_x_precedent, coord_y_precedent = map(int, raw_input().split())

somme_distances_minimales = 0

for indice_point in xrange(nombre_points - 1):
    
    coord_x_courant, coord_y_courant = map(int, raw_input().split())
    
    distance_option_1 = abs(coord_y_courant - coord_x_courant + coord_x_precedent - coord_y_precedent) + min(abs(coord_y_courant - coord_y_precedent), abs(coord_x_courant - coord_x_precedent))
    distance_option_2 = abs(coord_x_courant - coord_x_precedent) + abs(coord_y_courant - coord_y_precedent)
    
    somme_distances_minimales += min(distance_option_1, distance_option_2)
    
    coord_x_precedent, coord_y_precedent = coord_x_courant, coord_y_courant

print somme_distances_minimales