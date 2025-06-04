texte_entree = input()
motif_a_rechercher = input()

indices_des_caracteres_trouves = [0] * len(motif_a_rechercher)
compteur_de_caracteres_trouves = 0

for indice_dans_texte in range(len(texte_entree)):

    if texte_entree[indice_dans_texte] == motif_a_rechercher[compteur_de_caracteres_trouves]:
        indices_des_caracteres_trouves[compteur_de_caracteres_trouves] = indice_dans_texte
        compteur_de_caracteres_trouves += 1

        if compteur_de_caracteres_trouves == len(motif_a_rechercher):
            break

if compteur_de_caracteres_trouves != len(motif_a_rechercher):
    print("no")
    exit()

compteur_de_caracteres_trouves -= 1

for indice_du_texte_inversé in range(len(texte_entree) - 1, -1, -1):

    if texte_entree[indice_du_texte_inversé] == motif_a_rechercher[compteur_de_caracteres_trouves]:
        if indices_des_caracteres_trouves[compteur_de_caracteres_trouves] != indice_du_texte_inversé:
            print("no")
            exit()
        compteur_de_caracteres_trouves -= 1

    if compteur_de_caracteres_trouves == -1:
        break

if compteur_de_caracteres_trouves != -1:
    print("no")
else:
    print("yes")