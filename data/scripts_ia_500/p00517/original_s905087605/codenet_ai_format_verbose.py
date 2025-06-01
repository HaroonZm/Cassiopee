compteur_distance = 0

nombre_points, largeur_initiale, hauteur_initiale = 0, 0, 0
largeur_initiale, hauteur_initiale = 0, 0

nombre_points, largeur_initiale, hauteur_initiale = map(int, input().split())
largeur_courante, hauteur_courante = map(int, input().split())

for index_point in range(1, nombre_points):
    
    largeur_nouvelle, hauteur_nouvelle = map(int, input().split())
    
    condition_inversion = (hauteur_courante < hauteur_nouvelle and largeur_courante > largeur_nouvelle) or (hauteur_courante > hauteur_nouvelle and largeur_courante < largeur_nouvelle)
    
    if condition_inversion:
        distance_parcours = abs(hauteur_nouvelle - hauteur_courante) + abs(largeur_nouvelle - largeur_courante)
    else:
        distance_parcours = max(abs(hauteur_nouvelle - hauteur_courante), abs(largeur_nouvelle - largeur_courante))
    
    compteur_distance += distance_parcours
    
    largeur_courante = largeur_nouvelle
    hauteur_courante = hauteur_nouvelle

print(compteur_distance)