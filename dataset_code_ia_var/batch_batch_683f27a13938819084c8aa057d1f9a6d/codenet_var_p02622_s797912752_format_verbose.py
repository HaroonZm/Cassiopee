premiere_chaine_utilisateur = input()

deuxieme_chaine_utilisateur = input()

nombre_de_differences = 0

for indice_caractere in range(len(premiere_chaine_utilisateur)):

    if premiere_chaine_utilisateur[indice_caractere] != deuxieme_chaine_utilisateur[indice_caractere]:

        nombre_de_differences += 1

print(nombre_de_differences)