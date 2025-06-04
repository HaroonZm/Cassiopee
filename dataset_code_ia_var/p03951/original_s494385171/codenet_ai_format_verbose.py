nombre_de_caracteres = int(input())

chaine_source = input()

chaine_cible = input()

for longueur_total in range(nombre_de_caracteres, 2 * nombre_de_caracteres + 1):

    longueur_chevauchement = 2 * nombre_de_caracteres - longueur_total

    suffixe_source = chaine_source[nombre_de_caracteres - longueur_chevauchement : ]

    prefixe_cible = chaine_cible[ : longueur_chevauchement]

    if suffixe_source == prefixe_cible:

        print(longueur_total)

        exit()

print(2 * nombre_de_caracteres)