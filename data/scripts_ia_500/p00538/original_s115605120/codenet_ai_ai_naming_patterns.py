nombre_elements = int(input())
valeurs = [int(input()) for _ in range(nombre_elements)]

tableau_dp = [
    [
        valeurs[indice_i] if indice_i == indice_j
        else max(valeurs[indice_i], valeurs[(indice_i + 1) % nombre_elements]) if (indice_i + 1) % nombre_elements == indice_j
        else 0
        for indice_j in range(nombre_elements)
    ]
    for indice_i in range(nombre_elements)
]

debut_boucle = 3 if nombre_elements % 2 == 0 else 2
for ecart in range(debut_boucle, nombre_elements, 2):
    for indice_gauche in range(nombre_elements):
        indice_droite = (indice_gauche + ecart) % nombre_elements

        candidats_solutions = []
        for x, indice_gauche_suivant, indice_droite_suivant in [
            (indice_gauche, (indice_gauche + 1) % nombre_elements, indice_droite),
            (indice_droite, indice_gauche, (indice_droite + nombre_elements - 1) % nombre_elements),
        ]:
            if valeurs[indice_gauche_suivant] > valeurs[indice_droite_suivant]:
                indice_gauche_suivant = (indice_gauche_suivant + 1) % nombre_elements
            else:
                indice_droite_suivant = (indice_droite_suivant + nombre_elements - 1) % nombre_elements
            candidats_solutions.append(valeurs[x] + tableau_dp[indice_gauche_suivant][indice_droite_suivant])

        tableau_dp[indice_gauche][indice_droite] = max(candidats_solutions)

resultat_final = max(tableau_dp[(i + 1) % nombre_elements][i] for i in range(nombre_elements))
print(resultat_final)