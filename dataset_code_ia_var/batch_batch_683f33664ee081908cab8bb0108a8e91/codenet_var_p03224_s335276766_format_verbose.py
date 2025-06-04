nombre_d_entier = int(input())

racine_de_deux_fois_n = (2 * nombre_d_entier) ** 0.5
nombre_de_paires_faites = racine_de_deux_fois_n // 1

if nombre_d_entier != nombre_de_paires_faites * (nombre_de_paires_faites + 1) // 2:
    print("No")
else:
    print("Yes")
    nombre_de_paires_faites = int(nombre_de_paires_faites)
    print(nombre_de_paires_faites + 1)

    liste_resultat = [
        [0 for indice_colonne in range(nombre_de_paires_faites)]
        for indice_ligne in range(nombre_de_paires_faites + 1)
    ]

    indice_colonne_paire_un = 0
    indice_ligne_paire_un = 0
    indice_colonne_paire_deux = 0
    indice_ligne_paire_deux = 1

    for valeur_courante in range(nombre_d_entier):
        valeur_a_inserer = valeur_courante + 1
        liste_resultat[indice_ligne_paire_un][indice_colonne_paire_un] = valeur_a_inserer
        liste_resultat[indice_ligne_paire_deux][indice_colonne_paire_deux] = valeur_a_inserer

        if indice_ligne_paire_un == indice_colonne_paire_un:
            indice_ligne_paire_un = 0
            indice_colonne_paire_un += 1
            indice_ligne_paire_deux = indice_colonne_paire_un + 1
            indice_colonne_paire_deux = 0
        else:
            indice_ligne_paire_un += 1
            indice_colonne_paire_deux += 1

    for sous_liste in liste_resultat:
        print(
            str(nombre_de_paires_faites)
            + " "
            + " ".join(str(nombre) for nombre in sous_liste)
        )