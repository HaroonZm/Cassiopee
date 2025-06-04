nombre_de_stations_total, distance_entre_stations, longueur_du_train = [int(entree) for entree in input().split()]

nombre_de_trains_necessaires = (nombre_de_stations_total - longueur_du_train) // (distance_entre_stations + longueur_du_train)

print(nombre_de_trains_necessaires)