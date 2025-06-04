nombre_entrees = int(input())

liste_nombres = [int(input()) for indice_entree in range(nombre_entrees)]

dictionnaire_sommes_prefixes = {}

somme_courante = 0
longueur_maximale_sous_liste = 0

dictionnaire_sommes_prefixes[0] = -1

for indice_element in range(nombre_entrees):

    somme_courante += liste_nombres[indice_element]

    if somme_courante in dictionnaire_sommes_prefixes:
        longueur_sous_liste = indice_element - dictionnaire_sommes_prefixes[somme_courante]
        longueur_maximale_sous_liste = max(longueur_sous_liste, longueur_maximale_sous_liste)
    else:
        dictionnaire_sommes_prefixes[somme_courante] = indice_element

print(longueur_maximale_sous_liste)