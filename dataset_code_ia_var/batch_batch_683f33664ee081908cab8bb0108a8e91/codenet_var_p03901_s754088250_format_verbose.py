nombre_elements = int(input())
valeur_maximale = int(input())

if nombre_elements % 2:

    premier_element_ajuste = 1
    pairs_restants = (nombre_elements - 1) / 2
    ecart_vers_max = (100 - valeur_maximale)
    somme_nombres_elements = (nombre_elements + 1)
    coefficient_pairs = ecart_vers_max * somme_nombres_elements / 2 / valeur_maximale

    resultat = premier_element_ajuste + pairs_restants + coefficient_pairs

    print(resultat)

else:

    numerateur = nombre_elements * 50
    resultat = numerateur / valeur_maximale

    print(resultat)