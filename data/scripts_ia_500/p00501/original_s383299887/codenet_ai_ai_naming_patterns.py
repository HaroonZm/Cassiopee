import math
nombre_de_mots = int(input())
mot_cible = input()
liste_des_mots = [input() for _ in range(nombre_de_mots)]
taille_mot_cible = len(mot_cible)
presence_mot_cible = [0] * nombre_de_mots
for indice_mot in range(nombre_de_mots):
    longueur_mot = len(liste_des_mots[indice_mot])
    for indice_caractere in range(longueur_mot):
        for pas in range(1, 2 * math.ceil(longueur_mot / taille_mot_cible)):
            sous_sequence = liste_des_mots[indice_mot][indice_caractere::pas]
            if mot_cible in sous_sequence:
                presence_mot_cible[indice_mot] = 1
print(sum(presence_mot_cible))