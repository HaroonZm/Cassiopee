nombre_de_livres, nombre_de_conditions = [int(valeur) for valeur in input().split(" ")]

liste_des_numéros_de_bibliothèques = [int(input()) for indice_livre in range(nombre_de_livres)]

for dénominateur_condition in range(1, nombre_de_conditions + 1):

    for indice_livre in range(nombre_de_livres - 1):

        reste_modulo_courant = liste_des_numéros_de_bibliothèques[indice_livre] % dénominateur_condition
        reste_modulo_suivant = liste_des_numéros_de_bibliothèques[indice_livre + 1] % dénominateur_condition

        if reste_modulo_courant > reste_modulo_suivant:
            (
                liste_des_numéros_de_bibliothèques[indice_livre],
                liste_des_numéros_de_bibliothèques[indice_livre + 1]
            ) = (
                liste_des_numéros_de_bibliothèques[indice_livre + 1],
                liste_des_numéros_de_bibliothèques[indice_livre]
            )

for numéro_bibliothèque in liste_des_numéros_de_bibliothèques:
    print(numéro_bibliothèque)