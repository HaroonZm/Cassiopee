nombre_de_materiel_par_unite, nombre_total_de_materiel = map(int, input().split())

nombre_unites_necessaires = (nombre_total_de_materiel + nombre_de_materiel_par_unite - 1) // nombre_de_materiel_par_unite

print(nombre_unites_necessaires)