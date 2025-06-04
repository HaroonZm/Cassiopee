nombre_tests = int(input())

for indice_test in range(nombre_tests):

    prix_article_type_1, prix_article_type_2, quantite_article_1, quantite_article_2 = map(int, input().split())

    somme_initiale = prix_article_type_1 * quantite_article_1 + prix_article_type_2 * quantite_article_2

    seuil_reduction = int((prix_article_type_1 * 5 + prix_article_type_2 * 2) * 0.8)

    somme_potentielle = somme_initiale

    if somme_initiale <= seuil_reduction:
        print(somme_initiale)

    else:
        if 5 - quantite_article_1 > 0:
            somme_potentielle += (5 - quantite_article_1) * prix_article_type_1

        if 2 - quantite_article_2 > 0:
            somme_potentielle += (2 - quantite_article_2) * prix_article_type_2

        print(min(somme_initiale, int(somme_potentielle * 0.8)))