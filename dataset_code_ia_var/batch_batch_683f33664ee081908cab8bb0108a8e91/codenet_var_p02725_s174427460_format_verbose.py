nombre_de_positions, nombre_de_bornes = map(int, input().split())

liste_positions_bornes = list(map(int, input().split()))

liste_ecarts_successifs = []

for indice in range(nombre_de_bornes - 1):
    difference_entre_bornes_consecutives = liste_positions_bornes[indice + 1] - liste_positions_bornes[indice]
    liste_ecarts_successifs.append(difference_entre_bornes_consecutives)

distance_entre_premiere_et_derniere_borne = nombre_de_positions - liste_positions_bornes[-1] + liste_positions_bornes[0]
liste_ecarts_successifs.append(distance_entre_premiere_et_derniere_borne)

distance_minimale_maximale = nombre_de_positions - max(liste_ecarts_successifs)

print(distance_minimale_maximale)