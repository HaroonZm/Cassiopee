while True:
    nombre_de_paires = int(input())

    if nombre_de_paires == 0:
        break

    texte_a_dechiffrer = list(input())

    liste_de_paires_de_chiffrement = [
        list(map(int, input().split())) for _ in range(nombre_de_paires)
    ]

    for position_debut, position_fin in reversed(liste_de_paires_de_chiffrement):
        decalage = position_fin - position_debut
        indice_debut = position_debut - 1
        indice_fin = position_fin - 1

        caractere_debut = texte_a_dechiffrer[indice_debut]
        caractere_fin = texte_a_dechiffrer[indice_fin]

        texte_a_dechiffrer[indice_debut] = chr((ord(caractere_fin) - 97 + decalage) % 26 + 97)
        texte_a_dechiffrer[indice_fin] = chr((ord(caractere_debut) - 97 + decalage) % 26 + 97)

    texte_final_dechiffre = "".join(texte_a_dechiffrer)
    print(texte_final_dechiffre)