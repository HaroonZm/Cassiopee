nombre_points, nombre_deplacements = map(int, input().split())
liste_sommes_cumulees = [0]
for index_point in range(nombre_points - 1):
    distance = int(input())
    liste_sommes_cumulees.append(liste_sommes_cumulees[-1] + distance)
somme_absolue_distances = 0
position_courante = 0
for index_deplacement in range(nombre_deplacements):
    deplacement = int(input())
    difference_distance = abs(liste_sommes_cumulees[position_courante] - liste_sommes_cumulees[position_courante + deplacement])
    somme_absolue_distances += difference_distance
    somme_absolue_distances %= 100000
    position_courante += deplacement
print(somme_absolue_distances)