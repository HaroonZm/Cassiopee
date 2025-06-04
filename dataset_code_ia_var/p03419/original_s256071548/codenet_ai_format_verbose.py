nombre_lignes, nombre_colonnes = map(int, input().split())

nombre_de_cellules_touchees_par_le_bord = 0

if nombre_lignes == 1 and nombre_colonnes == 1:
    pass

elif nombre_lignes == 1 or nombre_colonnes == 1:
    nombre_de_cellules_touchees_par_le_bord += 2

else:
    nombre_de_cellules_touchees_par_le_bord += (nombre_lignes - 1) * 2
    nombre_de_cellules_touchees_par_le_bord += (nombre_colonnes - 1) * 2

nombre_de_cellules_possibles = nombre_lignes * nombre_colonnes - nombre_de_cellules_touchees_par_le_bord

print(nombre_de_cellules_possibles)