nombre_de_cas = int(input())

for indice_cas in range(nombre_de_cas):

    valeur_depart, valeur_arrivee = map(int, input().split())

    decalage = 2 ** 30

    valeur_depart += decalage
    valeur_arrivee += decalage

    nombre_operations = 0

    while valeur_depart + (valeur_depart & -valeur_depart) <= valeur_arrivee:
        valeur_depart += (valeur_depart & -valeur_depart)
        nombre_operations += 1

    difference = valeur_arrivee - valeur_depart

    while difference:
        difference -= (difference & -difference)
        nombre_operations += 1

    print(nombre_operations)