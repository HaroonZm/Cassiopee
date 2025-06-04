saisie_utilisateur = input()

liste_mots = saisie_utilisateur.split()

ensemble_mots_uniques = set(liste_mots)

nombre_de_mots_uniques = len(ensemble_mots_uniques)

print(nombre_de_mots_uniques)