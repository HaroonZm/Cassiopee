from bisect import bisect

nombre_de_elements, nombre_de_groupes, *liste_de_positions = map(int, open(0).read().split())

espaces_entre_positionnements = [
    (liste_de_positions[index + 1] - liste_de_positions[index]) - 1
    for index in range(nombre_de_elements - 1)
]

espaces_entre_positionnements.sort(reverse=True)

longueur_totale = liste_de_positions[-1] - liste_de_positions[0] + 1

somme_des_plus_grands_espaces = sum(espaces_entre_positionnements[:nombre_de_groupes - 1])

longueur_minimale_requise = longueur_totale - somme_des_plus_grands_espaces

print(longueur_minimale_requise)