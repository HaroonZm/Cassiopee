caractere_entree = list(input())
longueur_chaine = len(caractere_entree)
position_repetition = -1

def calculer_tableau_Z(sequence):
    longueur_sequence = len(sequence)
    tableau_z = [0] * longueur_sequence
    position_courante = 0
    masque_facteurs = [1] * longueur_sequence

    for indice in range(1, longueur_sequence):
        if indice + tableau_z[indice - position_courante] < position_courante + tableau_z[position_courante]:
            tableau_z[indice] = tableau_z[indice - position_courante]
        else:
            decalage = max(0, position_courante + tableau_z[position_courante] - indice)
            while indice + decalage < longueur_sequence and sequence[decalage] == sequence[indice + decalage]:
                decalage += 1
            tableau_z[indice] = decalage
            position_courante = indice

    for position in range(1, longueur_sequence):
        for repetition in range(2, tableau_z[position] // position + 2):
            masque_facteurs[repetition * position - 1] = 0

    return masque_facteurs

for longueur_motif in range(1, longueur_chaine // 2 + 1):
    if longueur_chaine % longueur_motif == 0 and caractere_entree[:longueur_chaine - longueur_motif] == caractere_entree[longueur_motif:]:
        position_repetition = longueur_motif
        break

if position_repetition == -1:
    print('1')
    print('1')
elif position_repetition == 1:
    print(longueur_chaine)
    print(1)
else:
    tableau_z_gauche = calculer_tableau_Z(caractere_entree)
    caractere_entree.reverse()
    tableau_z_droite = calculer_tableau_Z(caractere_entree)
    compteur_extension = 0
    for indice_fusion in range(0, longueur_chaine - 1):
        if tableau_z_gauche[indice_fusion] and tableau_z_droite[longueur_chaine - 2 - indice_fusion]:
            compteur_extension += 1
    print(2)
    print(compteur_extension)