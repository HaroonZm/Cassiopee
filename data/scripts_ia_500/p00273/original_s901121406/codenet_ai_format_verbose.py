nombre_de_tests = int(raw_input())

for index_test in range(nombre_de_tests):

    quantite_x, quantite_y, prix_b, prix_p = map(int, raw_input().split())

    cout_avec_prix_initial = quantite_x * prix_b + quantite_y * prix_p

    cout_avec_tarif_minimum_reduit = (quantite_x * max(prix_b, 5) + quantite_y * max(prix_p, 2)) * 0.8

    cout_minimal = min(cout_avec_prix_initial, cout_avec_tarif_minimum_reduit)

    print "%d" % cout_minimal