distance_total_du_cercle, nombre_de_points = map(int, input().split())

positions_points_sur_le_cercle = list(map(int, input().split()))

distances_entre_points_consecutifs = []

for indice_point in range(nombre_de_points - 1):
    
    distance_entre_points = positions_points_sur_le_cercle[indice_point + 1] - positions_points_sur_le_cercle[indice_point]
    
    distances_entre_points_consecutifs.append(distance_entre_points)

distance_du_dernier_au_premier = positions_points_sur_le_cercle[0] + distance_total_du_cercle - positions_points_sur_le_cercle[nombre_de_points - 1]

distances_entre_points_consecutifs.append(distance_du_dernier_au_premier)

plus_grande_distance_sautee = max(distances_entre_points_consecutifs)

distance_minimale_a_parcourir = distance_total_du_cercle - plus_grande_distance_sautee

print(distance_minimale_a_parcourir)