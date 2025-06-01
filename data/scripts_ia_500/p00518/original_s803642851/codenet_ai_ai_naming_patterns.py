nombre_entrees = int(input())
chaine_caracteres = input()
liste_caracteres = list(chaine_caracteres)

tableau_programmation_dynamique = [[0 for indice_colonne in range(8)] for indice_ligne in range(nombre_entrees + 1)]

tableau_programmation_dynamique[0][1] = 1

for indice_position in range(nombre_entrees):
    caractere_courant = chaine_caracteres[indice_position]
    if caractere_courant == "J":
        tableau_programmation_dynamique[indice_position + 1][1] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4]
        tableau_programmation_dynamique[indice_position + 1][2] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6]
        tableau_programmation_dynamique[indice_position + 1][3] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]
        tableau_programmation_dynamique[indice_position + 1][4] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]
        tableau_programmation_dynamique[indice_position + 1][5] = 0
        tableau_programmation_dynamique[indice_position + 1][6] = 0
        tableau_programmation_dynamique[indice_position + 1][7] = 0
    if caractere_courant == 'O':
        tableau_programmation_dynamique[indice_position + 1][1] = 0
        tableau_programmation_dynamique[indice_position + 1][2] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6]
        tableau_programmation_dynamique[indice_position + 1][3] = 0
        tableau_programmation_dynamique[indice_position + 1][4] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]
        tableau_programmation_dynamique[indice_position + 1][5] = tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6]
        tableau_programmation_dynamique[indice_position + 1][6] = tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]
        tableau_programmation_dynamique[indice_position + 1][7] = 0
    if caractere_courant == 'I':
        tableau_programmation_dynamique[indice_position + 1][1] = 0
        tableau_programmation_dynamique[indice_position + 1][2] = 0
        tableau_programmation_dynamique[indice_position + 1][3] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]
        tableau_programmation_dynamique[indice_position + 1][4] = tableau_programmation_dynamique[indice_position][1] + tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]
        tableau_programmation_dynamique[indice_position + 1][5] = 0
        tableau_programmation_dynamique[indice_position + 1][6] = tableau_programmation_dynamique[indice_position][2] + tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][5] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]
        tableau_programmation_dynamique[indice_position + 1][7] = tableau_programmation_dynamique[indice_position][3] + tableau_programmation_dynamique[indice_position][4] + tableau_programmation_dynamique[indice_position][6] + tableau_programmation_dynamique[indice_position][7]

resultat = sum(tableau_programmation_dynamique[nombre_entrees][1:8]) % 10007
print(resultat)