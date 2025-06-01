hauteur_totale_arbre, largeur_min_feuille, largeur_max_feuille = map(int, input().split())

nombre_de_feuilles_compatibles = 0

for largeur_feuille in range(largeur_min_feuille, largeur_max_feuille + 1):
    
    if hauteur_totale_arbre % largeur_feuille == 0:
        nombre_de_feuilles_compatibles += 1

print(nombre_de_feuilles_compatibles)