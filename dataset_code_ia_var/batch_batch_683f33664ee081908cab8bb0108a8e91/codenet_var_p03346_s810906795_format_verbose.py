nombre_d_entiers = int(input())

longueur_plus_long_sous_sequence_croissante = [0 for index in range(nombre_d_entiers + 1)]

for indice_entier in range(nombre_d_entiers):
    entier_actuel = int(input())
    longueur_plus_long_sous_sequence_croissante[entier_actuel] = longueur_plus_long_sous_sequence_croissante[entier_actuel - 1] + 1

longueur_max_sous_sequence_croissante = max(longueur_plus_long_sous_sequence_croissante)
minimum_elements_a_supprimer = nombre_d_entiers - longueur_max_sous_sequence_croissante

print(minimum_elements_a_supprimer)