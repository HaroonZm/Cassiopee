while True:

    nombre_de_lignes = int(input())

    if nombre_de_lignes == 0:
        break

    liste_entrees = [
        input().split()
        for _ in range(nombre_de_lignes)
    ]

    liste_analyse = [
        [
            ligne[0],                            # identifiant
            ligne.count('0'),                    # nombre de '0'
            ligne.count('1')                     # nombre de '1'
        ]
        for ligne in liste_entrees
    ]

    liste_analyse.sort(
        key=lambda entree: [
            -entree[1],                          # tri décroissant sur les '0'
            entree[2]                            # tri croissant sur les '1'
        ]
    )

    ordre_identifiants = [
        entree[0]
        for entree in liste_analyse
    ]

    print('\n'.join(ordre_identifiants))