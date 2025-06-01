nombre_elements = input()
chaine_entree = input()
liste_chaine = chaine_entree.split(' ')
liste_entiers = [int(element) for element in liste_chaine]
compteur_maximum = 1
compteur_courant = 1
for element in liste_entiers:
    if element == 1:
        compteur_courant += 1
    else:
        compteur_maximum = max(compteur_maximum, compteur_courant)
        compteur_courant = 1

compteur_maximum = max(compteur_maximum, compteur_courant)
print(compteur_maximum)