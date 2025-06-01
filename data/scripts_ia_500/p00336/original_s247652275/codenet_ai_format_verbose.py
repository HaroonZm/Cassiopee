texte_source = input()

texte_cible = input()

tableau_comparaison = [[0 for index_colonne in range(len(texte_source))] for index_ligne in range(len(texte_cible))]

if len(texte_source) > len(texte_cible):

    if texte_source[0] == texte_cible[0]:
        tableau_comparaison[0][0] = 1

    for index_colonne in range(1, len(texte_source)):

        if texte_source[index_colonne] == texte_cible[0]:
            tableau_comparaison[0][index_colonne] = tableau_comparaison[0][index_colonne - 1] + 1
        else:
            tableau_comparaison[0][index_colonne] = tableau_comparaison[0][index_colonne - 1]

    for index_ligne in range(1, len(texte_cible)):

        if texte_cible[index_ligne] == texte_source[index_ligne]:
            tableau_comparaison[index_ligne][index_ligne] = tableau_comparaison[index_ligne - 1][index_ligne - 1]

        for index_colonne in range(index_ligne + 1, len(texte_source)):

            if texte_cible[index_ligne] == texte_source[index_colonne]:
                tableau_comparaison[index_ligne][index_colonne] = tableau_comparaison[index_ligne - 1][index_colonne - 1] + tableau_comparaison[index_ligne][index_colonne - 1]
            else:
                tableau_comparaison[index_ligne][index_colonne] = tableau_comparaison[index_ligne][index_colonne - 1]

    print(tableau_comparaison[len(texte_cible) - 1][len(texte_source) - 1] % 1000000007)

elif len(texte_source) == len(texte_cible):

    if texte_source == texte_cible:
        print(1)
    else:
        print(0)

else:
    print(0)