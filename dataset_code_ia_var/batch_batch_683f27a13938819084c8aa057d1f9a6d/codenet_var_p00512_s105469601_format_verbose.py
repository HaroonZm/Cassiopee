# Dictionnaire pour stocker les totaux associés à chaque identifiant
identifiant_vers_total = {}

# Lecture du nombre d'entrées à traiter
nombre_entrees = int(input())

# Boucle de traitement des entrées utilisateur
for _ in range(nombre_entrees):

    identifiant, valeur = input().split()

    identifiant_vers_total[identifiant] = identifiant_vers_total.get(identifiant, 0) + int(valeur)

# Création d'une liste triée des identifiants selon la longueur puis ordre alphabétique
tri_identifiants = sorted([[len(identifiant), identifiant] for identifiant in identifiant_vers_total.keys()])

# Affichage du résultat formaté
for _, identifiant in tri_identifiants:

    print(identifiant, identifiant_vers_total[identifiant])