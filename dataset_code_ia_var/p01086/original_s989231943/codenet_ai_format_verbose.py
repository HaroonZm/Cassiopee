def lire_nombre_de_lignes():
    global nombre_de_lignes
    nombre_de_lignes = int(input())
    return nombre_de_lignes

def trouver_position_prochaine_debut_mot(indice_depart, longueur_requise):
    global longueurs_mots
    if indice_depart < 0:
        return -1
    while longueur_requise > 0 and indice_depart < nombre_de_lignes:
        longueur_requise -= longueurs_mots[indice_depart]
        indice_depart += 1
        if longueur_requise == 0:
            return indice_depart
    return -1

while lire_nombre_de_lignes() > 0:

    longueurs_mots = []
    for indice_ligne in range(nombre_de_lignes):
        longueur_mot = len(input())
        longueurs_mots.append(longueur_mot)

    for indice_mot in range(nombre_de_lignes):
        position_apres_5 = trouver_position_prochaine_debut_mot(indice_mot, 5)
        position_apres_7_1 = trouver_position_prochaine_debut_mot(position_apres_5, 7)
        position_apres_5_2 = trouver_position_prochaine_debut_mot(position_apres_7_1, 5)
        position_apres_7_2 = trouver_position_prochaine_debut_mot(position_apres_5_2, 7)
        position_apres_7_3 = trouver_position_prochaine_debut_mot(position_apres_7_2, 7)
        if position_apres_7_3 >= 0:
            print(indice_mot + 1)
            break