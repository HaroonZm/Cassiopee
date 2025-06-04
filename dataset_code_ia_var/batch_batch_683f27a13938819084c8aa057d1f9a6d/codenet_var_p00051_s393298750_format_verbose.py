nombre_de_tests = int(input())

while nombre_de_tests > 0:

    nombre_chaine = input()
    nombre_chaine_triee = ''.join(sorted(nombre_chaine))
    nombre_inverse_chaine_triee = nombre_chaine_triee[::-1]

    difference = int(nombre_inverse_chaine_triee) - int(nombre_chaine_triee)

    print(difference)

    nombre_de_tests -= 1