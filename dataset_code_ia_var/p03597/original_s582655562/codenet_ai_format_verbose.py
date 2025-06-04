nombre_de_cellules_par_cote = int(input())

nombre_de_cellules_noires = int(input())

aire_totale_grille = nombre_de_cellules_par_cote ** 2

nombre_de_cellules_blanches = aire_totale_grille - nombre_de_cellules_noires

print(nombre_de_cellules_blanches)