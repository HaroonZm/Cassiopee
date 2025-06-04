entiers_entrés_par_utilisateur = [int(valeur_saisie) for valeur_saisie in input().split()]

valeur_minimale = min(entiers_entrés_par_utilisateur)
valeur_maximale = max(entiers_entrés_par_utilisateur)

print("{} {}".format(valeur_minimale, valeur_maximale))