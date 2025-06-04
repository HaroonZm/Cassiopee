number_of_points = range(int(input("Entrez le nombre de sommets du polygone : ")))

list_of_polygon_points = []

for point_index in number_of_points:
    
    coordinates = [int(coordinate) for coordinate in input(f"Entrez les coordonnées du point {point_index+1} (séparées par un espace) : ").split()]
    
    list_of_polygon_points.append(coordinates)

polygon_area_sum = 0

list_of_polygon_points.append(list_of_polygon_points[0])

for current_index in number_of_points:
    
    next_index = current_index + 1
    
    polygon_area_sum += (
        list_of_polygon_points[current_index][0] * list_of_polygon_points[next_index][1] -
        list_of_polygon_points[current_index][1] * list_of_polygon_points[next_index][0]
    )

print(0.5 * polygon_area_sum)