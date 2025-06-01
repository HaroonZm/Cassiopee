nombre_de_lignes, nombre_de_colonnes, nombre_de_cartes_supplémentaires = map(int, input().split())

nombre_de_cartes_supplémentaires -= nombre_de_lignes * nombre_de_colonnes

if nombre_de_cartes_supplémentaires < 0:
    print(0)

else:
    coefficient_binomial = 1

    for index in range(nombre_de_cartes_supplémentaires):
        coefficient_binomial *= index + nombre_de_lignes

    for index in range(nombre_de_cartes_supplémentaires):
        coefficient_binomial //= index + 1

    print(coefficient_binomial)