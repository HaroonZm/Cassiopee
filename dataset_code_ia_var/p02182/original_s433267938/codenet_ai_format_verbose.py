nombre_lignes, nombre_colonnes = map(int, input().split())

grille_initiale = [list(input()) for _ in range(nombre_lignes)]

grille_finale = [list(input()) for _ in range(nombre_lignes)]

compteur_difference = 0

for indice_ligne in range(nombre_lignes):
    for indice_colonne in range(nombre_colonnes):
        if grille_initiale[indice_ligne][indice_colonne] != grille_finale[indice_ligne][indice_colonne]:
            compteur_difference += 1

print(compteur_difference)