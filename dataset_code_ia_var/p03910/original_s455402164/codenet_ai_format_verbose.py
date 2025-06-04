nombre_cible = int(input())

somme_courante = 0

for indice_courant in range(nombre_cible):

    somme_courante += indice_courant + 1

    if somme_courante >= nombre_cible:
        dernier_terme_utilise = indice_courant + 1
        break

if somme_courante == nombre_cible:

    for nombre in range(1, dernier_terme_utilise + 1):
        print(nombre)

else:

    if nombre_cible == 2:
        print(2)
    else:
        for nombre in range(1, dernier_terme_utilise + 1):
            if somme_courante - nombre != nombre_cible:
                print(nombre)