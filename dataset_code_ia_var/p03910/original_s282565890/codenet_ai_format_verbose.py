nombre_entier_cible = int(input())

somme_actuelle = 0

for nombre_actuel in range(1, nombre_entier_cible + 2):

    somme_actuelle += nombre_actuel

    if somme_actuelle >= nombre_entier_cible:

        valeur_a_exclure = somme_actuelle - nombre_entier_cible

        for numero_imprime in range(1, nombre_actuel + 1):

            if numero_imprime != valeur_a_exclure:

                print(numero_imprime)

        exit()