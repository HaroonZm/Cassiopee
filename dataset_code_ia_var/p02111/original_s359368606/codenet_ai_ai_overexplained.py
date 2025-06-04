# Demande à l'utilisateur de saisir une valeur et stocke cette valeur dans la variable 'th'
# La fonction 'input()' lit une chaîne de caractères tapée par l'utilisateur
th = input()

# Convertit la chaîne de caractères stockée dans 'th' en un entier (nombre)
# Ceci est nécessaire car les entrées de 'input()' sont toujours des chaînes
th = int(th)

# Calcule le nombre d'heures en divisant 'th' par 30
# 'th % 30' calcule le reste de la division de 'th' par 30 (partie minutes)
# 'th - th%30' enlève ce reste pour obtenir un multiple de 30
# '(th - th%30) / 30' donne combien de fois 30 est contenu dans 'th' (quotient entier)
# On convertit ce quotient réel en entier avec 'int()' bien que ce soit déjà un multiple de 30,
# pour être sûr d'obtenir un entier au cas où
h = int((th - th % 30) / 30)

# Calcule le nombre de minutes complémentaires
# 'th % 30' donne la partie de 'th' qui ne complète pas une heure, donc reste en minutes
# Chaque tranche de 30 unités correspond à 60 minutes (1 heure), donc chaque 1 unité
# correspond à 2 minutes (car 30 * 2 = 60)
# Donc on multiplie la partie restante par 2
m = int((th % 30) * 2)

# Affiche les résultats calculés (le nombre d'heures et de minutes)
# La fonction 'print()' affiche les valeurs des variables séparées par un espace
print(h, m)