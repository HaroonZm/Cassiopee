while True:

    prix_a_payer, nombre_pieces_1, nombre_pieces_5, nombre_pieces_10, nombre_pieces_50, nombre_pieces_100, nombre_pieces_500 = map(int, input().split())

    if prix_a_payer == 0:
        break

    valeurs_pieces = (500, 100, 50, 10, 5, 1)
    quantites_disponibles = (nombre_pieces_500, nombre_pieces_100, nombre_pieces_50, nombre_pieces_10, nombre_pieces_5, nombre_pieces_1)
    INFINI = 10 ** 20

    def calculer_nombre_pieces_monnaie(monnaie_a_rendre):

        nombre_total_pieces_monnaie = 0

        for valeur_piece in valeurs_pieces:
            nombre_pieces_de_cette_valeur = monnaie_a_rendre // valeur_piece
            nombre_total_pieces_monnaie += nombre_pieces_de_cette_valeur
            monnaie_a_rendre %= valeur_piece

        return nombre_total_pieces_monnaie

    def calculer_nombre_pieces_payement(montant_a_atteindre):

        nombre_total_pieces_payement = 0

        for valeur_piece, quantite_maximale_disponible in zip(valeurs_pieces, quantites_disponibles):
            nombre_pieces_utilisees = min(montant_a_atteindre // valeur_piece, quantite_maximale_disponible)
            nombre_total_pieces_payement += nombre_pieces_utilisees
            montant_a_atteindre -= valeur_piece * nombre_pieces_utilisees

        if montant_a_atteindre == 0:
            return nombre_total_pieces_payement

        return INFINI

    nombre_minimum_total_pieces = min(
        [
            calculer_nombre_pieces_payement(montant_exact_utilise) +
            calculer_nombre_pieces_monnaie(montant_exact_utilise - prix_a_payer)
            for montant_exact_utilise in range(prix_a_payer, prix_a_payer + 500)
        ]
    )

    print(nombre_minimum_total_pieces)