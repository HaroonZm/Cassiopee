nombre_cible = int(input())

liste_nombres_selectionnes = []
somme_actuelle = 0

for nombre_actuel in range(1, nombre_cible + 1):

    liste_nombres_selectionnes.append(nombre_actuel)

    if somme_actuelle + nombre_actuel > nombre_cible:
        break

    somme_actuelle += nombre_actuel

difference_a_eliminer = sum(liste_nombres_selectionnes) - nombre_cible

if difference_a_eliminer == 0:
    for nombre in liste_nombres_selectionnes:
        print(nombre)
else:
    index_difference = liste_nombres_selectionnes.index(difference_a_eliminer)
    del liste_nombres_selectionnes[index_difference]
    for nombre in liste_nombres_selectionnes:
        print(nombre)