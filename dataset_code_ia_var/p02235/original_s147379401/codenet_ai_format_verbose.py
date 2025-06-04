obtenir_entree_utilisateur = input

liste_sequences_positions = []

nombre_de_cas = int(obtenir_entree_utilisateur())

for compteur_cas in range(nombre_de_cas):

    chaine_reference = obtenir_entree_utilisateur()
    liste_positions = []

    chaine_a_chercher = obtenir_entree_utilisateur()

    for caractere_recherche in chaine_a_chercher:

        position_precedente = 0
        index_liste_positions = 0

        for position_actuelle in liste_positions:

            nouvelle_position = chaine_reference.find(caractere_recherche, position_precedente) + 1

            if nouvelle_position < 1:
                break

            if nouvelle_position < position_actuelle:
                liste_positions[index_liste_positions] = nouvelle_position

            position_precedente = position_actuelle
            index_liste_positions += 1

        else:

            nouvelle_position = chaine_reference.find(caractere_recherche, position_precedente) + 1

            if nouvelle_position:
                liste_positions.append(nouvelle_position)

    liste_sequences_positions.append(liste_positions)

for sequence_positions in liste_sequences_positions:
    print(len(sequence_positions))