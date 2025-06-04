# Lecture des trois entiers : taille_totale, taille_segment_pleine, taille_segment_partielle
taille_totale, taille_segment_pleine, taille_segment_partielle = map(int, input().split())

# Calcul de la taille du premier segment après l'étape initiale
taille_apres_premiere_etape = taille_segment_pleine + 2 * taille_segment_partielle

# Initialisation du nombre d'étapes nécessaires
nombre_etapes = 1

# Répétition jusqu'à ce que la taille supplémentaire ajoutée dépasse la limite
while taille_apres_premiere_etape <= taille_totale - (taille_segment_pleine + taille_segment_partielle):
    
    taille_apres_premiere_etape += taille_segment_pleine + taille_segment_partielle
    
    nombre_etapes += 1

# Affichage du résultat final
print(nombre_etapes)