from math import hypot

# Lecture des coordonnées du premier point du segment
start_point_x, start_point_y, end_point_x, end_point_y = map(int, input().split())

# Calcul du vecteur directeur du segment
segment_vector_x = end_point_x - start_point_x
segment_vector_y = end_point_y - start_point_y

# Calcul de la norme (longueur) du vecteur du segment
segment_vector_length = hypot(segment_vector_x, segment_vector_y)

# Lecture du nombre de points à projeter
number_of_projection_points = int(input())

# Boucle sur chaque point à projeter
for projection_point_x, projection_point_y in (map(int, input().split()) for _ in range(number_of_projection_points)):

    # Calcul du coefficient de projection scalaire sur le segment
    projection_scalar = ((projection_point_x - start_point_x) * segment_vector_x + (projection_point_y - start_point_y) * segment_vector_y) / (segment_vector_length ** 2)

    # Calcul des coordonnées du point projeté sur le segment
    projected_point_x = start_point_x + segment_vector_x * projection_scalar
    projected_point_y = start_point_y + segment_vector_y * projection_scalar

    print(projected_point_x, projected_point_y)