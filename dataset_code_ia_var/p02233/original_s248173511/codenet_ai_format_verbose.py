nombre_entier_donne = int(input())

liste_fibonacci = [0] * (nombre_entier_donne + 1)

liste_fibonacci[0] = 1
liste_fibonacci[1] = 1

for indice_terme in range(2, len(liste_fibonacci)):
    liste_fibonacci[indice_terme] = liste_fibonacci[indice_terme - 1] + liste_fibonacci[indice_terme - 2]

print(liste_fibonacci[nombre_entier_donne])