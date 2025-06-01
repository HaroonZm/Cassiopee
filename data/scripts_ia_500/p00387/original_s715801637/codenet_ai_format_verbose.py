nombre_elements_par_grille, nombre_total_elements = map(int, input().split())

nombre_grilles_necessaires = (nombre_total_elements + nombre_elements_par_grille - 1) // nombre_elements_par_grille

print(nombre_grilles_necessaires)