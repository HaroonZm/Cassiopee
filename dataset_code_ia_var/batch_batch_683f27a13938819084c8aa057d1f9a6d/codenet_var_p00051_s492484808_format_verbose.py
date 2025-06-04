nombre_de_test_cases = int(input())

for indice_test_case in range(nombre_de_test_cases):

    liste_caracteres_nombres = []

    chaine_nombre = input()

    for caractere in chaine_nombre:
        liste_caracteres_nombres.append(caractere)

    liste_caracteres_nombres.sort(reverse=True)
    nombre_maximum_possible_str = "".join(liste_caracteres_nombres)

    liste_caracteres_nombres.sort()
    nombre_minimum_possible_str = "".join(liste_caracteres_nombres)

    nombre_maximum_possible = int(nombre_maximum_possible_str)
    nombre_minimum_possible = int(nombre_minimum_possible_str)

    difference_max_min = nombre_maximum_possible - nombre_minimum_possible

    print(difference_max_min)