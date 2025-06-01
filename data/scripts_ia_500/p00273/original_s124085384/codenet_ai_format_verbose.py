nombre_de_test_cases = int(input())

for _ in range(nombre_de_test_cases):

    prix_unitaire_biere = int
    prix_unitaire_pretzel = int

    prix_biere, prix_pretzel, quantite_biere, quantite_pretzel = map(int, input().split())

    prix_total_sans_remise = (prix_biere * quantite_biere) + (prix_pretzel * quantite_pretzel)

    prix_remise_biere_5 = (prix_biere * 5)

    prix_remise_pretzel_2 = (prix_pretzel * 2)

    if quantite_biere < 5 and quantite_pretzel < 2:
        prix_total_avec_remise = min(
            prix_total_sans_remise,
            (prix_remise_biere_5 + prix_remise_pretzel_2) * 0.8
        )
    elif quantite_biere >= 5 and quantite_pretzel < 2:
        prix_total_avec_remise = min(
            prix_total_sans_remise,
            (prix_biere * quantite_biere + prix_remise_pretzel_2) * 0.8
        )
    elif quantite_biere < 5 and quantite_pretzel >= 2:
        prix_total_avec_remise = min(
            prix_total_sans_remise,
            (prix_remise_biere_5 + prix_pretzel * quantite_pretzel) * 0.8
        )
    else:
        prix_total_avec_remise = prix_total_sans_remise * 0.8

    print(int(prix_total_avec_remise))