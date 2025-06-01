tableau_dp = [[0 for index_somme in range(1001)] for index_nombre_elements in range(10)]

tableau_dp[0][0] = 1
tableau_dp[1][0] = 1

for valeur_actuelle in range(1, 101):

    for nombre_elements_utilises in range(9, 0, -1):

        ligne_courante = tableau_dp[nombre_elements_utilises]
        ligne_precedente = tableau_dp[nombre_elements_utilises - 1]

        for somme_courante in range(valeur_actuelle, 1001):

            ligne_courante[somme_courante] = ligne_precedente[somme_courante - valeur_actuelle] + ligne_courante[somme_courante]


while True:

    nombre_elements_demandes, somme_voulue = map(int, input().split())

    if nombre_elements_demandes == 0:
        break

    print(tableau_dp[nombre_elements_demandes][somme_voulue])