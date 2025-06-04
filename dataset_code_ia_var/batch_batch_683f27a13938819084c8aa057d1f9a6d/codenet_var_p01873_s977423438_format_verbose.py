nombre_elements = int(input())

liste_entiers = list(map(int, input().split()))

for taille_sous_sequence in range(1, nombre_elements + 1):

    if nombre_elements % taille_sous_sequence == 0:

        motif_valide = True

        for indice in range(nombre_elements):

            if indice >= taille_sous_sequence and liste_entiers[indice] != liste_entiers[indice - taille_sous_sequence]:

                motif_valide = False
                break

        if motif_valide:
            print(nombre_elements // taille_sous_sequence)
            exit()

print(1)