# Lecture du nombre total d'éléments à traiter
nombre_total_elements = int(input())

# Lecture du pourcentage de réussite et conversion en décimal
pourcentage_reussite_decimal = int(input()) / 100

# Calcul du nombre d'essais nécessaires en prenant en compte l'arrondi supérieur
nombre_essais_arrondis = (nombre_total_elements + 1) // 2

# Calcul du résultat final en fonction du pourcentage
resultat_calcul = nombre_essais_arrondis / pourcentage_reussite_decimal

# Affichage du résultat
print(resultat_calcul)