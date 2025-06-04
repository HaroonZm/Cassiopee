nombre_de_stations = int(input())

distance_max_par_station = [int(input()) for index_station in range(nombre_de_stations)]

distance_atteinte_croissante = 0
reponse_accessibilite = "yes"

# Vérification dans l'ordre croissant des stations
for index_station in range(nombre_de_stations):

    position_station = index_station * 10

    if distance_atteinte_croissante >= position_station:
        distance_atteinte_croissante = max(distance_atteinte_croissante, position_station + distance_max_par_station[index_station])
    else:
        reponse_accessibilite = "no"
        break

    if distance_atteinte_croissante >= (nombre_de_stations - 1) * 10:
        break

distance_atteinte_decroissante = 0

# Vérification dans l'ordre décroissant des stations
for index_station in range(nombre_de_stations):

    position_station = index_station * 10
    index_distant = nombre_de_stations - 1 - index_station

    if distance_atteinte_decroissante >= position_station:
        distance_atteinte_decroissante = max(distance_atteinte_decroissante, position_station + distance_max_par_station[index_distant])
    else:
        reponse_accessibilite = "no"
        break

    if distance_atteinte_decroissante >= (nombre_de_stations - 1) * 10:
        break

print(reponse_accessibilite)