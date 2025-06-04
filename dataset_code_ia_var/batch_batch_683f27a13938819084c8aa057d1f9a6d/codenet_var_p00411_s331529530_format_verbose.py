utilisateur_saisie = input()

liste_valeurs_flottantes = [float(valeur) for valeur in utilisateur_saisie.split()]

valeur_a = liste_valeurs_flottantes[0]
valeur_t = liste_valeurs_flottantes[1]
valeur_r = liste_valeurs_flottantes[2]

resultat_operation = (valeur_t * valeur_r) / valeur_a

print(resultat_operation)