# Lecture des valeurs d'entrée pour capacité totale, taille de l’article, et taille séparateur
total_capacity, item_size, separator_size = map(int, input().split())

# Initialisation du compteur de nombre d'articles pouvant être placés
number_of_items = 1

while True:
    # Calcul de l'espace utilisé en fonction du nombre d'articles et séparateurs nécessaires
    used_capacity = (number_of_items * item_size) + ((number_of_items - 1 + 1) * separator_size)
    
    if used_capacity > total_capacity:
        break
    else:
        number_of_items += 1

# Affichage du nombre maximal d'articles pouvant être placés sans dépasser la capacité totale
print(number_of_items - 1)