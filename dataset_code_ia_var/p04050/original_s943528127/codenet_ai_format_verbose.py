nombre_elements_total, nombre_elements_liste = [int(valeur) for valeur in input().split()]

liste_entiers = [int(element) for element in input().split()]

operation_impossible = False

for index_courant in range(1, nombre_elements_liste - 1):

    if liste_entiers[index_courant] % 2 == 1:

        if liste_entiers[0] % 2 == 1:

            if liste_entiers[len(liste_entiers) - 1] % 2 == 1:

                print("Impossible")
                operation_impossible = True
                break

            else:

                liste_entiers[index_courant], liste_entiers[len(liste_entiers) - 1] = liste_entiers[len(liste_entiers) - 1], liste_entiers[index_courant]

        else:

            liste_entiers[index_courant], liste_entiers[0] = liste_entiers[0], liste_entiers[index_courant]

if not operation_impossible:

    chaine_resultat = ''.join([str(element_valeur) + " " for element_valeur in liste_entiers])
    print(chaine_resultat[:-1])

    if nombre_elements_liste == 1:

        if liste_entiers[0] > 1:

            liste_entiers[0] -= 1
            liste_entiers.append(1)
            print(nombre_elements_liste + 1)

        else:

            print(nombre_elements_liste)

    else:

        if liste_entiers[len(liste_entiers) - 1] == 1:

            print(nombre_elements_liste - 1)
            liste_entiers.pop()
            liste_entiers[0] += 1

        else:

            print(nombre_elements_liste)
            liste_entiers[0] += 1
            liste_entiers[len(liste_entiers) - 1] -= 1

    chaine_resultat_finale = ''.join([str(element_valeur) + " " for element_valeur in liste_entiers])
    print(chaine_resultat_finale[:-1])